# IP-Spoofing - Cybersecurity Demo

This is a lab demonstration on **IP Spoofing**, a classic network attack technique where the attacker impersonates another IP address to gain unauthorized access or disrupt network communication.

## 🧪 Objective

To demonstrate how IP spoofing works in a controlled lab environment using tools like `Scapy` or basic socket programming in Python.  
This is intended for **educational purposes only**.

---

## 🖥️ Environment Setup

- OS: Kali Linux / Parrot OS
- Language: Python 3.x
- Virtual Environment: venv (activated before running scripts)
- Git for version control

---


---

## 📸 Screenshots

- **attack-terminal.png**: The attacker used to spoof IP packets
- **spoofed_packet_details.png**: Observation of response after sending the packet
- **wireshark-capture.png**: Wireshark capture showing spoofed packets

---

## ⚙️ How to Run

1. Clone this repo:
    ```bash
    git clone https://github.com/Anjalita/IP-Spoofing.git
    cd IP-Spoofing
    ```

2. Create and activate virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script (with `sudo` if needed for raw sockets):
    ```bash
    sudo python3 fake.py
    ```

---

## 🛑 Disclaimer

> ⚠️ This project is meant for **educational and ethical** purposes only.  
> Do **not** attempt to use this knowledge for malicious activities.  
> Always perform tests in **controlled environments** with permission.

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.


