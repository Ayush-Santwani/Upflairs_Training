import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = '127.0.0.1'
port_no = 2525
target_add = (target_ip, port_no)

def new_func(receiver_message):
    return receiver_message.decode('ascii')

while True:
    message = input("Enter your message (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    encrypt_message = message.encode('ascii')
    s.sendto(encrypt_message, target_add)

    receiver_message, _ = s.recvfrom(100)
    decrypted_message = new_func(receiver_message)
    print(decrypted_message)

    with open('received_messages.txt', 'a+') as file:
        file.write(decrypted_message + '\n')
