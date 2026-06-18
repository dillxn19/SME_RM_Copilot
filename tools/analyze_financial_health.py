"""
Tool: analyze_financial_health
Analyzes customer financial health metrics including revenue trends, payment history,
credit utilization, and account activity.
"""

from ibm_watsonx_orchestrate import tool
from typing import Dict, Any

# Synthetic data for 10 demo customers (Faker seed=42 equivalent)
CUSTOMER_DATA = {
    "CUST-001": {
        "company_name": "TechVenture Solutions",
        "industry": "Technology",
        "annual_revenue": 28000000,
        "relationship_tenure_years": 8,
        "revenue_trend_90d": [9200000, 9450000, 9350000],  # Last 3 months
        "payment_history": {
            "on_time_percentage": 98.5,
            "average_days_late": 0.5,
            "late_payments_90d": 0
        },
        "credit_utilization": 45.2,
        "account_activity": {
            "transaction_count_90d": 847,
            "average_daily_balance": 1850000,
            "deposits_90d": 28500000,
            "withdrawals_90d": 27200000
        }
    },
    "CUST-002": {
        "company_name": "GreenLeaf Manufacturing",
        "industry": "Manufacturing",
        "annual_revenue": 42000000,
        "relationship_tenure_years": 12,
        "revenue_trend_90d": [13800000, 14100000, 14100000],
        "payment_history": {
            "on_time_percentage": 95.0,
            "average_days_late": 2.1,
            "late_payments_90d": 1
        },
        "credit_utilization": 62.8,
        "account_activity": {
            "transaction_count_90d": 1243,
            "average_daily_balance": 2950000,
            "deposits_90d": 42800000,
            "withdrawals_90d": 41200000
        }
    },
    "CUST-003": {
        "company_name": "UrbanRetail Group",
        "industry": "Retail",
        "annual_revenue": 15000000,
        "relationship_tenure_years": 5,
        "revenue_trend_90d": [5200000, 4850000, 4950000],
        "payment_history": {
            "on_time_percentage": 78.5,
            "average_days_late": 8.3,
            "late_payments_90d": 2
        },
        "credit_utilization": 92.1,
        "account_activity": {
            "transaction_count_90d": 2156,
            "average_daily_balance": 425000,
            "deposits_90d": 15200000,
            "withdrawals_90d": 15800000
        }
    },
    "CUST-004": {
        "company_name": "Meridian Healthcare Services",
        "industry": "Healthcare",
        "annual_revenue": 35000000,
        "relationship_tenure_years": 7,
        "revenue_trend_90d": [11500000, 11700000, 11800000],
        "payment_history": {
            "on_time_percentage": 92.0,
            "average_days_late": 3.5,
            "late_payments_90d": 1
        },
        "credit_utilization": 58.4,
        "account_activity": {
            "transaction_count_90d": 1876,
            "average_daily_balance": 1950000,
            "deposits_90d": 35800000,
            "withdrawals_90d": 34500000
        }
    },
    "CUST-005": {
        "company_name": "Pinnacle Construction Group",
        "industry": "Construction",
        "annual_revenue": 52000000,
        "relationship_tenure_years": 15,
        "revenue_trend_90d": [17000000, 17500000, 17500000],
        "payment_history": {
            "on_time_percentage": 88.0,
            "average_days_late": 5.2,
            "late_payments_90d": 2
        },
        "credit_utilization": 75.3,
        "account_activity": {
            "transaction_count_90d": 956,
            "average_daily_balance": 3200000,
            "deposits_90d": 53500000,
            "withdrawals_90d": 51800000
        }
    },
    "CUST-006": {
        "company_name": "BlueLine Logistics",
        "industry": "Transportation",
        "annual_revenue": 22000000,
        "relationship_tenure_years": 6,
        "revenue_trend_90d": [7200000, 7350000, 7450000],
        "payment_history": {
            "on_time_percentage": 94.5,
            "average_days_late": 2.8,
            "late_payments_90d": 1
        },
        "credit_utilization": 68.9,
        "account_activity": {
            "transaction_count_90d": 1534,
            "average_daily_balance": 1150000,
            "deposits_90d": 22500000,
            "withdrawals_90d": 21800000
        }
    },
    "CUST-007": {
        "company_name": "NovaTech Solutions",
        "industry": "Technology",
        "annual_revenue": 18000000,
        "relationship_tenure_years": 4,
        "revenue_trend_90d": [5900000, 6050000, 6050000],
        "payment_history": {
            "on_time_percentage": 96.5,
            "average_days_late": 1.2,
            "late_payments_90d": 0
        },
        "credit_utilization": 52.1,
        "account_activity": {
            "transaction_count_90d": 723,
            "average_daily_balance": 980000,
            "deposits_90d": 18300000,
            "withdrawals_90d": 17900000
        }
    },
    "CUST-008": {
        "company_name": "Brightpath Insurance Agency",
        "industry": "Financial Services",
        "annual_revenue": 12000000,
        "relationship_tenure_years": 9,
        "revenue_trend_90d": [3950000, 4000000, 4050000],
        "payment_history": {
            "on_time_percentage": 99.0,
            "average_days_late": 0.3,
            "late_payments_90d": 0
        },
        "credit_utilization": 38.7,
        "account_activity": {
            "transaction_count_90d": 1245,
            "average_daily_balance": 1650000,
            "deposits_90d": 12200000,
            "withdrawals_90d": 11800000
        }
    },
    "CUST-009": {
        "company_name": "Atlas Retail Partners",
        "industry": "Retail",
        "annual_revenue": 8500000,
        "relationship_tenure_years": 3,
        "revenue_trend_90d": [2800000, 2750000, 2950000],
        "payment_history": {
            "on_time_percentage": 85.0,
            "average_days_late": 6.5,
            "late_payments_90d": 2
        },
        "credit_utilization": 81.4,
        "account_activity": {
            "transaction_count_90d": 1876,
            "average_daily_balance": 325000,
            "deposits_90d": 8600000,
            "withdrawals_90d": 8900000
        }
    },
    "CUST-010": {
        "company_name": "Quantum Energy Systems",
        "industry": "Energy",
        "annual_revenue": 48000000,
        "relationship_tenure_years": 11,
        "revenue_trend_90d": [15800000, 16000000, 16200000],
        "payment_history": {
            "on_time_percentage": 97.5,
            "average_days_late": 0.8,
            "late_payments_90d": 0
        },
        "credit_utilization": 55.6,
        "account_activity": {
            "transaction_count_90d": 1087,
            "average_daily_balance": 4200000,
            "deposits_90d": 48500000,
            "withdrawals_90d": 47200000
        }
    }
}


