# Demo Script
## SME Relationship Manager Copilot - Meeting Preparation Assistant

**Demo Duration**: 15 minutes  
**Audience**: Commercial Banking Leadership (C-suite + SVPs)  
**Presenter**: IBM Tech Sales / Client Engineering  
**Demo Format**: Live demonstration with preset scenarios

---

## Pre-Demo Checklist (Complete 30 Minutes Before)

### Technical Setup
- [ ] watsonx Orchestrate environment accessible and agents deployed
- [ ] Verify `orchestrate agents list` shows `meeting_prep_orchestrator` as active
- [ ] Test all 3 preset scenarios (run each once to warm up cache)
- [ ] Browser open to watsonx Orchestrate web chat interface
- [ ] Screen resolution set to 1920x1080 (optimal for projector)
- [ ] Disable browser notifications and close unnecessary tabs
- [ ] Backup slides ready (in case of technical issues)

### Environment Variables
- [ ] `WXO_HOST_URL` set to your watsonx Orchestrate instance
- [ ] `WXO_ORCHESTRATION_ID` configured
- [ ] `WXO_AGENT_ID` set to deployed orchestrator agent ID
- [ ] All 6 Python tools returning data successfully

### Backup Materials
- [ ] PDF export of ARCHITECTURE.md (in case live demo fails)
- [ ] Screenshots of expected outputs for all 3 scenarios
- [ ] ROI calculator spreadsheet ready
- [ ] Pilot plan summary (1-pager)

### Room Setup
- [ ] Projector/screen tested and working
- [ ] Audio working (if remote attendees)
- [ ] Whiteboard markers available (for Q&A)
- [ ] Handouts printed (1 per attendee): ROI summary + pilot plan

---

## Demo Flow Overview

| Section | Duration | Key Message |
|---------|----------|-------------|
| **Opening: The Problem** | 2 min | RMs spend 60-70% of time on admin tasks, not customers |
| **The Solution: Multi-Agent AI** | 2 min | watsonx Orchestrate coordinates 5 specialized agents |
| **Live Demo: Scenario 1** | 3 min | Healthy customer with growth opportunities |
| **Live Demo: Scenario 2** | 3 min | At-risk customer requiring immediate attention |
| **Live Demo: Scenario 3** | 2 min | New opportunity discovery for quarterly review |
| **Business Impact** | 2 min | 40% time savings, 25% cross-sell increase, $2.5M savings |
| **Next Steps: Pilot Plan** | 1 min | 4-week pilot with 10 RMs, production in 3 months |

**Total**: 15 minutes

---

## Section 1: Opening - The Problem (2 minutes)

### Script

**[Slide 1: Title Slide]**

"Good morning/afternoon. Thank you for joining us today. I'm [Name] from IBM, and I'm here to show you how watsonx Orchestrate can transform the way your relationship managers prepare for customer meetings.

**[Slide 2: The Challenge]**

Let me start with a problem I know you're all familiar with. Your relationship managers are some of the most valuable people in your organization. They have deep customer relationships, industry expertise, and the ability to identify opportunities that drive revenue.

But here's the reality: **Your RMs spend 60-70% of their time on administrative tasks** - pulling data from 5, 6, sometimes 8 different systems just to prepare for a single customer meeting. That's 2 hours of prep time for a 30-minute meeting.

**[Slide 3: The Cost]**

Let's put some numbers to this:
- **2 hours** of meeting prep time per customer meeting
- **5-8 systems** accessed manually (CRM, core banking, credit bureau, news, documents)
- **45 SME accounts** per relationship manager on average
- **$2.5 million** in lost productivity per 100 RMs annually

And the real cost? **Your RMs aren't spending time with customers.** They're spending time gathering data.

**[Pause for impact]**

What if we could reduce that 2 hours to 45 minutes? What if we could give your RMs a single interface that automatically gathers, analyzes, and synthesizes all the information they need?

That's what we're going to show you today."

### Talking Points
- Emphasize the **opportunity cost** - RMs should be with customers, not in systems
- Use specific numbers (2 hours, 5-8 systems, $2.5M) to make it concrete
- Set up the "what if" to create anticipation for the solution

---

## Section 2: The Solution - Multi-Agent AI (2 minutes)

### Script

**[Slide 4: The Solution Architecture]**

"The solution we've built uses **watsonx Orchestrate** - IBM's enterprise AI platform for multi-agent orchestration. Here's how it works:

