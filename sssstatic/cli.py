# sssstatic/cli.py
"""
CLI module for SSSSStatic - handles command line interface and argument parsing
"""

import argparse
from .project import create_new_project
from .display import show_main_header


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
        show_main_header()
    else:
        parser.print_help()
