import requests
import webbrowser


def github(console):
    console.print("\n[bold cyan]Choose Language[/bold cyan]")
    console.print("1. All")
    console.print("2. Python")
    console.print("3. Rust")
    console.print("4. Go")
    console.print("5. TypeScript")

    language = input("Choose language (1-5): ")

    console.print("\n[bold cyan]Choose Time Range[/bold cyan]")
    console.print("1. Daily")
    console.print("2. Weekly")
    console.print("3. Monthly")

    time_range = input("Choose Time Range (1-3): ")

    if time_range == "1":
        since = "daily"
    elif time_range == "2":
        since = "weekly"
    elif time_range == "3":
        since = "monthly"
    else:
        since = "daily"

    limit = int(input("\nNumber of repositories (1-30): "))

    if not 1 <= limit <= 30:
        console.print("[bold red]Enter a valid number between 1 and 30.[/bold red]")
        return

    if language == "1":
        url = "https://gitrends-api.vercel.app/trending"
    elif language == "2":
        url = "https://gitrends-api.vercel.app/trending?language=python"
    elif language == "3":
        url = "https://gitrends-api.vercel.app/trending?language=rust"
    elif language == "4":
        url = "https://gitrends-api.vercel.app/trending?language=go"
    elif language == "5":
        url = "https://gitrends-api.vercel.app/trending?language=typescript"
    else:
        console.print("[bold red]Invalid language.[/bold red]")
        return

    if "?" in url:
        url += f"&since={since}"
    else:
        url += f"?since={since}"

    with console.status("[bold green]Fetching GitHub Trending..."):
        repos = requests.get(url, timeout=10).json()

    console.print(f"\n[bold green]Top {limit} Trending Repositories[/bold green]\n")

    for number, repo in enumerate(repos[:limit], start=1):
        console.print(f"[bold]{number}. {repo['name']}[/bold]")
        console.print(
            f"[dim]{repo['language']} • ⭐ {repo['stars']}[/dim]"
        )
        console.print(f"[blue]{repo['url']}[/blue]")
        console.print("-" * 70)

    choice = int(input("\nOpen repository (0 to skip): "))

    if 1 <= choice <= len(repos):
        webbrowser.open(repos[choice - 1]["url"])