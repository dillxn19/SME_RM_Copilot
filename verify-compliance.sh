#!/bin/bash

# Compliance Verification Script for watsonx Orchestrate Agent Demo
# DEMO-BANK-001: SME Relationship Manager Copilot

echo "=========================================="
echo "watsonx Orchestrate Agent Demo Compliance Check"
echo "DEMO-BANK-001: SME Meeting Prep Assistant"
echo "=========================================="
echo ""

PASS=0
FAIL=0
WARN=0

# Function to check file exists
check_file() {
    if [ -f "$1" ]; then
        echo "✅ PASS: $2"
        ((PASS++))
        return 0
    else
        echo "❌ FAIL: $2"
        ((FAIL++))
        return 1
    fi
}

# Function to check directory exists
check_dir() {
    if [ -d "$1" ]; then
        echo "✅ PASS: $2"
        ((PASS++))
        return 0
    else
        echo "❌ FAIL: $2"
        ((FAIL++))
        return 1
    fi
}

# Function to check content in file
check_content() {
    if grep -q "$2" "$1" 2>/dev/null; then
        echo "✅ PASS: $3"
        ((PASS++))
        return 0
    else
        echo "❌ FAIL: $3"
        ((FAIL++))
        return 1
    fi
}

# Function to check NO content in file
check_no_content() {
    if ! grep -q "$2" "$1" 2>/dev/null; then
        echo "✅ PASS: $3"
        ((PASS++))
        return 0
    else
        echo "❌ FAIL: $3"
        ((FAIL++))
        return 1
    fi
}

echo "=== 1. WATSONX ORCHESTRATE AGENT STRUCTURE ==="
check_dir "agents" "agents/ directory exists"
check_dir "tools" "tools/ directory exists"
check_file "import-all.sh" "import-all.sh script exists"
check_file ".env.example" ".env.example exists"
check_file ".gitignore" ".gitignore exists"
echo ""

echo "=== 2. AGENT YAML FILES (5 AGENTS) ==="
check_file "agents/meeting_prep_orchestrator.yaml" "Main orchestrator agent YAML"
check_file "agents/customer_health_agent.yaml" "Customer health sub-agent YAML"
check_file "agents/growth_opportunity_agent.yaml" "Growth opportunity sub-agent YAML"
check_file "agents/risk_monitoring_agent.yaml" "Risk monitoring sub-agent YAML"
check_file "agents/customer_intelligence_agent.yaml" "Customer intelligence sub-agent YAML"
echo ""

echo "=== 3. AGENT YAML SCHEMA COMPLIANCE ==="
check_content "agents/meeting_prep_orchestrator.yaml" "spec_version: v1" "Orchestrator has spec_version: v1"
check_content "agents/meeting_prep_orchestrator.yaml" "kind: native" "Orchestrator has kind: native"
check_content "agents/meeting_prep_orchestrator.yaml" "llm: groq/openai/gpt-oss-120b" "Orchestrator uses default LLM"
check_content "agents/meeting_prep_orchestrator.yaml" "collaborators:" "Orchestrator has collaborators field"
check_content "agents/customer_health_agent.yaml" "tools:" "Sub-agent has tools field"
echo ""

echo "=== 4. PYTHON TOOLS (6 TOOLS) ==="
check_file "tools/analyze_financial_health.py" "analyze_financial_health tool"
check_file "tools/calculate_health_score.py" "calculate_health_score tool"
check_file "tools/identify_product_gaps.py" "identify_product_gaps tool"
check_file "tools/analyze_industry_benchmarks.py" "analyze_industry_benchmarks tool"
check_file "tools/check_credit_alerts.py" "check_credit_alerts tool"
check_file "tools/fetch_recent_interactions.py" "fetch_recent_interactions tool"
echo ""

echo "=== 5. TOOL DECORATOR COMPLIANCE ==="
check_content "tools/analyze_financial_health.py" "@tool()" "analyze_financial_health has @tool decorator"
check_content "tools/calculate_health_score.py" "@tool()" "calculate_health_score has @tool decorator"
check_content "tools/identify_product_gaps.py" "@tool()" "identify_product_gaps has @tool decorator"
check_content "tools/analyze_industry_benchmarks.py" "@tool()" "analyze_industry_benchmarks has @tool decorator"
check_content "tools/check_credit_alerts.py" "@tool()" "check_credit_alerts has @tool decorator"
check_content "tools/fetch_recent_interactions.py" "@tool()" "fetch_recent_interactions has @tool decorator"
echo ""

echo "=== 6. SYNTHETIC DATA COMPLIANCE ==="
check_content "tools/analyze_financial_health.py" "CUSTOMER_DATA" "analyze_financial_health has embedded synthetic data"
check_content "tools/identify_product_gaps.py" "PRODUCT_CATALOG" "identify_product_gaps has embedded synthetic data"
check_content "tools/analyze_industry_benchmarks.py" "INDUSTRY_BENCHMARKS" "analyze_industry_benchmarks has embedded synthetic data"
check_content "tools/check_credit_alerts.py" "CREDIT_ALERTS" "check_credit_alerts has embedded synthetic data"
check_content "tools/fetch_recent_interactions.py" "CUSTOMER_INTERACTIONS" "fetch_recent_interactions has embedded synthetic data"
check_no_content "tools/*.py" "real_customer_data" "No real customer data references"
check_no_content "tools/*.py" "production_database" "No production database references"
echo ""

echo "=== 7. EMAIL & PII COMPLIANCE ==="
check_content "tools/fetch_recent_interactions.py" "@example.com" "Uses @example.com for emails"
check_no_content "tools/*.py" "@gmail.com" "No @gmail.com emails"
check_no_content "tools/*.py" "@yahoo.com" "No @yahoo.com emails"
check_no_content "tools/*.py" "@ibm.com" "No real @ibm.com emails (only @demo.ibm.com allowed)"
echo ""

