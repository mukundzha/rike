# Rike

**Rike** is a lightweight terminal-based developer intelligence CLI that helps you stay updated without leaving your terminal.

It aggregates useful information from developer-focused sources into a fast, clean command-line interface.

> Built with Python and Rich.

---

## Features

### Hacker News

* Browse Top Stories
* Browse Best Stories
* Browse New Stories
* View title, author, score, and URL
* Open any story directly in your default browser

### GitHub Trending

* View trending repositories
* Display repository name
* Show programming language
* Show star count
* Open repositories directly from the terminal

### Terminal Experience

* Clean Rich-powered interface
* Fast and lightweight
* Simple interactive menus
* Browser integration

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mukundzha/rike.git
cd rike
```

Install dependencies:

```bash
pip install requests rich
```

Run:

```bash
python main.py
```

---

## Preview

```text
Rike
Developer Intelligence CLI

Choose Source
1. Hacker News
2. GitHub Trending
>
```

---

## Roadmap

### v0.1

* [x] Project setup
* [x] Hacker News integration
* [x] Rich terminal interface
* [x] Browser support

### v0.2

* [x] Multiple Hacker News feeds
* [x] Top Stories
* [x] Best Stories
* [x] New Stories

### v0.3

* [x] GitHub Trending integration
* [x] Repository metadata
* [x] Open repositories in browser

### Upcoming

* [ ] RSS feed support
* [ ] Security advisories (CVE, GitHub Security)
* [ ] Dev.to integration
* [ ] Reddit programming communities
* [ ] Product Hunt developer tools
* [ ] Bookmark stories
* [ ] Search across sources
* [ ] Keyboard shortcuts
* [ ] Configuration file
* [ ] Multiple themes
* [ ] AI-powered summaries
* [ ] Daily digest mode
* [ ] Plugin architecture

---

## Tech Stack

* Python
* Requests
* Rich

---

## Why Rike?

Developers often switch between Hacker News, GitHub, blogs, and other websites throughout the day.

Rike aims to bring those sources together into a single terminal-first experience that is fast, distraction-free, and extensible.

---

## Project Status

Rike is under active development.

New sources and improvements are being added incrementally while keeping the CLI lightweight and easy to use.

---

## Contributing

Issues, feature requests, and pull requests are welcome.

If you have an idea that would make Rike more useful for developers, feel free to open an issue or submit a contribution.

---

## License

MIT License.
