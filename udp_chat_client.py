import socket
import threading

# Настройки сервера
SERVER_HOST = 'localhost'  # IP-адрес сервера
SERVER_PORT = 9090         # Порт сервера

# Создаём UDP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Функция для получения сообщений
def receive_messages():
    while True:
        try:
            data, addr = client_socket.recvfrom(1024)  # Получаем до 1024 байт
            print("\n" + data.decode())
        except:
            break

# Запускаем поток для получения сообщений
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

try:
    print("Подключено к серверу чата. Введите сообщения для отправки (введите 'exit' для выхода).")

    while True:
        message = input()
        if message.lower() == 'exit':
            print("Выход из чата...")
            break

        # Отправляем сообщение на сервер
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

finally:
    client_socket.close()
    print("Чат завершён")
