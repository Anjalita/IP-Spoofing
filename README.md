
# IP-Spoofing - Cybersecurity Demo

This is a lab demonstration on **IP Spoofing**, a classic network attack technique where the attacker impersonates another IP address to gain unauthorized access or disrupt network communication.

## 🧪 Objective

To demonstrate how IP spoofing works in a controlled lab environment using tools like `Scapy`.  
This is intended strictly for **educational purposes only**.

---

## 🖥️ Environment Setup

- OS: Kali Linux / Parrot OS
- Language: Python 3.x
- Virtual Environment: `venv` (recommended)
- Git for version control

---

## 📦 Installation

1. Clone this repo:
   
   ```
   git clone https://github.com/Anjalita/IP-Spoofing.git
   cd IP-Spoofing
    ```

2. Create and activate virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate   # On Linux/macOS
   ```

3. Install Scapy:

   ```
   pip install scapy
   ```

---

## ⚙️ How to Run

Run the script (requires sudo due to use of raw sockets):

```
sudo python3 fake.py
```

You should see output indicating spoofed ICMP packets were sent.

---

## 📸 Screenshots

* **attack-terminal.png**
  ![attacker\_terminal](https://github.com/user-attachments/assets/a9c893d1-c9e5-4e60-a713-a175ebc964c3)
  *Terminal output where the spoofing is executed.*

* **spoofed\_packet\_details.png**
  ![spoofed\_packet\_details](https://github.com/user-attachments/assets/06931ec5-d13c-476f-a18a-6f5e1324b0d8)
  *Packet details showing spoofed source IP.*

* **wireshark-capture.png**
  ![wireshark\_capture](https://github.com/user-attachments/assets/be75c353-971d-4f5e-a2f2-e95652683a3a)
  *Wireshark showing ICMP Echo requests from fake source IP.*

---


## 🛑 Disclaimer

> ⚠️ This project is for **educational and ethical testing** only.
> Do **not** use this on unauthorized networks or systems.
> Always test in a **controlled environment** with permission.

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for full terms.

```

---


```
