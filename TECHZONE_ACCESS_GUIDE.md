# TechZone watsonx Orchestrate Environment - Access Guide

## 🎉 Environment Successfully Provisioned!

**Request ID**: `6a33accba7488b1b77105b72`  
**Status**: Scheduled → Provisioning  
**TechZone URL**: https://techzone.ibm.com/my/requests/6a33accba7488b1b77105b72

---

## 📋 Environment Details

### Platform Information
- **Platform**: watsonx Orchestrate Trial with CE
- **Region**: us-south (Americas)
- **Infrastructure**: IBM Cloud (ibmcloud-2)
- **Schedule**: 
  - Start: 2026-06-18 09:00:00 UTC (5:00 PM Malaysia Time)
  - End: 2026-06-18 21:00:00 UTC (5:00 AM Malaysia Time, next day)
  - Duration: 12 hours

### Included Services
✅ **watsonx Orchestrate** (lite plan)  
✅ **Watson Machine Learning** (v2-standard)  
✅ **Watson Studio** (free-v1)  
✅ **watsonx.governance** (essentials)  
✅ **Cloud Object Storage** (standard)  
✅ **Code Engine** (standard)

### Access Permissions
- **Manager, Administrator, WO User** roles for watsonx Orchestrate
- Full access to all provisioned services
- IBM ID authentication

---

## 🚀 Step-by-Step Access Instructions

### Step 1: Monitor Provisioning Status

The environment is currently being provisioned. This typically takes **30-60 minutes**.

**Check Status**:
1. Visit: https://techzone.ibm.com/my/requests/6a33accba7488b1b77105b72
2. Wait for status to change from "Scheduled" → "Provision" → "Ready"
3. You'll receive an email notification when ready

**Using TechZone MCP** (automated):
```bash
# From the demo directory
cd demo-BANK-001-sme-meeting-prep

# The project-scoped MCP is already configured in .bob/mcp.json
# You can check status programmatically through Bob's TechZone MCP tools
```

### Step 2: Access Your Environment (Once Ready)

When the environment status shows **"Ready"**:

1. **Go to TechZone Request Page**:
   - https://techzone.ibm.com/my/requests/6a33accba7488b1b77105b72

2. **Find Your Credentials**:
   - Click on the environment details
   - Look for "Access Information" or "Credentials" section
   - You'll find:
     - IBM Cloud Account ID
     - Resource Group Name
     - watsonx Orchestrate Instance URL
     - Service credentials

3. **Access watsonx Orchestrate**:
   - Navigate to the watsonx Orchestrate URL provided
   - Log in with your IBM ID (dillan.haran@ibm.com)
   - You'll land in the Orchestrate dashboard

### Step 3: Extract Required Credentials

You need these values to deploy the demo agents:

```bash
# Required environment variables for .env file:

# watsonx Orchestrate Connection
WXO_HOST_URL=<from TechZone - e.g., https://us-south.watson-orchestrate.cloud.ibm.com>
WXO_ORCHESTRATION_ID=<from Orchestrate instance>
WXO_CRN=<Cloud Resource Name from IBM Cloud>

# IBM Cloud API Key (generate this)
IBM_CLOUD_API_KEY=<generate from IBM Cloud IAM>

# watsonx.ai (if using WML)
WATSONX_API_KEY=<same as IBM_CLOUD_API_KEY>
WATSONX_PROJECT_ID=<create a project in Watson Studio>
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

### Step 4: Generate IBM Cloud API Key

1. **Access IBM Cloud Console**:
   - Go to: https://cloud.ibm.com
   - Log in with your IBM ID

2. **Navigate to IAM**:
   - Click on "Manage" → "Access (IAM)"
   - Select "API keys" from the left menu

3. **Create API Key**:
   - Click "Create an IBM Cloud API key"
   - Name: `wxo-demo-bank-001`
   - Description: `API key for SME Meeting Prep Demo`
   - Click "Create"
   - **IMPORTANT**: Copy and save the API key immediately (you can't retrieve it later)

### Step 5: Get watsonx Orchestrate Details

1. **Find Your Orchestrate Instance**:
   - In IBM Cloud Console, go to "Resource list"
   - Find "watsonx Orchestrate" under "AI / Machine Learning"
   - Click on the instance

2. **Get Orchestration ID**:
   - In the Orchestrate dashboard, go to "Settings" or "Instance details"
   - Copy the "Orchestration ID"

3. **Get CRN (Cloud Resource Name)**:
   - In IBM Cloud, on your Orchestrate instance page
   - Look for "CRN" in the instance details
   - Copy the full CRN string

### Step 6: Configure Demo Environment

1. **Update .env file**:
```bash
cd demo-BANK-001-sme-meeting-prep
cp .env.example .env
nano .env  # or use your preferred editor
```

2. **Add your credentials**:
```bash
# watsonx Orchestrate Configuration
WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
WXO_ORCHESTRATION_ID=<your-orchestration-id>
WXO_CRN=<your-crn>
WXO_DEFAULT_MODEL=groq/openai/gpt-oss-120b

