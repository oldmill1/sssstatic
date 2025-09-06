#!/usr/bin/env python3
# sssstatic.py
"""
SSSSStatic - A Simple Static Site Generator
"""

import argparse
import os
import sys
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def create_new_project():
    """Create a new static site project with wizard."""

    # Epic ASCII art header
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

    # Get project name with dramatic styling
    project_name = Prompt.ask(
        "[bold bright_cyan]╭─[/bold bright_cyan][bold bright_white] PROJECT CODENAME[/bold bright_white][bold bright_cyan] ──────────────────────╮\n│[/bold bright_cyan] [bold bright_yellow]>>>[/bold bright_yellow]")
    if not project_name.strip():
        console.print("[bold red]╭─[ CRITICAL ERROR ]─────────────────────╮[/bold red]")
        console.print("[bold red]│ INVALID CODENAME - ABORT SEQUENCE     │[/bold red]")
        console.print("[bold red]╰────────────────────────────────────────╯[/bold red]")
        return

    # Get project location
    current_dir = os.getcwd()
    console.print("")
    console.print(f"[dim bright_blue]>>> Default deployment zone: [bold]{current_dir}[/bold][/dim bright_blue]")
    project_location = Prompt.ask(
        "[bold bright_cyan]╭─[/bold bright_cyan][bold bright_white] TARGET COORDINATES[/bold bright_white][bold bright_cyan] ─────────────────╮\n│[/bold bright_cyan] [bold bright_yellow]>>>[/bold bright_yellow]",
        default=current_dir
    )

    # Create full project path
    project_path = Path(project_location) / project_name

    # Check if directory already exists
    if project_path.exists():
        console.print("")
        console.print("[bold red]╭─[ DEPLOYMENT CONFLICT ]────────────────╮[/bold red]")
        console.print(f"[bold red]│ Zone '{project_path}' already occupied  │[/bold red]")
        console.print("[bold red]│ MISSION ABORT - RETREAT IMMEDIATELY   │[/bold red]")
        console.print("[bold red]╰─────────────────────────────────────────╯[/bold red]")
        return

    try:
        console.print("")
        console.print("[bold bright_yellow]╔════════════════════════════════════════╗[/bold bright_yellow]")
        console.print(
            f"[bold bright_yellow]║[/bold bright_yellow] [bold bright_white]DEPLOYING PROJECT '{project_name}'...[/bold bright_white] [bold bright_yellow]║[/bold bright_yellow]")
        console.print("[bold bright_yellow]╚════════════════════════════════════════╝[/bold bright_yellow]")
        console.print("")

        import time

        # Create main project directory
        console.print("[bright_blue]>>> [/bright_blue][bright_white]Establishing command structure...[/bright_white]",
                      end="")
        time.sleep(0.3)
        project_path.mkdir(parents=True, exist_ok=True)
        console.print(" [bold bright_green]✓ COMPLETE[/bold bright_green]")

        # Create www directory
        console.print(
            "[bright_blue]>>> [/bright_blue][bright_white]Initializing web interface module...[/bright_white]", end="")
        time.sleep(0.3)
        www_dir = project_path / "www"
        www_dir.mkdir(exist_ok=True)
        console.print(" [bold bright_green]✓ COMPLETE[/bold bright_green]")

        # Create _config.yml
        config_content = f"""# SSSSStatic Configuration
site_name: "{project_name}"
description: "A static site generated with SSSSStatic"
author: "Your Name"
url: ""

# Build settings
output_dir: "_site"
source_dir: "www"

# Theme settings
theme:
  name: "default"
"""

        console.print("[bright_blue]>>> [/bright_blue][bright_white]Deploying configuration matrix...[/bright_white]",
                      end="")
        time.sleep(0.3)
        config_file = project_path / "_config.yml"
        config_file.write_text(config_content)
        console.print(" [bold bright_green]✓ COMPLETE[/bold bright_green]")

        # Create index.html
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name} - Generated by SSSSStatic</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .container {{
            background: white;
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            text-align: center;
            max-width: 600px;
            margin: 2rem;
        }}
        
        h1 {{
            color: #764ba2;
            margin-bottom: 1rem;
            font-size: 2.5rem;
        }}
        
        .subtitle {{
            color: #666;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }}
        
        .badge {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            margin-top: 1rem;
        }}
        
        .footer {{
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid #eee;
            color: #999;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to {project_name}!</h1>
        <p class="subtitle">Your static site has been successfully generated</p>
        <p>This site was created using <strong>SSSSStatic</strong>, a simple static site generator.</p>
        <div class="badge">Generated by SSSSStatic 🚀</div>
        <div class="footer">
            <p>Check the browser console for a hello message!</p>
            <p>Edit <code>www/index.html</code> to customize this page.</p>
        </div>
    </div>
    
    <script>
        console.log('🎉 Hello World from SSSSStatic!');
        console.log('Your static site is ready to be customized.');
        console.log('Project: {project_name}');
        console.log('Generated at:', new Date().toISOString());
    </script>
</body>
</html>"""

        console.print("[bright_blue]>>> [/bright_blue][bright_white]Generating primary interface...[/bright_white]",
                      end="")
        time.sleep(0.3)
        index_file = www_dir / "index.html"
        index_file.write_text(html_content)
        console.print(" [bold bright_green]✓ COMPLETE[/bold bright_green]")

        # Epic success message
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
            "[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Modify www/index.html to customize[/dim]")
        console.print(
            "[bold bright_red]│[/bold bright_red] [bright_yellow]>>>[/bright_yellow] [dim]Execute 'sssstatic build' to compile[/dim]")
        console.print("[bold bright_red]╰─────────────────────────────────────────╯[/bold bright_red]")
        console.print("")
        console.print("[blink bright_blue]>>> SYSTEM STANDING BY FOR FURTHER ORDERS...[/blink bright_blue]")

    except Exception as e:
        console.print("")
        console.print("[bold red]╔══════════════════════════════════════════╗[/bold red]")
        console.print(
            "[bold red]║[/bold red] [bold bright_white]🔥 CRITICAL SYSTEM FAILURE! 🔥[/bold bright_white] [bold red]║[/bold red]")
        console.print("[bold red]╚══════════════════════════════════════════╝[/bold red]")
        console.print(f"[bold red]>>> ERROR DETAILS: {e}[/bold red]")
        console.print("[bold red]>>> MISSION FAILED - EMERGENCY SHUTDOWN[/bold red]")


def main():
    """Main entry point for the static site generator."""
    parser = argparse.ArgumentParser(description="SSSSStatic - A Simple Static Site Generator")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new project")
    create_parser.add_argument("type", choices=["new"], help="Type of project to create")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "create" and args.type == "new":
        create_new_project()
    elif args.command is None:
        console.print("")
        console.print("[bold bright_green]╔════════════════════════════════════╗[/bold bright_green]")
        console.print(
            "[bold bright_green]║[/bold bright_green] [bold bright_cyan]🐍 SSSSStatic ONLINE 🐍[/bold bright_cyan] [bold bright_green]║[/bold bright_green]")
        console.print("[bold bright_green]╚════════════════════════════════════╝[/bold bright_green]")
        console.print("[dim bright_blue]>>> Static site generator ready for deployment[/dim bright_blue]")
        console.print("[dim]>>> Execute 'sssstatic create new' to begin mission[/dim]")
        console.print("")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
