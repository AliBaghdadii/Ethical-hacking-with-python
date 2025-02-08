import socket
import threading
from queue import Queue

# A more advanced port scanner that uses multithreading to imporve performance:
def port_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except:
        pass

def worker():
    while True:
        port = port_queue.get()
        port_scan(target, port)
        port_queue.task_done()

def main():
    global target, port_queue
    target = input("Enter the target IP address: ")
    ports = int(input("Enter the number of ports to scan: "))
    thread_count = int(input("Enter the number of threads to use: "))

    port_queue = Queue()

    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    for port in range(1, ports + 1):
        port_queue.put(port)

    port_queue.join()

if __name__ == '__main__':
    main()