# IBM Cloud Authentication
IBM_CLOUD_API_KEY=<your-api-key>

# watsonx.ai (optional - for WML integration)
WATSONX_API_KEY=<same-as-ibm-cloud-api-key>
WATSONX_PROJECT_ID=<create-in-watson-studio>
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

### Step 7: Deploy the Demo Agents

Once credentials are configured:

```bash
# Make the deployment script executable
chmod +x quick-deploy.sh

# Run the deployment
./quick-deploy.sh

# This will:
# 1. Validate your credentials
# 2. Import all 6 tools to Orchestrate
# 3. Deploy all 5 agents (4 specialists + 1 orchestrator)
# 4. Test the deployment
# 5. Provide you with the agent IDs
```

### Step 8: Test the Demo

After deployment completes:

```bash
# Test with a sample customer query
orchestrate chat ask -n meeting_prep_orchestrator \
  "Prepare for meeting with CUST-001 (Apex Manufacturing)" -r

# Expected output:
# - Customer health analysis
# - Financial metrics
# - Risk alerts
# - Growth opportunities
# - Meeting talking points
```

---

## 🔍 Troubleshooting

### Environment Not Ready After 1 Hour
- Check TechZone request page for any error messages
- Verify your IBM Cloud account has sufficient quota
- Contact TechZone support if status shows "Failed"

### Can't Find Orchestrate Instance
- Ensure you're logged into the correct IBM Cloud account
- Check the Resource Group specified in TechZone
- Look under "AI / Machine Learning" in Resource List

### API Key Issues
- Ensure the API key has "Manager" role for watsonx Orchestrate
- Verify the key hasn't expired
- Check that the key is for the correct IBM Cloud account

### Deployment Fails
```bash
# Check orchestrate CLI is installed
orchestrate --version

# Verify environment variables
cat .env | grep -v "^#" | grep -v "^$"

# Test connection
orchestrate env list
```

---

## 📞 Support Resources

### TechZone Support
- **Request Page**: https://techzone.ibm.com/my/requests/6a33accba7488b1b77105b72
- **Help Desk**: https://techzone.ibm.com/help
- **Slack**: #techzone-support

### watsonx Orchestrate Documentation
- **Getting Started**: https://www.ibm.com/docs/en/watsonx/watson-orchestrate
- **Agent Development Kit**: https://ibm.github.io/watsonx-orchestrate-adk-docs/
- **API Reference**: https://cloud.ibm.com/apidocs/watsonx-orchestrate

### Demo-Specific Help
- **README**: See `README.md` in this directory
- **Architecture**: See `ARCHITECTURE.md` for system design
- **Demo Script**: See `DEMO_SCRIPT.md` for presentation guide

---

## ⏰ Important Reminders

### Environment Lifecycle
- **Start Time**: 2026-06-18 09:00 UTC (5:00 PM Malaysia)
- **End Time**: 2026-06-18 21:00 UTC (5:00 AM Malaysia, next day)
- **Duration**: 12 hours
- **Auto-Shutdown**: Environment will be automatically deleted after end time

### Before Environment Expires
If you need to extend or recreate:

1. **Export Your Work**:
   ```bash
   # Export deployed agents
   orchestrate agents export -n meeting_prep_orchestrator -o backup/
   orchestrate agents export -n customer_intelligence_agent -o backup/
   # ... export all agents
   ```

2. **Save Credentials**: Keep your `.env` file backed up

3. **Request Extension**: 
   - Go to TechZone request page
   - Click "Extend" if available
   - Or provision a new environment using the same process

### Cost Considerations
- Trial plan is **FREE** for 30 days
- No charges for this demo environment
- Monitor usage in IBM Cloud dashboard

---

## 🎯 Next Steps

1. ✅ **Wait for provisioning to complete** (~30-60 minutes)
2. ✅ **Access TechZone request page** to get credentials
3. ✅ **Generate IBM Cloud API key**
4. ✅ **Configure .env file** with your credentials
5. ✅ **Run ./quick-deploy.sh** to deploy agents
6. ✅ **Test the demo** with sample customers
7. ✅ **Review DEMO_SCRIPT.md** for presentation guidance

---

## 📝 Quick Reference

### Key URLs
- **TechZone Request**: https://techzone.ibm.com/my/requests/6a33accba7488b1b77105b72
- **IBM Cloud Console**: https://cloud.ibm.com
- **watsonx Orchestrate**: (provided after provisioning)

### Key Commands
```bash
# Check environment status
orchestrate env list

# List deployed agents
orchestrate agents list

# Test an agent
orchestrate chat ask -n <agent-name> "<query>" -r

# View agent details
orchestrate agents get -n <agent-name>
```

### Demo Customers (Pre-loaded)
- **CUST-001**: Apex Manufacturing (High-value, stable)
- **CUST-005**: Greenfield Healthcare (Growth opportunity)
- **CUST-008**: Quantum Telecom (At-risk, needs attention)

---

**Generated**: 2026-06-18 16:31 UTC+8  
**Request ID**: 6a33accba7488b1b77105b72  
**Owner**: dillan.haran@ibm.com