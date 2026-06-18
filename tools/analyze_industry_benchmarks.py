"""
Tool: analyze_industry_benchmarks
Compares customer metrics against industry benchmarks.
"""

from ibm_watsonx_orchestrate import tool
from typing import Dict, Any

# Industry benchmark data
INDUSTRY_BENCHMARKS = {
    "Technology": {
        "avg_revenue_growth": 12.5,
        "avg_payment_on_time": 94.0,
        "avg_credit_utilization": 55.0,
        "avg_profit_margin": 18.5,
        "typical_products": ["Treasury Management", "Payroll Services", "FX Hedging", "Commercial Insurance"]
    },
    "Manufacturing": {
        "avg_revenue_growth": 6.5,
        "avg_payment_on_time": 91.0,
        "avg_credit_utilization": 68.0,
        "avg_profit_margin": 12.0,
        "typical_products": ["Equipment Financing", "Supply Chain Finance", "Working Capital Line", "ESG Financing"]
    },
    "Retail": {
        "avg_revenue_growth": 4.2,
        "avg_payment_on_time": 87.0,
        "avg_credit_utilization": 75.0,
        "avg_profit_margin": 8.5,
        "typical_products": ["Merchant Services", "Working Capital Line", "Trade Finance", "Commercial Insurance"]
    },
    "Healthcare": {
        "avg_revenue_growth": 7.8,
        "avg_payment_on_time": 93.0,
        "avg_credit_utilization": 62.0,
        "avg_profit_margin": 15.0,
        "typical_products": ["Equipment Financing", "Payroll Services", "Commercial Insurance", "Treasury Management"]
    },
    "Construction": {
        "avg_revenue_growth": 5.5,
        "avg_payment_on_time": 85.0,
        "avg_credit_utilization": 72.0,
        "avg_profit_margin": 10.5,
        "typical_products": ["Equipment Financing", "Working Capital Line", "ESG Financing", "Commercial Insurance"]
    },
    "Transportation": {
        "avg_revenue_growth": 6.0,
        "avg_payment_on_time": 90.0,
        "avg_credit_utilization": 70.0,
        "avg_profit_margin": 11.0,
        "typical_products": ["Equipment Financing", "FX Hedging", "Commercial Insurance", "Working Capital Line"]
    },
    "Financial Services": {
        "avg_revenue_growth": 8.5,
        "avg_payment_on_time": 96.0,
        "avg_credit_utilization": 45.0,
        "avg_profit_margin": 22.0,
        "typical_products": ["Treasury Management", "Commercial Insurance", "Payroll Services", "Merchant Services"]
    },
    "Energy": {
        "avg_revenue_growth": 7.0,
        "avg_payment_on_time": 92.0,
        "avg_credit_utilization": 60.0,
        "avg_profit_margin": 16.0,
        "typical_products": ["ESG Financing", "Equipment Financing", "FX Hedging", "Commercial Insurance"]
    }
}


