import socket
import datetime

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP and Port configuration
ip_address = '127.0.0.1'
port_no = 2525
complete_address = (ip_address, port_no)

# Bind the socket to the specified IP and port
s.bind(complete_address)

print(f"Receiver is listening on {ip_address}:{port_no}")

while True:
    # Receive message from sender
    message = s.recvfrom(100)
    received_message = message[0]
    decrypted_message = received_message.decode('ascii')
    
    # Get current time and sender address
    present_time = datetime.datetime.now()
    time = str(present_time)
    sender_address = message[1][0]

    # Print and save the received message with a timestamp
    print(f"{time} - {decrypted_message}")
    
    with open(sender_address + '.txt', 'a+') as file:
        file.write(time + " - " + decrypted_message + '\n')

    # Get a message from the user to send back to the sender
    receiver_message = input("Send the message to the sender: ")
    encrypted_message = receiver_message.encode('ascii')
    send_address = message[1]
    
    # Send the response message back to the sender
    s.sendto(encrypted_message, send_address)
