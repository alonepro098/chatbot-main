<h2 align="center">
    ──「 𓆩꯭❛ 𝙍𝘼𝘿𝙃𝙀 ❜꯭𓆪⁩ 」──
</h2>
<p align="center">
  <img src="https://i.ibb.co/wNRdVdnL/file-3604.jpg" alt="Radhe Bot Logo">
</p>
<h2 align="center"> ──「 ᴅᴇᴍᴏ ʀᴏʙᴏᴛ 」──</h2>
<p align="center">
  <a href="https://t.me/radhe_chat_bot">
    <img src="https://img.shields.io/badge/Check-Demo%20Robot-black?style=for-the-badge&logo=Telegram" width="220" height="39"/>
  </a>
</p>

An elegant, modern, high-performance Telegram Chatbot written in Python using **Pyrogram v2** and **MongoDB (Motor)**. Fully optimized for production deployments (e.g., Render, Heroku, VPS, or Docker).

---

## 🚀 Features

- **Asynchronous Architecture:** Rewritten to use purely non-blocking `Motor` asynchronous calls for MongoDB. Eliminates latency spikes and blockages in Pyrogram's event loop.
- **Auto-Learning Chatbot:** Dynamically learns conversation replies from chat groups and uses them to intelligently respond.
- **Admin Utilities:** Promotes, demotes, kicks, mutes, unmutes, bans, unbans, and pins messages using inline buttons.
- **Built-in Games:** Play dice, dart, basketball, bowling, football, and slot machines.
- **Media Download Command:** Download videos and images from Pinterest, Instagram, or YouTube via external API.
- **Broadcasting & Announcements:** Direct broadcasting and message forwarding to all served groups and users.
- **Flask Keep-Alive:** Integrated Flask server for port-binding and health checks in cloud environments (Render, Heroku).

---

## 🛠️ Configuration

Configure the bot using a `.env` file or direct environment variables:

| Variable | Description | Default |
| :--- | :--- | :--- |
| `API_ID` | Telegram API ID from my.telegram.org | `22243185` |
| `API_HASH` | Telegram API Hash from my.telegram.org | `39d926a67155f59b722db787a23893ac` |
| `BOT_TOKEN` | Bot Token from [@BotFather](https://t.me/BotFather) | *Required* |
| `MONGO_URL` | MongoDB Connection URI | *Required* |
| `OWNER_ID` | User ID of the primary owner | `1999645649` |
| `OWNER_USERNAME` | Username of the owner (without `@`) | `candy_caugh` |
| `SUPPORT_GRP` | Username of the support group | `dil_kee_alfaz` |
| `UPDATE_CHNL` | Username of the update channel | `about_candyy` |

---

## 📦 Deployment & Setup

### Local Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/chatbot-main.git
   cd chatbot-main
   ```
2. Copy `sample.env` to `.env` and fill in the values:
   ```bash
   cp sample.env .env
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the bot:
   ```bash
   bash start
   # or
   python3 -m Radhe
   ```

### Docker Deploy

Build and start the container:
```bash
docker build -t radhe-bot .
docker run -d --env-file .env --name radhe-bot radhe-bot
```

---

## 👥 Support & Community

- **Support Group:** [Join Chat](https://t.me/INDIAN_CHATTING_GC)
- **News Channel:** [Subscribe](https://t.me/about_candyy)
