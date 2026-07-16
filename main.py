import requests
from rich.console import Console

console = Console()

limit = int(input("Enter the number of top stories to display (max 30): "))

if not 1 <= limit <= 30:
    console.print("[bold red]Enter a valid number between 1 and 30.")
    exit()

try:
    story_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/beststories.json",
        timeout=10,
    ).json()
except requests.RequestException:
    console.print("[bold red]Failed to fetch Hacker News stories.")
    raise SystemExit

console.print(f"\n[bold cyan]Top {limit} Hacker News Stories\n")

for number, story_id in enumerate(story_ids[:limit], start=1):
    try:
        story = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
            timeout=10,
        ).json()
    except requests.RequestException:
        continue

    title = story.get("title", "No title")
    author = story.get("by", "Unknown")
    score = story.get("score", 0)
    url = story.get("url", "No URL")

    console.print(f"[bold cyan]{number}.[/] {title}")
    console.print(f"[dim]{author} • ⭐ {score}")
    console.print(f"[blue]{url}")
    console.print()