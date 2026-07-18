import requests
import webbrowser


def hackernews(console):
    feed = input(
        "\nChoose Feed\n"
        "1. Top Stories\n"
        "2. New Stories\n"
        "3. Best Stories\n"
        "> "
    )

    if feed == "1":
        feed_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    elif feed == "2":
        feed_url = "https://hacker-news.firebaseio.com/v0/newstories.json"
    elif feed == "3":
        feed_url = "https://hacker-news.firebaseio.com/v0/beststories.json"
    else:
        console.print("[yellow]Invalid choice. Using Top Stories.[/yellow]")
        feed_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    limit = int(input("\nNumber of stories (1-30): "))

    if not 1 <= limit <= 30:
        console.print("[bold red]Enter a valid number between 1 and 30.[/bold red]")
        return

    with console.status("[bold cyan]Fetching Hacker News..."):
        story_ids = requests.get(feed_url, timeout=10).json()

    stories = []

    console.print(f"\n[bold cyan]Top {limit} Hacker News Stories[/bold cyan]\n")

    for number, story_id in enumerate(story_ids[:limit], start=1):
        story = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
            timeout=10,
        ).json()

        stories.append(story)

        console.print(f"[bold]{number}. {story.get('title', 'No title')}[/bold]")
        console.print(
            f"[dim]{story.get('by', 'Unknown')} • ⭐ {story.get('score', 0)}[/dim]"
        )
        console.print(f"[blue]{story.get('url', 'No URL')}[/blue]")
        console.print("-" * 70)

    choice = int(input("\nOpen story (0 to skip): "))

    if 1 <= choice <= len(stories):
        webbrowser.open(stories[choice - 1]["url"])