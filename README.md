# 🎨 Board: Next-Gen Collaborative Whiteboard

**A production-grade, real-time workspace built with Django, React, and Generative AI.**

## 📖 Overview
**Board** is a SaaS-ready collaborative platform that allows teams to brainstorm, draw, and organize ideas simultaneously. It goes beyond simple drawing apps by integrating **Enterprise-Grade Security** (Waiting Rooms, RBAC) and **Generative AI** tools that enhance productivity.

Built as a modern Monorepo, it utilizes **WebSockets** for millisecond-latency updates and **Docker** for scalable deployment.

---

## 🚀 Key Features

### 🔐 Security & Room Management (SaaS Layer)
* **Granular Room Privacy:**
  * **Public Rooms:** Open to anyone with the link.
  * **Private Rooms:** Restricted to specific registered users (Invite-Only).
  * **Protected Rooms:** Accessible via a shared password.
* **The "Waiting Room":** A moderation queue where the Host must explicitly **Accept** or **Deny** join requests before a user can see the canvas.
* **Role-Based Access Control (RBAC):**
  * **Host:** Full control (manage waiting room, ban users, delete board, change settings).
  * **Editor:** Can draw, add notes, and upload images.
  * **Viewer:** Read-only access (perfect for presentations or classes).

### ⚡ Real-Time Collaboration
* **Live Multi-User Sync:** Users see each other's cursors and drawing strokes instantly via **Django Channels**.
* **Vector-Based Infinite Canvas:** Drawings are stored as mathematical vector coordinates (not pixels), allowing for infinite zooming and re-editing.
* **Integrated Chat:** Real-time text messaging sidebar for team communication alongside the whiteboard.
* **Conflict Resolution:** Handles high-concurrency updates using Redis to prevent data overwrites.

### 🧠 AI-Powered Tools (The "2026 Standard")
* **✨ Smart Shape Recognition:** Draws a messy circle or square? The system utilizes geometric algorithms to instantly "snap" it into a perfect shape.
* **🤖 Intelligent Summarization:** Users can click "Summarize Board," and the system uses an LLM (Gemini API) to read all text notes on the canvas and generate a structured meeting summary.

---

## 🏗️ Technical Architecture

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React + Vite | Interactive UI and Canvas manipulation (Konva.js). |
| **Backend** | Django + DRF | REST API for Auth, Rooms, and AI endpoints. |
| **Real-Time** | Django Channels | WebSocket consumer handling for live drawing. |
| **Message Broker** | Redis | Distributing WebSocket messages across workers. |
| **Database** | PostgreSQL | Persistent storage of Users, Rooms, and Vector Data. |
| **AI Integration** | Gemini API | Processing text for automated board summarization. |
| **Infrastructure** | Docker | Containerization for Nginx, Backend, and Database. |

---

## 📂 Project Structure

```text
board/
├── backend/            # Django Project (DRF + Channels)
│   ├── board_project/  # Core settings
│   ├── api/            # REST API endpoints
│   └── chat/           # WebSocket logic
├── frontend/           # React Project (Vite)
│   ├── src/
│   └── package.json
├── docker-compose.yml  # Container orchestration
└── README.md           # Project documentation
```
## 🗺️ Development Roadmap

### Phase 1: Foundation & Authentication

* [x] Initialize Monorepo structure.
* [ ] Configure Docker, PostgreSQL, and Redis.
* [ ] **User System:** Implement JWT Authentication (Login/Register).
* [ ] **Profile Management:** Allow users to manage their identity.

### Phase 2: The Real-Time Engine (MVP)

* [ ] Build the interactive canvas in React.
* [ ] **WebSocket Setup:** Configure Django Channels for live data transmission.
* [ ] **Broadcasting:** Ensure User A sees User B's strokes instantly.
* [ ] **Persistence:** Save drawing data to PostgreSQL.

### Phase 3: Advanced Room Logic

* [ ] **Room Types:** Implement Public vs. Private vs. Protected logic.
* [ ] **Waiting Room:** Build the "Knock" and "Accept/Deny" backend logic.
* [ ] **Permissions:** Create Middleware to enforce Host/Editor/Viewer rules.
* [ ] **Invitations:** Ability to invite specific users by email/username.

### Phase 4: AI & Polish

* [ ] **Smart Shapes:** Implement client-side geometric correction.
* [ ] **AI Summarization:** Connect Backend to Gemini API for text processing.
* [ ] **Deployment:** Final production build with Nginx reverse proxy.

---

## 🛠️ Getting Started

### Prerequisites

* Docker & Docker Compose
* Node.js (v18+)
* Python (v3.10+)

### Quick Start

1. **Clone the repo:**
```bash
git clone [https://github.com/yourusername/Collaborative-Board.git](https://github.com/yourusername/Collaborative-Board.git)
cd board

```


2. **Run with Docker:**
```bash
docker-compose up --build

```


3. **Access the app:**
* Frontend: `http://localhost:5173`
* Backend API: `http://localhost:8000`