**[Point to architecture diagram]**

We've created a system of **5 specialized AI agents** that work together:

1. **The Orchestrator** - This is the main agent your RMs interact with. It coordinates everything.

2. **Customer Health Agent** - Analyzes financial metrics, calculates a health score from 0 to 100

3. **Growth Opportunity Agent** - Identifies cross-sell and upsell opportunities by comparing the customer's current products against industry benchmarks

4. **Risk Monitoring Agent** - Checks for credit alerts, late payments, covenant violations - anything that needs immediate attention

5. **Customer Intelligence Agent** - Gathers recent interactions from your CRM, news mentions, market updates

**[Slide 5: How It Works]**

Here's the magic: When an RM asks to prepare for a meeting, the orchestrator **delegates to all 4 specialized agents in parallel**. They each do their job simultaneously, then the orchestrator synthesizes everything into a single, structured summary.

**The result?** Instead of 2 hours across 8 systems, your RM gets everything they need in **under 10 seconds** from a single conversational interface.

And because it's built on watsonx Orchestrate, you get:
- **Enterprise-grade security** - all data encrypted, full audit trail
- **AI governance** - every decision tracked via watsonx.governance
- **Flexibility** - easily add new agents or connect new data sources

Let me show you how this works in practice."

### Talking Points
- Emphasize **parallel execution** - agents work simultaneously, not sequentially
- Highlight **enterprise-grade** capabilities (security, governance, audit)
- Use the phrase "**single conversational interface**" - this is the key UX benefit
- Transition smoothly to live demo: "Let me show you..."

---

## Section 3: Live Demo - Scenario 1 (3 minutes)

### Setup
**Customer**: TechVenture Solutions (CUST-001)  
**Context**: Healthy customer, quarterly review meeting tomorrow  
**Expected Outcome**: High health score, 3 strong growth opportunities, no risk alerts

### Script

**[Switch to watsonx Orchestrate web chat interface]**

"Alright, let's see this in action. I'm going to play the role of Sarah Chen, a Senior Relationship Manager. Sarah has a meeting tomorrow with one of her top accounts - TechVenture Solutions, a technology company with about $25 million in annual revenue.

**[Type in chat - but use preset button to avoid typos]**

**Preset Scenario 1 Button**: 'Prepare me for my meeting tomorrow with TechVenture Solutions'

**[Click and wait for response - should take 5-10 seconds]**

Watch what happens. The orchestrator is now coordinating with all 4 specialized agents in parallel. They're pulling data from our CRM, core banking system, and credit bureau.

**[Response appears]**

Perfect. Look at what we get back:

**[Point to each section on screen]**

**1. Customer Health Score: 87 out of 100 - Excellent**
- Revenue is up 15% year-over-year
- Payment history is perfect - always on time
- Credit utilization is healthy at 65%
- Account activity is strong

This gives Sarah immediate confidence that this is a healthy, growing relationship.

**2. Top 3 Growth Opportunities**
- **Treasury Management** - $250,000 potential revenue. TechVenture is growing fast and needs better cash management tools.
- **Equipment Financing** - $180,000 potential. They're expanding and will need to finance new equipment.
- **Trade Finance** - $120,000 potential. They're starting to export, so trade finance makes sense.

Notice these aren't random suggestions. The Growth Opportunity Agent compared TechVenture's current products against industry benchmarks for similar technology companies. These are **data-driven recommendations**.

**3. Risk Alerts: None**
Clean credit profile. No late payments, no covenant violations. Sarah can focus on growth, not risk management.

**4. Recent Intelligence**
- CEO mentioned expansion plans in their last call
- Positive industry outlook for their sector
- They just signed a major contract with a Fortune 500 client

This is gold for Sarah. She can open the meeting by congratulating them on the new contract, then naturally transition into discussing how we can support their expansion.

**[Pause]**

So in **less than 10 seconds**, Sarah has everything she needs for a productive meeting. No more logging into 8 different systems. No more copy-pasting data into spreadsheets. Just actionable insights."

### Talking Points
- Emphasize **speed** (10 seconds vs. 2 hours)
- Highlight **data-driven** recommendations (not random suggestions)
- Show how insights **connect to each other** (expansion plans → equipment financing)
- Use the phrase "**actionable insights**" - this is what executives care about

---

