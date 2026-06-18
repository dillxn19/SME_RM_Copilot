# 🎨 SME Meeting Prep - Carbon UI Frontend

A professional Carbon Design System UI for the SME Relationship Manager AI Copilot demo.

## 🏗️ Architecture

This is a **Hybrid Demo** combining:
- **Backend**: watsonx Orchestrate multi-agent system (5 agents + 6 tools)
- **Frontend**: Carbon React UI with embedded Orchestrate web-chat

## ✨ Features

- 📊 **Dashboard**: Portfolio KPIs and health metrics
- 👥 **Customers**: SME customer cards with risk indicators
- 🤖 **AI Assistant**: Embedded watsonx Orchestrate chat interface
- 🎨 **Carbon Design**: IBM's design system with g90 dark theme
- 📱 **Responsive**: Works on desktop and tablet

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- watsonx Orchestrate environment (from TechZone)
- Deployed agents (see parent directory)

### Installation

```bash
# Install dependencies
npm install

# Copy environment template
cp .env.example .env

# Edit .env with your watsonx Orchestrate credentials
# Get these from your TechZone environment
```

### Configuration

Edit `.env` with your watsonx Orchestrate credentials:

```env
VITE_WXO_HOST_URL=https://us-south.watson-orchestrate.cloud.ibm.com
VITE_WXO_ORCHESTRATION_ID=your-orchestration-id
VITE_WXO_CRN=your-crn
VITE_WXO_AGENT_ID=your-deployed-agent-id
```

### Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
npm run preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/       # Reusable UI components
│   │   ├── DemoBanner.jsx
│   │   └── KPICard.jsx
│   ├── pages/           # Page components
│   │   ├── DashboardPage.jsx
│   │   ├── CustomersPage.jsx
│   │   └── AIChatPage.jsx
│   ├── data/            # Mock data
│   │   └── mockResponses/
│   │       └── customerData.js
│   ├── App.jsx          # Main app with routing
│   ├── App.scss         # App styles
│   ├── main.jsx         # Entry point
│   └── index.scss       # Global styles
├── index.html
├── vite.config.js
└── package.json
```

## 🎯 Pages

### 1. Dashboard (`/`)
- Portfolio KPIs (Total Customers, Avg Health Score, At-Risk, Revenue)
- Overview of AI capabilities

### 2. Customers (`/customers`)
- Customer cards with health scores
- Risk indicators and credit ratings
- Growth opportunities

### 3. AI Assistant (`/ai-chat`)
- Embedded watsonx Orchestrate chat
- Multi-agent system interaction
- Example queries provided

## 🔧 Technology Stack

- **React 18** - UI framework
- **Vite** - Build tool
- **Carbon Design System v11** - IBM's design system
- **React Router v6** - Client-side routing
- **Sass** - CSS preprocessing

## 🎨 Carbon Components Used

- Header & Navigation
- Tiles & Cards
- Tags (status indicators)
- Grid & Layout
- Inline Notifications
- Icons (@carbon/icons-react)

## 🔗 Integration with watsonx Orchestrate

The AI Assistant page embeds the watsonx Orchestrate web-chat using the official loader script:

```javascript
window.wxOConfiguration = {
  orchestrationID: "...",
  hostURL: "...",
  crn: "...",
  chatOptions: { agentId: "..." }
};
```

No backend API is needed to connect to Orchestrate - it's a pure frontend embed.

## 📝 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_WXO_HOST_URL` | Orchestrate host URL | `https://us-south.watson-orchestrate.cloud.ibm.com` |
| `VITE_WXO_ORCHESTRATION_ID` | Your orchestration ID | From TechZone |
| `VITE_WXO_CRN` | Cloud Resource Name | From TechZone |
| `VITE_WXO_AGENT_ID` | Deployed agent ID | From `orchestrate agents list` |

## 🐛 Troubleshooting

### Chat not loading?
- Check `.env` has all required variables
- Verify agent is deployed: `orchestrate agents list`
- Check browser console for errors

### Styles not working?
- Ensure `npm install` completed successfully
- Check `@carbon/react` and `sass` are installed

### Build errors?
- Clear cache: `rm -rf node_modules dist && npm install`
- Check Node.js version: `node --version` (should be 18+)

## 📚 Resources

- [Carbon Design System](https://carbondesignsystem.com/)
- [watsonx Orchestrate Docs](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

## 📄 License

This is a demonstration project. See parent directory LICENSE file.

---

**Built with IBM watsonx** 🚀