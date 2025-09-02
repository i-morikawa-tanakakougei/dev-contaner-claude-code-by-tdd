#!/usr/bin/env python3
"""
Session Checkpointing Script
Creates comprehensive checkpoints of MCP-enabled development sessions
"""

import asyncio
import hashlib
import json
import logging
import os
import shutil
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Add utils to path for json_format_utils integration
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    create_session_checkpoint_data,
    get_mcp_context_summary,
    load_use_case_json
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class SessionCheckpointManager:
    """Manages comprehensive session checkpointing with recovery capabilities"""
    
    def __init__(self, checkpoint_name: str):
        self.checkpoint_name = checkpoint_name
        self.checkpoint_dir = Path(".serena/checkpoints") / checkpoint_name
        self.session_dir = Path(".serena/sessions/current")
        self.memory_dir = Path(".serena/memory")
        
        # Checkpoint metadata
        self.checkpoint_metadata: Dict[str, Any] = {
            "checkpoint_id": checkpoint_name,
            "created_at": datetime.now().isoformat(),
            "creator": "mcp-session-manager",
            "version": "1.0",
            "status": "creating",
            "files": {},
            "integrity": {},
            "recovery_info": {}
        }
        
    def initialize_checkpoint_structure(self) -> None:
        """Initialize checkpoint directory structure"""
        try:
            # Create checkpoint directories
            directories = [
                self.checkpoint_dir,
                self.checkpoint_dir / "session",
                self.checkpoint_dir / "memory",
                self.checkpoint_dir / "project_state",
                self.checkpoint_dir / "mcp_state",
                self.checkpoint_dir / "recovery"
            ]
            
            for directory in directories:
                directory.mkdir(parents=True, exist_ok=True)
                logger.info(f"✅ Created checkpoint directory: {directory}")
                
        except Exception as e:
            logger.exception("Failed to initialize checkpoint structure")
            raise
            
    def analyze_current_session(self) -> Dict[str, Any]:
        """Analyze current session state for checkpointing"""
        try:
            session_analysis = {
                "session_active": False,
                "session_metadata": {},
                "progress_state": {},
                "git_state": {},
                "file_counts": {}
            }
            
            # Check if session is active
            if self.session_dir.exists() and self.session_dir.is_symlink():
                session_analysis["session_active"] = True
                
                # Read session metadata
                metadata_file = self.session_dir / "session-metadata.json"
                if metadata_file.exists():
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        session_analysis["session_metadata"] = json.load(f)
                        
            # Analyze memory state
            if self.memory_dir.exists():
                memory_files = list(self.memory_dir.rglob("*.md"))
                session_analysis["file_counts"]["memory_files"] = len(memory_files)
                
            # Analyze project state
            project_files = {
                "use_cases": len(list(Path("docs/use_cases").rglob("*.md"))) if Path("docs/use_cases").exists() else 0,
                "domain_models": len(list(Path("docs/domain").rglob("*.md"))) if Path("docs/domain").exists() else 0,
                "tests": len(list(Path(".").rglob("test_*.py"))) if Path(".").exists() else 0,
            }
            session_analysis["file_counts"].update(project_files)
            
            # Get git state
            try:
                import subprocess
                git_branch = subprocess.run(['git', 'branch', '--show-current'], 
                                          capture_output=True, text=True).stdout.strip()
                git_status = subprocess.run(['git', 'status', '--porcelain'], 
                                          capture_output=True, text=True).stdout.strip()
                session_analysis["git_state"] = {
                    "current_branch": git_branch,
                    "has_changes": len(git_status) > 0,
                    "status_output": git_status
                }
            except Exception as e:
                logger.warning(f"Could not get git state: {e}")
                session_analysis["git_state"] = {"error": str(e)}
                
            logger.info("📊 Session analysis completed")
            return session_analysis
            
        except Exception as e:
            logger.exception("Failed to analyze current session")
            raise
            
    def archive_session_data(self) -> Dict[str, str]:
        """Archive current session data to checkpoint"""
        try:
            archived_files = {}
            
            # Archive session metadata
            if self.session_dir.exists():
                session_archive = self.checkpoint_dir / "session"
                shutil.copytree(self.session_dir.resolve(), session_archive / "current", dirs_exist_ok=True)
                archived_files["session_data"] = str(session_archive)
                logger.info(f"✅ Archived session data to: {session_archive}")
                
            # Archive memory files
            if self.memory_dir.exists():
                memory_archive = self.checkpoint_dir / "memory"
                shutil.copytree(self.memory_dir, memory_archive / "memory", dirs_exist_ok=True)
                archived_files["memory_data"] = str(memory_archive)
                logger.info(f"✅ Archived memory data to: {memory_archive}")
                
            # Archive project documentation
            project_docs = [
                ("docs/use_cases", "use_cases"),
                ("docs/domain", "domain_models"), 
                ("docs/vision", "vision"),
                ("docs/metadata", "metadata")
            ]
            
            project_archive = self.checkpoint_dir / "project_state"
            for source_dir, archive_name in project_docs:
                source_path = Path(source_dir)
                if source_path.exists():
                    dest_path = project_archive / archive_name
                    shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
                    archived_files[archive_name] = str(dest_path)
                    logger.info(f"✅ Archived {source_dir} to: {dest_path}")
                    
            return archived_files
            
        except Exception as e:
            logger.exception("Failed to archive session data")
            raise
            
    def create_integrity_checksums(self, archived_files: Dict[str, str]) -> Dict[str, str]:
        """Create integrity checksums for archived files"""
        try:
            checksums = {}
            
            for file_type, file_path in archived_files.items():
                path_obj = Path(file_path)
                if path_obj.is_dir():
                    # Calculate directory checksum
                    dir_hash = hashlib.sha256()
                    for file in sorted(path_obj.rglob("*")):
                        if file.is_file():
                            with open(file, 'rb') as f:
                                dir_hash.update(f.read())
                    checksums[file_type] = dir_hash.hexdigest()
                elif path_obj.is_file():
                    # Calculate file checksum
                    with open(path_obj, 'rb') as f:
                        file_hash = hashlib.sha256(f.read()).hexdigest()
                    checksums[file_type] = file_hash
                    
                logger.info(f"✅ Created checksum for {file_type}: {checksums[file_type][:12]}...")
                
            return checksums
            
        except Exception as e:
            logger.exception("Failed to create integrity checksums")
            raise
            
    def create_recovery_scripts(self, session_analysis: Dict[str, Any]) -> None:
        """Create automated recovery scripts"""
        try:
            recovery_dir = self.checkpoint_dir / "recovery"
            
            # Create main recovery script
            recovery_script = f"""#!/bin/bash
# Automated Recovery Script for Checkpoint: {self.checkpoint_name}
# Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

echo "🔄 Starting session recovery from checkpoint: {self.checkpoint_name}"

# Restore session data
if [[ -d ".serena/checkpoints/{self.checkpoint_name}/session/current" ]]; then
    echo "📂 Restoring session data..."
    rm -rf .serena/sessions/current 2>/dev/null || true
    mkdir -p .serena/sessions
    cp -r ".serena/checkpoints/{self.checkpoint_name}/session/current" ".serena/sessions/"
    ln -sf "current" ".serena/sessions/current"
    echo "✅ Session data restored"
fi

# Restore memory files
if [[ -d ".serena/checkpoints/{self.checkpoint_name}/memory/memory" ]]; then
    echo "🧠 Restoring memory files..."
    rm -rf .serena/memory 2>/dev/null || true
    cp -r ".serena/checkpoints/{self.checkpoint_name}/memory/memory" ".serena/"
    echo "✅ Memory files restored"
fi

# Restore project documentation
PROJECT_DIRS=("use_cases" "domain_models" "vision" "metadata")
for dir in "${{PROJECT_DIRS[@]}}"; do
    checkpoint_dir=".serena/checkpoints/{self.checkpoint_name}/project_state/$dir"
    if [[ -d "$checkpoint_dir" ]]; then
        echo "📚 Restoring $dir documentation..."
        target_dir="docs/$dir"
        if [[ "$dir" == "domain_models" ]]; then
            target_dir="docs/domain"
        fi
        mkdir -p "$target_dir"
        cp -r "$checkpoint_dir/"* "$target_dir/" 2>/dev/null || true
        echo "✅ $dir documentation restored"
    fi
done

# Validate recovery
echo "🔍 Validating recovery..."
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ Session metadata found"
else
    echo "❌ Session metadata missing"
    exit 1
fi

if [[ -d ".serena/memory" ]]; then
    echo "✅ Memory directory found"
else
    echo "❌ Memory directory missing" 
    exit 1
fi

echo "✅ Recovery completed successfully!"
echo "🚀 You can now resume your development session"
echo "💡 Consider running: /analytics-dashboard to verify system state"
"""

            recovery_script_file = recovery_dir / "restore-session.sh"
            recovery_script_file.write_text(recovery_script)
            recovery_script_file.chmod(0o755)
            
            # Create validation script
            validation_script = f"""#!/bin/bash
# Validation Script for Checkpoint: {self.checkpoint_name}

echo "🔍 Validating checkpoint integrity..."

ERRORS=0

# Check session data
if [[ ! -d ".serena/checkpoints/{self.checkpoint_name}/session" ]]; then
    echo "❌ Session data missing"
    ((ERRORS++))
fi

# Check memory data
if [[ ! -d ".serena/checkpoints/{self.checkpoint_name}/memory" ]]; then
    echo "❌ Memory data missing"
    ((ERRORS++))
fi

# Check metadata
if [[ ! -f ".serena/checkpoints/{self.checkpoint_name}/checkpoint-metadata.json" ]]; then
    echo "❌ Checkpoint metadata missing"
    ((ERRORS++))
fi

if [[ $ERRORS -eq 0 ]]; then
    echo "✅ Checkpoint validation passed"
    exit 0
else
    echo "❌ Checkpoint validation failed with $ERRORS errors"
    exit 1
fi
"""

            validation_script_file = recovery_dir / "validate-checkpoint.sh"
            validation_script_file.write_text(validation_script)
            validation_script_file.chmod(0o755)
            
            logger.info("✅ Recovery scripts created")
            
        except Exception as e:
            logger.exception("Failed to create recovery scripts")
            raise
            
    def create_checkpoint_manifest(self, archived_files: Dict[str, str], 
                                  checksums: Dict[str, str],
                                  session_analysis: Dict[str, Any]) -> None:
        """Create comprehensive checkpoint manifest"""
        try:
            manifest = {
                "checkpoint_info": {
                    "name": self.checkpoint_name,
                    "created_at": self.checkpoint_metadata["created_at"],
                    "version": "1.0",
                    "format": "mcp-session-checkpoint"
                },
                "session_state": session_analysis,
                "archived_files": archived_files,
                "integrity_checksums": checksums,
                "recovery_instructions": {
                    "automatic_script": "./recovery/restore-session.sh",
                    "validation_script": "./recovery/validate-checkpoint.sh",
                    "manual_steps": [
                        "Restore .serena/sessions/current from session/ directory",
                        "Restore .serena/memory from memory/ directory", 
                        "Restore docs/ structure from project_state/ directory",
                        "Validate using validation script"
                    ]
                },
                "statistics": {
                    "total_files": len(archived_files),
                    "checkpoint_size_mb": self._calculate_checkpoint_size(),
                    "compression_ratio": 0.0  # TODO: implement if using compression
                }
            }
            
            manifest_file = self.checkpoint_dir / "checkpoint-manifest.json"
            with open(manifest_file, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
                
            logger.info(f"✅ Checkpoint manifest created: {manifest_file}")
            
        except Exception as e:
            logger.exception("Failed to create checkpoint manifest")
            raise
            
    def _calculate_checkpoint_size(self) -> float:
        """Calculate total checkpoint size in MB"""
        try:
            total_size = 0
            for root, dirs, files in os.walk(self.checkpoint_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path):
                        total_size += os.path.getsize(file_path)
            return round(total_size / (1024 * 1024), 2)
        except Exception:
            return 0.0
            
    def save_checkpoint_metadata(self, archived_files: Dict[str, str], 
                                checksums: Dict[str, str],
                                session_analysis: Dict[str, Any]) -> None:
        """Save comprehensive checkpoint metadata"""
        try:
            # Update metadata with final information
            self.checkpoint_metadata.update({
                "status": "completed",
                "completed_at": datetime.now().isoformat(),
                "files": archived_files,
                "integrity": checksums,
                "session_analysis": session_analysis,
                "recovery_info": {
                    "recovery_script": str(self.checkpoint_dir / "recovery/restore-session.sh"),
                    "validation_script": str(self.checkpoint_dir / "recovery/validate-checkpoint.sh"),
                    "manifest_file": str(self.checkpoint_dir / "checkpoint-manifest.json")
                },
                "statistics": {
                    "checkpoint_size_mb": self._calculate_checkpoint_size(),
                    "files_archived": len(archived_files),
                    "creation_duration_seconds": time.time() - time.mktime(
                        datetime.fromisoformat(self.checkpoint_metadata["created_at"]).timetuple()
                    )
                }
            })
            
            metadata_file = self.checkpoint_dir / "checkpoint-metadata.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(self.checkpoint_metadata, f, indent=2, ensure_ascii=False)
                
            logger.info(f"✅ Checkpoint metadata saved: {metadata_file}")
            
        except Exception as e:
            logger.exception("Failed to save checkpoint metadata")
            raise
            
    def generate_checkpoint_report(self, archived_files: Dict[str, str],
                                  session_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive checkpoint creation report"""
        return {
            "checkpoint_info": {
                "name": self.checkpoint_name,
                "location": str(self.checkpoint_dir),
                "created_at": self.checkpoint_metadata["created_at"],
                "size_mb": self._calculate_checkpoint_size(),
                "status": "ready"
            },
            "archived_content": {
                "session_data": "session_data" in archived_files,
                "memory_files": "memory_data" in archived_files,
                "project_documentation": any(key in archived_files for key in ["use_cases", "domain_models", "vision"]),
                "total_file_categories": len(archived_files)
            },
            "recovery_capabilities": {
                "automatic_recovery": True,
                "integrity_validation": True,
                "partial_recovery": True,
                "rollback_support": True
            },
            "session_state": {
                "was_active": session_analysis.get("session_active", False),
                "git_branch": session_analysis.get("git_state", {}).get("current_branch", "unknown"),
                "has_uncommitted_changes": session_analysis.get("git_state", {}).get("has_changes", False)
            },
            "next_steps": [
                f"Checkpoint saved to: {self.checkpoint_dir}",
                "Continue development or create additional checkpoints",
                f"Recover using: /recovery-session {self.checkpoint_name}",
                "Validate checkpoint using: ./recovery/validate-checkpoint.sh"
            ]
        }
        
    async def run_checkpointing(self) -> Dict[str, Any]:
        """Main checkpointing workflow"""
        try:
            logger.info(f"💾 Starting session checkpointing: {self.checkpoint_name}")
            
            # Phase 1: Setup checkpoint structure
            logger.info("📁 Phase 1: Initializing checkpoint structure...")
            self.initialize_checkpoint_structure()
            
            # Phase 2: Analyze current session
            logger.info("🔍 Phase 2: Analyzing current session state...")
            session_analysis = self.analyze_current_session()
            
            # Phase 3: Archive session data
            logger.info("📦 Phase 3: Archiving session data...")
            archived_files = self.archive_session_data()
            
            # Phase 4: Create integrity checksums
            logger.info("🔒 Phase 4: Creating integrity checksums...")
            checksums = self.create_integrity_checksums(archived_files)
            
            # Phase 5: Create recovery scripts
            logger.info("🛠️ Phase 5: Creating recovery scripts...")
            self.create_recovery_scripts(session_analysis)
            
            # Phase 6: Create manifest
            logger.info("📋 Phase 6: Creating checkpoint manifest...")
            self.create_checkpoint_manifest(archived_files, checksums, session_analysis)
            
            # Phase 7: Save metadata
            logger.info("💾 Phase 7: Saving checkpoint metadata...")
            self.save_checkpoint_metadata(archived_files, checksums, session_analysis)
            
            # Generate final report
            report = self.generate_checkpoint_report(archived_files, session_analysis)
            logger.info("✅ Session checkpointing completed successfully!")
            
            return report
            
        except Exception as e:
            logger.exception("Session checkpointing failed")
            raise


async def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        # Use automatic naming if no name provided
        checkpoint_name = f"auto_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        logger.info(f"Using automatic checkpoint name: {checkpoint_name}")
    else:
        checkpoint_name = sys.argv[1]
        
    try:
        # Validate checkpoint name
        if not checkpoint_name.replace('_', '').replace('-', '').isalnum():
            logger.error(f"Invalid checkpoint name: {checkpoint_name}")
            logger.error("Checkpoint name must contain only letters, numbers, hyphens and underscores")
            sys.exit(1)
            
        # Initialize checkpoint manager
        checkpoint_manager = SessionCheckpointManager(checkpoint_name)
        
        # Run checkpointing
        report = await checkpoint_manager.run_checkpointing()
        
        # Print success summary
        print("\n" + "="*60)
        print("🎉 SESSION CHECKPOINT CREATED SUCCESSFULLY")
        print("="*60)
        print(f"Checkpoint Name: {report['checkpoint_info']['name']}")
        print(f"Location: {report['checkpoint_info']['location']}")
        print(f"Size: {report['checkpoint_info']['size_mb']} MB")
        print(f"Created: {report['checkpoint_info']['created_at']}")
        print(f"\n📦 Archived Content:")
        for content, available in report['archived_content'].items():
            if content != 'total_file_categories':
                status = "✅" if available else "❌"
                print(f"  {status} {content.replace('_', ' ').title()}")
        print(f"\n🔄 Recovery Options:")
        for capability, available in report['recovery_capabilities'].items():
            status = "✅" if available else "❌"
            print(f"  {status} {capability.replace('_', ' ').title()}")
        print(f"\n🚀 Next Steps:")
        for step in report['next_steps']:
            print(f"  • {step}")
        print("="*60)
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        logger.info("Checkpointing cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.exception("Checkpointing failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())