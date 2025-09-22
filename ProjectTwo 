from socket import *
import sys

MAILSERVER = "list.winthrop.edu"
PORT = 25
SENDER = "atiasea2@winthrop.edu"
RECIPIENT = "sakyie2@winthrop.edu"
SUBJECT = "Lab Test"
BODY = "Testing my work"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((MAILSERVER, PORT))

recv = clientSocket.recv(1024).decode("ascii", errors="replace")
print(recv, end="")
if recv[:3] != "220":
    print("220 reply not received from server.", file=sys.stderr)

heloCommand = "HELO winthrop.edu\r\n"
clientSocket.sendall(heloCommand.encode("ascii"))
recv1 = clientSocket.recv(1024).decode("ascii", errors="replace")
print(recv1, end="")
if recv1[:3] != "250":
    print("250 reply not received from server.", file=sys.stderr)

clientSocket.sendall(f"MAIL FROM:<{SENDER}>\r\n".encode("ascii"))
print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

clientSocket.sendall(f"RCPT TO:<{RECIPIENT}>\r\n".encode("ascii"))
print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

clientSocket.sendall("DATA\r\n".encode("ascii"))
print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

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

clientSocket.sendall("QUIT\r\n".encode("ascii"))
print(clientSocket.recv(1024).decode("ascii", errors="replace"), end="")

clientSocket.close()