echo "=== 8. DOCUMENTATION FILES ==="
check_file "README.md" "README.md exists"
check_file "ARCHITECTURE.md" "ARCHITECTURE.md exists"
check_file "PILOT_PLAN.md" "PILOT_PLAN.md exists"
check_file "DEMO_SCRIPT.md" "DEMO_SCRIPT.md exists"
echo ""

echo "=== 9. ARCHITECTURE DOCUMENTATION ==="
check_content "ARCHITECTURE.md" "graph TB" "ARCHITECTURE.md has Mermaid diagram"
check_content "ARCHITECTURE.md" "watsonx Orchestrate" "ARCHITECTURE.md mentions watsonx Orchestrate"
check_content "ARCHITECTURE.md" "Multi-Agent" "ARCHITECTURE.md describes multi-agent architecture"
check_content "ARCHITECTURE.md" "Component Inventory" "ARCHITECTURE.md has component inventory"
echo ""

echo "=== 10. IMPORT SCRIPT COMPLIANCE ==="
check_content "import-all.sh" "orchestrate tools import" "import-all.sh imports tools"
check_content "import-all.sh" "orchestrate agents import" "import-all.sh imports agents"
check_content "import-all.sh" "orchestrate agents list" "import-all.sh verifies deployment"
if [ -x "import-all.sh" ]; then
    echo "✅ PASS: import-all.sh is executable"
    ((PASS++))
else
    echo "❌ FAIL: import-all.sh is not executable"
    ((FAIL++))
fi
echo ""

echo "=== 11. ENVIRONMENT CONFIGURATION ==="
check_content ".env.example" "WXO_HOST_URL" "Environment has WXO_HOST_URL"
check_content ".env.example" "WXO_ORCHESTRATION_ID" "Environment has WXO_ORCHESTRATION_ID"
check_content ".env.example" "WXO_DEFAULT_MODEL" "Environment has WXO_DEFAULT_MODEL"
check_no_content ".env.example" "sk-" "No hardcoded API keys in .env.example"
check_no_content ".env.example" "password123" "No hardcoded passwords in .env.example"
echo ""

echo "=== 12. GITIGNORE COMPLIANCE ==="
check_content ".gitignore" ".env" ".gitignore excludes .env"
check_content ".gitignore" "__pycache__" ".gitignore excludes Python cache"
check_content ".gitignore" "*.pyc" ".gitignore excludes .pyc files"
echo ""

echo "=== 13. WATSONX ORCHESTRATE DEFINITION OF DONE ==="
echo "⚠️  MANUAL CHECK: watsonx-orchestrate skill was invoked before building"
echo "⚠️  MANUAL CHECK: Real ADK artifacts exist (agents/*.yaml, tools/*.py)"
echo "⚠️  MANUAL CHECK: Agent YAML lists real tools (not just LLM with no tools)"
echo "⚠️  MANUAL CHECK: Artifacts ready for import (import-all.sh)"
echo "⚠️  MANUAL CHECK: User will run 'orchestrate agents list' after import"
echo "⚠️  MANUAL CHECK: User will chat-test agent after deployment"
echo "⚠️  MANUAL CHECK: ARCHITECTURE.md depicts Orchestrate agents (not FastAPI→model)"
((WARN+=7))
echo ""

echo "=== 14. DEMO SCRIPT COMPLIANCE ==="
check_content "DEMO_SCRIPT.md" "Scenario 1" "DEMO_SCRIPT.md has Scenario 1"
check_content "DEMO_SCRIPT.md" "Scenario 2" "DEMO_SCRIPT.md has Scenario 2"
check_content "DEMO_SCRIPT.md" "Scenario 3" "DEMO_SCRIPT.md has Scenario 3"
check_content "DEMO_SCRIPT.md" "TechVenture Solutions" "DEMO_SCRIPT.md has TechVenture scenario"
check_content "DEMO_SCRIPT.md" "UrbanRetail Group" "DEMO_SCRIPT.md has UrbanRetail scenario"
check_content "DEMO_SCRIPT.md" "GreenLeaf Manufacturing" "DEMO_SCRIPT.md has GreenLeaf scenario"
echo ""

echo "=== 15. PILOT PLAN COMPLIANCE ==="
check_content "PILOT_PLAN.md" "4 Weeks" "PILOT_PLAN.md has 4-week timeline"
check_content "PILOT_PLAN.md" "Sprint" "PILOT_PLAN.md has sprint breakdown"
check_content "PILOT_PLAN.md" "Success Criteria" "PILOT_PLAN.md has success criteria"
check_content "PILOT_PLAN.md" "ROI" "PILOT_PLAN.md has ROI calculation"
echo ""

echo "=========================================="
echo "COMPLIANCE CHECK SUMMARY"
echo "=========================================="
echo "✅ PASSED: $PASS checks"
echo "❌ FAILED: $FAIL checks"
echo "⚠️  WARNINGS: $WARN manual checks required"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "🎉 SUCCESS: All automated checks passed!"
    echo ""
    echo "NEXT STEPS:"
    echo "1. Install ibm-watsonx-orchestrate package: pip install ibm-watsonx-orchestrate"
    echo "2. Configure watsonx Orchestrate environment: orchestrate env add"
    echo "3. Run import script: ./import-all.sh"
    echo "4. Verify deployment: orchestrate agents list"
    echo "5. Test agent: orchestrate chat ask -n meeting_prep_orchestrator 'Prepare me for my meeting with TechVenture Solutions' -r"
    echo ""
    exit 0
else
    echo "⚠️  WARNING: $FAIL checks failed. Please review and fix before deployment."
    echo ""
    exit 1
fi
