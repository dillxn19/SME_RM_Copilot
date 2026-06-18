# SME Relationship Manager AI Copilot

**Multi-Agent AI System for Commercial Banking** | Built with IBM watsonx Orchestrate

---

## Overview

An AI-powered copilot that helps relationship managers prepare for SME client meetings by automatically analyzing customer health, identifying risks, and surfacing growth opportunities across multiple data sources.

**Business Impact:**
- ⏱️ **80% faster** meeting preparation (from 2 hours to 20 minutes)
- 📊 **Real-time insights** from financial data, transaction history, and market trends
- 🎯 **Proactive relationship management** with automated risk alerts
- 💰 **Increased revenue** through AI-identified cross-sell opportunities

---

## Architecture

### Multi-Agent System (5 Agents)
```
Meeting Prep Orchestrator (Main Agent)
├── Customer Intelligence Agent → Recent interactions & sentiment
├── Customer Health Agent → Financial metrics & health score
├── Risk Monitoring Agent → Credit alerts & compliance
└── Growth Opportunity Agent → Product gaps & upsell potential
```

### Technology Stack
- **Platform**: IBM watsonx Orchestrate (SaaS)
- **Model**: Groq OpenAI GPT-OSS-120B
- **Tools**: 6 Python tools with embedded synthetic data
- **Data**: 10 fictional SME customers with 90-day history

---

## Quick Start

