# sssstatic/cli.py
"""
CLI module for SSSStatic - handles command line interface and argument parsing
"""

import argparse
from .project_creator import create_new_project
from .dev_server import start_dev_server
from .dev_server_enhanced import start_enhanced_dev_server
from .site_builder import build_site
from .deploy import deploy_site
from .export import export_site
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

    # Dev command (build + serve + watch)
    dev_parser = subparsers.add_parser("dev", help="Build site, start development server with auto-rebuild")
    dev_parser.add_argument("--port", "-p", type=int, default=8000, help="Port to serve on (default: 8000)")
    dev_parser.add_argument("--enhanced", "-e", action="store_true", help="Use enhanced dev server with file watching (default)")
    dev_parser.add_argument("--simple", "-s", action="store_true", help="Use simple dev server without file watching")

    # Deploy command (build + copy + cmtmsg)
    deploy_parser = subparsers.add_parser("deploy", help="Build site and deploy to target directory with cmtmsg")
    deploy_parser.add_argument("target_dir", help="Target directory to deploy to")
    deploy_parser.add_argument("--skip-build", action="store_true", help="Skip building and only copy existing _site")

    # Export command (build + copy to specified path)
    export_parser = subparsers.add_parser("export", help="Build site and export to specified directory")
    export_parser.add_argument("--path", "-p", required=True, help="Full path where to export the site")
    export_parser.add_argument("--skip-build", action="store_true", help="Skip building and only copy existing _site")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "create" and args.type == "new":
        create_new_project()
    elif args.command == "build":
        build_site()
    elif args.command == "serve":
        start_dev_server(args.directory, args.port)
    elif args.command == "dev":
        # Use enhanced dev server by default, unless --simple is specified
        if args.simple:
            # Build first, then serve if build succeeds
            if build_site():
                start_dev_server("_site", args.port)
        else:
            # Use enhanced dev server with file watching
            start_enhanced_dev_server(args.port)
    elif args.command == "deploy":
        deploy_site(args.target_dir, args.skip_build)
    elif args.command == "export":
        export_site(args.path, args.skip_build)
    elif args.command is None:
        show_main_header()
    else:
        parser.print_help()
