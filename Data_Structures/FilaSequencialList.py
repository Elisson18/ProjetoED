class FilaException(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos da fila é identificada."""
    def __init__(self, msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja embutir na exceção."""
        super().__init__(msg)


class Fila:
    """A classe Fila.py implementa a estrutura de dados "Fila". 
       A classe permite que qualquer tipo de dado seja armazenada na fila.

    Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da fila.
    """
    def __init__(self):
        """ Construtor padrão da classe Fila sem argumentos. Ao instanciar um objeto do tipo Fila, esta iniciará vazia."""
        self.__dado = []

    def estaVazia(self):
        """ Método que verifica se a fila está vazia ou não.
        
        Returns:
            boolean: True se a fila estiver vazia, False caso contrário.
        """
        return len(self.__dado) == 0

    def tamanho(self):
        """ Método que consulta a quantidade de elementos existentes na fila.
        
        Returns:
            int: um número inteiro que determina o número de elementos existentes na fila.
        """
        return len(self.__dado)

    def elemento(self, posicao):
        """ Método que recupera o valor armazenado em um determinado elemento da fila.
        
        Args:
            posicao (int): um número correspondente à ordem do elemento existente, na direção da base até o topo.
        
        Returns:
            int: o valor armazenado na ordem indicada por posição.

        Raises:
            FilaException: Exceção lançada quando uma posição inválida é fornecida pelo usuário.
        """
        try:
            assert posicao > 0
            return self.__dado[posicao - 1]
        except IndexError:
            raise FilaException(f'Posicao {posicao} invalida para a Fila')
        except TypeError:
            raise FilaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise FilaException(f'A posicao deve ser um número maior que zero')

    def busca(self, valor):
        """ Método que recupera a posicao ordenada, dentro da fila, em que se encontra um valor passado como argumento.
        
        Args:
            valor: um item de dado que deseja procurar na fila.
        
        Returns:
            int: um número inteiro representando a posição, na fila, em que foi encontrado "valor".

        Raises:
            FilaException: Exceção lançada quando o argumento "valor" não está presente na fila.
        """
        try:
            return self.__dado.index(valor) + 1
        except ValueError:
            raise FilaException(f'O valor {valor} não está armazenado na fila')

    def enfileirar(self, valor):
        """ Método que adiciona um novo elemento na frente da fila.
        
        Args:
            valor(qualquer tipo de dado): o conteúdo que deseja armazenar na fila.
        """
        self.__dado.append(valor)

    def desenfileirar(self):
        """ Método que remove um elemento do final da fila e devolve o conteudo existente removido.
        
        Returns:
            qualquer tipo de dado: o conteúdo referente ao elemento removido.

        Raises:
            FilaException: Exceção lançada quando se tenta remover algo de uma fila vazia.
        """
        try:
            return self.__dado.pop(0)
        except IndexError:
            raise FilaException(f'Fila Vazia. Não é possível efetuar a remoção')

    def get_all_reservations(self):
        """ Método que retorna todas as reservas presentes na fila.
        
        Returns:
            list: uma lista com todos os elementos da fila.
        """
        return self.__dado.copy()

    def imprimir(self):
        """ Método que exibe a sequência ordenada dos elementos da fila."""
        print('Frente-> ' + self.__dado.__str__())

    def __str__(self):
        """ Método que retorna a representação da fila como string."""
        return self.__dado.__str__()