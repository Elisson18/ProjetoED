from Data_Structures.FilaSequencialList import Fila

class ReservationManager:
    def __init__(self) -> None:
        """
        Inicializa o gerenciador de reservas com uma fila de reservas vazia.
        """
        self.reservation_queue: Fila = Fila()  # Type hint para a fila de reservas

    def add_reservation(self, room_number: str, reservation_time: str) -> str:
        """
        Adiciona uma nova reserva à fila, se a sala não estiver reservada para o horário especificado.

        :param room_number: O número da sala a ser reservada.
        :param reservation_time: O horário da reserva.
        :return: Mensagem de confirmação ou erro.
        """
        if self.is_reserved(room_number, reservation_time):
            return f"A sala {room_number} já está reservada para o horário {reservation_time}."

        self.reservation_queue.enfileirar({"id": room_number, "horario": reservation_time})
        print(f"Reservas na fila após adição: {self.reservation_queue.get_all_reservations()}")
        return f"Reserva adicionada: Sala: {room_number}, Horário: {reservation_time}"

    def get_next_reservation(self) -> dict | None:
        """
        Retorna a próxima reserva da fila.

        :return: O próximo item da fila de reservas ou None se a fila estiver vazia.
        """
        return self.reservation_queue.desenfileirar()

    def is_reserved(self, room_number: str, reservation_time: str) -> bool:
        """
        Verifica se a sala está reservada para o horário especificado.

        :param room_number: O número da sala a ser verificado.
        :param reservation_time: O horário a ser verificado.
        :return: True se a sala estiver reservada, False caso contrário.
        """
        all_reservations = self.reservation_queue.get_all_reservations()
        for reservation in all_reservations:
            if reservation['id'] == room_number and reservation['horario'] == reservation_time:
                return True
        return False

    def view_all_reservations(self) -> list[dict]:
        """
        Retorna todas as reservas na fila.

        :return: Lista de dicionários representando todas as reservas.
        """
        return self.reservation_queue.get_all_reservations()

