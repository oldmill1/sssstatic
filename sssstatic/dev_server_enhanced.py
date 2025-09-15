# sssstatic/dev_server_enhanced.py
"""
Enhanced Development Server module for SSSStatic - combines building, serving, and file watching
"""

import os
import sys
import threading
import time
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rich.console import Console

from .site_builder import build_site
from .display import show_critical_error

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
        
        # Add ETag with timestamp for CSS files to force refresh
        if self.path.endswith('.css'):
            import time
            etag = f'"{int(time.time())}"'
            self.send_header('ETag', etag)
        
        super().end_headers()


class DevBuildHandler(FileSystemEventHandler):
    """Handler for file system events that triggers builds during development."""
    
    def __init__(self, config_path, site_dir):
        self.config_path = config_path
        self.site_dir = site_dir
        self.last_build_time = 0
        self.build_cooldown = 1  # seconds to wait between builds
        self.is_building = False
        
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
            
        # Check if the file is a Python file, YAML file, or config file
        file_path = Path(event.src_path)
        console.print(f"[dim]>>> File modified: {file_path}[/dim]")
        
        if file_path.suffix not in ['.py', '.yml', '.yaml'] and file_path.name != '_config.yml':
            console.print(f"[dim]>>> Ignoring file (not watched): {file_path}[/dim]")
            return
            
        # Avoid rapid successive builds
        current_time = time.time()
        if current_time - self.last_build_time < self.build_cooldown or self.is_building:
            console.print(f"[dim]>>> Skipping build (cooldown or building): {file_path}[/dim]")
            return
            
        console.print(f"[dim]>>> Triggering build for: {file_path}[/dim]")
        self.last_build_time = current_time
        self._trigger_build()
    
    def on_created(self, event):
        """Handle file creation events."""
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        if file_path.suffix not in ['.py', '.yml', '.yaml'] and file_path.name != '_config.yml':
            return
            
        current_time = time.time()
        if current_time - self.last_build_time < self.build_cooldown or self.is_building:
            return
            
        self.last_build_time = current_time
        self._trigger_build()
    
    def _trigger_build(self):
        """Execute the site build."""
        if self.is_building:
            return
            
        self.is_building = True
        console.print(f"\n[bold yellow]🔄 File change detected! Rebuilding site...[/bold yellow]")
        
        try:
            # Change to the directory containing the config
            original_dir = os.getcwd()
            config_dir = self.config_path.parent
            os.chdir(config_dir)
            
            # Check if _site directory exists before build
            site_dir = config_dir / "_site"
            console.print(f"[dim]>>> Building from: {config_dir}[/dim]")
            console.print(f"[dim]>>> Site directory: {site_dir}[/dim]")
            
            # Build the site in dev mode
            success = build_site(dev_mode=True)
            
            if success:
                console.print(f"[bold green]✅ Site rebuilt successfully![/bold green]")
                # Check if files were actually updated
                css_file = site_dir / "assets" / "styles.css"
                html_file = site_dir / "index.html"
                if css_file.exists():
                    css_mtime = css_file.stat().st_mtime
                    console.print(f"[dim]>>> CSS file updated: {css_mtime}[/dim]")
                if html_file.exists():
                    html_mtime = html_file.stat().st_mtime
                    console.print(f"[dim]>>> HTML file updated: {html_mtime}[/dim]")
            else:
                console.print(f"[bold red]❌ Site rebuild failed![/bold red]")
                
        except Exception as e:
            console.print(f"[bold red]❌ Unexpected error during rebuild: {e}[/bold red]")
            import traceback
            console.print(f"[dim red]{traceback.format_exc()}[/dim red]")
        finally:
            # Restore original directory
            os.chdir(original_dir)
            self.is_building = False


