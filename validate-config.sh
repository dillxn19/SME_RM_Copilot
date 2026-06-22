#!/bin/bash

# Configuration Validation Script for SME RM Copilot Demo
# This script validates that all required configurations are in place

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
ERRORS=0
WARNINGS=0
CHECKS=0

# Function to print colored output
print_header() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_check() {
    CHECKS=$((CHECKS + 1))
    echo -e "${BLUE}[CHECK $CHECKS]${NC} $1"
}

print_success() {
    echo -e "${GREEN}  ✓${NC} $1"
}

print_error() {
    ERRORS=$((ERRORS + 1))
    echo -e "${RED}  ✗${NC} $1"
}

print_warning() {
    WARNINGS=$((WARNINGS + 1))
    echo -e "${YELLOW}  ⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}  ℹ${NC} $1"
}

# Banner
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   SME RM Copilot - Configuration Validation                   ║"
echo "║   Checking prerequisites and environment setup                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# ============================================================================
# SECTION 1: System Prerequisites
# ============================================================================
print_header "SYSTEM PREREQUISITES"

# Check Node.js
print_check "Checking Node.js installation..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    print_success "Node.js installed: $NODE_VERSION"
    
    # Check if version is >= 18
    NODE_MAJOR=$(echo $NODE_VERSION | cut -d'.' -f1 | sed 's/v//')
    if [ "$NODE_MAJOR" -ge 18 ]; then
        print_success "Node.js version is compatible (>= 18.x)"
    else
        print_warning "Node.js version should be >= 18.x for best compatibility"
    fi
else
    print_error "Node.js is not installed"
    print_info "Install from: https://nodejs.org/"
fi

# Check npm
print_check "Checking npm installation..."
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    print_success "npm installed: v$NPM_VERSION"
else
    print_error "npm is not installed"
fi

# Check Python
print_check "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    print_success "Python installed: $PYTHON_VERSION"
else
    print_warning "Python 3 is not installed (required for watsonx Orchestrate CLI)"
    print_info "Install from: https://www.python.org/"
fi

# Check pip
print_check "Checking pip installation..."
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version)
    print_success "pip installed: $PIP_VERSION"
else
    print_warning "pip3 is not installed (required for watsonx Orchestrate CLI)"
fi

# Check watsonx Orchestrate CLI
print_check "Checking watsonx Orchestrate CLI..."
if command -v orchestrate &> /dev/null; then
    ORCHESTRATE_VERSION=$(orchestrate --version 2>&1 || echo "unknown")
    print_success "watsonx Orchestrate CLI installed: $ORCHESTRATE_VERSION"
else
    print_warning "watsonx Orchestrate CLI is not installed"
    print_info "Install with: pip install ibm-watsonx-orchestrate"
fi

# ============================================================================
# SECTION 2: Root Environment Configuration
# ============================================================================
print_header "ROOT ENVIRONMENT CONFIGURATION"

# Check root .env file
print_check "Checking root .env file..."
if [ -f ".env" ]; then
    print_success ".env file exists"
    
    # Check required variables
    print_check "Validating required environment variables..."
    
    # Source the .env file
    set -a
    source .env 2>/dev/null || true
    set +a
    
    # Check DEMO_MODE
    if [ -n "$DEMO_MODE" ]; then
        print_success "DEMO_MODE is set: $DEMO_MODE"
    else
        print_warning "DEMO_MODE is not set (defaults to 'mock')"
    fi
    
    # Check WXO_HOST_URL
    if [ -n "$WXO_HOST_URL" ]; then
        print_success "WXO_HOST_URL is set"
    else
        print_warning "WXO_HOST_URL is not set (required for deployment)"
    fi
    
    # Check WXO_API_KEY
    if [ -n "$WXO_API_KEY" ]; then
        print_success "WXO_API_KEY is set"
    else
        print_warning "WXO_API_KEY is not set (required for deployment)"
    fi
    
    # Check WXO_ORCHESTRATION_ID
    if [ -n "$WXO_ORCHESTRATION_ID" ]; then
        print_success "WXO_ORCHESTRATION_ID is set"
    else
        print_warning "WXO_ORCHESTRATION_ID is not set (required for deployment)"
    fi
    
    # Check WXO_DEFAULT_MODEL
    if [ -n "$WXO_DEFAULT_MODEL" ]; then
        print_success "WXO_DEFAULT_MODEL is set: $WXO_DEFAULT_MODEL"
    else
        print_warning "WXO_DEFAULT_MODEL is not set"
    fi
    
else
    print_error ".env file not found in root directory"
    print_info "Copy .env.example to .env and configure your values"
    print_info "  cp .env.example .env"
fi

# ============================================================================
# SECTION 3: Frontend Configuration
# ============================================================================
print_header "FRONTEND CONFIGURATION"

