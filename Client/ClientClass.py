import socket
import json
from Data_Structures.FilaSequencialList import Fila

HOST = '127.0.0.1'
PORT = 65432

def send_command(client_socket: socket.socket, command: str) -> str:
    """
    Envia um comando para o servidor e recebe a resposta.

    :param client_socket: O socket do cliente conectado ao servidor.
    :param command: O comando a ser enviado.
    :return: A resposta do servidor.
    """
    client_socket.sendall(command.encode('utf-8'))
    response = client_socket.recv(1024)
    return response.decode('utf-8')

def main() -> None:
    """
    Função principal do cliente que gerencia reservas e interage com o servidor.
    Permite ao usuário fazer reservas, processar reservas e sair do programa.
    """
    reservation_queue = Fila()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        while True:
            room_number = input("Digite o número da sala que deseja reservar: ")
            reservation_time = input("Digite o horário da reserva: ")

            reservation_queue.enfileirar({"id": room_number, "horario": reservation_time})

            if not reservation_queue.estaVazia():
                reservation_data = reservation_queue.desenfileirar()
                command = f"RESERVE {json.dumps(reservation_data)}"
                response = send_command(client_socket, command)
                print(f"Resposta do servidor: {response}")

            process_next = input("Deseja processar a próxima reserva na fila? (s/n): ")
            if process_next.lower() == 's':
                if not reservation_queue.estaVazia():
                    command = "PROCESS"
                    response = send_command(client_socket, command)
                    print(f"Resposta do servidor: {response}")
                else:
                    print("Não há reservas na fila para processar.")
            else:
                break 

if __name__ == "__main__":
    main()

