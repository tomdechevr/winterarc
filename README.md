# ❄️ Winter Arc

A personal, ultra-minimalist mini-SaaS to track your *Winter Arc*: finances, daily goals, journaling, and a countdown to December 25th — fully self-hosted, no account, no cloud, no dependencies.

No database, no framework: a single self-contained HTML/CSS/JS page and a ~150-line Python server (standard library only) that reads and writes directly to `.json` files at the root of the project.

---

## ✨ Features

| Page | What it does |
|---|---|
| **Dashboard** | Countdown to December 25th (day X / Y, progress bar, editable start date), global and today's wallet summary, goals progress, today's journal status |
| **Wallet** | Mini accounting: **+** / **−** buttons to log a transaction (amount + reason), running balance, full history |
| **Calendar** | Monthly grid with each day's balance shown in color (green positive, red negative, grey at zero) — click a date to jump straight into journaling for that day |
| **Goals** | **Daily** goals to check off each day, current 🔥 streak per goal, GitHub-style contribution grid |
| **Journaling** | 10-minute **Pomodoro** timer for your writing session, daily text entry + a rating out of 5, browsable history, rating trend line chart over time |

Ultra-minimalist design, cream & terracotta palette, Fraunces/Inter typography — in the spirit of claude.ai. Automatic dark mode based on system preferences. Mobile-friendly layout (bottom navigation bar).

---

## 🗂 Project structure

```
winter-arc/
├── index.html          # the app (single page, no external dependencies)
├── server.py            # local server (Python 3, standard library only)
├── transactions.json    # wallet transactions
├── goals.json            # goals and streak history
├── journal.json          # journaling entries
├── settings.json         # settings (Winter Arc start date)
└── README.md
```

Each `.json` file is read and rewritten in plain text on every action — open them with any text editor to inspect or back up your raw data.

---

## 🚀 Getting started

**Requirements:** Python 3 (already installed on macOS/Linux; on Windows, install it from [python.org](https://python.org) and check *Add Python to PATH*).

```bash
git clone https://github.com/<your-username>/winter-arc.git
cd winter-arc
python3 server.py
```

Your browser will open automatically at **http://localhost:8420**. If it doesn't, open that address yourself.

> ⚠️ Never open `index.html` directly (double-click): for security reasons, a standalone HTML file can't read or write files on disk. Always go through `server.py`.

### Access from your whole local network

The server listens on `0.0.0.0`: on startup, the terminal prints the address to use from another device on the same Wi-Fi network (phone, tablet...):

```
- On this device: http://localhost:8420
- From another device on the network: http://192.168.x.x:8420
```

### Running on Android (Termux)

```bash
pkg install python
termux-setup-storage
cd ~/storage/downloads/winter-arc
python server.py
```
Then open `http://localhost:8420` in the phone's browser.

---

## 🛠 Tech stack

- **Frontend**: vanilla HTML/CSS/JS, no build step, no external libraries (aside from Google Fonts)
- **Backend**: Python's standard library `http.server` — no Flask, no Django, no `pip install`
- **Storage**: plain `.json` files at the project root — readable, versionable, easy to back up

---

## 💾 Backing up your data

Your data lives only in the `.json` files in this folder. To back it up or move it to another device, just copy these four files:

```
transactions.json  goals.json  journal.json  settings.json
```

---

## 📌 Ideas for future work

- [ ] One-click export/import (zip of the `.json` files)
- [ ] Expense categories in the Wallet
- [ ] Weekly/monthly aggregated summary
- [ ] Guided journaling prompts
- [ ] Lightweight PIN code for network access

Contributions and suggestions are welcome via issues.

---

## 📄 License

MIT — do whatever you want with it.
