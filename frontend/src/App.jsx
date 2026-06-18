import React from 'react';
import { Routes, Route } from 'react-router-dom';
import {
  Header,
  HeaderContainer,
  HeaderName,
  HeaderNavigation,
  HeaderMenuItem,
  HeaderGlobalBar,
  HeaderGlobalAction,
  SkipToContent
} from '@carbon/react';
import { UserAvatar, Notification } from '@carbon/icons-react';
import DemoBanner from './components/DemoBanner';
import DashboardPage from './pages/DashboardPage';
import CustomersPage from './pages/CustomersPage';
import AIChatPage from './pages/AIChatPage';
import './App.scss';

function App() {
  return (
    <div className="app-container">
      <HeaderContainer
        render={() => (
          <>
            <Header aria-label="SME Meeting Prep">
              <SkipToContent />
              <HeaderName prefix="IBM">
                SME Meeting Prep
              </HeaderName>
              <HeaderNavigation aria-label="Main Navigation">
                <HeaderMenuItem href="/">Dashboard</HeaderMenuItem>
                <HeaderMenuItem href="/customers">Customers</HeaderMenuItem>
                <HeaderMenuItem href="/ai-chat">AI Assistant</HeaderMenuItem>
              </HeaderNavigation>
              <HeaderGlobalBar>
                <HeaderGlobalAction aria-label="Notifications">
                  <Notification size={20} />
                </HeaderGlobalAction>
                <HeaderGlobalAction aria-label="User Profile">
                  <UserAvatar size={20} />
                </HeaderGlobalAction>
              </HeaderGlobalBar>
            </Header>
          </>
        )}
      />
      
      <div className="demo-banner">
        <DemoBanner />
      </div>

      <div className="content-wrapper">
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/customers" element={<CustomersPage />} />
          <Route path="/ai-chat" element={<AIChatPage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;

// Made with Bob
