# 🚀 Complete Demo Access Guide

## Overview

This guide provides step-by-step instructions to access and run the **SME Meeting Prep Hybrid Demo** from start to finish.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] IBM Cloud account (IBMid)
- [ ] Access to IBM TechZone
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Python 3.9+ installed (`python3 --version`)
- [ ] Git installed
- [ ] Terminal/command line access

## 🎯 Complete Setup Flow

### Phase 1: Provision watsonx Orchestrate Environment (15 minutes)

#### Step 1.1: Access TechZone

1. Go to [IBM TechZone](https://techzone.ibm.com/)
2. Sign in with your IBMid
3. Search for: **"watsonx Orchestrate Trial with CE"**
4. Click on the environment tile

#### Step 1.2: Reserve Environment

1. Click **"Reserve"** button
2. Fill in reservation details:
   - **Purpose**: Select "Test"
   - **Purpose Description**: "SME Meeting Prep Demo"
   - **Preferred Geography**: Choose your region
   - **Start Date/Time**: Now (or schedule)
   - **End Date/Time**: +12 hours (or longer)
3. Click **"Submit"**
4. Wait ~15 minutes for provisioning

#### Step 1.3: Extract Credentials

Once provisioned (status = "Ready"):

1. Go to **My Reservations** → Click your reservation
2. Navigate to **"Reservation Details"** tab
3. Copy these values:

```
Orchestrate Instance Host: https://us-south.watson-orchestrate.cloud.ibm.com
Orchestration ID: [copy from TechZone]
CRN: [copy from TechZone]
```

4. Generate IBM Cloud API Key:
   - Go to [IBM Cloud API Keys](https://cloud.ibm.com/iam/apikeys)
   - Click **"Create"**
   - Name: "Orchestrate Demo"
   - Copy the API key (save it securely!)

### Phase 2: Deploy Agents to watsonx Orchestrate (10 minutes)

#### Step 2.1: Install Orchestrate CLI

```bash
# Install the ADK CLI
pip install ibm-watsonx-orchestrate

# Verify installation
orchestrate --version
```

#### Step 2.2: Configure Environment

```bash
# Navigate to demo directory
cd demo-BANK-001-sme-meeting-prep

# Set environment variables
export ORCHESTRATE_API_KEY="your-ibm-cloud-api-key"
export ORCHESTRATE_INSTANCE_HOST="your-orchestrate-host"
export ORCHESTRATE_ORCHESTRATION_ID="your-orchestration-id"

# Add and activate environment
orchestrate env add prod \
  --host "$ORCHESTRATE_INSTANCE_HOST" \
  --orchestration-id "$ORCHESTRATE_ORCHESTRATION_ID" \
  --api-key "$ORCHESTRATE_API_KEY"

orchestrate env activate prod

# Verify connection
orchestrate env list
```

#### Step 2.3: Deploy All Agents

```bash
# Run the deployment script
./import-all.sh

# Expected output:
# ✅ Importing tools...
# ✅ Importing agents...
# ✅ Deployment complete!
```

#### Step 2.4: Verify Deployment

```bash
# List deployed agents
orchestrate agents list

# You should see:
# - meeting_prep_orchestrator
# - customer_health_agent
# - risk_monitoring_agent
# - growth_opportunity_agent
# - customer_intelligence_agent

# Test the orchestrator
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare me for a meeting with TechVenture Solutions" -r
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

### Issue: Agents not deploying

**Symptoms:**
- `import-all.sh` fails
- `orchestrate agents list` shows no agents

**Solutions:**
1. Check API key permissions:
   ```bash
   orchestrate env list
   ```
2. Verify orchestration ID is correct
3. Ensure environment is activated:
   ```bash
   orchestrate env activate prod
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