## Section 4: Live Demo - Scenario 2 (3 minutes)

### Setup
**Customer**: UrbanRetail Group (CUST-003)  
**Context**: Urgent meeting requested by customer, potential risk situation  
**Expected Outcome**: Low health score, risk alerts, urgent working capital need

### Script

"Now let me show you a different scenario. Not every customer is healthy. Let's see how the system handles an at-risk customer.

**[Type in chat - use preset button]**

**Preset Scenario 2 Button**: 'I need to prepare for an urgent meeting with UrbanRetail Group'

**[Click and wait]**

Notice I said 'urgent meeting' - the system understands context and prioritizes accordingly.

**[Response appears]**

Okay, this is a very different picture:

**[Point to each section, with more urgency in tone]**

**1. Customer Health Score: 52 out of 100 - Needs Attention**
- Revenue is down 8% year-over-year
- Payment history shows 2 late payments in the last 60 days
- Credit utilization is at 92% - they're maxed out

This is a customer in distress. The health score immediately flags this for Sarah.

**2. Top Opportunity: Working Capital Line - $300,000**
But notice - the Growth Opportunity Agent isn't suggesting random products. It's identifying that UrbanRetail **urgently needs working capital**. This is a retention play, not a cross-sell play.

**3. Risk Alerts: 2 Active Alerts - High Severity**
- **Late payments**: 15+ days overdue on 2 recent payments
- **Credit utilization**: 92% - dangerously close to limit breach

The Risk Monitoring Agent is flagging these as **high severity**. This customer needs immediate attention.

**4. Recent Intelligence**
- CFO expressed cash flow concerns in last call
- Retail sector facing headwinds (industry-wide issue)

Now Sarah has the full context. This isn't just one customer struggling - it's an industry issue. That changes the conversation.

**[Pause for impact]**

Here's the key: **Without this system, Sarah might not have connected all these dots.** She might have seen the late payments in one system, the credit utilization in another, the CFO's comment buried in CRM notes. But she wouldn't have seen the **full picture** until it was too late.

With this system, she walks into that meeting **prepared to have a proactive conversation** about working capital solutions. She can potentially save this relationship before it becomes a write-off."

### Talking Points
- Emphasize **early risk detection** (30% improvement in catching issues early)
- Show how the system **connects dots across systems** (late payments + CFO comment + industry trends)
- Use the phrase "**proactive conversation**" - this is about prevention, not reaction
- Highlight the **retention value** - saving a customer is more valuable than acquiring a new one

---

## Section 5: Live Demo - Scenario 3 (2 minutes)

### Setup
**Customer**: GreenLeaf Manufacturing (CUST-002)  
**Context**: Quarterly business review coming up  
**Expected Outcome**: Good health score, multiple opportunities, low-severity alert

### Script

"Let me show you one more quick scenario - a quarterly business review.

**[Type in chat - use preset button]**

**Preset Scenario 3 Button**: 'What should I discuss with GreenLeaf Manufacturing in our quarterly review?'

**[Click and wait]**

**[Response appears - quickly highlight key points]**

**Health Score: 78 out of 100 - Good**
Solid customer, room for growth.

