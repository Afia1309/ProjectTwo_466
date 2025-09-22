#Afua Atiase
#CSCI 466 : SMTP Lab, Project Two

from socket import *
import sys
import time

# Setup
MAILSERVER = "list.winthrop.edu"
PORT = 25
SENDER = "atiasea2@winthrop.edu"
RECIPIENT = "sakyie2@winthrop.edu"
SUBJECT = "Lab Test"
BODY = "Testing my work"

# etablish connection with the mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10)

try:
    # attempt connection 
    try:
        clientSocket.connect((MAILSERVER, PORT))
    except OSError:
        time.sleep(1)
        clientSocket.connect((MAILSERVER, PORT))

    # initial server response
    recv = clientSocket.recv(1024).decode("ascii", errors="replace")
    print(recv, end="")
    if recv[:3] != "220":
        print("Expected 220 greeting not received.", file=sys.stderr)

    # introduce client to server
    heloCommand = "HELO winthrop.edu\r\n"
    clientSocket.sendall(heloCommand.encode("ascii"))
    recv1 = clientSocket.recv(1024).decode("ascii", errors="replace")
    print(recv1, end="")
    if recv1[:3] != "250":
        print("Expected 250 reply after HELO.", file=sys.stderr)

    # specify the sender
    clientSocket.sendall(f"MAIL FROM:<{SENDER}>\r\n".encode("ascii"))
    print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

    # specify the recipient
    clientSocket.sendall(f"RCPT TO:<{RECIPIENT}>\r\n".encode("ascii"))
    print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

    # start the message data
    clientSocket.sendall("DATA\r\n".encode("ascii"))
    print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

    # headers followed by message body
    headers = (
        f"Subject: {SUBJECT}\r\n"
        f"From: {SENDER}\r\n"
        f"To: {RECIPIENT}\r\n"
        "\r\n"
    )
    clientSocket.sendall(headers.encode("ascii"))
    clientSocket.sendall((BODY + "\r\n").encode("ascii"))

    clientSocket.sendall(".\r\n".encode("ascii"))
    print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

    # close the SMTP session
    clientSocket.sendall("QUIT\r\n".encode("ascii"))
    print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

finally:
    clientSocket.close()

