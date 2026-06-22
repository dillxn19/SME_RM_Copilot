# ⚡ Quick Start Guide

**Get the SME Meeting Prep Demo running in 5 minutes!**

This guide provides the fastest path to running the demo. For detailed instructions, see [DEMO_ACCESS_GUIDE.md](./DEMO_ACCESS_GUIDE.md).

---

## 📋 Prerequisites Checklist

Before you begin, ensure you have:

- [ ] **IBM Cloud account** with TechZone access
- [ ] **Node.js 18+** installed (`node --version`)
- [ ] **Python 3.9+** installed (`python3 --version`)
- [ ] **watsonx Orchestrate environment** provisioned on TechZone

**Quick Check**: Run this command to validate your system:
```bash
./validate-config.sh
```

---

## 🚀 5-Minute Setup

### Step 1: Get TechZone Credentials (2 minutes)

1. Go to [TechZone My Reservations](https://techzone.ibm.com/my/reservations)
2. Find your **watsonx Orchestrate** environment (status: Ready)
3. Copy these values:
   - `WXO_HOST_URL`
   - `WXO_ORCHESTRATION_ID`
   - `WXO_CRN`
4. Generate IBM Cloud API Key at [cloud.ibm.com/iam/apikeys](https://cloud.ibm.com/iam/apikeys)

### Step 2: Configure Environment (1 minute)

```bash
# Navigate to demo directory
cd demo-BANK-001-sme-meeting-prep

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env
```

**Add your credentials:**
```bash
WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
WXO_API_KEY=your-ibm-cloud-api-key
WXO_ORCHESTRATION_ID=your-orchestration-id
WXO_CRN=your-crn
```

### Step 3: Deploy Agents (2 minutes)

```bash
# Install watsonx Orchestrate CLI
pip3 install ibm-watsonx-orchestrate

# Run quick deployment
chmod +x quick-deploy.sh
./quick-deploy.sh
```

**What this does:**
- ✅ Validates your environment
- ✅ Imports 6 Python tools
- ✅ Deploys 5 AI agents
- ✅ Tests the deployment

### Step 4: Launch Frontend (30 seconds)

```bash
# Configure frontend
cd frontend
cp .env.example .env
nano .env  # Add same credentials as root .env

# Install and start
npm install
npm run dev
```

**Access the demo:** Open [http://localhost:3000](http://localhost:3000)

---

## ✅ Verification

### Test the Deployment

**Option 1: Via CLI**
```bash
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare me for a meeting with TechVenture Solutions" -r
```

**Option 2: Via UI**
1. Open http://localhost:3000
2. Click "AI Assistant" tab
3. Type: "Prepare me for a meeting with TechVenture Solutions"
4. Press Enter

**Expected Result:**
- Customer health analysis
- Financial metrics
- Risk assessment
- Growth opportunities
- Meeting talking points

---

## 🎯 Demo Scenarios

Try these queries in the AI Assistant:

### Scenario 1: Meeting Preparation
```
"Prepare me for a meeting with TechVenture Solutions"
```
**Shows:** Comprehensive customer analysis with health score, risks, and opportunities

### Scenario 2: Portfolio Risk Assessment
```
"What are the top risks in my SME portfolio?"
```
**Shows:** At-risk customers, credit alerts, and recommended actions

### Scenario 3: Growth Opportunities
```
"Show me growth opportunities for GreenLeaf Manufacturing"
```
**Shows:** Product gaps, cross-sell recommendations, and industry benchmarks

---

## 🛠️ Quick Troubleshooting

### Issue: Deployment fails
```bash
# Check environment
./validate-config.sh

# Verify CLI installation
orchestrate --version

# Check environment variables
cat .env | grep -v "^#"
```

### Issue: Frontend won't start
```bash
# Check Node.js version
node --version  # Should be 18+

# Reinstall dependencies
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Issue: No response from agents
```bash
# Verify agents are deployed
orchestrate agents list

# Check frontend .env file
cat frontend/.env

# Restart frontend
npm run dev
```

---

## 📚 Next Steps

### Explore the Demo
- **Dashboard** - View portfolio KPIs and metrics
- **Customers** - Browse customer cards with health scores
- **AI Assistant** - Chat with the multi-agent system

### Customize the Demo
- Modify agent prompts in `agents/*.yaml`
- Add new tools in `tools/*.py`
- Customize UI in `frontend/src/`

### Learn More
- [DEMO_ACCESS_GUIDE.md](./DEMO_ACCESS_GUIDE.md) - Complete setup guide
- [DEMO_SCRIPT.md](./DEMO_SCRIPT.md) - 15-minute presentation guide
- [ARCHITECTURE.md](./ARCHITECTURE.md) - Technical architecture
- [README.md](./README.md) - Full documentation

---

## 🎓 Understanding the Architecture

### What Just Happened?

1. **TechZone** provisioned a watsonx Orchestrate environment
2. **quick-deploy.sh** imported tools and agents to Orchestrate
3. **Frontend** connects to Orchestrate via web-chat embed
4. **Agents** coordinate to answer queries using Python tools
5. **Synthetic data** simulates real banking scenarios

### Multi-Agent System

```
User Query
    ↓
Meeting Prep Orchestrator
    ↓
┌─────────────┬──────────────┬─────────────┬──────────────┐
│   Health    │     Risk     │   Growth    │ Intelligence │
│   Agent     │    Agent     │   Agent     │    Agent     │
└─────────────┴──────────────┴─────────────┴──────────────┘
    ↓              ↓              ↓              ↓
Python Tools (analyze_financial_health, check_credit_alerts, etc.)
    ↓
Synthetic Customer Data
    ↓
Aggregated Response
```

---

## 💡 Pro Tips

### Speed Up Development
```bash
# Use quick-deploy.sh for fast deployment
./quick-deploy.sh

# Use validate-config.sh before deploying
./validate-config.sh

# Keep frontend running during agent updates
# Only restart if you change frontend code
```

### Demo Best Practices
1. **Test queries before presenting** - Ensure agents respond correctly
2. **Use full-screen mode** - Press F11 in browser
3. **Prepare backup scenarios** - Have 2-3 queries ready
4. **Monitor TechZone time** - Environments expire after 12-24 hours
5. **Export agents before expiration** - Save your work

### Common Commands
```bash
# List all agents
orchestrate agents list

# List all tools
orchestrate tools list

# Check environment
orchestrate env list

# Test an agent
orchestrate chat ask -n meeting_prep_orchestrator "your query" -r

# Start frontend
cd frontend && npm run dev

# Validate configuration
./validate-config.sh
```

---

## 🆘 Need Help?

### Quick Links
- **TechZone Support**: https://techzone.ibm.com/help
- **Orchestrate Docs**: https://ibm.github.io/watsonx-orchestrate-adk/
- **Carbon Design**: https://carbondesignsystem.com/

### Support Channels
- **TechZone Issues**: #techzone-support (Slack)
- **Orchestrate Questions**: Check documentation or IBM support
- **Demo Issues**: Review [DEMO_ACCESS_GUIDE.md](./DEMO_ACCESS_GUIDE.md)

### Validation Script
Run this anytime to check your setup:
```bash
./validate-config.sh
```

---

## 🎉 You're Ready!

Your SME Meeting Prep Demo is now running. Start exploring:

1. **Dashboard** - http://localhost:3000
2. **Try a query** - "Prepare me for a meeting with TechVenture Solutions"
3. **Review the script** - See [DEMO_SCRIPT.md](./DEMO_SCRIPT.md) for presentation guidance

**Happy demoing!** 🚀

---

**Last Updated**: 2026-06-22  
**Version**: 1.0  
**For**: demo-BANK-001-sme-meeting-prep