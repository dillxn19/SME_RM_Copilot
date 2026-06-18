# SME Relationship Manager AI Copilot Demo

**Built with IBM watsonx Orchestrate**

A multi-agent AI system that helps relationship managers prepare for SME client meetings by analyzing financial health, monitoring risks, and identifying growth opportunities.

---

## 🎯 What This Demo Shows

- **5 AI Agents** working together to prepare for client meetings
- **Multi-agent orchestration** with watsonx Orchestrate
- **Real-time financial analysis** and risk monitoring
- **Professional Carbon Design System UI** with embedded AI chat
- **Synthetic SME banking data** (5 customers, 6 analysis tools)

---

## 📋 Prerequisites

### 1. Request TechZone Environment via Bob

**Ask Bob to provision a watsonx Orchestrate environment:**

```
"Create a TechZone environment for watsonx Orchestrate in us-south region"
```

Bob will use the TechZone MCP to provision:
- watsonx Orchestrate (lite)
- Watson ML
- Watson Studio
- watsonx.governance
- IBM Cloud Code Engine
- Cloud Object Storage

**Save these from Bob's response:**
- IBM Cloud API Key
- Orchestration ID
- Account details

### 2. Install Required Tools

```bash
# IBM Cloud CLI
curl -fsSL https://clis.cloud.ibm.com/install/osx | sh

# watsonx Orchestrate CLI
pip3 install ibm-watsonx-orchestrate

# Node.js (if not installed)
brew install node
```

---

## 🚀 Quick Start

### Step 1: Get watsonx Orchestrate API Key

1. Login to watsonx Orchestrate:
   ```
   https://us-south.watson-orchestrate.cloud.ibm.com
   ```

2. Click user icon (top right) → **Settings** → **API details** tab

3. Click **"Generate API key"** → Create in IBM Cloud IAM

4. **Copy and save the API key** (you won't see it again!)

### Step 2: Configure Environment

```bash
cd demo-BANK-001-sme-meeting-prep

# Edit .env with your credentials
nano .env
```

Update these values:
```env
ORCHESTRATE_API_KEY=<YOUR_WXO_API_KEY>
ORCHESTRATE_ORCHESTRATION_ID=<FROM_TECHZONE>
ORCHESTRATE_CRN=<FROM_TECHZONE>
```

### Step 3: Deploy Agents

```bash
# Source environment
source .env

# Configure Orchestrate CLI
orchestrate env add -n prod \
  -u https://us-south.watson-orchestrate.cloud.ibm.com \
  --type ibm_iam

# Activate with your API key
orchestrate env activate prod --api-key "$ORCHESTRATE_API_KEY"

# Deploy agents and tools
chmod +x import-all.sh
./import-all.sh

# Verify deployment
orchestrate agents list
orchestrate tools list
```

**Expected:** 5 agents and 6 tools deployed

### Step 4: Configure Frontend

```bash
# Edit frontend/.env
nano frontend/.env
```

Update with your values:
```env
VITE_WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
VITE_WXO_ORCHESTRATION_ID=<YOUR_ORCHESTRATION_ID>
VITE_WXO_CRN=<YOUR_CRN>
VITE_WXO_AGENT_ID=meeting_prep_orchestrator
```

### Step 5: Start Demo

```bash
cd frontend
npm install
npm run dev
```

**Open:** http://localhost:3000

---

## 🎨 Demo Pages

### 1. Dashboard (`/`)
- Portfolio KPIs (Total Assets, Risk Score, Growth Opportunities, Active Alerts)
- Customer health overview
- Recent activity feed

### 2. Customers (`/customers`)
- 5 SME customer cards with health scores
- Financial metrics and risk indicators
- Quick access to customer details

### 3. AI Assistant (`/ai-chat`)
- Live watsonx Orchestrate chat interface
- Multi-agent orchestration in action
- Real-time analysis and recommendations

---

## 💬 Demo Queries

Try these in the AI Assistant:

```
"Prepare me for a meeting with TechVenture Solutions"

"What are the top risks in my SME portfolio?"

"Show me growth opportunities for GreenLeaf Manufacturing"

"Analyze the financial health of BlueSky Retail"

"What credit alerts do I need to know about?"
```

---

## 🤖 Architecture

### AI Agents (5)

1. **Meeting Prep Orchestrator** - Main coordinator
2. **Customer Health Agent** - Financial analysis
3. **Risk Monitoring Agent** - Credit & compliance
4. **Growth Opportunity Agent** - Cross-sell identification
5. **Customer Intelligence Agent** - Interaction insights

### Tools (6)

1. `analyze_financial_health` - Balance sheet analysis
2. `calculate_health_score` - Overall health scoring
3. `check_credit_alerts` - Credit risk monitoring
4. `fetch_recent_interactions` - Interaction history
5. `identify_product_gaps` - Product opportunity analysis
6. `analyze_industry_benchmarks` - Peer comparison

### Tech Stack

- **Backend:** watsonx Orchestrate (multi-agent orchestration)
- **Frontend:** React 18 + Vite + Carbon Design System v11
- **Data:** Synthetic SME banking data (5 customers)
- **Deployment:** IBM Cloud / Local development

---

## 🔧 Troubleshooting

### Authentication Expired

Orchestrate tokens expire every 2 hours. Re-activate:

```bash
source .env
orchestrate env activate prod --api-key "$ORCHESTRATE_API_KEY"
```

### Agents Not Deploying

```bash
# Check environment
orchestrate env list

# Re-activate
orchestrate env activate prod --api-key "$ORCHESTRATE_API_KEY"

# Try deploying one agent manually
orchestrate agents import agents/customer_health_agent.yaml
```

### Frontend Can't Connect

1. Get correct agent ID: `orchestrate agents list`
2. Update `frontend/.env` with `VITE_WXO_AGENT_ID`
3. Restart: `npm run dev`

---

## 📚 Additional Documentation

- **ARCHITECTURE.md** - Technical architecture details
- **DEMO_SCRIPT.md** - Presentation guide with timing
- **PILOT_PLAN.md** - 3-4 week Client Engineering plan

---

## ⚠️ Important Notes

- **All data is synthetic** - No real customer information
- **TechZone environment expires** - Check expiration date
- **Orchestrate tokens expire every 2 hours** - Re-activate as needed
- **IBM Cloud API key ≠ Orchestrate API key** - Get Orchestrate key from UI

---

## ✅ Success Checklist

- [ ] TechZone environment provisioned via Bob
- [ ] watsonx Orchestrate API key generated
- [ ] Environment configured (.env files)
- [ ] Orchestrate CLI activated
- [ ] 5 agents deployed
- [ ] 6 tools deployed
- [ ] Frontend configured and running
- [ ] All 3 pages tested
- [ ] AI Assistant queries tested

---

## 🎉 Demo Ready!

Once all checklist items are complete, your demo is ready to present.

**Demo URL:** http://localhost:3000

**Built with IBM watsonx Orchestrate**

---

## 📞 Support

For issues or questions:
1. Check troubleshooting section above
2. Review ARCHITECTURE.md for technical details
3. Consult DEMO_SCRIPT.md for presentation guidance

---

**Demo Code:** DEMO-BANK-001  
**Industry:** Financial Services  
**Use Case:** SME Relationship Management  
**IBM Products:** watsonx Orchestrate, Watson ML, watsonx.governance