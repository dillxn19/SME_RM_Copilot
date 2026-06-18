"""
Tool: fetch_recent_interactions
Fetches recent customer interactions from CRM including meetings, calls, emails, and service requests.
"""

from ibm_watsonx_orchestrate import tool
from typing import Dict, Any, List
from datetime import datetime, timedelta

# Recent interaction data by customer (last 30 days)
CUSTOMER_INTERACTIONS = {
    "CUST-001": [
        {
            "interaction_type": "Meeting",
            "date": "2026-06-10",
            "days_ago": 8,
            "subject": "Quarterly Business Review",
            "summary": "CEO discussed expansion plans for Q3. Mentioned hiring 15 new engineers and opening Austin office.",
            "participants": ["John Chen (CEO)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        },
        {
            "interaction_type": "Call",
            "date": "2026-06-05",
            "days_ago": 13,
            "subject": "Credit Line Inquiry",
            "summary": "CFO asked about increasing credit line for equipment purchases. Sent proposal for $500K increase.",
            "participants": ["Lisa Wong (CFO)", "Sarah Martinez (RM)"],
            "sentiment": "Neutral"
        },
        {
            "interaction_type": "Email",
            "date": "2026-05-28",
            "days_ago": 21,
            "subject": "Treasury Management Demo Request",
            "summary": "Operations Director requested demo of automated payment processing solution.",
            "participants": ["Mike Johnson (Ops Director)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        }
    ],
    "CUST-002": [
        {
            "interaction_type": "Meeting",
            "date": "2026-06-12",
            "days_ago": 6,
            "subject": "New Facility Financing Discussion",
            "summary": "Discussed $2M equipment financing for new manufacturing facility opening in September.",
            "participants": ["Robert Green (CEO)", "Tom Anderson (CFO)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        },
        {
            "interaction_type": "Call",
            "date": "2026-06-01",
            "days_ago": 17,
            "subject": "ESG Financing Options",
            "summary": "Explored green financing programs for solar panel installation at main facility.",
            "participants": ["Tom Anderson (CFO)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        }
    ],
    "CUST-003": [
        {
            "interaction_type": "Call",
            "date": "2026-06-15",
            "days_ago": 3,
            "subject": "Late Payment Follow-up",
            "summary": "CFO explained cash flow challenges due to slower holiday sales. Committed to payment by month-end.",
            "participants": ["Jennifer Park (CFO)", "Sarah Martinez (RM)"],
            "sentiment": "Concerned"
        },
        {
            "interaction_type": "Email",
            "date": "2026-06-08",
            "days_ago": 10,
            "subject": "Working Capital Line Request",
            "summary": "Requested emergency increase to working capital line to cover inventory for back-to-school season.",
            "participants": ["Jennifer Park (CFO)", "Sarah Martinez (RM)"],
            "sentiment": "Urgent"
        },
        {
            "interaction_type": "Service Request",
            "date": "2026-05-25",
            "days_ago": 24,
            "subject": "Merchant Services Fee Dispute",
            "summary": "Disputed processing fees. Resolved - waived $500 in fees as goodwill gesture.",
            "participants": ["Operations Team", "Sarah Martinez (RM)"],
            "sentiment": "Resolved"
        }
    ],
    "CUST-004": [
        {
            "interaction_type": "Meeting",
            "date": "2026-06-14",
            "days_ago": 4,
            "subject": "Annual Review",
            "summary": "Reviewed 2025 performance. Discussed expansion into telehealth services and related financing needs.",
            "participants": ["Dr. Maria Rodriguez (CEO)", "David Kim (CFO)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        }
    ],
    "CUST-005": [
        {
            "interaction_type": "Call",
            "date": "2026-06-11",
            "days_ago": 7,
            "subject": "Project Delay Impact",
            "summary": "Major project delayed 60 days due to permit issues. May impact Q3 revenue projections.",
            "participants": ["James Wilson (CEO)", "Sarah Martinez (RM)"],
            "sentiment": "Concerned"
        },
        {
            "interaction_type": "Meeting",
            "date": "2026-05-30",
            "days_ago": 19,
            "subject": "Equipment Financing Renewal",
            "summary": "Renewed $1.5M equipment financing for heavy machinery fleet. Favorable terms secured.",
            "participants": ["James Wilson (CEO)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        }
    ],
    "CUST-006": [
        {
            "interaction_type": "Email",
            "date": "2026-06-13",
            "days_ago": 5,
            "subject": "FX Hedging Strategy Review",
            "summary": "Requested review of currency hedging strategy given recent USD strength.",
            "participants": ["Carlos Mendez (CFO)", "Sarah Martinez (RM)", "FX Trading Desk"],
            "sentiment": "Neutral"
        }
    ],
    "CUST-007": [
        {
            "interaction_type": "Call",
            "date": "2026-06-09",
            "days_ago": 9,
            "subject": "New Client Win Celebration",
            "summary": "CEO shared news of landing Fortune 500 client. Discussed financing needs for scaling operations.",
            "participants": ["Amy Chen (CEO)", "Sarah Martinez (RM)"],
            "sentiment": "Very Positive"
        }
    ],
    "CUST-008": [
        {
            "interaction_type": "Meeting",
            "date": "2026-06-07",
            "days_ago": 11,
            "subject": "Quarterly Check-in",
            "summary": "Routine quarterly review. Business stable, no immediate needs identified.",
            "participants": ["Richard Brown (CEO)", "Sarah Martinez (RM)"],
            "sentiment": "Neutral"
        }
    ],
    "CUST-009": [
        {
            "interaction_type": "Call",
            "date": "2026-06-16",
            "days_ago": 2,
            "subject": "Competitor Threat Discussion",
            "summary": "Discussed impact of new competitor opening nearby. Exploring marketing support options.",
            "participants": ["Susan Lee (Owner)", "Sarah Martinez (RM)"],
            "sentiment": "Concerned"
        },
        {
            "interaction_type": "Email",
            "date": "2026-06-02",
            "days_ago": 16,
            "subject": "Payment Plan Request",
            "summary": "Requested 90-day payment plan for outstanding balance. Approved with conditions.",
            "participants": ["Susan Lee (Owner)", "Sarah Martinez (RM)"],
            "sentiment": "Neutral"
        }
    ],
    "CUST-010": [
        {
            "interaction_type": "Meeting",
            "date": "2026-06-06",
            "days_ago": 12,
            "subject": "ESG Reporting Requirements",
            "summary": "Discussed new ESG reporting requirements and potential financing for carbon reduction initiatives.",
            "participants": ["Dr. Patricia Moore (CEO)", "Sarah Martinez (RM)"],
            "sentiment": "Positive"
        }
    ]
}


@tool()
async def fetch_recent_interactions(customer_id: str, days: int = 30) -> Dict[str, Any]:
    """Fetches recent customer interactions from CRM including meetings, calls, emails, and service requests.
    
    This tool provides a chronological view of recent touchpoints with the customer,
    helping the Relationship Manager prepare for meetings by understanding recent
    conversations, concerns, and opportunities discussed.
    
    Args:
        customer_id (str): The unique customer identifier (format: CUST-XXX)
        days (int): Number of days to look back (default 30)
        
    Returns:
        dict: Recent interaction summary containing:
            - customer_id (str): Customer identifier
            - interaction_count (int): Total number of interactions
            - interactions (list): List of interaction details
            - most_recent_interaction (dict): Details of last touchpoint
            - key_themes (list): Common topics across interactions
            - sentiment_summary (str): Overall sentiment trend
            
    Example:
        >>> result = await fetch_recent_interactions("CUST-001", 30)
        >>> print(result["interaction_count"])
        3
        >>> print(result["most_recent_interaction"]["subject"])
        "Quarterly Business Review"
    """
    
    if customer_id not in CUSTOMER_INTERACTIONS:
        return {
            "error": f"Customer {customer_id} not found",
            "available_customers": list(CUSTOMER_INTERACTIONS.keys())
        }
    
    # Get interactions within the specified time window
    all_interactions = CUSTOMER_INTERACTIONS[customer_id]
    filtered_interactions = [i for i in all_interactions if i["days_ago"] <= days]
    
    # Sort by date (most recent first)
    filtered_interactions.sort(key=lambda x: x["days_ago"])
    
    # Get most recent interaction
    most_recent = filtered_interactions[0] if filtered_interactions else None
    
    # Extract key themes
    themes = []
    for interaction in filtered_interactions:
        subject = interaction["subject"].lower()
        if "financing" in subject or "credit" in subject or "loan" in subject:
            themes.append("Financing/Credit")
        if "expansion" in subject or "growth" in subject or "new" in subject:
            themes.append("Growth/Expansion")
        if "payment" in subject or "late" in subject:
            themes.append("Payment Issues")
        if "esg" in subject or "green" in subject or "sustainability" in subject:
            themes.append("ESG/Sustainability")
        if "review" in subject or "quarterly" in subject:
            themes.append("Relationship Management")
    
    themes = list(set(themes))  # Remove duplicates
    
    # Analyze sentiment trend
    sentiments = [i["sentiment"] for i in filtered_interactions]
    positive_count = sum(1 for s in sentiments if "Positive" in s)
    concerned_count = sum(1 for s in sentiments if "Concerned" in s or "Urgent" in s)
    
    if positive_count > concerned_count:
        sentiment_summary = "Predominantly positive interactions"
    elif concerned_count > positive_count:
        sentiment_summary = "Some concerns raised - follow-up needed"
    else:
        sentiment_summary = "Mixed sentiment - monitor closely"
    
    # Import customer data for context
    from .analyze_financial_health import CUSTOMER_DATA
    company_name = CUSTOMER_DATA.get(customer_id, {}).get("company_name", "Unknown")
    
    return {
        "customer_id": customer_id,
        "company_name": company_name,
        "interaction_count": len(filtered_interactions),
        "interactions": filtered_interactions,
        "most_recent_interaction": most_recent,
        "key_themes": themes if themes else ["Routine relationship management"],
        "sentiment_summary": sentiment_summary,
        "days_since_last_contact": most_recent["days_ago"] if most_recent else None
    }

# Made with Bob
