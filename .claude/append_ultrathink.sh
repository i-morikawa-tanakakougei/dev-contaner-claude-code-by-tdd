#!/bin/bash
# Simple hook to process trailing options

input=$(cat)

# Check if there are options at the end of prompt
if echo "$input" | grep -q '"prompt".*-[a-z]\+"'; then
    # Extract just the options part (e.g., "-uj" -> "uj")
    options=$(echo "$input" | grep -o '\-[a-z]\+"' | tail -1 | sed 's/-//' | sed 's/"//')

    # Process each character in the options
    for (( i=0; i<${#options}; i++ )); do
        opt="${options:$i:1}"

        case "$opt" in
            u)
                echo "use the maximum amount of ultrathink. Think deeply and systematically by questioning your initial assumptions, considering what you might be missing, exploring alternative perspectives, double-checking your logic and calculations, and identifying potential flaws in your reasoning. Take as much time as needed since thoroughness and accuracy are paramount."
                ;;
            j)
                echo "the output MUST be in Japanese"
                ;;
            v)
                echo "Be verbose and provide detailed explanations."
                ;;
            # Add more options here
        esac
    done
fi