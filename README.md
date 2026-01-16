# 🎨 Board: Real-Time Collaborative Whiteboard

**A production-grade collaborative workspace built with Django, React, and Generative AI.**

## 📖 Overview
Board is a real-time collaborative whiteboard that allows multiple users to draw, brainstorm, and organize ideas simultaneously. Unlike simple drawing apps, Board utilizes **WebSockets** for millisecond-latency updates and integrates **Generative AI** to enhance productivity—automatically correcting rough hand-drawn shapes and summarizing whiteboard contents into actionable text.

## 🚀 Key Features

### ⚡ Real-Time Collaboration (The Core)
* **Live Multi-User Drawing:** Users see each other's cursors and strokes instantly.
* **Conflict Resolution:** Handles high-concurrency updates using Redis and Django Channels.
* **Vector-Based Storage:** Stores shapes as mathematical coordinates (not just pixels) in PostgreSQL, allowing for infinite resizing and editing.

### 🧠 AI-Powered Tools (The "2026 Standard")
* **✨ Smart Shape Recognition:** Draws a rough square or circle? The system instantly snaps it to a perfect geometric shape using geometric logic algorithms.
* **🤖 Board Summarization:** Users can click "Summarize," and the system uses an LLM (Gemini/OpenAI) to read text nodes on the board and generate a structured summary of the brainstorming session.

### 🛠️ Engineering Highlights
* **Architecture:** Monorepo containing a decoupled Django REST Framework backend and React frontend.
* **DevOps:** Fully containerized with Docker and Docker Compose.
* **Deployment:** Nginx reverse proxy configuration for handling both HTTP (API) and WebSocket (WSS) connections securely.

---

## 🏗️ Technical Architecture

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React + Vite | UI and Canvas manipulation (Konva.js / HTML5 Canvas). |
| **Backend** | Django + DRF | API endpoints and business logic. |
| **Real-Time** | Django Channels | WebSocket consumer handling. |
| **Message Broker** | Redis | Distributing WebSocket messages across workers. |
| **Database** | PostgreSQL | Persistent storage of user data and vector shapes. |
| **AI Integration** | Gemini API | Processing text for board summarization. |

---

## 🗺️ Development Roadmap

### Phase 1: The Foundation
- [ ] Set up Monorepo (Django + React).
- [ ] Configure Docker & PostgreSQL.
- [ ] Implement basic WebSocket connection (Django Channels).

### Phase 2: Collaboration Engine
- [ ] Build the infinite canvas in React.
- [ ] Sync drawing data via WebSockets (Broadcast updates).
- [ ] Implement Redis layer for performance.

### Phase 3: AI & Polish
- [ ] Implement "Smart Shape" logic (Client-side).
- [ ] Integrate "Summarize" feature (Server-side LLM).
- [ ] Deploy to production (Hetzner/AWS).