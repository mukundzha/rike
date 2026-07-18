# Rike 🚀

> Developer Intelligence CLI — discover programming trends directly from your terminal.

Rike brings developer-focused information into one simple command-line interface.

Currently supported:

- 📢 Hacker News stories
- ⭐ GitHub Trending repositories
- 🔍 Language filtering
- ⏱ Time-based GitHub trends
- 🌐 Open links directly from terminal

---

# Installation

Install Rike from PyPI:

```bash
pip install rike

Run:

rike
Features
Hacker News

Browse Hacker News directly from your terminal.

Available feeds:

Top Stories
New Stories
Best Stories

Example:

Choose Source

1. Hacker News
2. GitHub Trending
q. Quit

> 1

Select a feed:

Choose Feed

1. Top Stories
2. New Stories
3. Best Stories

> 1

Rike will display:

Story title
Author
Score
URL

You can open any story directly from the terminal.

GitHub Trending

Explore trending repositories from GitHub.

Supported filters:

Languages
All
Python
Rust
Go
TypeScript
Time Range
Daily
Weekly
Monthly

Example:

Choose Source

1. Hacker News
2. GitHub Trending

> 2

Select:

Language:

1. All
2. Python
3. Rust
4. Go
5. TypeScript


Time Range:

1. Daily
2. Weekly
3. Monthly

Output:

1. vercel/next.js

JavaScript • ⭐ 96,500

https://github.com/vercel/next.js
Screenshots

Add screenshots here:

docs/
 ├── hackernews.png
 └── github-trending.png

Example:

Why Rike?

Developers constantly switch between:

Hacker News
GitHub Trending
Browser tabs
News websites

Rike provides a lightweight terminal workflow for discovering:

New technologies
Popular repositories
Developer discussions
Project Structure
rike/
│
├── rike/
│   ├── main.py
│   ├── github.py
│   ├── hackernews.py
│   ├── ui.py
│   └── utils.py
│
├── README.md
├── LICENSE
└── pyproject.toml
Development Setup

Clone the repository:

git clone https://github.com/mukundzha/rike.git

cd rike

Create virtual environment:

python -m venv .venv

Activate:

Linux/macOS:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -e .

Run:

python -m rike.main
Dependencies

Rike uses:

Requests — API communication
Rich — terminal UI formatting
Roadmap
v0.2.0
 Better error handling
 Search functionality
 Improved terminal UI
 Configuration file
v0.3.0
 More data sources
 Local caching
 User preferences
v1.0.0
 Stable API
 Full CLI arguments
 Production-ready release
Contributing

Contributions are welcome.

Steps:

Fork the repository
Create a branch
git checkout -b feature-name
Make changes
Commit
git commit -m "Add feature"
Push
git push origin feature-name
Open a Pull Request
Reporting Issues

Found a bug?

Open an issue:

https://github.com/mukundzha/rike/issues

Include:

Operating system
Python version
Error message
Steps to reproduce
License

MIT License

Copyright (c) 2026 Mukund
