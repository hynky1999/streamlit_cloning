import os
import socket
import subprocess
import logging
import uuid


sessions = {}

def port_to_streamlit_url(port):
    nginx_url = os.environ.get("NGINX_URL")
    server_path = f"/streamlit_apps/{port}"
    return f"{nginx_url}{server_path}"

def start_streamlit_process(filepath):
    port = find_available_port()
    # This is the front-facing URL that user will see
    server_path = f"/streamlit_apps/{port}"

    process = subprocess.Popen([
        "streamlit",
        "run",
        filepath,
        "--server.headless", "true",
        "--browser.serverAddress", "0.0.0.0",
        "--server.port", str(port),
        "--server.runOnSave", "false",
        "--server.enableCORS", "false",
        f"--server.baseUrlPath", f"{server_path}"
    ])

    sessions[port] = {
        'process': process,
        'port': port,
        'filepath': filepath,
    }
    return port_to_streamlit_url(port)

def stop_streamlit_process(session_id):
    print(f"Stopping session {session_id}")
    print(sessions)
    if session_id in sessions:
        print("Found session")
        sessions[session_id]['process'].terminate()
        del sessions[session_id]
        print("Deleted session")
        print(sessions)


def find_available_port():
    for port in range(14000, 14100):  # Define a range of port numbers
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost',port))
        if result != 0:
            return port
    raise Exception("No available ports")
