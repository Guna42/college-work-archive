#!/usr/bin/env python3
"""
Multi-threaded Proxy Server (Python)
- Accepts URL from client (length-prefixed), fetches the page (HTTP/HTTPS),
  caches results (LRU), and returns raw bytes to client with length prefix.
- Uses ThreadPoolExecutor for concurrency.
"""

import socket
import struct
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib import request, error, parse
from collections import OrderedDict
import time

# CONFIG
HOST = '127.0.0.1'
PORT = 8888
MAX_WORKERS = 12
SOCKET_TIMEOUT = 20            # seconds for client socket operations
REMOTE_FETCH_TIMEOUT = 10      # seconds for fetching remote pages
MAX_CONTENT_SIZE = 10 * 1024 * 1024  # 10 MB max response size accepted
CACHE_MAX_ENTRIES = 50

# Simple LRU cache for responses
class LRUCache:
    def __init__(self, max_entries=100):
        self.max_entries = max_entries
        self.lock = threading.Lock()
        self.data = OrderedDict()  # key -> bytes

    def get(self, key):
        with self.lock:
            if key in self.data:
                self.data.move_to_end(key, last=True)
                return self.data[key]
            return None

    def put(self, key, value):
        with self.lock:
            if key in self.data:
                self.data.move_to_end(key, last=True)
            self.data[key] = value
            if len(self.data) > self.max_entries:
                self.data.popitem(last=False)

# Normalize URL (basic)
def normalize_url(url):
    parsed = parse.urlparse(url)
    scheme = parsed.scheme if parsed.scheme else 'http'
    netloc = parsed.netloc
    path = parsed.path or '/'
    query = parsed.query
    # Sort query parameters for stable key (optional)
    return parse.urlunparse((scheme, netloc, path, '', query, ''))

cache = LRUCache(max_entries=CACHE_MAX_ENTRIES)

def fetch_remote(url):
    """Fetch remote URL bytes. Returns bytes on success, raises on failure."""
    normalized = normalize_url(url)
    req = request.Request(normalized, headers={'User-Agent': 'SimpleProxy/1.0'})
    with request.urlopen(req, timeout=REMOTE_FETCH_TIMEOUT) as resp:
        content = resp.read(MAX_CONTENT_SIZE + 1)  # read up to limit + 1
        if len(content) > MAX_CONTENT_SIZE:
            raise ValueError("Content too large")
        return content

def recv_all(sock, n):
    """Receive exactly n bytes or raise."""
    data = bytearray()
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Socket closed while reading")
        data.extend(chunk)
    return bytes(data)

def handle_client_connection(conn, addr):
    try:
        conn.settimeout(SOCKET_TIMEOUT)
        # Read 4 bytes for URL length (we'll use 4 bytes unsigned int)
        raw = recv_all(conn, 4)
        (url_len,) = struct.unpack('!I', raw)
        if url_len <= 0 or url_len > 16_384:  # cap URL length
            raise ValueError("Invalid URL length")
        url_bytes = recv_all(conn, url_len)
        url = url_bytes.decode('utf-8', errors='replace').strip()
        print(f"[{time.strftime('%H:%M:%S')}] Request from {addr}: {url}")

        key = normalize_url(url)
        cached = cache.get(key)
        if cached is not None:
            response_bytes = cached
            print(f"[CACHE HIT] {key}")
        else:
            try:
                response_bytes = fetch_remote(url)
                cache.put(key, response_bytes)
                print(f"[FETCHED] {key} ({len(response_bytes)} bytes)")
            except Exception as e:
                err_msg = f"ERROR: failed to fetch URL: {e}".encode('utf-8')
                # Send error back with special zero-length? We'll just send error bytes
                response_bytes = err_msg
                print(f"[ERROR] fetching {key}: {e}")

        # Send 8-byte length prefix (unsigned long long network order)
        conn.sendall(struct.pack('!Q', len(response_bytes)))
        # Then send the content
        conn.sendall(response_bytes)
    except Exception as e:
        print(f"[ERR] Connection handler error from {addr}: {e}")
    finally:
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Proxy server listening on {HOST}:{PORT} ...")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            try:
                while True:
                    conn, addr = s.accept()
                    # Hand off to thread pool
                    pool.submit(handle_client_connection, conn, addr)
            except KeyboardInterrupt:
                print("Shutting down server...")

if __name__ == '__main__':
    start_server()
