#!/usr/bin/env python3
"""
Proxy Client (Python)
- Connects to local proxy server, sends URL, receives length-prefixed content, saves to sanitized HTML file.
"""

import socket
import struct
import os
import time
from urllib import parse
import re

# CONFIG
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8888
SOCKET_TIMEOUT = 30

def sanitize_filename(s):
    # Keep only safe chars
    s = re.sub(r'[^A-Za-z0-9._-]', '_', s)
    return s

def make_filename_from_url(url):
    parsed = parse.urlparse(url)
    host = parsed.netloc or 'site'
    path = parsed.path or ''
    if path.endswith('/'):
        path = path[:-1]
    base = host + path
    if not base:
        base = 'page'
    base = sanitize_filename(base)
    ts = time.strftime("%Y%m%d_%H%M%S")
    return f"{base}_{ts}.html"

def recv_all(sock, n):
    data = bytearray()
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Socket closed while reading")
        data.extend(chunk)
    return bytes(data)

def request_url_and_save(url, out_dir='.'):
    # Prepare URL bytes and length (4 bytes unsigned int)
    url_bytes = url.encode('utf-8')
    if len(url_bytes) > 16_384:
        raise ValueError("URL too long")
    payload = struct.pack('!I', len(url_bytes)) + url_bytes

    with socket.create_connection((SERVER_HOST, SERVER_PORT), timeout=SOCKET_TIMEOUT) as s:
        s.sendall(payload)
        # Now read 8-byte length prefix (unsigned long long)
        raw = recv_all(s, 8)
        (content_len,) = struct.unpack('!Q', raw)
        if content_len == 0:
            print("Empty response")
            return None
        content = recv_all(s, content_len)

    filename = make_filename_from_url(url)
    path = os.path.join(out_dir, filename)
    with open(path, 'wb') as f:
        f.write(content)
    return path

def main():
    print("Simple Proxy Client")
    while True:
        url = input("Enter URL (or 'q' to quit): ").strip()
        if not url:
            continue
        if url.lower() == 'q':
            break
        # If no scheme provided, add http
        if '://' not in url:
            url = 'http://' + url
        try:
            saved = request_url_and_save(url)
            if saved:
                print(f"Saved to: {saved}")
        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == '__main__':
    main()
