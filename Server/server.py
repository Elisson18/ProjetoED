import socket
import json
from .reservation_handler import ReservationHandler
from Client.ReservationManager import ReservationManager

HOST = '127.0.0.1'
PORT = 65432

def start_server() -> None:
    """
    Inicia o servidor de reservas, escutando conexões e processando comandos de clientes.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor iniciado e escutando em {HOST}:{PORT}")

        handler = ReservationHandler()

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Conectado por {addr}")

                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    command = data.decode('utf-8')
                    print(f"Comando recebido: {command}")

                    if command.startswith("RESERVE"):
                        try:
                            reservation_data = json.loads(command.split(" ", 1)[1])
                            room_number = reservation_data['id']
                            reservation_time = reservation_data['horario']
                            print(f"Adicionando reserva: Quarto: {room_number}, Horário: {reservation_time}")
                            result = handler.add_reservation_request(room_number, reservation_time) 
                        except (ValueError, KeyError) as e:
                            result = f"Erro ao processar a reserva: {str(e)}"
                        conn.sendall(result.encode('utf-8'))

                    elif command == "VIEW_RESERVATIONS":
                        try:
                            reservations = handler.list_reservations()
                            if reservations:
                                response_data = json.dumps(reservations).encode('utf-8')
                                conn.sendall(response_data)
                            else:
                                conn.sendall(b"[]")

                        except Exception as e:
                            result = f"Erro ao listar reservas: {str(e)}"
                            conn.sendall(result.encode('utf-8'))

                    elif command.startswith("PROCESS"):
                        result = handler.process_next_request()
                        conn.sendall(result.encode('utf-8'))

                    elif command.startswith("CHECK"):
                        _, room_number = command.split()
                        result = handler.search_reservation(room_number)
                        conn.sendall(result.encode('utf-8'))

                    elif command == "SHUTDOWN":
                        print("Servidor encerrando...")
                        conn.sendall(b"Servidor encerrado.")
                        return

                    else:
                        conn.sendall(b"Comando desconhecido.")

if __name__ == "__main__":
    start_server()