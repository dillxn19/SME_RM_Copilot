"""
Tool: check_credit_alerts
Checks for credit-related alerts and warnings for a customer.
"""

from ibm_watsonx_orchestrate import tool
from typing import Dict, Any, List
from datetime import datetime, timedelta

# Credit alert data by customer
CREDIT_ALERTS = {
    "CUST-001": [],  # No alerts - healthy customer
    "CUST-002": [
        {
            "alert_type": "Late Payment",
            "severity": "Low",
            "description": "Payment 5 days late on commercial loan",
            "days_active": 12,
            "amount_involved": 45000,
            "recommended_action": "Monitor - isolated incident"
        }
    ],
    "CUST-003": [
        {
            "alert_type": "Late Payment",
            "severity": "High",
            "description": "Payment 18 days late on working capital line",
            "days_active": 18,
            "amount_involved": 125000,
            "recommended_action": "Immediate outreach required"
        },
        {
            "alert_type": "Credit Limit Breach",
            "severity": "High",
            "description": "Credit utilization at 92% - approaching limit",
            "days_active": 8,
            "amount_involved": 920000,
            "recommended_action": "Discuss credit line increase or payment plan"
        }
    ],
    "CUST-004": [
        {
            "alert_type": "Industry Headwind",
            "severity": "Medium",
            "description": "Healthcare sector facing reimbursement delays",
            "days_active": 45,
            "amount_involved": 0,
            "recommended_action": "Proactive check-in on cash flow"
        }
    ],
    "CUST-005": [
        {
            "alert_type": "Late Payment",
            "severity": "Medium",
            "description": "Payment 12 days late on equipment financing",
            "days_active": 12,
            "amount_involved": 85000,
            "recommended_action": "Schedule payment discussion"
        },
        {
            "alert_type": "Covenant Violation",
            "severity": "Medium",
            "description": "Debt-to-equity ratio exceeded covenant threshold",
            "days_active": 22,
            "amount_involved": 0,
            "recommended_action": "Review financial statements and discuss remediation"
        }
    ],
    "CUST-006": [],  # No alerts
    "CUST-007": [],  # No alerts
    "CUST-008": [],  # No alerts
    "CUST-009": [
        {
            "alert_type": "Late Payment",
            "severity": "High",
            "description": "Payment 22 days late on merchant services fees",
            "days_active": 22,
            "amount_involved": 15000,
            "recommended_action": "Urgent follow-up required"
        },
        {
            "alert_type": "Negative News",
            "severity": "Medium",
            "description": "Local competitor opened nearby - potential revenue impact",
            "days_active": 15,
            "amount_involved": 0,
            "recommended_action": "Discuss competitive positioning and support options"
        }
    ],
    "CUST-010": [
        {
            "alert_type": "Industry Headwind",
            "severity": "Low",
            "description": "Energy sector commodity price volatility",
            "days_active": 30,
            "amount_involved": 0,
            "recommended_action": "Monitor - offer hedging solutions if needed"
        }
    ]
}


@tool()
async def check_credit_alerts(customer_id: str) -> Dict[str, Any]:
    """Checks for credit-related alerts and warnings including late payments, credit limit breaches, covenant violations, and industry headwinds.
    
    This tool monitors various risk indicators and flags issues that require the
    Relationship Manager's attention. Alerts are categorized by severity (Critical,
    High, Medium, Low) to help prioritize follow-up actions.
    
    Args:
        customer_id (str): The unique customer identifier (format: CUST-XXX)
        
    Returns:
        dict: Credit alert summary containing:
            - customer_id (str): Customer identifier
            - alert_count (int): Total number of active alerts
            - alerts (list): List of alert details
            - highest_severity (str): Most severe alert level
            - requires_immediate_action (bool): Whether urgent action is needed
            - summary (str): Executive summary of alert status
            
    Example:
        >>> result = await check_credit_alerts("CUST-003")
        >>> print(result["alert_count"])
        2
        >>> print(result["highest_severity"])
        "High"
    """
    
    if customer_id not in CREDIT_ALERTS:
        return {
            "error": f"Customer {customer_id} not found",
            "available_customers": list(CREDIT_ALERTS.keys())
        }
    
    alerts = CREDIT_ALERTS[customer_id]
    
    # Determine highest severity
    severity_order = {"Critical": 4, "High": 3, "Medium": 2, "Low": 1}
    highest_severity = "None"
    if alerts:
        highest_severity = max(alerts, key=lambda x: severity_order.get(x["severity"], 0))["severity"]
    
    # Check if immediate action required
    requires_immediate_action = any(
        alert["severity"] in ["Critical", "High"] for alert in alerts
    )
    
    # Generate summary
    if not alerts:
        summary = "No active credit alerts. Customer account is in good standing."
    elif len(alerts) == 1:
        summary = f"1 active alert ({alerts[0]['severity']} severity): {alerts[0]['alert_type']}"
    else:
        summary = f"{len(alerts)} active alerts. Highest severity: {highest_severity}. "
        if requires_immediate_action:
            summary += "Immediate action required."
        else:
            summary += "Monitor and follow up as needed."
    
    # Add alert age information
    for alert in alerts:
        if alert["days_active"] > 30:
            alert["age_status"] = "Long-standing issue"
        elif alert["days_active"] > 14:
            alert["age_status"] = "Escalating concern"
        else:
            alert["age_status"] = "Recent development"
    
    # Import customer data for context
    from .analyze_financial_health import CUSTOMER_DATA
    company_name = CUSTOMER_DATA.get(customer_id, {}).get("company_name", "Unknown")
    
    return {
        "customer_id": customer_id,
        "company_name": company_name,
        "alert_count": len(alerts),
        "alerts": alerts,
        "highest_severity": highest_severity,
        "requires_immediate_action": requires_immediate_action,
        "summary": summary,
        "alert_types_present": list(set(alert["alert_type"] for alert in alerts)) if alerts else []
    }

# Made with Bob
