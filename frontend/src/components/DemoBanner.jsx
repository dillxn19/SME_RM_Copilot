import React from 'react';
import { InlineNotification } from '@carbon/react';

function DemoBanner() {
  return (
    <InlineNotification
      kind="info"
      title="Demonstration Environment"
      subtitle="All data is synthetic. No real client data or PII is used."
      hideCloseButton
      lowContrast
    />
  );
}

export default DemoBanner;

// Made with Bob
