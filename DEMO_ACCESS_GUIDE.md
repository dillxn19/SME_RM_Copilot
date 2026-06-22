# 🚀 Complete Demo Access Guide

## Overview

This guide provides step-by-step instructions to access and run the **SME Meeting Prep Hybrid Demo** from start to finish. It combines TechZone provisioning, agent deployment, and frontend setup into a complete workflow.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] IBM Cloud account (IBMid)
- [ ] Access to IBM TechZone
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Python 3.9+ installed (`python3 --version`)
- [ ] Git installed
- [ ] Terminal/command line access

**Quick Validation**: Run `./validate-config.sh` to check your system prerequisites.

## 🎯 Complete Setup Flow

### Phase 1: Provision watsonx Orchestrate Environment (30-60 minutes)

#### Step 1.1: Access TechZone

1. Go to [IBM TechZone](https://techzone.ibm.com/)
2. Sign in with your IBMid
3. Search for: **"watsonx Orchestrate Trial with CE"**
4. Click on the environment tile

**What you'll get:**
- ✅ watsonx Orchestrate (lite plan)
- ✅ Watson Machine Learning (v2-standard)
- ✅ Watson Studio (free-v1)
- ✅ watsonx.governance (essentials)
- ✅ Cloud Object Storage (standard)
- ✅ Code Engine (standard)

#### Step 1.2: Reserve Environment

1. Click **"Reserve"** button
2. Fill in reservation details:
   - **Purpose**: Select "Test" or "Education"
   - **Purpose Description**: "SME Meeting Prep Demo - Multi-Agent Banking Solution"
   - **Preferred Geography**: Choose your region (us-south recommended)
   - **Start Date/Time**: Now (or schedule)
   - **End Date/Time**: +12 hours minimum (24 hours recommended)
3. Click **"Submit"**
4. **Note your Request ID** - you'll need this to track status

#### Step 1.3: Monitor Provisioning Status

**Provisioning typically takes 30-60 minutes**. You can monitor progress:

**Option 1: TechZone Web Interface**
1. Go to [My Reservations](https://techzone.ibm.com/my/reservations)
2. Find your request
3. Wait for status: "Scheduled" → "Provisioning" → "Ready"
4. You'll receive an email when ready

**Option 2: Using TechZone MCP** (if configured)
```bash
# The project includes TechZone MCP configuration in .bob/mcp.json
# You can check status programmatically through Bob's tools
```

#### Step 1.4: Extract Credentials

Once provisioned (status = "Ready"):

1. Go to **My Reservations** → Click your reservation
2. Navigate to **"Reservation Details"** or **"Access Information"** tab
3. Copy these critical values:

```bash
# watsonx Orchestrate Connection Details
WXO_HOST_URL: https://us-south.watson-orchestrate.cloud.ibm.com
WXO_ORCHESTRATION_ID: [copy from TechZone]
WXO_CRN: [copy from TechZone - Cloud Resource Name]

# IBM Cloud Account Details
IBM_CLOUD_ACCOUNT_ID: [from TechZone]
RESOURCE_GROUP: [from TechZone]
```

#### Step 1.5: Generate IBM Cloud API Key

**Important**: The API key must have proper permissions for your Orchestrate instance.

1. Go to [IBM Cloud Console](https://cloud.ibm.com)
2. Log in with your IBM ID
3. Navigate to **Manage** → **Access (IAM)** → **API keys**
4. Click **"Create an IBM Cloud API key"**
5. Configuration:
   - **Name**: `wxo-demo-sme-meeting-prep`
   - **Description**: `API key for SME Meeting Prep Demo - watsonx Orchestrate`
6. Click **"Create"**
7. **CRITICAL**: Copy and save the API key immediately
   - You cannot retrieve it later
   - Store it securely (password manager recommended)

**Verify API Key Permissions**:
- Should have "Manager" or "Administrator" role for watsonx Orchestrate
- Check in IBM Cloud → Resource List → watsonx Orchestrate → Manage Access

### Phase 2: Configure Demo Environment (5 minutes)

#### Step 2.1: Configure Root Environment Variables

```bash
# Navigate to demo directory
cd demo-BANK-001-sme-meeting-prep

# Copy environment template
cp .env.example .env

# Edit with your credentials
nano .env  # or use your preferred editor
```

**Add your TechZone credentials to .env:**

```bash
# watsonx Orchestrate Configuration
WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
WXO_API_KEY=your-ibm-cloud-api-key-here
WXO_ORCHESTRATION_ID=your-orchestration-id-from-techzone
WXO_CRN=your-crn-from-techzone

# Default Model for All Agents
WXO_DEFAULT_MODEL=groq/openai/gpt-oss-120b

# Demo Configuration
DEMO_MODE=mock
DEMO_TITLE="SME Relationship Manager Copilot - Built with IBM watsonx Orchestrate"
DEMO_CLIENT_CODE=BANK-001
```

#### Step 2.2: Validate Configuration

```bash
# Run the validation script
./validate-config.sh

# This checks:
# ✓ System prerequisites (Node.js, Python, npm)
# ✓ Environment variables
# ✓ Project structure
# ✓ Required files
# ✓ watsonx Orchestrate CLI installation
```

**Expected output**: All checks should pass or show warnings only.

### Phase 3: Deploy Agents to watsonx Orchestrate (10 minutes)

#### Step 3.1: Install Orchestrate CLI

```bash
# Install the watsonx Orchestrate CLI
pip3 install ibm-watsonx-orchestrate

# Verify installation
orchestrate --version

# Expected: ibm-watsonx-orchestrate version x.x.x
```

#### Step 3.2: Configure Orchestrate Environment

```bash
# Add your TechZone environment
orchestrate env add demo-bank-sme \
  --url "$WXO_HOST_URL" \
  --apikey "$WXO_API_KEY" \
  --orchestration-id "$WXO_ORCHESTRATION_ID"

# Activate the environment
orchestrate env activate demo-bank-sme

# Verify connection
orchestrate env list

# Expected output should show "demo-bank-sme" as active
```

#### Step 3.3: Deploy All Agents (Quick Method)

**Option A: Use quick-deploy.sh (Recommended)**

```bash
# Make executable (if not already)
chmod +x quick-deploy.sh

# Run the automated deployment
./quick-deploy.sh

# This script will:
# 1. Validate CLI and environment
# 2. Import all 6 Python tools
# 3. Import all 4 specialist agents
# 4. Import the main orchestrator
# 5. Deploy and test the orchestrator
```

**Option B: Manual deployment with import-all.sh**

```bash
# Make executable
chmod +x import-all.sh

# Run manual import
./import-all.sh

# Expected output:
# ✅ Importing tools...
# ✅ Importing agents...
# ✅ Deployment complete!
```

#### Step 3.4: Verify Deployment

```bash
# List all deployed agents
orchestrate agents list

# You should see 5 agents:
# 1. meeting_prep_orchestrator (main)
# 2. customer_health_agent
# 3. risk_monitoring_agent
# 4. growth_opportunity_agent
# 5. customer_intelligence_agent

# List all imported tools
orchestrate tools list

# You should see 6 tools:
# 1. analyze_financial_health
# 2. calculate_health_score
# 3. identify_product_gaps
# 4. analyze_industry_benchmarks
# 5. check_credit_alerts
# 6. fetch_recent_interactions

# Test the orchestrator via CLI
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare me for a meeting with TechVenture Solutions" -r

# Expected: Comprehensive meeting prep with health score, risks, opportunities
```

### Phase 3: Launch the Carbon UI (5 minutes)

#### Step 3.1: Install Frontend Dependencies

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

#### Step 3.2: Configure Orchestrate Credentials

```bash
# Copy environment template
cp .env.example .env

# Edit .env file
nano .env  # or use your preferred editor
```

Add your credentials:

```env
VITE_WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
VITE_WXO_ORCHESTRATION_ID=your-orchestration-id-here
VITE_WXO_CRN=your-crn-here
VITE_WXO_AGENT_ID=meeting_prep_orchestrator
```

**Note**: The `VITE_WXO_AGENT_ID` should be the name of your deployed orchestrator agent (usually `meeting_prep_orchestrator`).

#### Step 3.3: Start Development Server

```bash
# Start the UI
npm run dev

# Expected output:
# VITE v6.x.x ready in xxx ms
# ➜ Local: http://localhost:3000/
```

#### Step 3.4: Access the Demo

1. Open browser: [http://localhost:3000](http://localhost:3000)
2. You should see the Carbon UI with three tabs:
   - **Dashboard** - Portfolio KPIs
   - **Customers** - Customer cards
   - **AI Assistant** - Orchestrate chat

## 🎬 Demo Walkthrough

### 1. Dashboard View

**What to show:**
- Portfolio overview with 4 KPI cards
- Total customers, health scores, at-risk count, revenue
- Clean Carbon Design System styling

**Talking points:**
- "This dashboard gives relationship managers a real-time view of their SME portfolio"
- "All metrics are powered by AI agents running in watsonx Orchestrate"

### 2. Customers View

**What to show:**
- Customer cards with health scores and risk indicators
- Credit ratings and revenue data
- Growth opportunities per customer

**Talking points:**
- "Each customer has a health score calculated by our AI agents"
- "Risk levels are color-coded: green (low), yellow (medium), red (high)"
- "Growth opportunities are automatically identified"

### 3. AI Assistant View

**What to show:**
- Embedded watsonx Orchestrate chat interface
- Live interaction with the multi-agent system

**Demo queries:**

#### Query 1: Comprehensive Meeting Prep
```
"Prepare me for a meeting with TechVenture Solutions"
```

**Expected response includes:**
- Financial health analysis
- Health score (85/100)
- Risk assessment (Low risk)
- Growth opportunities
- Recent interactions

#### Query 2: Risk Assessment
```
"What are the top risks in my SME portfolio?"
```

**Expected response includes:**
- List of at-risk customers
- Credit alerts
- Recommended actions

#### Query 3: Growth Opportunities
```
"Show me growth opportunities for GreenLeaf Manufacturing"
```

**Expected response includes:**
- Product gap analysis
- Cross-sell recommendations
- Industry benchmarks

## 🔍 Behind the Scenes

### Multi-Agent Architecture

When you ask a question, here's what happens:

1. **Meeting Prep Orchestrator** receives your query
2. It delegates to specialist agents:
   - **Customer Health Agent** → Analyzes financials
   - **Risk Monitoring Agent** → Checks credit alerts
   - **Growth Opportunity Agent** → Identifies products
   - **Customer Intelligence Agent** → Fetches interactions
3. Each agent calls Python tools with synthetic data
4. Orchestrator synthesizes responses
5. Result displayed in the UI

### Data Flow

```
User Query (UI)
    ↓
Orchestrate Web-Chat Embed
    ↓
Meeting Prep Orchestrator Agent
    ↓
Specialist Agents (parallel execution)
    ↓
Python Tools (synthetic data)
    ↓
Aggregated Response
    ↓
Display in UI
```

## 🛠️ Troubleshooting

### TechZone Environment Issues

#### Issue: Environment Not Ready After 1 Hour

**Symptoms:**
- TechZone status stuck on "Provisioning"
- No access credentials available

**Solutions:**
1. Check TechZone request page for error messages
2. Verify your IBM Cloud account has sufficient quota
3. Try a different region (us-south, eu-de, etc.)
4. Contact TechZone support if status shows "Failed"
   - Visit: https://techzone.ibm.com/help
   - Slack: #techzone-support

#### Issue: Can't Find Orchestrate Instance

**Symptoms:**
- Orchestrate instance not visible in IBM Cloud
- Resource list is empty

**Solutions:**
1. Ensure you're logged into the correct IBM Cloud account
2. Check the Resource Group specified in TechZone
3. Look under "AI / Machine Learning" in Resource List
4. Verify the environment is in "Ready" state in TechZone
5. Wait a few minutes after provisioning completes

#### Issue: Environment Expired

**Symptoms:**
- TechZone shows "Expired" or "Deleted"
- Can't access Orchestrate instance

**Solutions:**
1. Request a new environment from TechZone
2. If you need to extend:
   - Go to TechZone request page
   - Click "Extend" (if available before expiration)
   - Or provision a new environment
3. Export your agents before expiration:
   ```bash
   orchestrate agents export -n meeting_prep_orchestrator -o backup/
   ```

### Deployment Issues

#### Issue: Agents not deploying

**Symptoms:**
- `quick-deploy.sh` or `import-all.sh` fails
- `orchestrate agents list` shows no agents

**Solutions:**
1. Run validation script first:
   ```bash
   ./validate-config.sh
   ```
2. Check API key permissions:
   ```bash
   orchestrate env list
   ```
3. Verify orchestration ID is correct in .env file
4. Ensure environment is activated:
   ```bash
   orchestrate env activate demo-bank-sme
   ```
5. Check for specific error messages in deployment output

#### Issue: API Key Issues

**Symptoms:**
- Authentication errors
- "Unauthorized" or "Forbidden" messages

**Solutions:**
1. Verify API key has "Manager" role for watsonx Orchestrate
2. Check the key hasn't expired
3. Ensure the key is for the correct IBM Cloud account
4. Regenerate API key if needed:
   - Go to https://cloud.ibm.com/iam/apikeys
   - Delete old key
   - Create new key with proper permissions
5. Update .env file with new key

#### Issue: Deployment Script Fails

**Symptoms:**
- Script exits with errors
- Tools or agents not imported

**Solutions:**
1. Check orchestrate CLI is installed:
   ```bash
   orchestrate --version
   ```
2. Verify environment variables:
   ```bash
   cat .env | grep -v "^#" | grep -v "^$"
   ```
3. Test connection manually:
   ```bash
   orchestrate env list
   orchestrate agents list
   ```
4. Try importing one agent manually:
   ```bash
   orchestrate agents import -f agents/customer_health_agent.yaml
   ```

### Issue: UI not connecting to Orchestrate

**Symptoms:**
- Chat interface shows "Configuration Required"
- No response from agents

**Solutions:**
1. Verify `.env` file exists in `frontend/` directory
2. Check all environment variables are set:
   ```bash
   cat frontend/.env
   ```
3. Ensure agent is deployed:
   ```bash
   orchestrate agents list | grep meeting_prep
   ```
4. Check browser console for errors (F12)

### Issue: Frontend build errors

**Symptoms:**
- `npm install` fails
- `npm run dev` shows errors

**Solutions:**
1. Check Node.js version:
   ```bash
   node --version  # Should be 18+
   ```
2. Clear cache and reinstall:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```
3. Check for missing dependencies:
   ```bash
   npm install @carbon/react @carbon/icons-react react react-dom react-router-dom
   ```

### Issue: Tools failing

**Symptoms:**
- Agent responses show errors
- Tools not executing

**Solutions:**
1. Test tools individually:
   ```bash
   python tools/analyze_financial_health.py
   ```
2. Check Python version:
   ```bash
   python3 --version  # Should be 3.9+
   ```
3. Verify tool imports:
   ```bash
   orchestrate tools list
   ```

## 📊 Demo Checklist

Before presenting, verify:

- [ ] TechZone environment is "Ready"
- [ ] All 5 agents deployed (`orchestrate agents list`)
- [ ] All 6 tools imported (`orchestrate tools list`)
- [ ] Frontend running on http://localhost:3000
- [ ] Dashboard loads with KPIs
- [ ] Customers page shows 5 customer cards
- [ ] AI Assistant chat interface loads
- [ ] Test query returns response
- [ ] Browser is in full-screen mode (F11)
- [ ] Demo scenarios prepared

## 🎯 Quick Reference

### Essential Commands

```bash
# Check environment
orchestrate env list

# List agents
orchestrate agents list

# List tools
orchestrate tools list

# Test agent via CLI
orchestrate chat ask -n meeting_prep_orchestrator "your query" -r

# Start frontend
cd frontend && npm run dev

# Check frontend logs
# Open browser console (F12)
```

### Essential URLs

- **TechZone**: https://techzone.ibm.com/
- **IBM Cloud API Keys**: https://cloud.ibm.com/iam/apikeys
- **Demo UI**: http://localhost:3000
- **Orchestrate Docs**: https://ibm.github.io/watsonx-orchestrate-adk/

### Environment Variables

```bash
# Backend (Orchestrate CLI)
export ORCHESTRATE_API_KEY="..."
export ORCHESTRATE_INSTANCE_HOST="..."
export ORCHESTRATE_ORCHESTRATION_ID="..."

# Frontend (.env file)
VITE_WXO_HOST_URL=...
VITE_WXO_ORCHESTRATION_ID=...
VITE_WXO_CRN=...
VITE_WXO_AGENT_ID=meeting_prep_orchestrator
```

## 📝 Notes

- **TechZone environments expire** - Check your reservation end time
- **All data is synthetic** - No real customer information
- **Demo mode** - Not for production use
- **Hybrid architecture** - Agents in Orchestrate, UI runs locally

## 🎓 Next Steps

After the demo:

1. **Extend the agents** - Add more tools or specialist agents
2. **Customize the UI** - Add more pages or visualizations
3. **Deploy to production** - Build and host the frontend
4. **Integrate real data** - Connect to actual banking systems
5. **Add authentication** - Implement IBM Verify or App ID

## 📚 Additional Resources

- [watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)
- [Agent Development Kit (ADK)](https://ibm.github.io/watsonx-orchestrate-adk/)
- [Carbon Design System](https://carbondesignsystem.com/)
- [TechZone User Guide](https://techzone.ibm.com/help)

---

**Ready to demo!** 🚀

If you encounter any issues not covered here, check:
- [`README.md`](./README.md) - Main documentation
- [`TECHZONE_ACCESS_GUIDE.md`](./TECHZONE_ACCESS_GUIDE.md) - Detailed TechZone setup
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) - Technical architecture
- [`DEMO_SCRIPT.md`](./DEMO_SCRIPT.md) - Presentation guide