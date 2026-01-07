# proxy_client_backend.py
import socket
import struct
import os
import time
from urllib import parse
import re

# Defaults (you can override when calling functions)
DEFAULT_SERVER_HOST = '127.0.0.1'
DEFAULT_SERVER_PORT = 8888
DEFAULT_SOCKET_TIMEOUT = 30

# helper: sanitize filename
_filename_safe_re = re.compile(r'[^A-Za-z0-9._-]')

def sanitize_filename(s):
    return _filename_safe_re.sub('_', s)

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

def request_url_and_save(url,
                         server_host=DEFAULT_SERVER_HOST,
                         server_port=DEFAULT_SERVER_PORT,
                         out_dir='downloads',
                         socket_timeout=DEFAULT_SOCKET_TIMEOUT):
    """
    Connects to proxy server, sends URL, receives length-prefixed content,
    saves to an automatically named file inside out_dir.
    Returns a dict: {'ok': True/False, 'path': path_or_None,
                     'msg': status message, 'cached': True/False}
    """
    os.makedirs(out_dir, exist_ok=True)
    # Ensure scheme
    if '://' not in url:
        url = 'http://' + url

    url_bytes = url.encode('utf-8')
    if len(url_bytes) > 16_384:
        return {'ok': False, 'path': None, 'msg': 'URL too long', 'cached': False}

    payload = struct.pack('!I', len(url_bytes)) + url_bytes

    try:
        with socket.create_connection((server_host, server_port), timeout=socket_timeout) as s:
            # send request
            s.sendall(payload)
            # read 8-byte length prefix
            raw = recv_all(s, 8)
            (content_len,) = struct.unpack('!Q', raw)
            if content_len == 0:
                return {'ok': False, 'path': None, 'msg': 'Empty response', 'cached': False}
            content = recv_all(s, content_len)
    except Exception as e:
        return {'ok': False, 'path': None, 'msg': f'Network error: {e}', 'cached': False}

    # The server may return an "ERROR: ..." text as bytes -> detect
    try:
        # decode start to check prefix (not full decode)
        sample = content[:64].decode('utf-8', errors='ignore')
        if sample.startswith("ERROR:"):
            # treat as error
            return {'ok': False, 'path': None, 'msg': f'Server error: {sample}', 'cached': False}
    except Exception:
        pass

    # Save file
    filename = make_filename_from_url(url)
    path = os.path.join(out_dir, filename)
    try:
        with open(path, 'wb') as f:
            f.write(content)
    except Exception as e:
        return {'ok': False, 'path': None, 'msg': f'File write error: {e}', 'cached': False}

    # Heuristic: server prints "[CACHE HIT]" only in console and does NOT mark content; we cannot 100% know
    # from content whether it was cached. For now we return cached=False (server logs show hits).
    # Optionally server could send a header flag; we did not implement that, so leave cached=False.
    return {'ok': True, 'path': path, 'msg': f'Saved ({len(content)} bytes)', 'cached': False}
