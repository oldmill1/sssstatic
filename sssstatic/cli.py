# sssstatic/cli.py
"""
CLI module for SSSStatic - handles command line interface and argument parsing
"""

import argparse
from .project_creator import create_new_project
from .dev_server import start_dev_server
from .site_builder import build_site
from .deploy import deploy_site
from .display import show_main_header


def main():
    """Main entry point for the static site generator."""
    parser = argparse.ArgumentParser(description="SSSStatic - A Simple Static Site Generator")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new project")
    create_parser.add_argument("type", choices=["new"], help="Type of project to create")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build the static site")

    # Serve command
    serve_parser = subparsers.add_parser("serve", help="Start development server")
    serve_parser.add_argument("--port", "-p", type=int, default=8000, help="Port to serve on (default: 8000)")
    serve_parser.add_argument("--directory", "-d", default="_site", help="Directory to serve (default: _site)")

    # Dev command (build + serve)
    dev_parser = subparsers.add_parser("dev", help="Build site and start development server")
    dev_parser.add_argument("--port", "-p", type=int, default=8000, help="Port to serve on (default: 8000)")
    dev_parser.add_argument("--directory", "-d", default="_site", help="Directory to serve (default: _site)")

    # Deploy command (build + copy + cmtmsg)
    deploy_parser = subparsers.add_parser("deploy", help="Build site and deploy to target directory with cmtmsg")
    deploy_parser.add_argument("target_dir", help="Target directory to deploy to")
    deploy_parser.add_argument("--skip-build", action="store_true", help="Skip building and only copy existing _site")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "create" and args.type == "new":
        create_new_project()
    elif args.command == "build":
        build_site()
    elif args.command == "serve":
        start_dev_server(args.directory, args.port)
    elif args.command == "dev":
        # Build first, then serve if build succeeds
        if build_site():
            start_dev_server(args.directory, args.port)
    elif args.command == "deploy":
        deploy_site(args.target_dir, args.skip_build)
    elif args.command is None:
        show_main_header()
    else:
        parser.print_help()
