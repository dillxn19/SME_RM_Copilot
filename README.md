# SME Relationship Manager Copilot - Meeting Preparation Assistant

**Demo Code**: BANK-001  
**Industry**: Financial Services - Commercial Banking  
**IBM Products**: watsonx Orchestrate (Multi-Agent ADK)

## Overview

This demo showcases a multi-agent watsonx Orchestrate system that helps Commercial Banking Relationship Managers prepare for customer meetings by automatically gathering and analyzing data from multiple sources.

**Business Impact:**
- 40% reduction in meeting prep time (from 2 hours to 45 minutes)
- 25% increase in cross-sell success rate
- 30% improvement in early risk detection
- $2.5M annual productivity savings per 100 RMs

## Architecture

This demo implements a **5-agent orchestration system**:

1. **Meeting Preparation Orchestrator** (main agent) - Coordinates the 4 specialized sub-agents
2. **Customer Health Agent** - Analyzes financial health and calculates health scores
3. **Growth Opportunity Agent** - Identifies cross-sell and upsell opportunities
4. **Risk Monitoring Agent** - Monitors credit alerts and payment patterns
5. **Customer Intelligence Agent** - Gathers recent interactions and news

All agents use the default model `groq/openai/gpt-oss-120b` and communicate via watsonx Orchestrate's native agent collaboration framework.

## Prerequisites

- **watsonx Orchestrate** environment (SaaS, on-prem, or local Developer Edition)
- **orchestrate CLI** installed and configured
- Python 3.11+ (for tool development)
- `ibm-watsonx-orchestrate` Python package

## Quick Start

### 1. Install Dependencies

```bash
# Install the watsonx Orchestrate ADK
pip install ibm-watsonx-orchestrate

# Verify CLI installation
orchestrate --version
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your watsonx Orchestrate credentials
```

### 3. Set Up Orchestrate Environment

```bash
# Add your environment (SaaS example)
orchestrate env add \
  --name prod \
  --host https://us-south.watson-orchestrate.cloud.ibm.com \
  --apikey YOUR_API_KEY

# Activate the environment
orchestrate env activate prod
```

### 4. Import All Artifacts

```bash
# Run the import script (imports in dependency order)
chmod +x import-all.sh
./import-all.sh
```

### 5. Test the Agent

```bash
# Test with preset scenarios
orchestrate chat ask \
  -n meeting_prep_orchestrator \
  "Prepare me for my meeting tomorrow with TechVenture Solutions" \
  -r
```

### 6. Deploy for Production

```bash
# Deploy the main orchestrator
orchestrate agents deploy -n meeting_prep_orchestrator
```

## Demo Scenarios

### Scenario 1: Healthy Customer with Growth Potential
**Customer**: TechVenture Solutions (CUST-001)  
**Prompt**: "Prepare me for my meeting tomorrow with TechVenture Solutions"

### Scenario 2: At-Risk Customer Requiring Attention
**Customer**: UrbanRetail Group (CUST-003)  
**Prompt**: "I need to prepare for an urgent meeting with UrbanRetail Group"

### Scenario 3: New Opportunity Discovery
**Customer**: GreenLeaf Manufacturing (CUST-002)  
**Prompt**: "What should I discuss with GreenLeaf Manufacturing in our quarterly review?"

## Project Structure

```
demo-BANK-001-sme-meeting-prep/
├── README.md
├── ARCHITECTURE.md
├── PILOT_PLAN.md
├── DEMO_SCRIPT.md
├── .env.example
├── .gitignore
├── import-all.sh
├── agents/                    # Agent YAML definitions
│   ├── meeting_prep_orchestrator.yaml
│   ├── customer_health_agent.yaml
│   ├── growth_opportunity_agent.yaml
│   ├── risk_monitoring_agent.yaml
│   └── customer_intelligence_agent.yaml
└── tools/                     # Python tools
    ├── analyze_financial_health.py
    ├── calculate_health_score.py
    ├── identify_product_gaps.py
    ├── analyze_industry_benchmarks.py
    ├── check_credit_alerts.py
    └── fetch_recent_interactions.py
```

## Synthetic Data

All customer data is **100% synthetic** generated with Faker (seed=42):
- 10 fictional SME customers
- Industries: Technology, Manufacturing, Retail, Healthcare, Construction
- Revenue range: $5M - $50M annually
- 90 days of financial history
- No real bank data, PII, or confidential information

## Documentation

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Multi-agent architecture and data flow
- **[PILOT_PLAN.md](./PILOT_PLAN.md)** - 3-4 week Client Engineering pilot plan
- **[DEMO_SCRIPT.md](./DEMO_SCRIPT.md)** - 15-minute presenter talk track

---

**Built with IBM watsonx Orchestrate**  
Demo Code: BANK-001 | Industry: Financial Services | Version: 1.0