# proxy_client_gui.py
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QTextEdit, QFileDialog, QMessageBox, QProgressBar
)
# optional web preview
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    WEB_AVAILABLE = True
except Exception:
    WEB_AVAILABLE = False

from proxy_client_backend import request_url_and_save

# Worker thread to run network call so UI doesn't block
class FetchWorker(QThread):
    finished_sig = pyqtSignal(dict)  # will emit the result dict

    def __init__(self, url, server_host, server_port, out_dir):
        super().__init__()
        self.url = url
        self.server_host = server_host
        self.server_port = server_port
        self.out_dir = out_dir

    def run(self):
        result = request_url_and_save(self.url, server_host=self.server_host,
                                      server_port=self.server_port, out_dir=self.out_dir)
        self.finished_sig.emit(result)

class ProxyClientUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-threaded Proxy Client — Premium UI")
        self.setMinimumSize(1000, 650)
        self.server_host = '127.0.0.1'
        self.server_port = 8888
        self.out_dir = 'downloads'
        os.makedirs(self.out_dir, exist_ok=True)

        self._build_ui()
        self._apply_styles()

    def _build_ui(self):
        main = QHBoxLayout(self)
        left = QVBoxLayout()
        right = QVBoxLayout()
        main.addLayout(left, 3)
        main.addLayout(right, 2)

        # Header
        header = QLabel("🚀 Multi-threaded Proxy Client")
        header.setObjectName("header")
        left.addWidget(header)

        # URL input row
        row = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL (e.g. https://example.com)")
        self.fetch_btn = QPushButton("Fetch Page")
        self.fetch_btn.clicked.connect(self.on_fetch_clicked)
        row.addWidget(self.url_input)
        row.addWidget(self.fetch_btn)
        left.addLayout(row)

        # Status and progress
        self.status_label = QLabel("Ready")
        self.status_label.setObjectName("status")
        left.addWidget(self.status_label)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        left.addWidget(self.progress)

        # Saved file and open button
        save_row = QHBoxLayout()
        self.saved_label = QLabel("No file saved yet")
        self.open_file_btn = QPushButton("Open Saved File")
        self.open_file_btn.clicked.connect(self.open_saved_file)
        self.open_file_btn.setEnabled(False)
        save_row.addWidget(self.saved_label)
        save_row.addWidget(self.open_file_btn)
        left.addLayout(save_row)

        # Preview area (either web view or raw html)
        if WEB_AVAILABLE:
            self.preview = QWebEngineView()
            self.preview.setHtml("<html><body><i>Preview will appear here</i></body></html>")
        else:
            self.preview = QTextEdit()
            self.preview.setReadOnly(True)
            self.preview.setPlainText("Preview unavailable (PyQtWebEngine not installed). Raw HTML will be shown here.")
        left.addWidget(self.preview, 1)

        # Right panel: history and controls
        history_label = QLabel("History")
        right.addWidget(history_label)
        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.on_history_click)
        right.addWidget(self.history_list, 1)

        controls = QHBoxLayout()
        self.clear_history_btn = QPushButton("Clear History")
        self.clear_history_btn.clicked.connect(self.on_clear_history)
        self.browse_save_btn = QPushButton("Change Save Location")
        self.browse_save_btn.clicked.connect(self.on_browse_save)
        controls.addWidget(self.clear_history_btn)
        controls.addWidget(self.browse_save_btn)
        right.addLayout(controls)

        # row: server settings
        srv_row = QHBoxLayout()
        self.server_edit = QLineEdit(f"{self.server_host}:{self.server_port}")
        self.server_edit.setToolTip("Server host:port (e.g. 127.0.0.1:8888)")
        self.server_apply_btn = QPushButton("Apply")
        self.server_apply_btn.clicked.connect(self.on_apply_server)
        srv_row.addWidget(QLabel("Proxy Server:"))
        srv_row.addWidget(self.server_edit)
        srv_row.addWidget(self.server_apply_btn)
        right.addLayout(srv_row)

        # finalize
        self.setLayout(main)

    def _apply_styles(self):
        qss = """
        QWidget { background: qlineargradient(x1:0 y1:0, x2:1 y2:1,
                   stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364);
                 color: #e6f3f3; font-family: "Segoe UI", Roboto, Arial; }
        #header { font-size: 22px; font-weight: 700; padding: 12px; }
        QLineEdit { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.08);
                    padding: 8px; border-radius: 8px; color: #fff; }
        QPushButton { background: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 #56ab2f, stop:1 #a8e063);
                      border: none; padding: 8px 12px; border-radius: 8px; color: #04271b;
                      font-weight: 600; }
        QPushButton:hover { transform: scale(1.01); }
        #status { color: #cfeee3; font-style: italic; padding: 6px 0; }
        QListWidget { background: rgba(0,0,0,0.12); border-radius: 6px; padding: 6px; }
        QTextEdit { background: rgba(255,255,255,0.04); border-radius: 6px; }
        QProgressBar { border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; text-align: center; }
        """
        self.setStyleSheet(qss)

    def on_apply_server(self):
        text = self.server_edit.text().strip()
        if ':' in text:
            host, sep, port = text.partition(':')
            try:
                portnum = int(port)
                self.server_host = host
                self.server_port = portnum
                self.status_label.setText(f"Server set to {host}:{portnum}")
            except:
                QMessageBox.warning(self, "Invalid port", "Port must be an integer")
        else:
            QMessageBox.warning(self, "Invalid server", "Use format host:port")

    def on_browse_save(self):
        d = QFileDialog.getExistingDirectory(self, "Select Save Directory", os.getcwd())
        if d:
            self.out_dir = d
            self.status_label.setText(f"Save dir: {d}")

    def on_clear_history(self):
        self.history_list.clear()
        self.status_label.setText("History cleared")

    def on_fetch_clicked(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.information(self, "Enter URL", "Please enter a URL to fetch.")
            return
        # Add to history immediately
        self.history_list.addItem(url)
        # Disable UI actions while fetching
        self._set_fetching_state(True)
        self.status_label.setText("Connecting to proxy server...")
        # Start worker thread
        self.worker = FetchWorker(url, self.server_host, self.server_port, self.out_dir)
        self.worker.finished_sig.connect(self.on_fetch_finished)
        self.worker.start()

    def _set_fetching_state(self, fetching: bool):
        self.fetch_btn.setEnabled(not fetching)
        self.progress.setValue(0 if not fetching else 0)
        if fetching:
            # Indeterminate mode
            self.progress.setRange(0, 0)
            self.open_file_btn.setEnabled(False)
        else:
            self.progress.setRange(0, 100)
            self.progress.setValue(100)

    def on_fetch_finished(self, result: dict):
        # result: {'ok', 'path', 'msg', 'cached'}
        self._set_fetching_state(False)
        if result.get('ok'):
            path = result.get('path')
            self.saved_label.setText(path)
            self.open_file_btn.setEnabled(True)
            self.status_label.setText("Success: " + result.get('msg', 'Saved'))
            # Load preview (web engine if available)
            try:
                if WEB_AVAILABLE:
                    # load local file into QWebEngineView
                    self.preview.load(QtCore.QUrl.fromLocalFile(os.path.abspath(path)))
                else:
                    with open(path, 'r', encoding='utf-8', errors='replace') as f:
                        txt = f.read()
                    self.preview.setPlainText(txt[:200000])  # limit to avoid slow UI
            except Exception as e:
                self.status_label.setText(f"Saved but preview failed: {e}")
        else:
            self.status_label.setText("Failed: " + result.get('msg', 'Error'))
            QMessageBox.warning(self, "Fetch Failed", result.get('msg', 'Unknown error'))

    def open_saved_file(self):
        path = self.saved_label.text()
        if not path or path == "No file saved yet":
            return
        # open with default OS application
        try:
            if sys.platform.startswith('darwin'):
                os.system(f'open "{path}"')
            elif os.name == 'nt':
                os.startfile(path)
            else:
                os.system(f'xdg-open "{path}"')
        except Exception as e:
            QMessageBox.warning(self, "Open failed", f"Could not open file: {e}")

    def on_history_click(self, item):
        # set as URL input and optionally fetch again
        self.url_input.setText(item.text())

def main():
    app = QApplication(sys.argv)
    w = ProxyClientUI()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
