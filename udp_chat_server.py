import socket

# Настройки сервера
HOST = ''  # Пустая строка означает, что сервер доступен на всех интерфейсах
PORT = 9090  # Порт для прослушивания

# Создаём UDP-сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к адресу и порту
server_socket.bind((HOST, PORT))
print(f"Сервер запущен на порту {PORT}...")

# Список подключённых клиентов
clients = set()

try:
    while True:
        # Принимаем сообщение от клиента
        data, addr = server_socket.recvfrom(1024)  # Получаем до 1024 байт
        message = data.decode()

        # Если клиент отправляет новое сообщение, добавляем его адрес в список
        if addr not in clients:
            clients.add(addr)
            print(f"Новый клиент подключился: {addr}")

        # Логируем полученное сообщение
        print(f"Сообщение от {addr}: {message}")

        # Рассылаем сообщение всем подключённым клиентам
        for client in clients:
            if client != addr:  # Не отправляем сообщение отправителю
                server_socket.sendto(data, client)

except KeyboardInterrupt:
    print("\nСервер остановлен вручную")

finally:
    server_socket.close()
    print("Сервер полностью остановлен")