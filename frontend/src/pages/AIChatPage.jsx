import React, { useEffect } from 'react';
import { Grid, Column, InlineNotification } from '@carbon/react';

function AIChatPage() {
  useEffect(() => {
    // Load watsonx Orchestrate web-chat embed script
    const hostURL = import.meta.env.VITE_WXO_HOST_URL || 'https://us-south.watson-orchestrate.cloud.ibm.com';
    const orchestrationID = import.meta.env.VITE_WXO_ORCHESTRATION_ID;
    const crn = import.meta.env.VITE_WXO_CRN;
    const agentId = import.meta.env.VITE_WXO_AGENT_ID;

    if (!orchestrationID || !crn || !agentId) {
      console.warn('watsonx Orchestrate credentials not configured. Please set environment variables.');
      return;
    }

    // Configure watsonx Orchestrate
    window.wxOConfiguration = {
      orchestrationID: orchestrationID,
      hostURL: hostURL,
      rootElementID: 'orchestrate-chat-root',
      deploymentPlatform: 'ibmcloud',
      crn: crn,
      chatOptions: { 
        agentId: agentId,
        hideHeader: false,
        hideInput: false
      }
    };

    // Load the Orchestrate loader script
    const script = document.createElement('script');
    script.src = `${hostURL}/wxochat/wxoLoader.js?embed=true`;
    script.addEventListener('load', () => {
      if (window.wxoLoader) {
        window.wxoLoader.init();
      }
    });
    document.head.appendChild(script);

    return () => {
      // Cleanup
      if (script.parentNode) {
        script.parentNode.removeChild(script);
      }
    };
  }, []);

  const isConfigured = import.meta.env.VITE_WXO_ORCHESTRATION_ID && 
                       import.meta.env.VITE_WXO_CRN && 
                       import.meta.env.VITE_WXO_AGENT_ID;

  return (
    <div>
      <div className="page-header">
        <h1>AI Meeting Preparation Assistant</h1>
        <p>Interact with the watsonx Orchestrate multi-agent system</p>
      </div>

      {!isConfigured && (
        <InlineNotification
          kind="warning"
          title="Configuration Required"
          subtitle="Please configure watsonx Orchestrate credentials in .env file to enable the AI assistant."
          style={{ marginBottom: '1rem' }}
        />
      )}

      <Grid>
        <Column lg={16}>
          <div className="chat-container">
            <div 
              id="orchestrate-chat-root" 
              className="orchestrate-embed"
              style={{
                minHeight: '600px',
                background: 'var(--cds-layer-01)',
                borderRadius: '4px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}
            >
              {!isConfigured && (
                <div style={{ textAlign: 'center', padding: '2rem' }}>
                  <h3>🤖 watsonx Orchestrate Integration</h3>
                  <p style={{ marginTop: '1rem', color: 'var(--cds-text-secondary)' }}>
                    Configure your watsonx Orchestrate credentials to enable the AI assistant.
                  </p>
                  <p style={{ marginTop: '0.5rem', fontSize: '0.875rem' }}>
                    Required environment variables:
                  </p>
                  <ul style={{ 
                    listStyle: 'none', 
                    padding: 0, 
                    marginTop: '1rem',
                    fontSize: '0.875rem',
                    fontFamily: 'IBM Plex Mono'
                  }}>
                    <li>VITE_WXO_HOST_URL</li>
                    <li>VITE_WXO_ORCHESTRATION_ID</li>
                    <li>VITE_WXO_CRN</li>
                    <li>VITE_WXO_AGENT_ID</li>
                  </ul>
                </div>
              )}
            </div>
          </div>
        </Column>
      </Grid>

      <Grid style={{ marginTop: '2rem' }}>
        <Column lg={16}>
          <InlineNotification
            kind="info"
            title="Try These Queries"
            subtitle="Example questions to ask the AI assistant:"
            hideCloseButton
            lowContrast
          />
          <ul style={{ marginTop: '1rem', paddingLeft: '2rem' }}>
            <li>"Prepare me for a meeting with TechVenture Solutions"</li>
            <li>"What are the top risks in my SME portfolio?"</li>
            <li>"Show me growth opportunities for GreenLeaf Manufacturing"</li>
            <li>"Analyze the financial health of Urban Retail Group"</li>
          </ul>
        </Column>
      </Grid>
    </div>
  );
}

export default AIChatPage;

// Made with Bob
