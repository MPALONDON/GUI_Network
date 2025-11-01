# Python GUI Chat Application

A simple client-server chat application built with Python using **Tkinter** for the GUI and **sockets** for network communication. This application allows multiple clients to connect to a server, exchange messages, and provides administrative controls for managing connected clients.

---

## Features

### Server
- Start and stop the server on a specified port.
- Broadcast messages to all connected clients.
- Send private messages to individual clients.
- Kick or ban clients based on IP address.
- Displays connection history and active client list.
- Friendly GUI interface using Tkinter.

### Client
- Connect to a server using host IP and port.
- Choose a display name and message color.
- Send messages to all clients or disconnect gracefully.
- Receive messages with timestamps and color-coded usernames.
- Simple and intuitive GUI for easy interaction.

---

## Technologies Used
- **Python 3.x**
- **Tkinter** – GUI development.
- **Socket** – TCP/IP networking.
- **Threading** – Handle multiple clients simultaneously.
- **JSON** – Message serialization and communication.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/MPALONDON/GUI_Network.git
cd GUI_Network
```

2. Ensure Python 3.x is installed.
3. Install any required packages (all are part of Python standard library, no extra packages required).

---

## Usage

### Server
1. Run `server.py`.
2. Enter a port number and click **Start Server**.
3. Use **Broadcast**, **PM**, **Kick**, and **Ban** buttons to manage messages and clients.
4. Click **End Server** to shut down.

### Client
1. Run `client.py`.
2. Enter your **Name**, **Host IP**, and **Port Number**.
3. Choose a message color and click **Connect**.
4. Type messages in the input box and click **Send**.
5. Click **Disconnect** to leave the server.

---

## File Structure
```
GUI_Network/
├── server.py
├── client.py
├── README.md
├── favicon/
│   └── Web_.ico
└── screenshots/
    ├── Chat Server.png
    └── chat client.png
```

---

## How it Works
- **Server:** Listens for client connections and manages all connected clients. It handles broadcasting, private messaging, and client management using threading for concurrency.
- **Client:** Connects to the server and communicates by sending and receiving JSON-encoded messages. Each message includes flags, sender info, timestamp, and color.

---

## Screenshots

### Server GUI
![Server GUI](https://github.com/MPALONDON/GUI_Network/raw/main/screenshots/Chat%20Server.png)

### Client GUI
![Client GUI](https://github.com/MPALONDON/GUI_Network/raw/main/screenshots/chat%20client.png)

---

## Notes
- Only one server can run per port.
- Banned clients are blocked by IP.
- Messages are color-coded for better readability.
- The app currently runs on local networks or within the same subnet.
- The application icon is located at `favicon/Web_.ico`.

---

## License
MIT License – free to use and modify.

