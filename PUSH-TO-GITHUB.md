# Push to GitHub Instructions

## Repository: https://github.com/eimribar/hissuno.ai

Run these commands in your terminal:

```bash
cd /Users/eimribar/Desktop/fin-replica

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Fin.ai pixel-perfect replica

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Add remote (if repository already exists, this will fail - that's okay)
git remote add origin https://github.com/eimribar/hissuno.ai.git

# If the above fails, use this instead:
# git remote set-url origin https://github.com/eimribar/hissuno.ai.git

# Rename branch to main
git branch -M main

# Force push to overwrite repository
git push -u origin main --force
```

## What's included:
- index.html (2.4 MB)
- 8 CSS files (assets/css/)
- 38 JavaScript files (assets/js/)
- 34 images (assets/images/)
- 14 fonts (fonts/)
- Server configuration files
- vercel.json for deployment

## After pushing:
1. Go to https://vercel.com
2. Click "New Project"
3. Import from GitHub: eimribar/hissuno.ai
4. Vercel will auto-detect it as a static site
5. Click "Deploy"