@tool()
async def analyze_industry_benchmarks(customer_id: str, industry: str) -> Dict[str, Any]:
    """Compares customer metrics against industry benchmarks to identify performance gaps and opportunities.
    
    This tool provides industry-specific benchmark data to help Relationship Managers
    understand how a customer performs relative to their peers. It highlights areas where
    the customer excels or lags behind industry averages.
    
    Args:
        customer_id (str): The unique customer identifier (format: CUST-XXX)
        industry (str): Customer's industry sector (Technology, Manufacturing, Retail, etc.)
        
    Returns:
        dict: Benchmark comparison containing:
            - industry (str): Industry sector
            - benchmarks (dict): Industry average metrics
            - customer_metrics (dict): Customer's actual metrics
            - percentile_rankings (dict): Customer's percentile rank in each category
            - performance_summary (str): Overall performance assessment
            - recommendations (list): Suggested actions based on gaps
            
    Example:
        >>> result = await analyze_industry_benchmarks("CUST-001", "Technology")
        >>> print(result["percentile_rankings"]["revenue_growth"])
        "75th percentile"
    """
    
    # Get industry benchmarks
    if industry not in INDUSTRY_BENCHMARKS:
        return {
            "error": f"Industry '{industry}' not found",
            "available_industries": list(INDUSTRY_BENCHMARKS.keys())
        }
    
    benchmarks = INDUSTRY_BENCHMARKS[industry]
    
    # Import customer data to get actual metrics
    from .analyze_financial_health import CUSTOMER_DATA
    
    if customer_id not in CUSTOMER_DATA:
        return {
            "error": f"Customer {customer_id} not found"
        }
    
    customer = CUSTOMER_DATA[customer_id]
    
    # Calculate customer metrics
    revenue_growth = round(
        ((customer["revenue_trend_90d"][-1] - customer["revenue_trend_90d"][0]) / 
         customer["revenue_trend_90d"][0] * 100), 2
    )
    payment_on_time = customer["payment_history"]["on_time_percentage"]
    credit_util = customer["credit_utilization"]
    
    # Calculate percentile rankings
    def calculate_percentile(customer_value, benchmark_value, higher_is_better=True):
        if higher_is_better:
            if customer_value >= benchmark_value * 1.15:
                return "90th percentile (Top 10%)"
            elif customer_value >= benchmark_value * 1.05:
                return "75th percentile (Above Average)"
            elif customer_value >= benchmark_value * 0.95:
                return "50th percentile (Average)"
            elif customer_value >= benchmark_value * 0.85:
                return "25th percentile (Below Average)"
            else:
                return "10th percentile (Bottom 10%)"
        else:  # Lower is better (e.g., credit utilization)
            if customer_value <= benchmark_value * 0.85:
                return "90th percentile (Top 10%)"
            elif customer_value <= benchmark_value * 0.95:
                return "75th percentile (Above Average)"
            elif customer_value <= benchmark_value * 1.05:
                return "50th percentile (Average)"
            elif customer_value <= benchmark_value * 1.15:
                return "25th percentile (Below Average)"
            else:
                return "10th percentile (Bottom 10%)"
    
    percentile_rankings = {
        "revenue_growth": calculate_percentile(revenue_growth, benchmarks["avg_revenue_growth"], True),
        "payment_performance": calculate_percentile(payment_on_time, benchmarks["avg_payment_on_time"], True),
        "credit_utilization": calculate_percentile(credit_util, benchmarks["avg_credit_utilization"], False)
    }
    
    # Generate performance summary
    above_avg_count = sum(1 for p in percentile_rankings.values() if "90th" in p or "75th" in p)
    below_avg_count = sum(1 for p in percentile_rankings.values() if "25th" in p or "10th" in p)
    
    if above_avg_count >= 2:
        performance_summary = f"Customer performs above industry average in {above_avg_count} of 3 key metrics"
    elif below_avg_count >= 2:
        performance_summary = f"Customer underperforms industry average in {below_avg_count} of 3 key metrics"
    else:
        performance_summary = "Customer performs at industry average across key metrics"
    
    # Generate recommendations
    recommendations = []
    
    if revenue_growth < benchmarks["avg_revenue_growth"]:
        recommendations.append(f"Revenue growth ({revenue_growth:.1f}%) below industry avg ({benchmarks['avg_revenue_growth']:.1f}%). Explore growth financing options.")
    
    if payment_on_time < benchmarks["avg_payment_on_time"]:
        recommendations.append(f"Payment performance ({payment_on_time:.1f}%) below industry avg ({benchmarks['avg_payment_on_time']:.1f}%). Consider cash flow management solutions.")
    
    if credit_util > benchmarks["avg_credit_utilization"]:
        recommendations.append(f"Credit utilization ({credit_util:.1f}%) above industry avg ({benchmarks['avg_credit_utilization']:.1f}%). Review credit line adequacy.")
    
    if not recommendations:
        recommendations.append("Customer metrics align well with industry benchmarks. Focus on relationship deepening and cross-sell opportunities.")
    
    return {
        "customer_id": customer_id,
        "company_name": customer["company_name"],
        "industry": industry,
        "benchmarks": {
            "avg_revenue_growth": benchmarks["avg_revenue_growth"],
            "avg_payment_on_time": benchmarks["avg_payment_on_time"],
            "avg_credit_utilization": benchmarks["avg_credit_utilization"],
            "avg_profit_margin": benchmarks["avg_profit_margin"]
        },
        "customer_metrics": {
            "revenue_growth": revenue_growth,
            "payment_on_time": payment_on_time,
            "credit_utilization": credit_util
        },
        "percentile_rankings": percentile_rankings,
        "performance_summary": performance_summary,
        "recommendations": recommendations,
        "typical_products_for_industry": benchmarks["typical_products"]
    }

# Made with Bob
