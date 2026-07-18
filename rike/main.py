from .hackernews import hackernews
from .github import github
from .ui import banner, console

def main():
    banner()

    while True:
        source = input(
            "\nChoose Source\n"
            "1. Hacker News\n"
            "2. GitHub Trending\n"
            "q. Quit\n"
            "> "
        )

        if source == "1":
            hackernews(console)

        elif source == "2":
            github(console)

        elif source.lower() == "q":
            console.print("\n[bold green]Goodbye![/bold green]")
            break

        else:
            console.print("[bold red]Invalid option.[/bold red]")


if __name__ == "__main__":
    main()