# 🎓 Learning Path & Core Concepts

To build the **Board** project, the team needs to master the following concepts. Focus on learning them in this order.

## 🟢 1. Backend Concepts (Django & Python)

### REST Architecture
* **What it is:** How the frontend talks to the backend using standard HTTP methods.
* **Key Terms:** `GET` (Fetch), `POST` (Create), `PATCH` (Update), `401 Unauthorized`, `JSON Serialization`.
* **Goal:** Build an API that returns a list of users in JSON format.

### JWT Authentication (JSON Web Tokens)
* **What it is:** A stateless way to log users in.
* **Key Terms:** `Access Token` (short-lived), `Refresh Token` (long-lived), `HTTPOnly Cookies`.
* **Goal:** Understand why we don't use simple Sessions for a separate React frontend.

### Django Channels (Real-Time)
* **What it is:** The library that allows Django to handle WebSockets.
* **Key Terms:** `ASGI` (Asynchronous Server Gateway Interface), `Consumers` (like Views, but for sockets), `Channel Layers`.
* **Goal:** Send a "Hello" message from one browser tab and see it appear in another tab instantly.

### Redis (Message Broker)
* **What it is:** A super-fast memory store used to pass messages between users.
* **Key Terms:** `Pub/Sub` (Publish/Subscribe).
* **Goal:** Understand that Redis is the "post office" sorting messages for Django Channels.

---

## 🔵 2. Frontend Concepts (React & JS)

### React Hooks (Deep Dive)
* **What it is:** The engine of modern React.
* **Key Hooks:**
    * `useState`: Managing simple data (e.g., current tool: "pen" or "eraser").
    * `useEffect`: Running code when the component loads (e.g., connecting to the WebSocket).
    * `useRef`: **Critical for Canvas.** Accessing the actual `<canvas>` HTML element directly.

### HTML5 Canvas API
* **What it is:** The browser technology for drawing graphics.
* **Key Terms:** `Context (ctx)`, `moveTo()`, `lineTo()`, `stroke()`, Coordinate System `(x:0, y:0 is top-left)`.
* **Goal:** Draw a single red line on a blank screen using code.

### WebSockets (Client Side)
* **What it is:** A permanent 2-way phone call between browser and server.
* **Key Events:** `.onopen` (Connected!), `.onmessage` (Data received!), `.onclose` (Disconnected).
* **Goal:** Log incoming messages to the browser console.

### Optimistic UI
* **What it is:** Showing the user's action *instantly* before the server confirms it.
* **Why:** If you wait for the server, drawing will feel laggy.
* **Goal:** Draw the line immediately, then send the data to the server in the background.

---

## 🟣 3. Architecture & DevOps

### Docker & Containerization
* **What it is:** Packaging your app so it runs the same on your laptop and the server.
* **Key Terms:** `Container` vs `Image`, `Volumes` (Saving data), `Networking` (How containers talk).

### Nginx (Reverse Proxy)
* **What it is:** The traffic cop.
* **Role:** It directs `http://` traffic to Django and `ws://` (WebSocket) traffic to the Channels server.
* **Goal:** Configure `nginx.conf` to handle both protocols on one port.

### CORS (Cross-Origin Resource Sharing)
* **The Problem:** Browsers block React (Port 5173) from talking to Django (Port 8000) for security.
* **The Fix:** Configuring `django-cors-headers` to whitelist your frontend.