@tool()
async def analyze_financial_health(customer_id: str) -> Dict[str, Any]:
    """Analyzes customer financial health metrics including revenue trends, payment history, credit utilization, and account activity.
    
    This tool retrieves comprehensive financial data for a customer to assess their
    overall financial health and stability. The data includes revenue trends over the
    last 90 days, payment performance, credit utilization, and account activity metrics.
    
    Args:
        customer_id (str): The unique customer identifier (format: CUST-XXX)
        
    Returns:
        dict: Financial health metrics containing:
            - company_name (str): Customer company name
            - industry (str): Industry sector
            - annual_revenue (int): Annual revenue in USD
            - relationship_tenure_years (int): Years as customer
            - revenue_trend_90d (list): Monthly revenue for last 3 months
            - payment_history (dict): Payment performance metrics
            - credit_utilization (float): Credit utilization percentage
            - account_activity (dict): Transaction and balance metrics
            
    Example:
        >>> result = await analyze_financial_health("CUST-001")
        >>> print(result["company_name"])
        "TechVenture Solutions"
        >>> print(result["payment_history"]["on_time_percentage"])
        98.5
    """
    
    # Validate customer ID
    if customer_id not in CUSTOMER_DATA:
        return {
            "error": f"Customer {customer_id} not found",
            "available_customers": list(CUSTOMER_DATA.keys())
        }
    
    # Return customer financial data
    customer = CUSTOMER_DATA[customer_id]
    
    return {
        "customer_id": customer_id,
        "company_name": customer["company_name"],
        "industry": customer["industry"],
        "annual_revenue": customer["annual_revenue"],
        "relationship_tenure_years": customer["relationship_tenure_years"],
        "revenue_trend_90d": customer["revenue_trend_90d"],
        "revenue_growth_rate": round(
            ((customer["revenue_trend_90d"][-1] - customer["revenue_trend_90d"][0]) / 
             customer["revenue_trend_90d"][0] * 100), 2
        ),
        "payment_history": customer["payment_history"],
        "credit_utilization": customer["credit_utilization"],
        "account_activity": customer["account_activity"],
        "net_cash_flow_90d": customer["account_activity"]["deposits_90d"] - 
                             customer["account_activity"]["withdrawals_90d"]
    }

# Made with Bob
