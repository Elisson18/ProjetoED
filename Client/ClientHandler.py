import socket

class ClientHandler:
    def __init__(self, host: str, port: int) -> None:
        """
        Inicializa o manipulador de cliente com o endereço do servidor e a porta.

        :param host: O endereço IP do servidor.
        :param port: A porta do servidor.
        """
        self.host = host
        self.port = port
        self.socket: socket.socket | None = None  # Type hint para o socket, inicializado como None

    def connect(self) -> None:
        """Estabelece uma conexão com o servidor."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        
    def send_command(self, command: str) -> str:
        """
        Envia um comando para o servidor e recebe a resposta.

        :param command: O comando a ser enviado para o servidor.
        :return: A resposta do servidor.
        """
        self.socket.sendall(command.encode('utf-8'))
        response = self.socket.recv(1024)
        return response.decode('utf-8')

    def close_connection(self) -> None:
        """Fecha a conexão com o servidor."""
        if self.socket:
            self.socket.close()

