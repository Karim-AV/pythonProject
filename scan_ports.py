import socket

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

host = input("Введите IP-адрес для сканирования: ")
start_port = int(input("Введите начальный порт: "))
end_port = int(input("Введите конечный порт: "))

print(f"Сканируются порты от {start_port} до {end_port} на хосте {host}...")

open_ports = scan_ports(host, start_port, end_port)

if len(open_ports) > 0:
    print("Открытые порты:")
    for port in open_ports:
        print(f"Порт {port} открыт")
else:
    print("Открытых портов не найдено.")