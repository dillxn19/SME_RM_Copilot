"""
Tool: calculate_health_score
Calculates overall customer health score (0-100) based on financial metrics.
"""

from ibm_watsonx_orchestrate import tool
from typing import Dict, Any


@tool()
async def calculate_health_score(financial_data: dict) -> Dict[str, Any]:
    """Calculates overall customer health score (0-100) based on weighted financial metrics.
    
    This tool takes financial data from analyze_financial_health and computes a composite
    health score using a weighted algorithm. The score helps Relationship Managers quickly
    assess customer financial stability and prioritize attention.
    
    Scoring Algorithm:
    - Revenue Stability (30%): Based on revenue growth rate and consistency
    - Payment Performance (30%): Based on on-time payment percentage
    - Credit Utilization (20%): Inverse score (lower utilization = higher score)
    - Account Activity (20%): Based on positive cash flow and transaction volume
    
    Args:
        financial_data (dict): Financial metrics from analyze_financial_health tool
        
    Returns:
        dict: Health score breakdown containing:
            - overall_score (int): Composite health score (0-100)
            - score_category (str): Excellent/Good/Fair/Needs Attention/Critical
            - component_scores (dict): Individual category scores
            - key_strengths (list): Top 2-3 positive indicators
            - areas_of_concern (list): Issues requiring attention
            - recommendation (str): Action recommendation for RM
            
    Example:
        >>> financial_data = await analyze_financial_health("CUST-001")
        >>> score = await calculate_health_score(financial_data)
        >>> print(score["overall_score"])
        87
        >>> print(score["score_category"])
        "Excellent"
    """
    
    # Extract key metrics
    revenue_growth = financial_data.get("revenue_growth_rate", 0)
    payment_on_time = financial_data.get("payment_history", {}).get("on_time_percentage", 0)
    credit_util = financial_data.get("credit_utilization", 0)
    net_cash_flow = financial_data.get("net_cash_flow_90d", 0)
    transaction_count = financial_data.get("account_activity", {}).get("transaction_count_90d", 0)
    
    # Component 1: Revenue Stability (30 points)
    if revenue_growth >= 5:
        revenue_score = 30
    elif revenue_growth >= 0:
        revenue_score = 20 + (revenue_growth * 2)
    elif revenue_growth >= -5:
        revenue_score = 15 + (revenue_growth * 1)
    else:
        revenue_score = max(0, 10 + revenue_growth)
    
    # Component 2: Payment Performance (30 points)
    payment_score = (payment_on_time / 100) * 30
    
    # Component 3: Credit Utilization (20 points)
    if credit_util <= 50:
        credit_score = 20
    elif credit_util <= 75:
        credit_score = 15
    elif credit_util <= 90:
        credit_score = 10
    else:
        credit_score = 5
    
    # Component 4: Account Activity (20 points)
    if net_cash_flow > 0 and transaction_count > 1000:
        activity_score = 20
    elif net_cash_flow > 0:
        activity_score = 15
    elif transaction_count > 1000:
        activity_score = 12
    elif net_cash_flow >= -500000:
        activity_score = 8
    else:
        activity_score = 5
    
    # Calculate overall score
    overall_score = int(revenue_score + payment_score + credit_score + activity_score)
    
    # Determine category
    if overall_score >= 80:
        category = "Excellent"
    elif overall_score >= 70:
        category = "Good"
    elif overall_score >= 60:
        category = "Fair"
    elif overall_score >= 50:
        category = "Needs Attention"
    else:
        category = "Critical"
    
    # Identify strengths
    strengths = []
    if payment_on_time >= 95:
        strengths.append(f"Strong payment performance ({payment_on_time:.1f}% on-time)")
    if revenue_growth > 0:
        strengths.append(f"Positive revenue growth ({revenue_growth:.1f}%)")
    if credit_util < 60:
        strengths.append(f"Healthy credit utilization ({credit_util:.1f}%)")
    if net_cash_flow > 0:
        strengths.append(f"Positive cash flow (${net_cash_flow:,.0f})")
    
    # Identify concerns
    concerns = []
    if payment_on_time < 90:
        concerns.append(f"Payment performance below target ({payment_on_time:.1f}% on-time)")
    if revenue_growth < -2:
        concerns.append(f"Declining revenue trend ({revenue_growth:.1f}%)")
    if credit_util > 85:
        concerns.append(f"High credit utilization ({credit_util:.1f}%)")
    if net_cash_flow < -500000:
        concerns.append(f"Negative cash flow (${net_cash_flow:,.0f})")
    
    # Generate recommendation
    if overall_score >= 80:
        recommendation = "Customer is in excellent health. Focus on growth opportunities and relationship deepening."
    elif overall_score >= 70:
        recommendation = "Customer is performing well. Monitor key metrics and explore expansion opportunities."
    elif overall_score >= 60:
        recommendation = "Customer is stable but showing some weakness. Schedule check-in to discuss concerns."
    elif overall_score >= 50:
        recommendation = "Customer requires attention. Proactive outreach recommended to address issues."
    else:
        recommendation = "Customer is at risk. Immediate intervention required to prevent deterioration."
    
    return {
        "overall_score": overall_score,
        "score_category": category,
        "component_scores": {
            "revenue_stability": round(revenue_score, 1),
            "payment_performance": round(payment_score, 1),
            "credit_utilization": round(credit_score, 1),
            "account_activity": round(activity_score, 1)
        },
        "key_strengths": strengths[:3],  # Top 3
        "areas_of_concern": concerns,
        "recommendation": recommendation,
        "customer_id": financial_data.get("customer_id"),
        "company_name": financial_data.get("company_name")
    }

# Made with Bob
