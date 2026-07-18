import webbrowser

from rike.ui import console


def open_url(url):
    """Open a URL in the user's default browser."""
    with console.status("[bold green]Opening browser..."):
        webbrowser.open(url)


def get_limit():
    """Prompt for the number of items to display."""
    limit = int(input("\nNumber of results (1-30): "))

    if not 1 <= limit <= 30:
        console.print("[bold red]Enter a valid number between 1 and 30.[/bold red]")
        return None

    return limit


def separator():
    """Print a separator line."""
    console.rule()


def pause():
    """Wait for the user before returning to the main menu."""
    input("\nPress Enter to continue...")