def show_dev_server_header(config_path, site_dir, port):
    """Display enhanced dev server startup message."""
    from .display import show_epic_header
    
    # Use the epic ASCII art header
    show_epic_header()
    
    console.print(f"[bold bright_cyan]╭─[ DEV SERVER STATUS ]─────────────────────────────────╮[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Config:[/bold bright_white] [bright_yellow]{config_path}[/bright_yellow]")
    console.print(f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Site Directory:[/bold bright_white] [bright_yellow]{site_dir}[/bright_yellow]")
    console.print(f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Port:[/bold bright_white] [bright_yellow]{port}[/bright_yellow]")
    console.print(f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]URL:[/bold bright_white] [bright_green]http://localhost:{port}[/bright_green]")
    console.print(f"[bold bright_cyan]╰─────────────────────────────────────────────────────────╯[/bold bright_cyan]")
    console.print("")
    console.print("[bold bright_blue]╭─[ WATCHING ]───────────────────────────────────────────╮[/bold bright_blue]")
    console.print("[bold bright_blue]│[/bold bright_blue] [bright_yellow]>>>[/bright_yellow] [bright_white]Config file changes[/bright_white]")
    console.print("[bold bright_blue]│[/bold bright_blue] [bright_yellow]>>>[/bright_yellow] [bright_white]SSSStatic source files (.py)[/bright_white]")
    console.print("[bold bright_blue]│[/bold bright_blue] [bright_yellow]>>>[/bright_yellow] [bright_white]YAML configuration files[/bright_white]")
    console.print("[bold bright_blue]╰─────────────────────────────────────────────────────────╯[/bold bright_blue]")
    console.print("")
    console.print("[bold bright_red]╭─[ CONTROL COMMANDS ]───────────────────────────────────╮[/bold bright_red]")
    console.print("[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [bright_white]Press Ctrl+C to shutdown[/bright_white]")
    console.print("[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Server will auto-open in browser[/dim]")
    console.print("[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Auto-rebuild on file changes[/dim]")
    console.print("[bold bright_red]╰─────────────────────────────────────────────────────────╯[/bold bright_red]")
    console.print("")


def show_dev_server_shutdown():
    """Display enhanced dev server shutdown message."""
    console.print("")
    console.print("[bold bright_red]╔══════════════════════════════════════════════════════════╗[/bold bright_red]")
    console.print("[bold bright_red]║[/bold bright_red] [bold bright_white]🛑 ENHANCED DEV SERVER SHUTDOWN COMPLETE 🛑[/bold bright_white] [bold bright_red]║[/bold bright_red]")
    console.print("[bold bright_red]╚══════════════════════════════════════════════════════════╝[/bold bright_red]")
    console.print("[dim bright_blue]>>> Mission complete - standing by...[/dim bright_blue]")
    console.print("")


def find_config_in_sssstatic_root():
    """Find _config.yml in the sssstatic root directory."""
    # Get the sssstatic package directory
    sssstatic_root = Path(__file__).parent.parent  # Go up from sssstatic/sssstatic to sssstatic/
    config_path = sssstatic_root / "_config.yml"
    
    if config_path.exists():
        return config_path
    
    return None


def start_enhanced_dev_server(port=8000):
    """Start the enhanced development server with file watching."""
    
    # First, try to find config in sssstatic root directory
    config_path = find_config_in_sssstatic_root()
    
    if not config_path:
        show_critical_error(
            "No config found", 
            "No _config.yml found in sssstatic root directory. Please create one for development."
        )
        return False
    
    console.print(f"[bright_blue]>>> Found config: {config_path}[/bright_blue]")
    
    # Build the site first
    console.print("[bright_blue]>>> Building site from config...[/bright_blue]")
    
    # Change to config directory for building
    original_dir = os.getcwd()
    config_dir = config_path.parent
    os.chdir(config_dir)
    
    try:
        if not build_site(dev_mode=True):
            show_critical_error("Build failed", "Could not build site from config")
            return False
    finally:
        os.chdir(original_dir)
    
    # Set up paths
    site_dir = config_dir / "_site"
    
    if not site_dir.exists():
        show_critical_error("Site directory not found", f"Expected site directory {site_dir} not found after build")
        return False
    
    # Set up file watcher
    console.print("[bright_blue]>>> Setting up file watcher...[/bright_blue]")
    
    # Watch both the config directory and the sssstatic source directory
    event_handler = DevBuildHandler(config_path, site_dir)
    observer = Observer()
    
    # Watch config directory for config changes
    observer.schedule(event_handler, str(config_dir), recursive=False)
    
    # Watch sssstatic source directory for source changes
    sssstatic_source_dir = Path(__file__).parent  # sssstatic/sssstatic/
    observer.schedule(event_handler, str(sssstatic_source_dir), recursive=True)
    
    observer.start()
    
    try:
        # Start HTTP server
        serve_path = site_dir
        os.chdir(serve_path)
        
        server = HTTPServer(('localhost', port), SSSStaticHandler)
        
        # Show startup message
        show_dev_server_header(config_path, site_dir, port)
        
        # Auto-open browser
        try:
            webbrowser.open(f'http://localhost:{port}')
            console.print("[bright_green]>>> Browser launched automatically![/bright_green]")
        except Exception:
            console.print("[dim yellow]>>> Could not auto-open browser[/dim yellow]")
        
        console.print("[blink bright_blue]>>> Server running with auto-rebuild... Press Ctrl+C to stop[/blink bright_blue]")
        console.print("")
        
        # Start serving in a separate thread
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()
        
        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            show_critical_error("Port in use", f"Port {port} is already in use")
        else:
            show_critical_error("Server error", str(e))
    except Exception as e:
        show_critical_error("Unexpected error", str(e))
    finally:
        # Cleanup
        observer.stop()
        observer.join()
        os.chdir(original_dir)
        show_dev_server_shutdown()
    
    return True
