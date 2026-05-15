# python-vigenere-cipher

A lightweight, command-line Python tool to encrypt and decrypt text files using the classic Vigenère cipher.

## ✨ Features
* **Two-Way Cryptography:** Easily switch between encrypting and decrypting messages.
* **Preserves Formatting:** Maintains original letter casing (upper/lower) and ignores non-alphabetical characters (spaces, punctuation, numbers).
* **Memory Optimized:** Processes the text manipulation in memory and executes a single file write at the end, preventing disk I/O bottlenecks.
* **Cross-Platform Safe:** Uses explicit UTF-8 encoding to ensure characters don't break across different operating systems.

## 🚀 How to Use
1. Clone this repository to your local machine.
2. Change the file named `message.txt` in the same directory and paste your secret text inside.
3. Run the script from your terminal:
   ```bash
   python cry.py