# Check frontend .env file
print_check "Checking frontend/.env file..."
if [ -f "frontend/.env" ]; then
    print_success "frontend/.env file exists"
    
    # Check required variables
    print_check "Validating frontend environment variables..."
    
    # Source the frontend .env file
    set -a
    source frontend/.env 2>/dev/null || true
    set +a
    
    # Check VITE_WXO_HOST_URL
    if [ -n "$VITE_WXO_HOST_URL" ]; then
        print_success "VITE_WXO_HOST_URL is set"
    else
        print_warning "VITE_WXO_HOST_URL is not set"
    fi
    
    # Check VITE_WXO_ORCHESTRATION_ID
    if [ -n "$VITE_WXO_ORCHESTRATION_ID" ]; then
        print_success "VITE_WXO_ORCHESTRATION_ID is set"
    else
        print_warning "VITE_WXO_ORCHESTRATION_ID is not set"
    fi
    
    # Check VITE_WXO_CRN
    if [ -n "$VITE_WXO_CRN" ]; then
        print_success "VITE_WXO_CRN is set"
    else
        print_warning "VITE_WXO_CRN is not set"
    fi
    
    # Check VITE_WXO_AGENT_ID
    if [ -n "$VITE_WXO_AGENT_ID" ]; then
        print_success "VITE_WXO_AGENT_ID is set"
    else
        print_warning "VITE_WXO_AGENT_ID is not set (required after agent deployment)"
    fi
    
else
    print_error "frontend/.env file not found"
    print_info "Copy frontend/.env.example to frontend/.env and configure your values"
    print_info "  cp frontend/.env.example frontend/.env"
fi

# Check if frontend dependencies are installed
print_check "Checking frontend dependencies..."
if [ -d "frontend/node_modules" ]; then
    print_success "Frontend dependencies are installed"
else
    print_warning "Frontend dependencies not installed"
    print_info "Run: cd frontend && npm install"
fi

# ============================================================================
# SECTION 4: Project Structure
# ============================================================================
print_header "PROJECT STRUCTURE"

# Check critical directories
print_check "Checking project directories..."

REQUIRED_DIRS=(
    "agents"
    "tools"
    "frontend"
    "frontend/src"
    "frontend/public"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        print_success "Directory exists: $dir"
    else
        print_error "Missing directory: $dir"
    fi
done

# Check critical files
print_check "Checking critical files..."

REQUIRED_FILES=(
    "README.md"
    "DEMO_SCRIPT.md"
    "ARCHITECTURE.md"
    "quick-deploy.sh"
    "import-all.sh"
    "frontend/package.json"
    "frontend/index.html"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        print_success "File exists: $file"
    else
        print_error "Missing file: $file"
    fi
done

# Check agent files
print_check "Checking agent configuration files..."

AGENT_FILES=(
    "agents/meeting_prep_orchestrator.yaml"
    "agents/customer_health_agent.yaml"
    "agents/growth_opportunity_agent.yaml"
    "agents/risk_monitoring_agent.yaml"
    "agents/customer_intelligence_agent.yaml"
)

for file in "${AGENT_FILES[@]}"; do
    if [ -f "$file" ]; then
        print_success "Agent file exists: $file"
    else
        print_error "Missing agent file: $file"
    fi
done

# Check tool files
print_check "Checking tool files..."

TOOL_FILES=(
    "tools/analyze_financial_health.py"
    "tools/calculate_health_score.py"
    "tools/identify_product_gaps.py"
    "tools/analyze_industry_benchmarks.py"
    "tools/check_credit_alerts.py"
    "tools/fetch_recent_interactions.py"
)

for file in "${TOOL_FILES[@]}"; do
    if [ -f "$file" ]; then
        print_success "Tool file exists: $file"
    else
        print_error "Missing tool file: $file"
    fi
done

# ============================================================================
# SECTION 5: Orchestrate Environment
# ============================================================================
print_header "WATSONX ORCHESTRATE ENVIRONMENT"

if command -v orchestrate &> /dev/null; then
    print_check "Checking active Orchestrate environment..."
    
    ACTIVE_ENV=$(orchestrate env list 2>&1 | grep "active" || echo "")
    if [ -n "$ACTIVE_ENV" ]; then
        print_success "Active environment found: $ACTIVE_ENV"
    else
        print_warning "No active watsonx Orchestrate environment configured"
        print_info "Configure with: orchestrate env add --name <name> --url <url> --apikey <key>"
    fi
else
    print_warning "Cannot check Orchestrate environment (CLI not installed)"
fi

# ============================================================================
# SUMMARY
# ============================================================================
print_header "VALIDATION SUMMARY"

echo ""
echo "Total Checks: $CHECKS"
echo -e "${GREEN}Passed: $((CHECKS - ERRORS - WARNINGS))${NC}"
echo -e "${YELLOW}Warnings: $WARNINGS${NC}"
echo -e "${RED}Errors: $ERRORS${NC}"
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                  ✓ ALL CHECKS PASSED! ✓                       ║"
    echo "║         Your environment is ready for deployment!              ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Next steps:"
    echo "  1. Deploy agents: ./quick-deploy.sh"
    echo "  2. Start frontend: cd frontend && npm run dev"
    echo ""
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║              ⚠ VALIDATION COMPLETED WITH WARNINGS ⚠           ║"
    echo "║     Review warnings above and fix if needed                   ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "You can proceed, but some features may not work correctly."
    echo ""
    exit 0
else
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                ✗ VALIDATION FAILED ✗                          ║"
    echo "║        Please fix the errors above before proceeding          ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Common fixes:"
    echo "  - Install missing prerequisites (Node.js, Python, npm)"
    echo "  - Copy .env.example to .env and configure values"
    echo "  - Copy frontend/.env.example to frontend/.env"
    echo "  - Run: cd frontend && npm install"
    echo ""
    exit 1
fi

# Made with Bob
