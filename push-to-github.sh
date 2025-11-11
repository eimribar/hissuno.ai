#!/bin/bash
cd /Users/eimribar/Desktop/fin-replica

# Initialize git if not already initialized
if [ ! -d .git ]; then
    git init
fi

# Add all files
git add .

# Commit
git commit -m "Initial commit: Fin.ai pixel-perfect replica

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Add remote
git remote add origin https://github.com/eimribar/hissuno.ai.git || git remote set-url origin https://github.com/eimribar/hissuno.ai.git

# Push to main branch
git branch -M main
git push -u origin main
