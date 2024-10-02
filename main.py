from Client.ReservationManager import ReservationManager
from Client.ClientHandler import ClientHandler
import json

def run_client() -> None:
    """
    Executa o cliente para gerenciar reservas, permitindo que o usuário faça reservas, veja todas as reservas e saia.
    """
    reservation_manager = ReservationManager()
    client_handler = ClientHandler('127.0.0.1', 65432)

    client_handler.connect()

    while True:
        print("\nMenu de Reservas")        
        print("1. Fazer reserva")        
        print("2. Ver todas as reservas")
        print("3. Sair")
        
        option = input("Escolha uma opção: ")
        
        if option == '1':
            room_number = input("Digite o número da sala que deseja reservar: ")
            reservation_time = input("Digite o horário da reserva: ")

            reservation_response = reservation_manager.add_reservation(room_number, reservation_time)

            if "já está reservada" in reservation_response:
                print(reservation_response)
            else:
                print(reservation_response)

                reservation_data = {"id": room_number, "horario": reservation_time}
                command = f"RESERVE {json.dumps(reservation_data)}"
                server_response = client_handler.send_command(command)
                print(f"Resposta do servidor: {server_response}")

        elif option == '2':
            all_reservations = reservation_manager.view_all_reservations()
            print("\nReservas atuais:")
            if not all_reservations:
                print("Não há reservas.")
            else:
                for reservation in all_reservations:
                    print(f"Sala: {reservation['id']}, Horário: {reservation['horario']}")

            command = "VIEW_RESERVATIONS"
            response = client_handler.send_command(command)

        elif option == '3':
            client_handler.send_command("SHUTDOWN")
            break

    client_handler.close_connection()

if __name__ == "__main__":
    run_client()

