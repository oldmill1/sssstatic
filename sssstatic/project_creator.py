# sssstatic/project.py
"""
Project module for SSSStatic - handles project creation and file operations
"""

import os
from pathlib import Path
from rich.prompt import Prompt

from .display import (
    show_epic_header, show_default_location, show_directory_conflict,
    show_deployment_header, show_progress_step, show_success_message,
    show_critical_error, show_error, console
)
from .templates import get_config_template


def get_project_details():
    """Get project name and location from user input."""
    # Get project name with dramatic styling
    project_name = Prompt.ask(
        "[bold bright_cyan]╭─[/bold bright_cyan][bold bright_white] PROJECT CODENAME[/bold bright_white][bold bright_cyan] ──────────────────────╮\n│[/bold bright_cyan] [bold bright_yellow]>>>[/bold bright_yellow]")

    if not project_name.strip():
        show_error("CRITICAL ERROR", "INVALID CODENAME - ABORT SEQUENCE")
        return None, None

    # Get project location
    current_dir = os.getcwd()
    show_default_location(current_dir)
    project_location = Prompt.ask(
        "[bold bright_cyan]╭─[/bold bright_cyan][bold bright_white] TARGET COORDINATES[/bold bright_white][bold bright_cyan] ─────────────────╮\n│[/bold bright_cyan] [bold bright_yellow]>>>[/bold bright_yellow]",
        default=current_dir
    )

    return project_name, project_location


def create_project_structure(project_path, project_name):
    """Create the project directory structure and files."""
    try:
        show_deployment_header(project_name)

        # Create main project directory
        show_progress_step("Establishing command structure")
        project_path.mkdir(parents=True, exist_ok=True)

        # Create _config.yml
        show_progress_step("Deploying configuration matrix")
        config_content = get_config_template(project_name)
        config_file = project_path / "_config.yml"
        config_file.write_text(config_content)

        return True

    except Exception as e:
        show_critical_error(str(e), "MISSION FAILED - EMERGENCY SHUTDOWN")
        return False


def create_new_project():
    """Create a new static site project with wizard."""
    # Show epic header
    show_epic_header()

    # Get project details
    project_name, project_location = get_project_details()
    if not project_name or not project_location:
        return

    # Create full project path
    project_path = Path(project_location) / project_name

    # Check if directory already exists
    if project_path.exists():
        show_directory_conflict(project_path)
        return

    # Create project structure
    if create_project_structure(project_path, project_name):
        show_success_message(project_name, project_path)