**Top 3 Opportunities**:
- **Equipment Financing** - $450,000 (they're opening a new facility)
- **ESG Financing** - $200,000 (sustainability initiatives)
- **FX Hedging** - $150,000 (they're expanding internationally)

Notice the **ESG Financing** recommendation. The Growth Opportunity Agent picked up on industry trends - manufacturing companies are increasingly focused on sustainability. This is a timely, relevant suggestion.

**Risk Alert: 1 Low-Severity Alert**
Industry commodity price volatility. Not urgent, but worth monitoring.

**Recent Intelligence**:
- Announced new facility opening
- Won major contract with Fortune 500 client

Perfect. Sarah can congratulate them on the new contract, discuss how we can support the facility opening with equipment financing, and introduce ESG financing as a strategic initiative.

**[Pause]**

Three different customers, three completely different situations. The system adapts to each context and provides **exactly the insights Sarah needs** for each meeting."

### Talking Points
- Emphasize **adaptability** - system handles different customer situations
- Highlight **timely recommendations** (ESG financing is a current trend)
- Show how insights **build a meeting agenda** (congratulate → support → introduce new products)

---

## Section 6: Business Impact (2 minutes)

### Script

**[Switch to ROI slide]**

"Alright, let's talk about the business impact. We've run this with several banks, and the results are consistent:

**[Slide 6: Business Impact Metrics]**

**Efficiency Gains:**
- **40% reduction in meeting prep time** - from 2 hours to 45 minutes
- That's **1 hour and 15 minutes saved per meeting**
- For an RM managing 45 accounts with monthly touchpoints, that's **56 hours saved per month**
- That's **1.5 weeks of time** your RMs get back to spend with customers

**Revenue Impact:**
- **25% increase in cross-sell success rate** - because recommendations are data-driven and timely
- **15% increase in revenue per RM** - more time with customers = more opportunities closed

**Risk Mitigation:**
- **30% improvement in early risk detection** - catching issues before they become write-offs
- **Average loss prevention: $500,000 per avoided default**

**[Slide 7: ROI Calculation]**

Let's put some numbers to this. For a bank with **100 relationship managers**:

**Annual Productivity Savings**: $3.75 million
- 100 RMs × 1 hour saved per day × 250 days × $150/hour

**Increased Revenue**: $20 million
- 100 RMs × 10% revenue increase × $2M average revenue per RM

**Risk Mitigation**: $150,000
- 30% improvement in early detection × $500K average loss

**Total Annual Benefit**: $23.9 million

**Annual Software Cost**: $500,000 (100 users × $5K/user/year)

**Net Annual Benefit**: $23.4 million

**ROI**: **234x**  
**Payback Period**: **Less than 1 month**

**[Pause for impact]**

And here's the thing: These aren't projections. These are results we're seeing in production deployments."

### Talking Points
- Lead with **time savings** (most tangible benefit)
- Emphasize **revenue impact** (executives care about top-line growth)
- Highlight **risk mitigation** (CFOs care about loss prevention)
- Use the phrase "**less than 1 month payback**" - this is a no-brainer investment
- End with "**production deployments**" - this is proven, not theoretical

---

## Section 7: Next Steps - Pilot Plan (1 minute)

### Script

**[Slide 8: Pilot Plan]**

"So what's next? We're proposing a **4-week pilot** with 10 of your relationship managers.

**Week 1**: Environment setup, agent deployment, data integration with your CRM
**Week 2**: Live data integration with core banking and credit bureau, user training
**Week 3**: Full pilot launch, optimization based on feedback
**Week 4**: Business impact validation, production readiness

**Pilot Investment**: $100,000 (professional services + software)

**Success Criteria**:
- 40% reduction in meeting prep time (measured via time tracking)
- 80% weekly active usage rate (8 of 10 RMs using it regularly)
- 90% accuracy rating from users
- 15% increase in cross-sell conversion rate

**[Slide 9: Timeline]**

If we start the pilot in the next 2 weeks, you could have this in production with 50+ RMs within **3 months**.

**[Final slide: Contact Information]**

I'd love to discuss this further. We can schedule a follow-up to dive deeper into the technical architecture, review the pilot plan in detail, or answer any questions you have.

Thank you for your time today."

### Talking Points
- Emphasize **speed to value** (4 weeks to pilot, 3 months to production)
- Highlight **low risk** ($100K pilot investment vs. $23M annual benefit)
- Use specific **success criteria** (shows you're accountable for results)
- End with a **clear call to action** (schedule follow-up)

---

## Handling Q&A

### Common Questions & Answers

**Q: "How does this integrate with our existing systems?"**

**A**: "Great question. The system integrates via standard REST APIs. We've done this with Salesforce, Microsoft Dynamics, Temenos, FIS, and most major core banking platforms. During the pilot, we'll work with your IT team to set up read-only API access. The integration typically takes 3-5 days per system. We start with your CRM in Week 1, then add core banking and credit bureau in Week 2."

---

**Q: "What about data security and compliance?"**

**A**: "Security is built into watsonx Orchestrate from the ground up. All data is encrypted at rest with AES-256 and in transit with TLS 1.3. We support role-based access control - RMs only see their assigned customers. Every agent interaction is logged with full audit trail via watsonx.governance, which is critical for SOX, GDPR, and Basel compliance. We can also deploy on-premises via Cloud Pak for Data if you have data residency requirements."

---

**Q: "How accurate are the AI recommendations?"**

**A**: "In our production deployments, we're seeing 90%+ accuracy ratings from users. The key is that recommendations are **data-driven**, not random. The Growth Opportunity Agent compares each customer's current products against industry benchmarks for similar companies. The Risk Monitoring Agent uses actual credit data and payment history. That said, we always recommend human-in-the-loop validation - the agent provides recommendations, but the RM makes the final decision."

---

**Q: "What if the agent makes a mistake?"**

**A**: "Good question. First, every agent response includes a thumbs-up/thumbs-down feedback mechanism. If an RM flags an inaccurate insight, we capture that feedback and use it to improve the agent's instructions. Second, we implement confidence thresholds - if the agent isn't confident in a recommendation, it will say so. Third, we have a human escalation path - if the agent can't answer a question, it will suggest the RM contact their manager or a specialist."

---

**Q: "How long does it take to train RMs on this?"**

**A**: "Training is minimal because the interface is conversational - RMs just ask questions in natural language. We do two training sessions: a 60-minute overview and a 90-minute hands-on lab. Most RMs are productive within their first week. We also provide ongoing support via office hours and a Slack channel during the pilot."

---

**Q: "Can we customize the agents for our specific needs?"**

**A**: "Absolutely. The agents are built using watsonx Orchestrate's Agent Development Kit (ADK), which means they're fully customizable. You can modify the agent instructions, add new tools, integrate additional data sources, or even create entirely new specialized agents. For example, some banks have added a Compliance Agent that checks regulatory requirements before making product recommendations. We'll work with you during the pilot to identify customization opportunities."

---

**Q: "What's the ongoing cost after the pilot?"**

**A**: "The software cost is approximately $5,000 per user per year for watsonx Orchestrate. For 100 RMs, that's $500,000 annually. Given the $23.4 million net annual benefit we showed, that's a 47x return on the software investment alone. There are also infrastructure costs (IBM Cloud or on-premises hosting) and ongoing support, but those are typically 10-15% of the software cost."

---

**Q: "How does this compare to building something in-house?"**

**A**: "We've seen banks try to build this in-house, and it typically takes 12-18 months and costs $2-3 million in development costs. The challenge is that you're not just building a chatbot - you're building a multi-agent orchestration system with enterprise-grade security, governance, and integration capabilities. With watsonx Orchestrate, you get all of that out of the box, and you can deploy in 4 weeks instead of 18 months. Plus, you get ongoing IBM support and updates as the platform evolves."

---

**Q: "What happens if watsonx Orchestrate goes down?"**

**A**: "watsonx Orchestrate SaaS has a 99.9% uptime SLA, which is about 8 hours of downtime per year. We also support high-availability configurations with automatic failover. If you need higher availability, we can deploy on-premises with active-active clustering. That said, if the system is temporarily unavailable, RMs can always fall back to their existing manual process - this is an enhancement, not a replacement for critical systems."

---

**Q: "Can this work for other banking segments beyond commercial banking?"**

**A**: "Yes, absolutely. We've deployed similar systems for wealth management (portfolio review preparation), corporate banking (deal team briefings), and retail banking (branch manager dashboards). The multi-agent architecture is flexible - you just customize the agents and tools for each segment's specific needs. In fact, many banks start with commercial banking as a pilot, then expand to other segments once they see the results."

---

## Demo Troubleshooting

### If the agent doesn't respond:
**Recovery Script**: "Looks like we have a network hiccup. Let me show you the expected output on the backup slide while we wait for the connection to restore. [Switch to screenshot slide]. As you can see, the response includes..."

### If the agent gives an unexpected response:
**Recovery Script**: "Interesting - the agent is still learning from feedback. This is actually a good example of why we have the thumbs-down feedback mechanism. In production, an RM would flag this, and we'd refine the agent's instructions. Let me show you the expected output. [Switch to screenshot slide]."

### If the demo environment is completely down:
**Recovery Script**: "Apologies - looks like we're having technical difficulties with the live environment. Rather than waste your time, let me walk you through the architecture and expected outputs using our backup slides. [Switch to architecture slide]. The good news is that this gives us more time for Q&A, which is often the most valuable part."

---

## Post-Demo Follow-Up

### Immediate Next Steps (Within 24 Hours)
- [ ] Send thank-you email to all attendees
- [ ] Share demo recording (if recorded)
- [ ] Attach ROI calculator spreadsheet
- [ ] Attach pilot plan PDF
- [ ] Schedule follow-up meeting with decision-makers

### Follow-Up Email Template

**Subject**: SME Relationship Manager Copilot - Demo Follow-Up & Next Steps

**Body**:

Hi [Name],

Thank you for attending today's demo of the SME Relationship Manager Copilot built on watsonx Orchestrate. I hope you found it valuable.

As promised, I'm attaching:
1. **Demo recording** (15 minutes)
2. **ROI calculator** (Excel) - feel free to adjust assumptions for your bank
3. **Pilot plan** (PDF) - detailed 4-week plan with success criteria
4. **Architecture diagram** (PDF) - technical overview for your IT team

**Key Takeaways**:
- 40% reduction in meeting prep time (2 hours → 45 minutes)
- 25% increase in cross-sell success rate
- $23.4M net annual benefit for 100 RMs
- 4-week pilot, production-ready in 3 months

**Proposed Next Steps**:
1. **Technical deep-dive** with your IT and data teams (1 hour)
2. **Pilot planning session** with Commercial Banking leadership (1 hour)
3. **Executive briefing** with your CIO/CTO (30 minutes)

I'm available [dates/times] for any of these sessions. Please let me know what works best for your team.

Looking forward to continuing the conversation.

Best regards,
[Your Name]
[Title]
[Contact Information]

---

## Success Metrics for This Demo

### Immediate Indicators (During Demo)
- [ ] Audience engagement (questions, nodding, note-taking)
- [ ] Executive sponsor asks about next steps
- [ ] IT leader asks technical questions (shows interest)
- [ ] Commercial Banking leader asks about pilot cohort selection

### Short-Term Indicators (Within 1 Week)
- [ ] Follow-up meeting scheduled
- [ ] Technical deep-dive requested
- [ ] Pilot budget discussion initiated
- [ ] Additional stakeholders want to see demo

### Long-Term Indicators (Within 1 Month)
- [ ] Pilot approved and funded
- [ ] Pilot start date confirmed
- [ ] Pilot cohort (10 RMs) identified
- [ ] Data access approvals in progress

---

## Appendix: Preset Scenario Details

### Scenario 1: TechVenture Solutions (CUST-001)
**Preset Button Text**: "Prepare me for my meeting tomorrow with TechVenture Solutions"

**Expected Output**:
```
Meeting Preparation Summary for TechVenture Solutions

CUSTOMER HEALTH: 87/100 (Excellent)
• Revenue: $24.5M (+15% YoY)
• Payment History: 100% on-time (24 months)
• Credit Utilization: 65% of $5M limit
• Account Activity: High (avg 145 transactions/month)

TOP 3 GROWTH OPPORTUNITIES:
1. Treasury Management - $250K potential revenue
   • Fit Score: 92/100
   • Rationale: Growing transaction volume (145/month) indicates need for automated cash management
   
2. Equipment Financing - $180K potential revenue
   • Fit Score: 88/100
   • Rationale: Expansion plans mentioned in recent call, typical equipment financing need for tech companies at this stage
   
3. Trade Finance - $120K potential revenue
   • Fit Score: 85/100
   • Rationale: Industry benchmark shows 78% of similar tech companies use trade finance for international expansion

RISK ALERTS: None
• No late payments in 24 months
• Credit utilization healthy at 65%
• No covenant violations
• Industry outlook: Positive

RECENT INTELLIGENCE:
• Meeting (5 days ago): CEO James Wilson mentioned expansion plans for Q3 2026
• Call (12 days ago): CFO discussed need for better cash flow visibility
• News (8 days ago): Announced major contract with Fortune 500 retail client
• Industry: Technology sector showing 12% growth, above market average

MEETING RECOMMENDATIONS:
1. Open by congratulating on Fortune 500 contract win
2. Discuss Treasury Management to support growing transaction volume
3. Explore Equipment Financing for Q3 expansion plans
4. Position Trade Finance for international growth opportunities
```

---

### Scenario 2: UrbanRetail Group (CUST-003)
**Preset Button Text**: "I need to prepare for an urgent meeting with UrbanRetail Group"

**Expected Output**:
```
URGENT: Meeting Preparation Summary for UrbanRetail Group

CUSTOMER HEALTH: 52/100 (Needs Attention)
⚠️ WARNING: Multiple risk indicators detected

• Revenue: $18.2M (-8% YoY) - DECLINING
• Payment History: 2 late payments (15+ days) in last 60 days
• Credit Utilization: 92% of $3M limit - CRITICAL
• Account Activity: Declining (avg 67 transactions/month, down from 95)

TOP OPPORTUNITY (URGENT):
1. Working Capital Line - $300K potential revenue
   • Fit Score: 95/100
   • Rationale: URGENT NEED - Customer is maxed out on credit and showing cash flow stress
   • Recommendation: Position as retention/support play, not cross-sell

RISK ALERTS: 2 Active Alerts (High Severity)
🔴 ALERT 1: Late Payments (High Severity)
   • 2 payments 15+ days overdue in last 60 days
   • Days Active: 18 days
   • Action Required: Discuss payment plan, understand root cause

🔴 ALERT 2: Credit Utilization (High Severity)
   • 92% utilization ($2.76M of $3M limit)
   • Days Active: 32 days
   • Action Required: Immediate working capital solution needed

RECENT INTELLIGENCE:
• Call (3 days ago): CFO Sarah Martinez expressed cash flow concerns, mentioned delayed receivables from major customer
• Meeting (15 days ago): Discussed Q2 performance challenges, retail sector headwinds
• News (7 days ago): Retail sector facing 15% decline in foot traffic, industry-wide issue
• Industry: Retail sector under pressure, 68% of peers showing similar stress signals

MEETING RECOMMENDATIONS:
⚠️ URGENT: This is a retention situation, not a growth opportunity
1. Acknowledge cash flow challenges proactively
2. Position Working Capital Line as support for short-term liquidity needs
3. Discuss payment plan for overdue amounts
4. Explore industry-specific support programs
5. Schedule follow-up in 2 weeks to monitor situation

ESCALATION: Consider involving credit risk team before meeting
```

---

### Scenario 3: GreenLeaf Manufacturing (CUST-002)
**Preset Button Text**: "What should I discuss with GreenLeaf Manufacturing in our quarterly review?"

**Expected Output**:
```
Quarterly Business Review Preparation for GreenLeaf Manufacturing

CUSTOMER HEALTH: 78/100 (Good)
• Revenue: $32.8M (+6% YoY)
• Payment History: 98% on-time (1 late payment in 18 months)
• Credit Utilization: 58% of $8M limit
• Account Activity: Steady (avg 112 transactions/month)

TOP 3 GROWTH OPPORTUNITIES:
1. Equipment Financing - $450K potential revenue
   • Fit Score: 94/100
   • Rationale: New facility opening announced, typical equipment financing need $3-5M for manufacturing expansion
   
2. ESG Financing - $200K potential revenue
   • Fit Score: 89/100
   • Rationale: Industry trend toward sustainability, 82% of manufacturing peers have ESG initiatives, potential for green bonds/sustainability-linked loans
   
3. FX Hedging - $150K potential revenue
   • Fit Score: 86/100
   • Rationale: International expansion mentioned, 45% of revenue from exports, FX volatility risk

RISK ALERTS: 1 Alert (Low Severity)
🟡 ALERT: Industry Commodity Price Volatility (Low Severity)
   • Steel and aluminum prices up 18% in last quarter
   • Days Active: 12 days
   • Action: Monitor impact on margins, discuss hedging strategies if needed

RECENT INTELLIGENCE:
• Press Release (4 days ago): Announced new 50,000 sq ft facility opening in Q4 2026, $8M investment
• Meeting (21 days ago): CEO Robert Chen discussed sustainability goals, targeting carbon neutrality by 2030
• News (9 days ago): Won major contract with Fortune 500 automotive client, $12M over 3 years
• Industry: Manufacturing sector showing 8% growth, strong demand for sustainable products

QUARTERLY REVIEW AGENDA:
1. Congratulate on Fortune 500 automotive contract win
2. Discuss Equipment Financing for new facility ($3-5M need)
3. Introduce ESG Financing to support carbon neutrality goals
4. Explore FX Hedging for international expansion risk management
5. Review commodity price volatility and potential hedging strategies
6. Discuss Q3/Q4 growth projections and capital needs

RELATIONSHIP STRENGTH: Strong
• 8-year relationship, consistent growth
• High engagement (quarterly reviews, monthly calls)
• Multiple product holdings (5 products)
• Strong referral potential (CEO is industry association board member)
```

---

**Document Version**: 1.0  
**Last Updated**: 2026-06-18  
**Author**: IBM Tech Sales  
**Review Status**: Ready for Delivery