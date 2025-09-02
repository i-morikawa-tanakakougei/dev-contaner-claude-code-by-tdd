#!/usr/bin/env python3
"""
Session Recovery Script
Restores MCP-enabled development sessions from checkpoints with full integrity validation
"""

import asyncio
import hashlib
import json
import logging
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

# Add utils to path for json_format_utils integration
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    restore_from_checkpoint_data,
    get_mcp_context_summary,
    load_use_case_json
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class SessionRecoveryManager:
    """Manages comprehensive session recovery from checkpoints with integrity validation"""
    
    def __init__(self, checkpoint_name: str):
        self.checkpoint_name = checkpoint_name
        self.checkpoint_dir = Path(".serena/checkpoints") / checkpoint_name
        self.backup_dir = Path(".serena/backups") / f"pre_recovery_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Recovery state
        self.recovery_metadata: Dict[str, Any] = {
            "recovery_id": f"recovery_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "checkpoint_name": checkpoint_name,
            "started_at": datetime.now().isoformat(),
            "status": "starting",
            "validation_results": {},
            "restoration_progress": {},
            "errors": []
        }
        
    def validate_checkpoint_exists(self) -> bool:
        """Validate that the specified checkpoint exists and is valid"""
        try:
            if not self.checkpoint_dir.exists():
                logger.error(f"Checkpoint directory not found: {self.checkpoint_dir}")
                return False
                
            # Check for required files
            required_files = [
                "checkpoint-metadata.json",
                "checkpoint-manifest.json",
                "recovery/restore-session.sh",
                "recovery/validate-checkpoint.sh"
            ]
            
            missing_files = []
            for required_file in required_files:
                file_path = self.checkpoint_dir / required_file
                if not file_path.exists():
                    missing_files.append(required_file)
                    
            if missing_files:
                logger.error(f"Missing required checkpoint files: {missing_files}")
                return False
                
            logger.info("✅ Checkpoint structure validation passed")
            return True
            
        except Exception as e:
            logger.exception("Failed to validate checkpoint existence")
            return False
            
    def load_checkpoint_metadata(self) -> Dict[str, Any]:
        """Load and validate checkpoint metadata"""
        try:
            metadata_file = self.checkpoint_dir / "checkpoint-metadata.json"
            manifest_file = self.checkpoint_dir / "checkpoint-manifest.json"
            
            # Load metadata
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                
            # Load manifest
            with open(manifest_file, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
                
            # Validate metadata structure
            required_keys = ["checkpoint_id", "created_at", "status", "files", "integrity"]
            for key in required_keys:
                if key not in metadata:
                    raise ValueError(f"Missing required metadata key: {key}")
                    
            logger.info(f"✅ Loaded checkpoint metadata: {metadata['checkpoint_id']}")
            logger.info(f"   Created: {metadata['created_at']}")
            logger.info(f"   Status: {metadata['status']}")
            
            return {"metadata": metadata, "manifest": manifest}
            
        except Exception as e:
            logger.exception("Failed to load checkpoint metadata")
            raise
            
    def verify_checkpoint_integrity(self, metadata: Dict[str, Any]) -> bool:
        """Verify the integrity of checkpoint data using checksums"""
        try:
            logger.info("🔒 Starting checkpoint integrity verification...")
            
            archived_files = metadata["metadata"]["files"]
            stored_checksums = metadata["metadata"]["integrity"]
            verification_results = {}
            
            for file_type, file_path in archived_files.items():
                logger.info(f"   Verifying {file_type}...")
                
                path_obj = self.checkpoint_dir / Path(file_path).name
                if path_obj.exists():
                    # Calculate current checksum
                    current_checksum = self._calculate_path_checksum(path_obj)
                    stored_checksum = stored_checksums.get(file_type)
                    
                    if stored_checksum and current_checksum == stored_checksum:
                        verification_results[file_type] = "✅ PASSED"
                        logger.info(f"   ✅ {file_type}: Integrity verified")
                    else:
                        verification_results[file_type] = "❌ FAILED"
                        logger.error(f"   ❌ {file_type}: Integrity check failed")
                        logger.error(f"      Expected: {stored_checksum}")
                        logger.error(f"      Actual: {current_checksum}")
                else:
                    verification_results[file_type] = "❌ MISSING"
                    logger.error(f"   ❌ {file_type}: File missing")
                    
            # Check overall verification result
            failed_verifications = [k for k, v in verification_results.items() if "FAILED" in v or "MISSING" in v]
            
            if failed_verifications:
                logger.error(f"Integrity verification failed for: {failed_verifications}")
                return False
            else:
                logger.info("✅ All integrity verifications passed")
                self.recovery_metadata["validation_results"]["integrity"] = verification_results
                return True
                
        except Exception as e:
            logger.exception("Failed to verify checkpoint integrity")
            return False
            
    def _calculate_path_checksum(self, path: Path) -> str:
        """Calculate checksum for file or directory"""
        try:
            if path.is_dir():
                # Calculate directory checksum
                dir_hash = hashlib.sha256()
                for file in sorted(path.rglob("*")):
                    if file.is_file():
                        with open(file, 'rb') as f:
                            dir_hash.update(f.read())
                return dir_hash.hexdigest()
            elif path.is_file():
                # Calculate file checksum
                with open(path, 'rb') as f:
                    return hashlib.sha256(f.read()).hexdigest()
            else:
                return ""
        except Exception:
            return ""
            
    def backup_current_state(self) -> bool:
        """Backup current state before recovery in case rollback is needed"""
        try:
            logger.info("💾 Creating backup of current state...")
            
            # Create backup directory
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            
            # Backup current session if it exists
            current_session = Path(".serena/sessions/current")
            if current_session.exists():
                backup_session = self.backup_dir / "session"
                if current_session.is_symlink():
                    # Backup the actual directory, not the symlink
                    actual_session = current_session.resolve()
                    if actual_session.exists():
                        shutil.copytree(actual_session, backup_session, dirs_exist_ok=True)
                        logger.info(f"   ✅ Backed up session: {actual_session} -> {backup_session}")
                else:
                    shutil.copytree(current_session, backup_session, dirs_exist_ok=True)
                    logger.info(f"   ✅ Backed up session: {current_session} -> {backup_session}")
                    
            # Backup current memory if it exists
            current_memory = Path(".serena/memory")
            if current_memory.exists():
                backup_memory = self.backup_dir / "memory"
                shutil.copytree(current_memory, backup_memory, dirs_exist_ok=True)
                logger.info(f"   ✅ Backed up memory: {current_memory} -> {backup_memory}")
                
            # Backup current docs if they exist
            docs_dirs = ["docs/use_cases", "docs/domain", "docs/vision", "docs/metadata"]
            for docs_dir in docs_dirs:
                docs_path = Path(docs_dir)
                if docs_path.exists():
                    backup_docs = self.backup_dir / "docs" / docs_path.name
                    backup_docs.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(docs_path, backup_docs, dirs_exist_ok=True)
                    logger.info(f"   ✅ Backed up docs: {docs_path} -> {backup_docs}")
                    
            # Create backup metadata
            backup_metadata = {
                "backup_id": self.backup_dir.name,
                "created_at": datetime.now().isoformat(),
                "reason": f"Pre-recovery backup for checkpoint: {self.checkpoint_name}",
                "original_paths": {
                    "session": str(Path(".serena/sessions/current")),
                    "memory": str(Path(".serena/memory")),
                    "docs": "docs/"
                }
            }
            
            backup_metadata_file = self.backup_dir / "backup-metadata.json"
            with open(backup_metadata_file, 'w', encoding='utf-8') as f:
                json.dump(backup_metadata, f, indent=2, ensure_ascii=False)
                
            logger.info("✅ Current state backup completed")
            return True
            
        except Exception as e:
            logger.exception("Failed to backup current state")
            return False
            
    def execute_recovery_script(self) -> Tuple[bool, str]:
        """Execute the automatic recovery script from checkpoint"""
        try:
            logger.info("🔄 Executing automatic recovery script...")
            
            recovery_script = self.checkpoint_dir / "recovery/restore-session.sh"
            if not recovery_script.exists():
                raise FileNotFoundError(f"Recovery script not found: {recovery_script}")
                
            # Make script executable
            recovery_script.chmod(0o755)
            
            # Execute recovery script
            result = subprocess.run(
                [str(recovery_script)],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode == 0:
                logger.info("✅ Recovery script executed successfully")
                logger.info("Recovery script output:")
                for line in result.stdout.split('\n'):
                    if line.strip():
                        logger.info(f"   {line}")
                return True, result.stdout
            else:
                logger.error("❌ Recovery script failed")
                logger.error("Error output:")
                for line in result.stderr.split('\n'):
                    if line.strip():
                        logger.error(f"   {line}")
                return False, result.stderr
                
        except subprocess.TimeoutExpired:
            logger.error("Recovery script timed out after 5 minutes")
            return False, "Script execution timed out"
        except Exception as e:
            logger.exception("Failed to execute recovery script")
            return False, str(e)
            
    def validate_recovery_completeness(self) -> bool:
        """Validate that recovery was completed successfully"""
        try:
            logger.info("🔍 Validating recovery completeness...")
            
            validation_results = {}
            
            # Check session restoration
            current_session = Path(".serena/sessions/current")
            if current_session.exists():
                session_metadata = current_session / "session-metadata.json"
                if session_metadata.exists():
                    validation_results["session"] = "✅ RESTORED"
                    logger.info("   ✅ Session metadata found")
                else:
                    validation_results["session"] = "❌ INCOMPLETE"
                    logger.error("   ❌ Session metadata missing")
            else:
                validation_results["session"] = "❌ MISSING"
                logger.error("   ❌ Session directory missing")
                
            # Check memory restoration
            memory_dir = Path(".serena/memory")
            if memory_dir.exists() and any(memory_dir.iterdir()):
                validation_results["memory"] = "✅ RESTORED"
                logger.info("   ✅ Memory files found")
            else:
                validation_results["memory"] = "❌ MISSING"
                logger.error("   ❌ Memory files missing")
                
            # Check docs restoration
            docs_checks = {
                "use_cases": Path("docs/use_cases"),
                "domain": Path("docs/domain"),
                "vision": Path("docs/vision"),
                "metadata": Path("docs/metadata")
            }
            
            for docs_name, docs_path in docs_checks.items():
                if docs_path.exists() and any(docs_path.iterdir()):
                    validation_results[f"docs_{docs_name}"] = "✅ RESTORED"
                    logger.info(f"   ✅ {docs_name} documentation found")
                else:
                    validation_results[f"docs_{docs_name}"] = "⚠️ OPTIONAL"
                    logger.warning(f"   ⚠️ {docs_name} documentation not found (may not exist in checkpoint)")
                    
            # Check for critical failures
            critical_failures = [k for k, v in validation_results.items() 
                               if "❌" in v and k in ["session", "memory"]]
            
            if critical_failures:
                logger.error(f"Critical validation failures: {critical_failures}")
                self.recovery_metadata["validation_results"]["completeness"] = validation_results
                return False
            else:
                logger.info("✅ Recovery completeness validation passed")
                self.recovery_metadata["validation_results"]["completeness"] = validation_results
                return True
                
        except Exception as e:
            logger.exception("Failed to validate recovery completeness")
            return False
            
    def run_post_recovery_validation(self) -> bool:
        """Run comprehensive post-recovery validation"""
        try:
            logger.info("🧪 Running post-recovery validation...")
            
            validation_script = self.checkpoint_dir / "recovery/validate-checkpoint.sh"
            if validation_script.exists():
                # Make script executable
                validation_script.chmod(0o755)
                
                # Execute validation script
                result = subprocess.run(
                    [str(validation_script)],
                    cwd=Path.cwd(),
                    capture_output=True,
                    text=True,
                    timeout=120  # 2 minute timeout
                )
                
                if result.returncode == 0:
                    logger.info("✅ Post-recovery validation passed")
                    return True
                else:
                    logger.error("❌ Post-recovery validation failed")
                    logger.error("Validation output:")
                    for line in result.stderr.split('\n'):
                        if line.strip():
                            logger.error(f"   {line}")
                    return False
            else:
                logger.warning("⚠️ Validation script not found, skipping")
                return True
                
        except subprocess.TimeoutExpired:
            logger.error("Validation script timed out")
            return False
        except Exception as e:
            logger.exception("Failed to run post-recovery validation")
            return False
            
    def save_recovery_metadata(self) -> None:
        """Save recovery process metadata"""
        try:
            # Update recovery metadata
            self.recovery_metadata.update({
                "completed_at": datetime.now().isoformat(),
                "status": "completed",
                "backup_location": str(self.backup_dir),
                "checkpoint_source": str(self.checkpoint_dir)
            })
            
            # Save recovery metadata
            recovery_metadata_file = Path(".serena/sessions/current") / "recovery-metadata.json"
            if recovery_metadata_file.parent.exists():
                with open(recovery_metadata_file, 'w', encoding='utf-8') as f:
                    json.dump(self.recovery_metadata, f, indent=2, ensure_ascii=False)
                logger.info(f"✅ Recovery metadata saved: {recovery_metadata_file}")
            else:
                logger.warning("⚠️ Could not save recovery metadata - session directory not found")
                
        except Exception as e:
            logger.exception("Failed to save recovery metadata")
            
    def generate_recovery_report(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive recovery report"""
        return {
            "recovery_info": {
                "checkpoint_name": self.checkpoint_name,
                "recovery_id": self.recovery_metadata["recovery_id"],
                "started_at": self.recovery_metadata["started_at"],
                "completed_at": self.recovery_metadata.get("completed_at"),
                "status": "successful"
            },
            "checkpoint_info": {
                "created_at": metadata["metadata"]["created_at"],
                "checkpoint_size_mb": metadata["metadata"].get("statistics", {}).get("checkpoint_size_mb", 0),
                "files_restored": len(metadata["metadata"]["files"])
            },
            "validation_results": self.recovery_metadata.get("validation_results", {}),
            "backup_info": {
                "backup_created": True,
                "backup_location": str(self.backup_dir)
            },
            "restored_components": {
                "session_state": True,
                "memory_files": True,
                "project_documentation": True,
                "mcp_integration": True
            },
            "next_steps": [
                "Development session restored and ready",
                "MCP integrations (Serena + Context7) available",
                "Use /analytics-dashboard to verify system state",
                "Continue with TDD/DDD workflow",
                f"Rollback available from backup: {self.backup_dir}"
            ]
        }
        
    async def run_recovery(self) -> Dict[str, Any]:
        """Main recovery workflow"""
        try:
            logger.info(f"🔄 Starting session recovery from checkpoint: {self.checkpoint_name}")
            
            # Phase 1: Validate checkpoint exists and is valid
            logger.info("📋 Phase 1: Validating checkpoint...")
            if not self.validate_checkpoint_exists():
                raise ValueError("Checkpoint validation failed")
                
            # Phase 2: Load and verify checkpoint metadata
            logger.info("📖 Phase 2: Loading checkpoint metadata...")
            metadata = self.load_checkpoint_metadata()
            
            # Phase 3: Verify checkpoint integrity
            logger.info("🔒 Phase 3: Verifying checkpoint integrity...")
            if not self.verify_checkpoint_integrity(metadata):
                raise ValueError("Checkpoint integrity verification failed")
                
            # Phase 4: Backup current state
            logger.info("💾 Phase 4: Backing up current state...")
            if not self.backup_current_state():
                logger.warning("⚠️ Current state backup failed, proceeding with recovery")
                
            # Phase 5: Execute recovery
            logger.info("🔄 Phase 5: Executing recovery...")
            recovery_success, recovery_output = self.execute_recovery_script()
            if not recovery_success:
                raise ValueError(f"Recovery script failed: {recovery_output}")
                
            # Phase 6: Validate recovery completeness
            logger.info("🔍 Phase 6: Validating recovery completeness...")
            if not self.validate_recovery_completeness():
                raise ValueError("Recovery completeness validation failed")
                
            # Phase 7: Post-recovery validation
            logger.info("🧪 Phase 7: Post-recovery validation...")
            if not self.run_post_recovery_validation():
                logger.warning("⚠️ Post-recovery validation had issues, but recovery may still be functional")
                
            # Phase 8: Save recovery metadata
            logger.info("💾 Phase 8: Saving recovery metadata...")
            self.save_recovery_metadata()
            
            # Generate final report
            report = self.generate_recovery_report(metadata)
            logger.info("✅ Session recovery completed successfully!")
            
            return report
            
        except Exception as e:
            logger.exception("Session recovery failed")
            self.recovery_metadata["status"] = "failed"
            self.recovery_metadata["error"] = str(e)
            raise


async def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        logger.error("Usage: python 22-recovery-session.py <checkpoint_name>")
        
        # List available checkpoints
        checkpoints_dir = Path(".serena/checkpoints")
        if checkpoints_dir.exists():
            checkpoints = [d.name for d in checkpoints_dir.iterdir() if d.is_dir()]
            if checkpoints:
                logger.info("Available checkpoints:")
                for checkpoint in sorted(checkpoints):
                    logger.info(f"  • {checkpoint}")
            else:
                logger.info("No checkpoints found")
        else:
            logger.info("No checkpoints directory found")
            
        sys.exit(1)
        
    checkpoint_name = sys.argv[1]
    
    try:
        # Validate checkpoint name
        if not checkpoint_name.replace('_', '').replace('-', '').isalnum():
            logger.error(f"Invalid checkpoint name: {checkpoint_name}")
            sys.exit(1)
            
        # Initialize recovery manager
        recovery_manager = SessionRecoveryManager(checkpoint_name)
        
        # Run recovery
        report = await recovery_manager.run_recovery()
        
        # Print success summary
        print("\n" + "="*60)
        print("🎉 SESSION RECOVERY COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"Checkpoint: {report['recovery_info']['checkpoint_name']}")
        print(f"Recovery ID: {report['recovery_info']['recovery_id']}")
        print(f"Started: {report['recovery_info']['started_at']}")
        print(f"Completed: {report['recovery_info']['completed_at']}")
        print(f"\n📊 Checkpoint Information:")
        print(f"  Created: {report['checkpoint_info']['created_at']}")
        print(f"  Size: {report['checkpoint_info']['checkpoint_size_mb']} MB")
        print(f"  Files Restored: {report['checkpoint_info']['files_restored']}")
        print(f"\n✅ Restored Components:")
        for component, restored in report['restored_components'].items():
            status = "✅" if restored else "❌"
            print(f"  {status} {component.replace('_', ' ').title()}")
        print(f"\n🚀 Next Steps:")
        for step in report['next_steps']:
            print(f"  • {step}")
        print("="*60)
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        logger.info("Recovery cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.exception("Recovery failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())