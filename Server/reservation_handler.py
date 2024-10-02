from Data_Structures.BinarySearchTree import BinarySearchTree
from Data_Structures.FilaSequencialList import Fila  

class ReservationHandler:
    def __init__(self):
        self.bst: BinarySearchTree = BinarySearchTree()
        self.request_queue: Fila = Fila()

    def add_reservation_request(self, room_number: str, reservation_time: str) -> str:
        """
        Adiciona uma nova solicitação de reserva à fila.

        :param room_number: O número da sala sendo reservada.
        :param reservation_time: O horário da reserva.
        :return: Mensagem informando que a solicitação foi adicionada à fila.
        """
        reservation = {'id': room_number, 'horario': reservation_time}
        self.request_queue.enfileirar(reservation)
        return f"Solução de reserva da sala {room_number} para o horário {reservation_time} foi colocada na fila."

    def process_next_request(self) -> str:
        """
        Processa a próxima solicitação de reserva da fila.

        :return: Mensagem de sucesso ou falha ao processar a reserva.
        """
        if not self.request_queue.estaVazia():
            reservation = self.request_queue.desenfileirar()
            room_number = reservation['id']
            reservation_time = reservation['horario']
            return self.add_reservation_request(room_number, reservation_time)

    def add_reservation_request(self, room_number: str, reservation_time: str) -> str:
        """
        Adiciona uma nova reserva à árvore, se a sala não estiver reservada.

        :param room_number: O número da sala a ser reservada.
        :param reservation_time: O horário da reserva.
        :return: Mensagem de sucesso ou falha ao adicionar a reserva.
        """
        if self.bst.search(room_number):
            return f"A sala {room_number} já está reservada."

        self.request_queue.enfileirar({"id": room_number, "horario": reservation_time})
        self.bst.add(room_number, reservation_time)
        return f"Reserva adicionada: Quarto: {room_number}, Horário: {reservation_time}"

    def search_reservation(self, room_number: str) -> str:
        """
        Busca por uma reserva específica na árvore binária.

        :param room_number: O número da sala a ser buscada.
        :return: O horário da reserva, se existir.
        """
        result = self.bst.search(room_number)
        if result:
            return f"Sala {room_number} está reservada para o horário {result}."
        else:
            return f"Não há reserva para a sala {room_number}."

    def list_reservations(self) -> str:
        """
        Retorna uma lista de todas as reservas feitas.

        :return: Uma string com todas as reservas listadas.
        """
        reservations = self.bst.traversal(order=self.bst.inorder)
        if reservations:
            return "Reservas atuais:\n" + "\n".join([f"Sala {room} reservada para {time}" for room, time in reservations])
        else:
            return "Nenhuma reserva feita no momento."


