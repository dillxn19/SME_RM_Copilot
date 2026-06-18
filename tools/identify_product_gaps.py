"""
Tool: identify_product_gaps
Identifies products the customer doesn't have but should consider based on their profile.
"""

from ibm_watsonx_orchestrate import tool
from typing import Dict, Any

# Product catalog with fit criteria
PRODUCT_CATALOG = {
    "Treasury Management": {
        "description": "Automated cash management and payment processing",
        "typical_revenue_range": [10000000, 100000000],
        "industries": ["Manufacturing", "Retail", "Technology", "Healthcare"],
        "revenue_potential_range": [150000, 350000]
    },
    "Equipment Financing": {
        "description": "Financing for equipment purchases and upgrades",
        "typical_revenue_range": [5000000, 75000000],
        "industries": ["Manufacturing", "Construction", "Healthcare", "Transportation"],
        "revenue_potential_range": [100000, 500000]
    },
    "Trade Finance": {
        "description": "Import/export financing and letters of credit",
        "typical_revenue_range": [15000000, 150000000],
        "industries": ["Manufacturing", "Retail", "Technology"],
        "revenue_potential_range": [80000, 250000]
    },
    "Working Capital Line": {
        "description": "Revolving credit line for operational expenses",
        "typical_revenue_range": [5000000, 50000000],
        "industries": ["Retail", "Manufacturing", "Construction", "Technology"],
        "revenue_potential_range": [200000, 400000]
    },
    "FX Hedging": {
        "description": "Foreign exchange risk management solutions",
        "typical_revenue_range": [20000000, 200000000],
        "industries": ["Manufacturing", "Technology", "Retail"],
        "revenue_potential_range": [75000, 200000]
    },
    "ESG Financing": {
        "description": "Sustainable and green financing programs",
        "typical_revenue_range": [10000000, 100000000],
        "industries": ["Manufacturing", "Energy", "Construction"],
        "revenue_potential_range": [150000, 300000]
    },
    "Merchant Services": {
        "description": "Payment processing and POS solutions",
        "typical_revenue_range": [3000000, 50000000],
        "industries": ["Retail", "Healthcare", "Financial Services"],
        "revenue_potential_range": [50000, 150000]
    },
    "Payroll Services": {
        "description": "Automated payroll processing and tax filing",
        "typical_revenue_range": [5000000, 75000000],
        "industries": ["All"],
        "revenue_potential_range": [40000, 120000]
    },
    "Commercial Insurance": {
        "description": "Business insurance products and risk management",
        "typical_revenue_range": [8000000, 100000000],
        "industries": ["All"],
        "revenue_potential_range": [60000, 180000]
    },
    "Supply Chain Finance": {
        "description": "Supplier payment optimization and financing",
        "typical_revenue_range": [25000000, 200000000],
        "industries": ["Manufacturing", "Retail", "Construction"],
        "revenue_potential_range": [100000, 350000]
    }
}

# Current product holdings by customer
CUSTOMER_PRODUCTS = {
    "CUST-001": ["Business Checking", "Business Savings", "Commercial Loan"],
    "CUST-002": ["Business Checking", "Commercial Loan", "Working Capital Line"],
    "CUST-003": ["Business Checking", "Merchant Services"],
    "CUST-004": ["Business Checking", "Business Savings", "Commercial Loan", "Payroll Services"],
    "CUST-005": ["Business Checking", "Commercial Loan", "Equipment Financing", "Commercial Insurance"],
    "CUST-006": ["Business Checking", "Commercial Loan", "FX Hedging"],
    "CUST-007": ["Business Checking", "Business Savings", "Payroll Services"],
    "CUST-008": ["Business Checking", "Business Savings", "Commercial Insurance", "Merchant Services"],
    "CUST-009": ["Business Checking", "Merchant Services"],
    "CUST-010": ["Business Checking", "Commercial Loan", "ESG Financing", "Commercial Insurance"]
}

