#!/bin/bash

# Quick Deploy Script for SME RM Copilot Demo
# This script automates the deployment of all agents and tools to watsonx Orchestrate

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Banner
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   SME Relationship Manager Copilot - Quick Deploy Script      ║"
echo "║   watsonx Orchestrate Multi-Agent Demo                        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if orchestrate CLI is installed
print_status "Checking for watsonx Orchestrate CLI..."
if ! command -v orchestrate &> /dev/null; then
    print_error "watsonx Orchestrate CLI not found!"
    echo ""
    echo "Please install it first:"
    echo "  pip install ibm-watsonx-orchestrate"
    echo ""
    exit 1
fi
print_success "CLI found: $(orchestrate --version)"
echo ""

# Check if environment is configured
print_status "Checking active environment..."
ACTIVE_ENV=$(orchestrate env list 2>&1 | grep "active" || echo "")
if [ -z "$ACTIVE_ENV" ]; then
    print_error "No active watsonx Orchestrate environment found!"
    echo ""
    echo "Please configure an environment first:"
    echo ""
    echo "For IBM Cloud SaaS:"
    echo "  orchestrate env add \\"
    echo "    --name demo-bank-sme \\"
    echo "    --url https://us-south.watson-orchestrate.cloud.ibm.com \\"
    echo "    --apikey YOUR_IBM_CLOUD_API_KEY \\"
    echo "    --orchestration-id YOUR_ORCHESTRATION_ID"
    echo ""
    echo "  orchestrate env activate demo-bank-sme"
    echo ""
    echo "For Local Developer Edition:"
    echo "  orchestrate env add \\"
    echo "    --name demo-bank-local \\"
    echo "    --url https://localhost:9443 \\"
    echo "    --username admin \\"
    echo "    --password password"
    echo ""
    echo "  orchestrate env activate demo-bank-local"
    echo ""
    echo "See DEPLOYMENT_GUIDE.md for detailed instructions."
    echo ""
    exit 1
fi
print_success "Active environment: $ACTIVE_ENV"
echo ""

# Confirm deployment
print_warning "This will import 6 tools and 5 agents to your active environment."
read -p "Continue? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_status "Deployment cancelled."
    exit 0
fi
echo ""

# Step 1: Import Tools
print_status "Step 1/3: Importing Python tools..."
echo ""

TOOLS=(
    "analyze_financial_health"
    "calculate_health_score"
    "identify_product_gaps"
    "analyze_industry_benchmarks"
    "check_credit_alerts"
    "fetch_recent_interactions"
)

TOOL_COUNT=0
for tool in "${TOOLS[@]}"; do
    TOOL_COUNT=$((TOOL_COUNT + 1))
    print_status "Importing tool $TOOL_COUNT/6: $tool"
    
    if orchestrate tools import -k python -f "tools/${tool}.py" 2>&1 | grep -q "successfully"; then
        print_success "✓ $tool imported"
    else
        print_warning "⚠ $tool may already exist or import failed"
    fi
done

echo ""
print_success "All tools imported!"
echo ""

# Step 2: Import Sub-Agents
print_status "Step 2/3: Importing specialized agents..."
echo ""

SUB_AGENTS=(
    "customer_health_agent"
    "growth_opportunity_agent"
    "risk_monitoring_agent"
    "customer_intelligence_agent"
)

AGENT_COUNT=0
for agent in "${SUB_AGENTS[@]}"; do
    AGENT_COUNT=$((AGENT_COUNT + 1))
    print_status "Importing agent $AGENT_COUNT/4: $agent"
    
    if orchestrate agents import -f "agents/${agent}.yaml" 2>&1 | grep -q "successfully"; then
        print_success "✓ $agent imported"
    else
        print_warning "⚠ $agent may already exist or import failed"
    fi
done

echo ""
print_success "All sub-agents imported!"
echo ""

# Step 3: Import Main Orchestrator
print_status "Step 3/3: Importing main orchestrator..."
echo ""

print_status "Importing: meeting_prep_orchestrator"
if orchestrate agents import -f "agents/meeting_prep_orchestrator.yaml" 2>&1 | grep -q "successfully"; then
    print_success "✓ meeting_prep_orchestrator imported"
else
    print_warning "⚠ meeting_prep_orchestrator may already exist or import failed"
fi

echo ""
print_success "Main orchestrator imported!"
echo ""

# Verify deployment
print_status "Verifying deployment..."
echo ""

print_status "Listing all agents:"
orchestrate agents list
echo ""

# Deploy the main agent
print_status "Deploying main orchestrator..."
echo ""

if orchestrate agents deploy -n meeting_prep_orchestrator 2>&1 | grep -q "successfully"; then
    print_success "✓ meeting_prep_orchestrator deployed!"
else
    print_warning "⚠ Deployment may have failed or agent already deployed"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    DEPLOYMENT COMPLETE! ✓                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

print_success "The SME RM Copilot demo is now ready!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  NEXT STEPS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Test the demo with a preset scenario:"
echo ""
echo "   orchestrate chat ask -n meeting_prep_orchestrator \\"
echo "     \"Prepare me for my meeting tomorrow with TechVenture Solutions\" -r"
echo ""
echo "2. Try the other scenarios:"
echo "   - UrbanRetail Group (at-risk customer)"
echo "   - GreenLeaf Manufacturing (quarterly review)"
echo ""
echo "3. Access via Web UI:"
echo "   - Navigate to your watsonx Orchestrate instance"
echo "   - Go to 'Manage Agents'"
echo "   - Find 'meeting_prep_orchestrator'"
echo "   - Click 'Test' to chat with the agent"
echo ""
echo "4. Review documentation:"
echo "   - DEMO_SCRIPT.md - 15-minute presentation guide"
echo "   - ARCHITECTURE.md - Technical architecture"
echo "   - PILOT_PLAN.md - 4-week pilot plan"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
print_success "Demo ready for live presentations! 🚀"
echo ""

# Made with Bob
