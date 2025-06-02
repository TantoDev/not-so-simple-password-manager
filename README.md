# 🔐 Not-So-Simple Password Manager

As you can see this is a not so simple password manager🤷🏾‍♂️ I built to get more practice with **Object-Oriented Programming** and basic logic.


## ✨ Features

- Add new credentials (title, username, password)  
- View all saved credentials  
- Search by title or username  
- Delete credentials  
- Data stored persistently in `vault.json` using JSON format  
- Basic error handling for corrupted or missing files  

The `Credential` class represents each saved login, and `Vault` handles all storage logic.  
I used JSON to serialize and deserialize the data instead of saving Python objects directly, lightweight, readable, and beginner friendly.  
Also added basic handling for when the vault file is missing or broken, so it doesn’t crash.


## 📖 Backstory

I found this project **really exciting**, even though I ran into errors *literally all the way*.  
Made it a personal challenge to **debug things myself** and only fall back to AI when totally stuck — just to build that dev muscle.  
Not gonna lie, it was time consuming and yeah... I definitely broke some stuff along the way 😂

One tricky part was storing data.  
I started off trying to save actual Python objects, but turns out **JSON doesn't like that**.  
So I had to figure out how to convert the data into a format JSON understands and then reconstruct it later.  
That took me a minute... okay, an hour 😅.  
But when everything finally clicked and ran smoothly ✅ .. **that hit felt amazing** 🤓✨

I was planning to add encryption, a cleaner menu, and better error prompts but my battery died mid-session and well... priorities 😅


## 🛠️ How to Run

Just run the script in any **Python 3** environment.  
It’ll automatically create a `vault.json` file in the same directory to store your saved data.


## 💬 Final Note

Feel free to fork, modify, break, or upgrade the project.  
It’s raw and simple, just how learning projects should be.
