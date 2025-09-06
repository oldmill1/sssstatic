"""
Display module for SSSStatic - handles all ASCII art and console output
"""

import time
from pathlib import Path
from rich.console import Console

console = Console()


def show_epic_header():
    """Display the epic ASCII art header."""
    console.print("")
    console.print(
        "[bold bright_green]╔══════════════════════════════════════════════════════════════╗[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]███████╗███████╗███████╗███████╗███████╗████████╗ █████╗ ████████╗██╗ ██████╗[/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝[/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]███████╗███████╗███████╗███████╗███████╗   ██║   ███████║   ██║   ██║██║     [/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]╚════██║╚════██║╚════██║╚════██║╚════██║   ██║   ██╔══██║   ██║   ██║██║     [/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]███████║███████║███████║███████║███████║   ██║   ██║  ██║   ██║   ██║╚██████╗[/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝[/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]╚══════════════════════════════════════════════════════════════╝[/bold bright_green]")
    console.print("")
    console.print("[bold bright_red]    ▼ ▼ ▼  STATIC SITE GENERATOR DEPLOYMENT PROTOCOL  ▼ ▼ ▼[/bold bright_red]")
    console.print("")
    console.print("[blink bright_yellow]>>> SYSTEM INITIALIZING...[/blink bright_yellow]")
    console.print("[dim bright_blue]>>> Awaiting operator input...[/dim bright_blue]")
    console.print("")


def show_main_header():
    """Display the main program header."""
    console.print("")
    console.print("[bold bright_green]╔════════════════════════════════════╗[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_cyan]🐍 SSSStatic ONLINE 🐍[/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
    console.print("[bold bright_green]╚════════════════════════════════════╝[/bold bright_green]")
    console.print("[dim bright_blue]>>> Static site generator ready for deployment[/dim bright_blue]")
    console.print("[dim]>>> Execute 'sssstatic create new' to begin mission[/dim]")
    console.print("")


def show_error(title, message):
    """Display a formatted error message."""
    console.print(f"[bold red]╭─[ {title} ]─────────────────────╮[/bold red]")
    console.print(f"[bold red]│ {message}     │[/bold red]")
    console.print("[bold red]╰────────────────────────────────────────╯[/bold red]")


def show_critical_error(message, details=None):
    """Display a critical system failure message."""
    console.print("")
    console.print("[bold red]╔══════════════════════════════════════════╗[/bold red]")
    console.print(
        "[bold red]║[/bold red] [bold bright_white]🔥 CRITICAL SYSTEM FAILURE! 🔥[/bold bright_white] [bold red]║[/bold red]")
    console.print("[bold red]╚══════════════════════════════════════════╝[/bold red]")
    console.print(f"[bold red]>>> ERROR DETAILS: {message}[/bold red]")
    if details:
        console.print(f"[bold red]>>> {details}[/bold red]")
    console.print("[bold red]>>> MISSION FAILED - EMERGENCY SHUTDOWN[/bold red]")


def show_deployment_header(project_name):
    """Display deployment start message."""
    console.print("")
    console.print("[bold bright_yellow]╔════════════════════════════════════════╗[/bold bright_yellow]")
    console.print(
        f"[bold bright_yellow]║[/bold bright_yellow] [bold bright_white]DEPLOYING PROJECT '{project_name}'...[/bold bright_white] [bold bright_yellow]║[/bold bright_yellow]")
    console.print("[bold bright_yellow]╚════════════════════════════════════════╝[/bold bright_yellow]")
    console.print("")


def show_progress_step(message, delay=0.3):
    """Display a progress step with completion marker."""
    console.print(f"[bright_blue]>>> [/bright_blue][bright_white]{message}...[/bright_white]", end="")
    time.sleep(delay)
    console.print(" [bold bright_green]✓ COMPLETE[/bold bright_green]")


def show_success_message(project_name, project_path):
    """Display the epic success message."""
    console.print("")
    console.print(
        "[bold bright_green]╔══════════════════════════════════════════════════════════╗[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_yellow]🚀 DEPLOYMENT SUCCESSFUL! MISSION ACCOMPLISHED! 🚀[/bold bright_yellow] [bold bright_green]║[/bold bright_green]")
    console.print(
        "[bold bright_green]╚══════════════════════════════════════════════════════════╝[/bold bright_green]")
    console.print("")
    console.print(f"[bold bright_cyan]╭─[ PROJECT STATUS ]──────────────────────╮[/bold bright_cyan]")
    console.print(
        f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Codename:[/bold bright_white] [bright_yellow]{project_name}[/bright_yellow]")
    console.print(
        f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Location:[/bold bright_white] [dim]{project_path}[/dim]")
    console.print(f"[bold bright_cyan]╰─────────────────────────────────────────╯[/bold bright_cyan]")
    console.print("")
    console.print("[bold bright_red]╭─[ NEXT OPERATIONS ]─────────────────────╮[/bold bright_red]")
    console.print(
        f"[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [bright_white]cd {project_name}[/bright_white]")
    console.print(
        "[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Add your source files and content[/dim]")
    console.print(
        "[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Execute 'sssstatic build' to generate site[/dim]")
    console.print("[bold bright_red]╰─────────────────────────────────────────╯[/bold bright_red]")
    console.print("")
    console.print("[blink bright_blue]>>> SYSTEM STANDING BY FOR FURTHER ORDERS...[/blink bright_blue]")


def show_directory_conflict(project_path):
    """Display directory conflict error."""
    console.print("")
    console.print("[bold red]╭─[ DEPLOYMENT CONFLICT ]────────────────╮[/bold red]")
    console.print(f"[bold red]│ Zone '{project_path}' already occupied  │[/bold red]")
    console.print("[bold red]│ MISSION ABORT - RETREAT IMMEDIATELY   │[/bold red]")
    console.print("[bold red]╰─────────────────────────────────────────╯[/bold red]")


def show_default_location(current_dir):
    """Display the default project location."""
    console.print("")
    console.print(f"[dim bright_blue]>>> Default deployment zone: [bold]{current_dir}[/bold][/dim bright_blue]")
