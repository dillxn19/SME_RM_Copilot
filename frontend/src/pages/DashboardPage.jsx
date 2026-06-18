import React from 'react';
import { Grid, Column } from '@carbon/react';
import { UserMultiple, ChartLine, WarningAlt, Currency } from '@carbon/icons-react';
import KPICard from '../components/KPICard';
import { mockKPIs } from '../data/mockResponses/customerData';

function DashboardPage() {
  return (
    <div>
      <div className="page-header">
        <h1>SME Portfolio Dashboard</h1>
        <p>Real-time insights powered by watsonx Orchestrate AI agents</p>
      </div>

      <div className="kpi-grid">
        <KPICard
          title="Total SME Customers"
          value={mockKPIs.totalCustomers}
          icon={UserMultiple}
          color="blue"
          trend={5}
          trendLabel="+5 this quarter"
        />
        <KPICard
          title="Average Health Score"
          value={mockKPIs.avgHealthScore}
          unit="/100"
          icon={ChartLine}
          color="green"
          trend={3}
          trendLabel="+3 points"
        />
        <KPICard
          title="At-Risk Customers"
          value={mockKPIs.atRiskCustomers}
          icon={WarningAlt}
          color="red"
          trend={-2}
          trendLabel="-2 from last month"
        />
        <KPICard
          title="Total Portfolio Value"
          value="$125M"
          icon={Currency}
          color="purple"
          trend={8}
          trendLabel="+8% YoY"
        />
      </div>

      <Grid>
        <Column lg={16}>
          <div style={{ 
            padding: '2rem', 
            background: 'var(--cds-layer-01)', 
            borderRadius: '4px',
            textAlign: 'center'
          }}>
            <h3>🤖 AI-Powered Meeting Preparation</h3>
            <p style={{ marginTop: '1rem', color: 'var(--cds-text-secondary)' }}>
              Navigate to the <strong>AI Assistant</strong> tab to interact with the watsonx Orchestrate agents.
              <br />
              The multi-agent system analyzes customer health, identifies risks, and suggests growth opportunities.
            </p>
          </div>
        </Column>
      </Grid>
    </div>
  );
}

export default DashboardPage;

// Made with Bob