### Prerequisites
- IBM Cloud account with watsonx Orchestrate access
- `orchestrate` CLI installed ([Installation Guide](https://ibm.github.io/watsonx-orchestrate-adk-docs/))
- Python 3.9+ (for local tool development)

### Deployment (5 minutes)

```bash
# 1. Clone repository
git clone <repo-url>
cd demo-BANK-001-sme-meeting-prep

# 2. Configure credentials
cp .env.example .env
# Edit .env with your watsonx Orchestrate credentials

# 3. Deploy all agents and tools
chmod +x quick-deploy.sh
./quick-deploy.sh

# 4. Test the demo
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare for meeting with CUST-001 (Apex Manufacturing)" -r
```

---

## Configuration

### Required Environment Variables

Create a `.env` file with the following:

```bash
# watsonx Orchestrate Connection
WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
WXO_ORCHESTRATION_ID=<your-orchestration-id>
WXO_CRN=<your-cloud-resource-name>

# IBM Cloud Authentication
IBM_CLOUD_API_KEY=<your-api-key>

# Optional: watsonx.ai Integration
WATSONX_API_KEY=<same-as-ibm-cloud-api-key>
WATSONX_PROJECT_ID=<your-project-id>
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

### Getting Credentials

**Option 1: Use TechZone** (Recommended for demos)
- Provision environment: [TechZone watsonx Orchestrate](https://techzone.ibm.com)
- See `TECHZONE_ACCESS_GUIDE.md` for detailed instructions

**Option 2: Use Existing Instance**
1. Access your watsonx Orchestrate instance in IBM Cloud
2. Navigate to instance details to find Orchestration ID and CRN
3. Generate API key: IBM Cloud → Manage → Access (IAM) → API keys

---

## Demo Scenarios

### Pre-loaded Customers (10 Fictional SMEs)

| ID | Company | Industry | Health Score | Use Case |
|----|---------|----------|--------------|----------|
| CUST-001 | Apex Manufacturing | Manufacturing | 85 | Growth opportunities |
| CUST-005 | Greenfield Healthcare | Healthcare | 81 | Cross-sell potential |
| CUST-008 | Quantum Telecom | Telecommunications | 62 | Risk detection |

**All data is synthetic** - no real customer information is used.

### Example Queries

**Scenario 1: High-Value Customer Analysis**
```bash
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare for meeting with CUST-001 (Apex Manufacturing)" -r
```

**Expected Output:**
- Customer health score: 85/100 (Excellent)
- Revenue trend: ↑15% YoY
- Risk alerts: None
- Growth opportunities: Equipment financing ($500K), Trade finance
- Talking points: 4 actionable recommendations

**Scenario 2: At-Risk Customer**
```bash
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare for meeting with CUST-008 (Quantum Telecom)" -r
```

**Expected Output:**
- Customer health score: 62/100 (Watch)
- Risk alerts: Payment delays, declining revenue
- Retention strategies: 3 recommendations
- Talking points: Risk mitigation focus

**Scenario 3: Growth Opportunity**
```bash
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare for meeting with CUST-005 (Greenfield Healthcare)" -r
```

**Expected Output:**
- Customer health score: 81/100 (Good)
- Growth indicators: Expansion plans, hiring
- Cross-sell opportunities: 3 products identified
- Revenue potential: $150K annual

---

## Repository Structure

```
demo-BANK-001-sme-meeting-prep/
├── README.md                          # This file
├── TECHZONE_ACCESS_GUIDE.md          # TechZone provisioning guide
├── ARCHITECTURE.md                    # Technical architecture
├── DEMO_SCRIPT.md                     # Presentation guide
├── quick-deploy.sh                    # One-command deployment
├── import-all.sh                      # Manual import script
├── .env.example                       # Environment template
├── agents/                            # 5 agent YAML files
│   ├── meeting_prep_orchestrator.yaml
│   ├── customer_intelligence_agent.yaml
│   ├── customer_health_agent.yaml
│   ├── risk_monitoring_agent.yaml
│   └── growth_opportunity_agent.yaml
└── tools/                             # 6 Python tools
    ├── fetch_recent_interactions.py
    ├── analyze_financial_health.py
    ├── calculate_health_score.py
    ├── check_credit_alerts.py
    ├── identify_product_gaps.py
    └── analyze_industry_benchmarks.py
```

---

## Agent Details

### Meeting Prep Orchestrator
**Role**: Main coordinator  
**Function**: Orchestrates all specialist agents and synthesizes insights  
**Output**: Comprehensive meeting preparation summary with talking points

### Customer Intelligence Agent
**Role**: Interaction analysis  
**Function**: Analyzes recent customer interactions and sentiment  
**Data Sources**: CRM logs, email history, call transcripts

### Customer Health Agent
**Role**: Financial analysis  
**Function**: Evaluates financial metrics and calculates health score  
**Metrics**: Revenue trends, cash flow, profitability, payment history

### Risk Monitoring Agent
**Role**: Risk assessment  
**Function**: Identifies credit risks and compliance issues  
**Alerts**: Payment delays, credit score changes, regulatory flags

### Growth Opportunity Agent
**Role**: Revenue optimization  
**Function**: Identifies cross-sell and upsell opportunities  
**Analysis**: Product gaps, industry benchmarks, expansion potential

---

## Tool Details

### 1. fetch_recent_interactions
Retrieves last 30 days of customer touchpoints including:
- Meeting notes and outcomes
- Email correspondence
- Phone call summaries
- Sentiment analysis

### 2. analyze_financial_health
Analyzes financial metrics:
- Revenue trends (YoY, QoQ)
- Cash flow analysis
- Profitability ratios
- Working capital trends

### 3. calculate_health_score
Computes composite health score (0-100) based on:
- Financial performance (40%)
- Payment history (30%)
- Relationship strength (20%)
- Growth trajectory (10%)

### 4. check_credit_alerts
Monitors credit and compliance:
- Credit score changes
- Payment delays
- Covenant breaches
- Regulatory issues

### 5. identify_product_gaps
Identifies revenue opportunities:
- Current product usage
- Available products not utilized
- Peer comparison
- Estimated revenue potential

### 6. analyze_industry_benchmarks
Provides market context:
- Industry performance metrics
- Peer comparison
- Market trends
- Competitive positioning

---

## Development

### Local Testing

```bash
# Test individual tools
cd tools
python fetch_recent_interactions.py

# Test agent locally (requires orchestrate CLI)
orchestrate chat ask -n meeting_prep_orchestrator \
  "Test query" -r --debug
```

### Adding New Tools

1. Create tool in `tools/` directory
2. Follow Python `@tool` decorator pattern
3. Include Google-style docstrings
4. Use synthetic data only
5. Import via `import-all.sh`

### Adding New Agents

1. Create agent YAML in `agents/` directory
2. Define `kind: native` and `spec_version: v1`
3. List required tools in `tools:` section
4. Deploy via `orchestrate agents deploy`

---

## Troubleshooting

### Environment Not Provisioning
- Check TechZone request status
- Verify IBM Cloud account quota
- Contact TechZone support if status shows "Failed"

### Deployment Fails
```bash
# Verify orchestrate CLI
orchestrate --version

# Check environment variables
cat .env | grep -v "^#" | grep -v "^$"

# Test connection
orchestrate env list
```

### Agent Not Responding
```bash
# List deployed agents
orchestrate agents list

# Check agent details
orchestrate agents get -n meeting_prep_orchestrator

# View logs
orchestrate chat ask -n meeting_prep_orchestrator "test" -r --debug
```

---

## Documentation

- **TECHZONE_ACCESS_GUIDE.md** - Complete TechZone provisioning guide
- **ARCHITECTURE.md** - Detailed technical architecture
- **DEMO_SCRIPT.md** - Presentation guide with timing
- **[watsonx Orchestrate Docs](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)** - Official documentation
- **[ADK Documentation](https://ibm.github.io/watsonx-orchestrate-adk-docs/)** - Agent Development Kit

---

## Use Cases

### Commercial Banking
- SME relationship management
- Credit risk assessment
- Portfolio management
- Customer retention

### Wealth Management
- Client meeting preparation
- Portfolio review automation
- Risk profiling
- Investment recommendations

### Retail Banking
- Customer service automation
- Product recommendations
- Churn prediction
- Onboarding optimization

---

## Roadmap

### Phase 1: Core Functionality (Complete)
- ✅ Multi-agent orchestration
- ✅ 6 analytical tools
- ✅ Synthetic data generation
- ✅ Demo scenarios

### Phase 2: Enhanced Integration (Planned)
- [ ] Real-time CRM integration
- [ ] Live financial data feeds
- [ ] Email/calendar integration
- [ ] Mobile app support

### Phase 3: Advanced Features (Future)
- [ ] Predictive analytics
- [ ] Natural language reporting
- [ ] Voice interface
- [ ] Multi-language support

---

## Contributing

This is a demonstration project. For production use:

1. Replace synthetic data with real data sources
2. Implement proper authentication and authorization
3. Add comprehensive error handling
4. Include monitoring and logging
5. Conduct security review
6. Perform load testing

---

## License

This demo is for IBM internal use and client demonstrations only.

---

## Support

For questions or issues:
- **TechZone**: https://techzone.ibm.com/help
- **watsonx Orchestrate**: https://www.ibm.com/docs/en/watsonx/watson-orchestrate
- **ADK Documentation**: https://ibm.github.io/watsonx-orchestrate-adk-docs/

---

**Built with IBM watsonx Orchestrate** | Demo Version 1.0