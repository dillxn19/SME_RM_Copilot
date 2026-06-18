import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Theme } from '@carbon/react';
import App from './App';
import './index.scss';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Theme theme="g90">
        <App />
      </Theme>
    </BrowserRouter>
  </React.StrictMode>
);

// Made with Bob
