#!/bin/bash

# Import script for watsonx Orchestrate SME Meeting Prep Demo
# This script imports all tools and agents in the correct dependency order

set -e  # Exit on any error

echo "========================================="
echo "watsonx Orchestrate Import Script"
echo "Demo: SME Relationship Manager Copilot"
echo "========================================="
echo ""

# Check if orchestrate CLI is available
if ! command -v orchestrate &> /dev/null; then
    echo "ERROR: orchestrate CLI not found"
    echo "Please install: pip install ibm-watsonx-orchestrate"
    exit 1
fi

# Check if an environment is active
ACTIVE_ENV=$(orchestrate env list 2>/dev/null | grep "* " | awk '{print $2}')
if [ -z "$ACTIVE_ENV" ]; then
    echo "ERROR: No active watsonx Orchestrate environment"
    echo "Please run: orchestrate env activate <env-name>"
    exit 1
fi

echo "Active environment: $ACTIVE_ENV"
echo ""

# Step 1: Import Tools
echo "Step 1/3: Importing Python tools..."
echo "-----------------------------------"

TOOLS=(
    "tools/analyze_financial_health.py"
    "tools/calculate_health_score.py"
    "tools/identify_product_gaps.py"
    "tools/analyze_industry_benchmarks.py"
    "tools/check_credit_alerts.py"
    "tools/fetch_recent_interactions.py"
)

for tool in "${TOOLS[@]}"; do
    echo "Importing: $tool"
    orchestrate tools import -f "$tool"
    if [ $? -eq 0 ]; then
        echo "✓ Successfully imported $(basename $tool)"
    else
        echo "✗ Failed to import $(basename $tool)"
        exit 1
    fi
    echo ""
done

echo "All tools imported successfully!"
echo ""

# Step 2: Import Sub-Agents
echo "Step 2/3: Importing specialized sub-agents..."
echo "----------------------------------------------"

SUB_AGENTS=(
    "agents/customer_health_agent.yaml"
    "agents/growth_opportunity_agent.yaml"
    "agents/risk_monitoring_agent.yaml"
    "agents/customer_intelligence_agent.yaml"
)

for agent in "${SUB_AGENTS[@]}"; do
    echo "Importing: $agent"
    orchestrate agents import -f "$agent"
    if [ $? -eq 0 ]; then
        echo "✓ Successfully imported $(basename $agent .yaml)"
    else
        echo "✗ Failed to import $(basename $agent .yaml)"
        exit 1
    fi
    echo ""
done

echo "All sub-agents imported successfully!"
echo ""

# Step 3: Import Main Orchestrator
echo "Step 3/3: Importing main orchestrator agent..."
echo "-----------------------------------------------"

echo "Importing: agents/meeting_prep_orchestrator.yaml"
orchestrate agents import -f "agents/meeting_prep_orchestrator.yaml"
if [ $? -eq 0 ]; then
    echo "✓ Successfully imported meeting_prep_orchestrator"
else
    echo "✗ Failed to import meeting_prep_orchestrator"
    exit 1
fi
echo ""

# Verification
echo "========================================="
echo "Import Complete! Verifying..."
echo "========================================="
echo ""

echo "Listing imported agents:"
orchestrate agents list | grep -E "(meeting_prep_orchestrator|customer_health_agent|growth_opportunity_agent|risk_monitoring_agent|customer_intelligence_agent)"
echo ""

echo "Listing imported tools:"
orchestrate tools list | grep -E "(analyze_financial_health|calculate_health_score|identify_product_gaps|analyze_industry_benchmarks|check_credit_alerts|fetch_recent_interactions)"
echo ""

echo "========================================="
echo "✓ All artifacts imported successfully!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Test the agent:"
echo "   orchestrate chat ask -n meeting_prep_orchestrator \"Prepare me for my meeting with TechVenture Solutions\" -r"
echo ""
echo "2. Deploy the agent:"
echo "   orchestrate agents deploy -n meeting_prep_orchestrator"
echo ""
echo "3. View deployment details:"
echo "   orchestrate agents get -n meeting_prep_orchestrator"
echo ""

# Made with Bob
