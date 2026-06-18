# GitHub Repository Setup Instructions

This guide walks you through publishing the SME RM Copilot demo to GitHub.

## Prerequisites

- Git installed and configured
- GitHub account
- GitHub CLI (`gh`) installed (optional, but recommended)

## Option 1: Using GitHub CLI (Recommended)

The GitHub CLI provides the fastest way to create and push to a new repository.

### Step 1: Install GitHub CLI (if not already installed)

**macOS:**
```bash
brew install gh
```

**Linux:**
```bash
# Debian/Ubuntu
sudo apt install gh

# Fedora/RHEL
sudo dnf install gh
```

**Windows:**
```bash
winget install --id GitHub.cli
```

### Step 2: Authenticate with GitHub

```bash
gh auth login
```

Follow the prompts to authenticate via browser or token.

### Step 3: Create and Push Repository

```bash
# Navigate to the demo directory
cd "/Users/dillan.ibm/Downloads/Bob Demo Builder/demo-BANK-001-sme-meeting-prep"

# Create a new public repository on GitHub and push
gh repo create sme-rm-copilot-demo \
  --public \
  --source=. \
  --description="AI-Powered Meeting Preparation for Commercial Banking RMs - Built with IBM watsonx Orchestrate" \
  --push

# Or create a private repository
gh repo create sme-rm-copilot-demo \
  --private \
  --source=. \
  --description="AI-Powered Meeting Preparation for Commercial Banking RMs - Built with IBM watsonx Orchestrate" \
  --push
```

### Step 4: Verify

```bash
# Open the repository in your browser
gh repo view --web
```

**Done!** Your demo is now on GitHub.

---

## Option 2: Using GitHub Web Interface

### Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in repository details:
   - **Repository name**: `sme-rm-copilot-demo`
   - **Description**: `AI-Powered Meeting Preparation for Commercial Banking RMs - Built with IBM watsonx Orchestrate`
   - **Visibility**: Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

### Step 2: Push Local Repository

GitHub will show you commands. Use these:

```bash
# Navigate to the demo directory
cd "/Users/dillan.ibm/Downloads/Bob Demo Builder/demo-BANK-001-sme-meeting-prep"

# Add the remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/sme-rm-copilot-demo.git

# Verify the remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify

Visit your repository at: `https://github.com/YOUR-USERNAME/sme-rm-copilot-demo`

---

## Option 3: Using SSH (For Advanced Users)

### Step 1: Set Up SSH Key (if not already done)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Start ssh-agent
eval "$(ssh-agent -s)"

# Add SSH key
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard (macOS)
pbcopy < ~/.ssh/id_ed25519.pub

# Or display it to copy manually
cat ~/.ssh/id_ed25519.pub
```

### Step 2: Add SSH Key to GitHub

1. Go to https://github.com/settings/keys
2. Click "New SSH key"
3. Paste your public key
4. Click "Add SSH key"

### Step 3: Create Repository and Push

```bash
# Create repository on GitHub (via web interface or gh CLI)
# Then add SSH remote

cd "/Users/dillan.ibm/Downloads/Bob Demo Builder/demo-BANK-001-sme-meeting-prep"

# Add SSH remote (replace YOUR-USERNAME)
git remote add origin git@github.com:YOUR-USERNAME/sme-rm-copilot-demo.git

# Push
git branch -M main
git push -u origin main
```

---

## Post-Setup: Configure Repository

### Add Topics/Tags

Add these topics to help others discover your demo:

```
ibm watsonx watsonx-orchestrate ai-agents multi-agent banking fintech 
commercial-banking relationship-management demo python financial-services
```

**Via GitHub CLI:**
```bash
gh repo edit --add-topic ibm,watsonx,watsonx-orchestrate,ai-agents,multi-agent,banking,fintech,commercial-banking,relationship-management,demo,python,financial-services
```

**Via Web Interface:**
1. Go to your repository
2. Click the gear icon next to "About"
3. Add topics in the "Topics" field

### Set Repository Description

**Via GitHub CLI:**
```bash
gh repo edit --description "AI-Powered Meeting Preparation for Commercial Banking RMs - Built with IBM watsonx Orchestrate"
```

**Via Web Interface:**
1. Go to your repository
2. Click the gear icon next to "About"
3. Add description

### Add Repository Website (Optional)

If you deploy a live demo, add the URL:

**Via GitHub CLI:**
```bash
gh repo edit --homepage "https://your-demo-url.com"
```

### Enable GitHub Pages (Optional)

To host documentation:

1. Go to Settings > Pages
2. Source: Deploy from a branch
3. Branch: main, folder: / (root)
4. Click Save

Your docs will be available at: `https://YOUR-USERNAME.github.io/sme-rm-copilot-demo/`

