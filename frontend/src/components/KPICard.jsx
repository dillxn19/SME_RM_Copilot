import React from 'react';
import { Tile } from '@carbon/react';
import { ArrowUp, ArrowDown } from '@carbon/icons-react';

function KPICard({ title, value, unit, trend, trendLabel, icon: Icon, color = 'blue' }) {
  const borderColors = {
    blue: '#0f62fe',
    green: '#198038',
    red: '#fa4d56',
    purple: '#6929c4'
  };

  return (
    <Tile style={{ borderLeft: `4px solid ${borderColors[color]}`, padding: '1rem' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
        <h4 style={{ fontSize: '0.875rem', fontWeight: 400, margin: 0 }}>{title}</h4>
        {Icon && <Icon size={20} />}
      </div>
      <div style={{ fontSize: '2rem', fontWeight: 300, marginBottom: '0.5rem' }}>
        {value}{unit && <span style={{ fontSize: '1rem', marginLeft: '0.25rem' }}>{unit}</span>}
      </div>
      {trend && (
        <div style={{ display: 'flex', alignItems: 'center', fontSize: '0.875rem', color: trend > 0 ? '#198038' : '#fa4d56' }}>
          {trend > 0 ? <ArrowUp size={16} /> : <ArrowDown size={16} />}
          <span style={{ marginLeft: '0.25rem' }}>{trendLabel}</span>
        </div>
      )}
    </Tile>
  );
}

export default KPICard;

// Made with Bob
