import requests
import webbrowser

from rich.console import Console

input_feed = input("Choose Feed : \n1. Top Stories\n2. New Stories\n3. Best Stories\nEnter your choice (1-3): ")
if input_feed == "1":
    feed_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
elif input_feed == "2":
    feed_url = "https://hacker-news.firebaseio.com/v0/newstories.json"
elif input_feed == "3":
    feed_url = "https://hacker-news.firebaseio.com/v0/beststories.json"
else:
    print("Invalid choice. Defaulting to Top Stories.")
    feed_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

console = Console()
limit = int(input("Enter the number of top stories to display (max 30): "))

if not 1 <= limit <= 30:
    console.print("[bold red]Enter a valid number between 1 and 30.")
    exit()

try:
    story_ids = requests.get(
        f"{feed_url}",
        timeout=10,
    ).json()
except requests.RequestException:
    console.print("[bold red]Failed to fetch Hacker News stories.")
    exit()

stories = []

console.print(f"\n[bold cyan]Top {limit} Hacker News Stories\n")

for number, story_id in enumerate(story_ids[:limit], start=1):
    try:
        story = requests.get(
            timeout=10,
            url=f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
        ).json()
    except requests.RequestException:
        continue

    stories.append(story)

    console.print(f"[bold cyan]{number}. {story.get('title', 'No title')}")
    console.print(f"[dim]{story.get('by', 'Unknown')} • ⭐ {story.get('score', 0)}")
    console.print(f"[blue]{story.get('url', 'No URL')}")
    console.print()

choice = int(input("Enter story number to open (0 to skip): "))

if choice != 0:
    webbrowser.open(stories[choice - 1]["url"])

