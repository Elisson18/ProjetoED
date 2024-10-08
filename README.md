# ProjetoED

### Classes Principais

#### Node
Representa um nó da árvore binária, contendo dados e referências para filhos à esquerda e à direita.

#### BinarySearchTree
Gerencia a estrutura da árvore binária e fornece métodos para adicionar e buscar nós.

#### ReservationHandler
Gerencia os pedidos de reserva, utilizando a árvore binária para armazenar e organizar as reservas.

#### Fila
Uma estrutura de dados que é utilizada para gerenciar os pedidos de reserva, garantindo que sejam processados na ordem em que foram recebidos. A fila é particularmente útil para manter um fluxo organizado de solicitações, permitindo que os usuários consultem a disponibilidade de salas e realizem reservas de forma eficiente.

### Métodos

#### Node
- `__init__(data: object, key: any)`: Construtor que inicializa um nó com os dados e a chave.

#### BinarySearchTree
- `__init__()`: Inicializa a árvore vazia.
- `add(data: any)`: Adiciona um novo nó à árvore.
- `__add(data: any, node: 'Node')`: Método auxiliar para inserir nós de forma recursiva.
- `search(key: any)`: Busca um nó na árvore pelo seu valor de chave.
- `delete(key: any)`: Remove um nó da árvore com base na chave.

#### ReservationHandler
- `__init__()`: Inicializa o manipulador de reservas e a árvore binária.
- `add_reservation_request(room_number: int, reservation_time: str)`: Adiciona um pedido de reserva à árvore.

#### Fila
- Métodos para adicionar e remover pedidos de reserva, garantindo que as solicitações sejam processadas de maneira justa e eficiente.

### Mensagens do Servidor

O servidor processa diferentes comandos recebidos dos clientes e envia mensagens informativas de volta. As mensagens ajudam a monitorar a atividade do sistema e fornecem feedback sobre o status das operações. Abaixo estão os principais comandos que o servidor pode receber e como ele responde:

- **Comando: `RESERVE`**
  - **Descrição**: Este comando é usado para adicionar uma nova reserva. O formato esperado é `RESERVE {"id": número_do_quarto, "horario": "tempo_da_reserva"}`.
  - **Mensagem de Log**: `"Adicionando reserva: Quarto: {número_do_quarto}, Horário: {tempo_da_reserva}"`
  - **Resposta**: O servidor envia uma mensagem de confirmação ou um erro, se algo der errado.

- **Comando: `VIEW_RESERVATIONS`**
  - **Descrição**: Solicita a lista de reservas ativas.
  - **Resposta**: O servidor retorna um JSON contendo todas as reservas ou uma lista vazia `[]` se não houver reservas.

- **Comando: `PROCESS`**
  - **Descrição**: Processa o próximo pedido na fila.
  - **Resposta**: O servidor envia uma mensagem de confirmação sobre o processamento do pedido.

- **Comando: `CHECK`**
  - **Descrição**: Verifica uma reserva específica pelo número do quarto. O formato esperado é `CHECK número_do_quarto`.
  - **Resposta**: O servidor retorna as informações da reserva ou uma mensagem informando que a reserva não foi encontrada.

- **Comando: `SHUTDOWN`**
  - **Descrição**: Este comando encerra o servidor.
  - **Mensagem de Log**: `"Servidor encerrando..."`
  - **Resposta**: O servidor confirma o encerramento com a mensagem `"Servidor encerrado."`.

- **Comando Desconhecido**
  - Se um comando não for reconhecido, o servidor responderá com a mensagem: `"Comando desconhecido."`

Essas mensagens são fundamentais para depuração e para garantir que o sistema esteja funcionando conforme o esperado. Elas ajudam a entender as interações entre o cliente e o servidor durante o uso da aplicação.


## Como Utilizar

1. **Instalação**: Clone o repositório e instale as dependências necessárias (se houver).

2. **Iniciar o Servidor**: Abra um terminal e execute o seguinte comando para iniciar o servidor da aplicação:
   ```bash
   python -m Server.server
