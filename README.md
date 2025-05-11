# discordsb 🤖  
A versatile "user bot" for Discord  

`discordsb` allows you to run commands directly from your user account, enabling you to automate actions and manage Discord activities with a bot-like experience while maintaining the flexibility of using your personal account. **Note:** This bot is a userbot and may be against Discord’s Terms of Service (TOS), so use at your own risk.

---

## 🚨 **DISCLAIMER**  
This project may violate Discord's TOS, as Discord only allows user applications, not bots running on user accounts. Although Discord allows some user apps, using this tool might still result in account suspension or termination. **You are responsible for any actions taken with this tool.**

---

## ⚙️ **Installation**

### Prerequisites

- Python 3.7+
- `discord.py-self` library (used for self bots)

To install the required dependencies, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/bedxnta/discordsb.git
   cd discordsb
    ```
   
2. Install the `discord.py-self` library:
   pip install discord.py-self

---

## ⚡ **Getting Started**

1. Open the `main.py` file.
2. Replace the `user_token` variable with your own Discord user token.  
   **Important:** Be cautious with your token—do not share it with anyone.
   
   user_token = "YOUR_DISCORD_USER_TOKEN"

3. Run the script:
   python main.py

This will start the bot, allowing you to run commands through your personal Discord account.

---

## 📝 **Available Commands**  
Currently, there are only two demo commands included, but you can add more according to your needs:

- **avatar:** Displays avatar of the user.
- **ping:** Pings the server.

Further commands can be added as needed by adding command.py files (where command is your command name) in the `commands` directory.

---

## 🚨 **Important Notes**

- Running a userbot is **against Discord's TOS** and may result in account suspension or termination.
- Always ensure you’re not spamming or violating any community guidelines while using the bot.
