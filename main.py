from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        # websocket -> room
        self.active_connections: dict[WebSocket, str] = {}
        # websocket -> username
        self.usernames: dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str, room: str):
        self.active_connections[websocket] = room
        self.usernames[websocket] = username
        await self.broadcast_system(room, f"{username} joined {room} 👋")

    def disconnect(self, websocket: WebSocket):
        room = self.active_connections.get(websocket)
        username = self.usernames.get(websocket, "Someone")
        self.active_connections.pop(websocket, None)
        self.usernames.pop(websocket, None)
        return username, room

    async def broadcast_room(self, room: str, data: dict):
        for ws, user_room in self.active_connections.items():
            if user_room == room:
                await ws.send_json(data)

    async def broadcast_system(self, room: str, message: str):
        await self.broadcast_room(room, {
            "type": "system",
            "message": message
        })

manager = ConnectionManager()

@app.get("/")
async def root():
    return {"message": "Chatterbox Unified WebSocket Server Running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    username = "Anonymous"
    room = "general"

    try:
        # First message must be join info
        join_data = await websocket.receive_json()

        username = join_data.get("username", "Anonymous")
        room = join_data.get("room", "general")

        await manager.connect(websocket, username, room)

        while True:
            data = await websocket.receive_json()
            event_type = data.get("type")

            if event_type == "chat":
                message = data.get("message", "").strip()
                if not message:
                    continue

                print(f"[{room}] {username}: {message}")

                # Echo (Milestone 1 compatibility)
                await websocket.send_json({
                    "type": "echo",
                    "message": f"You said -> {message}"
                })

                # Broadcast to room
                await manager.broadcast_room(room, {
                    "type": "chat",
                    "username": username,
                    "message": message
                })

            elif event_type == "typing":
                await manager.broadcast_room(room, {
                    "type": "typing",
                    "username": username
                })

            elif event_type == "stop_typing":
                await manager.broadcast_room(room, {
                    "type": "stop_typing",
                    "username": username
                })

    except WebSocketDisconnect:
        username, room = manager.disconnect(websocket)
        if room:
            await manager.broadcast_system(room, f"{username} left {room} ❌")
        print(f"{username} disconnected")

    except Exception as e:
        username, room = manager.disconnect(websocket)
        if room:
            await manager.broadcast_system(room, f"{username} left due to error ❌")
        print("Error:", e)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
