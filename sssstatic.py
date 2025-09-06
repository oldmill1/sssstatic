#!/usr/bin/env python3
# sssstatic.py
"""
SSSSStatic - A Simple Static Site Generator
"""

from rich.console import Console

console = Console()


def main():
    """Main entry point for the static site generator."""
    console.print("Hello world from SSSSStatic!", style="bold green")
    console.print("Static site generator initialized successfully.", style="dim")


if __name__ == "__main__":
    main()
