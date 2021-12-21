import logging
from server.server_runner import run_server

# Service port
SERVER_PORT = 8001

# Set logger
root = logging.getLogger()
root.setLevel(logging.INFO)


def run_service():
    # Forward call to the server runner
    run_server(SERVER_PORT)


if __name__ == '__main__':
    run_service()
