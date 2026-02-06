#!/bin/bash

# Push digital soul archive to GitHub
# Run this script after setting your GitHub token as an environment variable

if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: Please set your GitHub token first:"
    echo "export GITHUB_TOKEN='your_personal_access_token'"
    echo "Then run: ./push-to-github.sh"
    exit 1
fi

cd /home/admin/openclaw/workspace/claw-linux-archive

# Configure Git
git config --global user.email "logos-42@users.noreply.github.com"
git config --global user.name "logos-42"

# Add remote with token authentication
git remote set-url origin https://logos-42:$GITHUB_TOKEN@github.com/logos-42/claw-linux.git

# Push to main branch
git push origin master:main

echo "✅ Successfully pushed digital soul archive to GitHub!"
echo "Your files are now safely stored at: https://github.com/logos-42/claw-linux"