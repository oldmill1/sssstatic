# sssstatic/server.py
"""
Server module for SSSStatic - handles development server functionality
"""

import os
import sys
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rich.console import Console

console = Console()


class SSSStaticHandler(SimpleHTTPRequestHandler):
    """Custom handler with better error pages and logging."""

    def log_message(self, format, *args):
        """Override to use rich console for prettier logs."""
        console.print(f"[dim bright_blue]>>> {format % args}[/dim bright_blue]")

    def end_headers(self):
        """Add custom headers for better development experience."""
        # Disable caching for development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()


def show_server_header(directory, port):
    """Display server startup message."""
    console.print("")
    console.print("[bold bright_green]╔════════════════════════════════════════════╗[/bold bright_green]")
    console.print(
        "[bold bright_green]║[/bold bright_green] [bold bright_yellow]🚀 SSSStatic DEV SERVER ONLINE! 🚀[/bold bright_yellow] [bold bright_green]║[/bold bright_green]")
    console.print("[bold bright_green]╚════════════════════════════════════════════╝[/bold bright_green]")
    console.print("")
    console.print(f"[bold bright_cyan]╭─[ SERVER STATUS ]──────────────────────╮[/bold bright_cyan]")
    console.print(
        f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Directory:[/bold bright_white] [bright_yellow]{directory}[/bright_yellow]")
    console.print(
        f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Port:[/bold bright_white] [bright_yellow]{port}[/bright_yellow]")
    console.print(
        f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]URL:[/bold bright_white] [bright_green]http://localhost:{port}[/bright_green]")
    console.print(f"[bold bright_cyan]╰─────────────────────────────────────────╯[/bold bright_cyan]")
    console.print("")
    console.print("[bold bright_red]╭─[ CONTROL COMMANDS ]───────────────────╮[/bold bright_red]")
    console.print(
        "[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [bright_white]Press Ctrl+C to shutdown[/bright_white]")
    console.print(
        "[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Server will auto-open in browser[/dim]")
    console.print("[bold bright_red]╰─────────────────────────────────────────╯[/bold bright_red]")
    console.print("")


def show_server_shutdown():
    """Display server shutdown message."""
    console.print("")
    console.print("[bold bright_red]╔═══════════════════════════════════════╗[/bold bright_red]")
    console.print(
        "[bold bright_red]║[/bold bright_red] [bold bright_white]🛑 SERVER SHUTDOWN COMPLETE 🛑[/bold bright_white] [bold bright_red]║[/bold bright_red]")
    console.print("[bold bright_red]╚═══════════════════════════════════════╝[/bold bright_red]")
    console.print("[dim bright_blue]>>> Mission complete - standing by...[/dim bright_blue]")
    console.print("")


def show_server_error(directory, error):
    """Display server error message."""
    console.print("")
    console.print("[bold red]╔══════════════════════════════════════════╗[/bold red]")
    console.print(
        "[bold red]║[/bold red] [bold bright_white]🔥 SERVER DEPLOYMENT FAILED! 🔥[/bold bright_white] [bold red]║[/bold red]")
    console.print("[bold red]╚══════════════════════════════════════════╝[/bold red]")
    console.print(f"[bold red]>>> ERROR: {error}[/bold red]")
    console.print(f"[bold red]>>> TARGET: {directory}[/bold red]")
    console.print("[bold red]>>> MISSION ABORTED[/bold red]")


def start_dev_server(directory="www", port=8000):
    """Start the development server."""
    # Validate directory exists
    serve_path = Path(directory)
    if not serve_path.exists():
        show_server_error(directory, f"Directory '{directory}' not found")
        return

    if not serve_path.is_dir():
        show_server_error(directory, f"'{directory}' is not a directory")
        return

    try:
        # Change to the target directory
        original_dir = os.getcwd()
        os.chdir(serve_path)

        # Create server
        server = HTTPServer(('localhost', port), SSSStaticHandler)

        # Show startup message
        show_server_header(serve_path.absolute(), port)

        # Auto-open browser
        try:
            webbrowser.open(f'http://localhost:{port}')
            console.print("[bright_green]>>> Browser launched automatically![/bright_green]")
        except Exception:
            console.print("[dim yellow]>>> Could not auto-open browser[/dim yellow]")

        console.print("[blink bright_blue]>>> Server running... Press Ctrl+C to stop[/blink bright_blue]")
        console.print("")

        # Start serving
        server.serve_forever()

    except KeyboardInterrupt:
        show_server_shutdown()
    except OSError as e:
        if e.errno == 48:  # Address already in use
            show_server_error(directory, f"Port {port} is already in use")
        else:
            show_server_error(directory, str(e))
    except Exception as e:
        show_server_error(directory, str(e))
    finally:
        # Restore original directory
        os.chdir(original_dir)
