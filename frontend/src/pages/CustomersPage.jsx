import React from 'react';
import { Tile, Tag } from '@carbon/react';
import { mockCustomers } from '../data/mockResponses/customerData';

function CustomersPage() {
  const getRiskColor = (risk) => {
    switch (risk) {
      case 'Low': return 'green';
      case 'Medium': return 'yellow';
      case 'High': return 'red';
      default: return 'gray';
    }
  };

  const getHealthColor = (score) => {
    if (score >= 80) return 'green';
    if (score >= 60) return 'yellow';
    return 'red';
  };

  return (
    <div>
      <div className="page-header">
        <h1>SME Customer Portfolio</h1>
        <p>View and analyze your SME customer relationships</p>
      </div>

      <div className="customer-grid">
        {mockCustomers.map((customer) => (
          <Tile key={customer.id} style={{ padding: '1.5rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '1rem' }}>
              <div>
                <h4 style={{ margin: 0, marginBottom: '0.25rem' }}>{customer.name}</h4>
                <p style={{ margin: 0, fontSize: '0.875rem', color: 'var(--cds-text-secondary)' }}>
                  {customer.id} • {customer.industry}
                </p>
              </div>
              <Tag type={getRiskColor(customer.riskLevel)} size="sm">
                {customer.riskLevel} Risk
              </Tag>
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                <span style={{ fontSize: '0.875rem' }}>Health Score</span>
                <Tag type={getHealthColor(customer.healthScore)} size="sm">
                  {customer.healthScore}/100
                </Tag>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                <span style={{ fontSize: '0.875rem' }}>Annual Revenue</span>
                <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>
                  ${(customer.revenue / 1000000).toFixed(1)}M
                </span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                <span style={{ fontSize: '0.875rem' }}>Credit Rating</span>
                <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>{customer.creditRating}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span style={{ fontSize: '0.875rem' }}>Last Contact</span>
                <span style={{ fontSize: '0.875rem' }}>{customer.lastContact}</span>
              </div>
            </div>

            <div>
              <p style={{ fontSize: '0.75rem', fontWeight: 600, marginBottom: '0.5rem', textTransform: 'uppercase' }}>
                Growth Opportunities
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
                {customer.opportunities.map((opp, idx) => (
                  <Tag key={idx} type="blue" size="sm">{opp}</Tag>
                ))}
              </div>
            </div>
          </Tile>
        ))}
      </div>
    </div>
  );
}

export default CustomersPage;

// Made with Bob
