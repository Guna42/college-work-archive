# README — Multi-Threaded Proxy Server & Premium GUI Client (Python)

## Project Overview
This project implements a **Multi-Threaded Proxy Server** and a **Premium Desktop Client UI** (PyQt5).  
The proxy server accepts any URL from the client, fetches the webpage, and returns the full HTML back to the client.  
The client then **saves the HTML** into a local file and shows a **beautiful GUI preview**.

The system is built with **Operating System concepts**, **socket programming**, **multithreading**, and **file handling**, along with a modern **PyQt5 GUI**.

## Features

### Proxy Server
- Multi-threaded (Thread Pool Executor)
- Accepts multiple clients simultaneously
- Fetches web pages through HTTP/HTTPS
- LRU Cache (50 entries default)
- Length-prefixed data protocol
- OS-level socket API usage
- Proper error handling & logging
- Normalized URL processing

### Advanced Client UI
- Modern PyQt5 Premium UI design
- HTML preview using QWebEngineView
- Save output files automatically (sanitized filenames)
- History panel for previously fetched URLs
- Progress loading indicator
- Beautiful gradient theme
- Fully asynchronous (no UI blocking)

## System Architecture
Client UI → Sends URL → Proxy Server → Fetches from Internet  
Then returns HTML back to client, which saves & previews it.

## OS Concepts Used

### 1. Multithreading
Proxy Server uses ThreadPoolExecutor to handle each incoming client connection in a separate worker thread.

### 2. Sockets & System Calls
Uses socket(), bind(), listen(), accept(), connect(), send(), recv(), close().

### 3. Thread Synchronization
LRU cache on server protected using threading.Lock().

### 4. File Handling
Client saves webpage HTML; server logs events.

### 5. URL Normalization & Caching
Implemented using OrderedDict and memory optimization.

### 6. Blocking & Non-Blocking I/O
Timeouts prevent the server threads from hanging.

## Project Directory Structure
project/
│
├── server.py                 
├── proxy_client_backend.py   
├── proxy_client_gui.py       
├── downloads/                
└── README.md                 

## File-by-file Explanation

### server.py
Multi-threaded proxy server. Handles URL requests, caching, and response.

### proxy_client_backend.py
Networking logic: connects to server, sends URL, receives HTML, saves file.

### proxy_client_gui.py
Advanced PyQt5 UI: URL input, history panel, HTML preview, progress bar.

## Execution Flow

1. Start server.py  
2. Start proxy_client_gui.py  
3. Enter URL  
4. Client sends URL to server  
5. Server fetches/caches page  
6. Client saves and previews it  

## Communication Protocol

Client → server:
- 4 bytes: URL length
- N bytes: URL

Server → client:
- 8 bytes: content length
- M bytes: HTML content

## Installation

pip install pyqt5 pyqtwebengine requests

## Run

python server.py  
python proxy_client_gui.py  

## Why This Project Scores High
- Demonstrates OS concepts clearly
- Real socket programming
- Multi-threaded server
- Caching (LRU)
- Custom binary protocol
- Full PyQt5 UI
- Clean architecture