---

## Rename GITHUB_README.md to README.md

The repository includes a GitHub-optimized README. To use it:

```bash
cd "/Users/dillan.ibm/Downloads/Bob Demo Builder/demo-BANK-001-sme-meeting-prep"

# Backup original README
mv README.md README_ORIGINAL.md

# Use GitHub README
mv GITHUB_README.md README.md

# Commit the change
git add README.md README_ORIGINAL.md
git commit -m "Use GitHub-optimized README"
git push
```

---

## Verify Repository Contents

After pushing, verify these files are visible on GitHub:

### Core Files
- ✅ README.md (or GITHUB_README.md)
- ✅ LICENSE
- ✅ .gitignore
- ✅ .env.example

### Agents
- ✅ agents/meeting_prep_orchestrator.yaml
- ✅ agents/customer_health_agent.yaml
- ✅ agents/growth_opportunity_agent.yaml
- ✅ agents/risk_monitoring_agent.yaml
- ✅ agents/customer_intelligence_agent.yaml

### Tools
- ✅ tools/analyze_financial_health.py
- ✅ tools/calculate_health_score.py
- ✅ tools/identify_product_gaps.py
- ✅ tools/analyze_industry_benchmarks.py
- ✅ tools/check_credit_alerts.py
- ✅ tools/fetch_recent_interactions.py

### Documentation
- ✅ DEPLOYMENT_GUIDE.md
- ✅ ARCHITECTURE.md
- ✅ PILOT_PLAN.md
- ✅ DEMO_SCRIPT.md
- ✅ COMPLIANCE_REPORT.md

### Scripts
- ✅ quick-deploy.sh
- ✅ import-all.sh
- ✅ verify-compliance.sh

### Excluded Files (should NOT be visible)
- ❌ .env (excluded by .gitignore)
- ❌ __pycache__/ (excluded by .gitignore)
- ❌ *.pyc (excluded by .gitignore)
- ❌ .DS_Store (excluded by .gitignore)

---

## Troubleshooting

### Error: "remote origin already exists"

```bash
# Remove existing remote
git remote remove origin

# Add new remote
git remote add origin https://github.com/YOUR-USERNAME/sme-rm-copilot-demo.git
```

### Error: "failed to push some refs"

```bash
# Pull first (if repository was initialized with README)
git pull origin main --allow-unrelated-histories

# Then push
git push -u origin main
```

### Error: "Permission denied (publickey)"

Your SSH key is not set up correctly. Use HTTPS instead:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/sme-rm-copilot-demo.git
```

### Large File Warning

If you get warnings about large files:

```bash
# Check file sizes
du -sh * | sort -h

# If needed, use Git LFS for large files
git lfs install
git lfs track "*.large-file-extension"
```

---

## Next Steps

After publishing to GitHub:

1. **Share the Repository**: Send the GitHub URL to stakeholders
2. **Create Releases**: Tag versions for major updates
3. **Enable Issues**: Allow users to report bugs or request features
4. **Add CI/CD**: Set up GitHub Actions for automated testing
5. **Create Wiki**: Document advanced usage and troubleshooting
6. **Add Contributors**: Invite team members to collaborate

---

## GitHub Repository URL

After setup, your repository will be available at:

```
https://github.com/YOUR-USERNAME/sme-rm-copilot-demo
```

Replace `YOUR-USERNAME` with your actual GitHub username.

---

## Support

For GitHub-specific issues:
- GitHub Docs: https://docs.github.com
- GitHub CLI Docs: https://cli.github.com/manual/
- GitHub Support: https://support.github.com

For demo-specific issues:
- Open an issue in the repository
- Contact IBM Tech Sales or Client Engineering

---

**Built with IBM watsonx** | **Demo Code: DEMO-BANK-001**