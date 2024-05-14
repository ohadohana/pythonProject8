import socket
import os
from urllib.parse import urlparse, parse_qs

# Constants
IP = '127.0.0.1' # local host
PORT = 80
WEBROOT = 'C:\\Users\\User\\Downloads\\webroot\\webroot' # path of the webroot directory
SOCKET_TIMEOUT = 30
CONTENT_TYPE_MAPPING = {
    'html': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'ico': 'image/x-icon'
}


def get_content_type(file_path):
    ext = file_path.split('.')[-1]
    return CONTENT_TYPE_MAPPING.get(ext, 'application/octet-stream')


def get_file_data(filename):
    try:
        with open(filename, 'rb') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None


def send_response(client_socket, status_code, content_type, content):
    """Send HTTP response"""
    reason = {
        200: "OK",
        404: "Not Found"
    }.get(status_code, "OK")

    header = f"HTTP/1.1 {status_code} {reason}\r\n"
    if content_type:
        header += f"Content-Type: {content_type}\r\n"
    if content:
        header += f"Content-Length: {len(content)}\r\n"
    header += "Connection: close\r\n\r\n"

    client_socket.send(header.encode())
    if content:
        client_socket.send(content)


def handle_client_request(resource, client_socket):
    # print(f"Requested resource: {resource}")  # Debug

    parsed_url = urlparse(resource)
    query_components = parse_qs(parsed_url.query)

    if resource == '':
        resource = 'index.html'

    # 4.5/6
    if resource.startswith('calculate-next'):
        num = query_components.get('num', [None])[0]

        if num is not None:
            try:
                num_value = int(num)
                num_value += 1
                send_response(client_socket, 200, "text/plain", str(num_value).encode())
            except ValueError:
                send_response(client_socket, 400, "text/plain", b"Invalid number format")
            else:
                send_response(client_socket, 400, "text/plain", b"Number parameter missing")
        return

    # 4.9
    if resource.startswith('calculate-area'):
        height = query_components.get('height', [None])[0]
        width = query_components.get('width', [None])[0]

        # print(f"Width: {width}") #Debug
        # print(f"Height: {height}") #Debug

        if resource.startswith('calculate-area'):
            height = query_components.get('height', [None])[0]
            width = query_components.get('width', [None])[0]
            if height is not None and width is not None:
                try:
                    height_value = int(height)
                    width_value = int(width)
                    area = (height_value * width_value) / 2
                    if area.is_integer():
                        area = int(area)
                    send_response(client_socket, 200, "text/plain", str(area).encode())
                except ValueError:
                    send_response(client_socket, 400, "text/plain", b"Invalid number format for height or width")
            else:
                send_response(client_socket, 400, "text/plain", b"Height or width parameter missing")
            return

    file_path = os.path.join(WEBROOT, resource)
    if not os.path.exists(file_path):
        send_response(client_socket, 404, "text/html", b"<h1>404 Not Found</h1>")
    else:
        content_type = get_content_type(file_path)
        content = get_file_data(file_path)
        send_response(client_socket, 200, content_type, content)


def validate_http_request(request):
    try:
        lines = request.split('\r\n')
        method, resource, _ = lines[0].split()
        if method == 'GET':
            return True, resource.strip('/')
    except Exception as e:
        print(f"Error validating request: {e}")
    return False, ""


def handle_client(client_socket):
    print('Client connected')
    try:
        client_request = client_socket.recv(1024).decode()
        if not client_request:
            return  # Prevents hanging if client closes connection
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            handle_client_request(resource, client_socket)
        else:
            send_response(client_socket, 400, "text/html", b"<h1>400 Bad Request</h1>")
    finally:
        print('Closing connection')
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)
    print(f"Listening for connections on port {PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    main()