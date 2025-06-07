# 🔐 Not-So-Simple Password Manager

A simple password manager built to sharpen my Object-Oriented Python skills and practice basic logic.

## ✨ Features

- Add, view, search, and delete credentials  
- Clear all credentials with confirmation  
- Data saved persistently in `vault.json` (JSON format)  
- Master password stored separately in `mastervault.json` for simple authentication  
- Handles missing/corrupted files without crashing  
- Prevents empty user inputs  

`Credential` manages each saved login, `Vault` handles storage and interaction.

## 📖 Backstory

I took this on as a personal challenge — debugging and building it mostly on my own.

I also added a master password system to keep things a bit secure.

I’m still planning to improve encryption, clean up the menu, and make error messages better. I'll do that when I'm less annoyed. Just happy it works now. Messy code? I know.

## 🛠️ How to Run

Run it with Python 3. The program will create `vault.json` and `mastervault.json` automatically to store your data.

## 💬 Final Note

This is a raw learning project. Feel free to fork it, improve it, or just play around.