# Customer data reference (minimal for this tool)
CUSTOMER_DATA = {
    "CUST-001": {"company_name": "TechVenture Solutions", "industry": "Technology", "annual_revenue": 28000000, "relationship_tenure_years": 8},
    "CUST-002": {"company_name": "GreenLeaf Manufacturing", "industry": "Manufacturing", "annual_revenue": 42000000, "relationship_tenure_years": 12},
    "CUST-003": {"company_name": "UrbanRetail Group", "industry": "Retail", "annual_revenue": 15000000, "relationship_tenure_years": 5},
    "CUST-004": {"company_name": "Meridian Healthcare Services", "industry": "Healthcare", "annual_revenue": 35000000, "relationship_tenure_years": 7},
    "CUST-005": {"company_name": "Pinnacle Construction Group", "industry": "Construction", "annual_revenue": 52000000, "relationship_tenure_years": 15},
    "CUST-006": {"company_name": "BlueLine Logistics", "industry": "Transportation", "annual_revenue": 22000000, "relationship_tenure_years": 6},
    "CUST-007": {"company_name": "NovaTech Solutions", "industry": "Technology", "annual_revenue": 18000000, "relationship_tenure_years": 4},
    "CUST-008": {"company_name": "Brightpath Insurance Agency", "industry": "Financial Services", "annual_revenue": 12000000, "relationship_tenure_years": 9},
    "CUST-009": {"company_name": "Atlas Retail Partners", "industry": "Retail", "annual_revenue": 8500000, "relationship_tenure_years": 3},
    "CUST-010": {"company_name": "Quantum Energy Systems", "industry": "Energy", "annual_revenue": 48000000, "relationship_tenure_years": 11}
}


@tool()
async def identify_product_gaps(customer_id: str) -> Dict[str, Any]:
    """Identifies products the customer doesn't have but should consider based on their profile and industry.
    
    This tool analyzes the customer's current product portfolio against the full product
    catalog and identifies gaps that represent cross-sell and upsell opportunities. It
    considers the customer's industry, revenue size, and business profile to recommend
    the most relevant products with estimated revenue potential.
    
    Args:
        customer_id (str): The unique customer identifier (format: CUST-XXX)
        
    Returns:
        dict: Product gap analysis containing:
            - customer_id (str): Customer identifier
            - current_products (list): Products customer currently has
            - product_gaps (list): Recommended products with details
            - total_opportunity_value (int): Sum of all opportunity revenue potential
            - top_3_opportunities (list): Highest priority recommendations
            
    Example:
        >>> result = await identify_product_gaps("CUST-001")
        >>> print(len(result["product_gaps"]))
        7
        >>> print(result["top_3_opportunities"][0]["product_name"])
        "Treasury Management"
    """
    
    if customer_id not in CUSTOMER_DATA:
        return {
            "error": f"Customer {customer_id} not found",
            "available_customers": list(CUSTOMER_DATA.keys())
        }
    
    customer = CUSTOMER_DATA[customer_id]
    current_products = CUSTOMER_PRODUCTS.get(customer_id, ["Business Checking"])
    
    # Identify product gaps
    product_gaps = []
    
    for product_name, product_info in PRODUCT_CATALOG.items():
        # Skip if customer already has this product
        if product_name in current_products:
            continue
        
        # Calculate fit score (0-100)
        fit_score = 0
        
        # Industry fit (40 points)
        if customer["industry"] in product_info["industries"] or "All" in product_info["industries"]:
            fit_score += 40
        
        # Revenue fit (40 points)
        min_rev, max_rev = product_info["typical_revenue_range"]
        if min_rev <= customer["annual_revenue"] <= max_rev:
            fit_score += 40
        elif customer["annual_revenue"] < min_rev:
            if customer["annual_revenue"] >= min_rev * 0.7:
                fit_score += 25
        elif customer["annual_revenue"] > max_rev:
            fit_score += 35
        
        # Relationship tenure bonus (20 points)
        if customer["relationship_tenure_years"] >= 5:
            fit_score += 20
        elif customer["relationship_tenure_years"] >= 2:
            fit_score += 10
        
        # Only include products with fit score >= 60
        if fit_score >= 60:
            min_potential, max_potential = product_info["revenue_potential_range"]
            revenue_factor = customer["annual_revenue"] / 30000000
            estimated_revenue = int((min_potential + max_potential) / 2 * revenue_factor)
            
            product_gaps.append({
                "product_name": product_name,
                "description": product_info["description"],
                "fit_score": fit_score,
                "estimated_annual_revenue": estimated_revenue,
                "rationale": f"Strong fit for {customer['industry']} companies with ${customer['annual_revenue']:,.0f} revenue"
            })
    
    # Sort by fit score and revenue potential
    product_gaps.sort(key=lambda x: (x["fit_score"], x["estimated_annual_revenue"]), reverse=True)
    
    # Calculate total opportunity
    total_opportunity = sum(p["estimated_annual_revenue"] for p in product_gaps)
    
    return {
        "customer_id": customer_id,
        "company_name": customer["company_name"],
        "industry": customer["industry"],
        "current_products": current_products,
        "current_product_count": len(current_products),
        "product_gaps": product_gaps,
        "product_gap_count": len(product_gaps),
        "total_opportunity_value": total_opportunity,
        "top_3_opportunities": product_gaps[:3]
    }

# Made with Bob
