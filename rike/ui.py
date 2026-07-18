from rich.console import Console
from rich.rule import Rule

console = Console()


def banner():
    console.print()
    console.print("[bold cyan]Rike[/bold cyan]")
    console.print("[dim]Developer Intelligence CLI[/dim]")


def separator():
    console.print(Rule())


def heading(text):
    console.print()
    console.print(f"[bold cyan]{text}[/bold cyan]")
    console.print()


def success(text):
    console.print(f"[bold green]{text}[/bold green]")


def error(text):
    console.print(f"[bold red]{text}[/bold red]")


def warning(text):
    console.print(f"[bold yellow]{text}[/bold yellow]")


def info(text):
    console.print(f"[bold blue]{text}[/bold blue]")
