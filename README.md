# Chatterbox – Real-Time WebSocket Chat Application

Chatterbox is a real-time chat application built using **FastAPI**, **WebSockets**, and a modern **HTML + CSS frontend**.  
The project is implemented milestone-wise, gradually adding features such as rooms, typing indicators, timestamps, and enhanced UI/UX.

---

## Features Implemented

### Milestone 1 – Basic WebSocket Chat
- Real-time messaging using WebSockets
- Client–server communication with FastAPI
- Simple echo and broadcast functionality

### Milestone 2 – Multi-User Support
- Multiple users can join the chat simultaneously
- System messages for user join/leave events

### Milestone 3 – Rooms & Typing Indicator
- Room-based chats: **General**, **Tech**, **Fun**
- Users only receive messages from their selected room
- Live typing indicator
- Online users list per room

### Milestone 4 – UI/UX Enhancements & State Management
- Modern UI built with **Tailwind CSS**
- Login page for username & room selection
- Persistent username and room using `sessionStorage.`
- Message timestamps
- Messages are preserved per room on switching
- Smooth auto-scrolling on new messages
- Animated typing dots for better UX
- Improved visual hierarchy and readability

---

## Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- FastAPI
- WebSockets
- Uvicorn (ASGI server)

---

## 📂 Project Structure

```
chatterbox/
├── main.py          # FastAPI backend with WebSocket logic
├── login.html       # Login page (username + room selection)
├── chat.html        # Chat UI (rooms, messages, typing indicator)
├── README.md        # Project documentation
└── .venv/           # Virtual environment (not pushed to GitHub)
```



---

## How to Run the Project

### 1. Backend Setup
```bash
pip install fastapi uvicorn
```
Run the Server
```bash
python main.py
```
### 2. Frontend
- Open login.html in your browser
- Enter your username and select a room
- You will be redirected to the chat interface





