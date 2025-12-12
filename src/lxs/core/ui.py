from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


def info(msg: str) -> None:
    console.print(f"[blue][INFO][/blue]  {msg}")


def ok(msg: str) -> None:
    console.print(f"[green][OK][/green]    {msg}")


def warn(msg: str) -> None:
    console.print(f"[yellow][WARN][/yellow]  {msg}")


def error(msg: str) -> None:
    console.print(f"[red][ERROR][/red] {msg}")


def step(msg: str) -> None:
    console.print(f"[cyan]>>>[/cyan] {msg}")


def section(title: str) -> None:
    console.print()
    console.print(Panel(title, style="cyan", expand=False))
    console.print()


def spinner(msg: str) -> Progress:
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    )
