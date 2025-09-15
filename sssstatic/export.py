# sssstatic/export.py
"""
Export module for SSSStatic - handles exporting built site to specified directory
"""

import shutil
from pathlib import Path
from .display import console, show_critical_error
from .site_builder import build_site


def export_site(export_path, skip_build=False):
    """
    Export the built site to the specified directory.
    
    Args:
        export_path (str): Full path where to export the site
        skip_build (bool): Whether to skip building and only copy existing _site
    """
    # Convert to Path object
    export_path = Path(export_path)
    
    # Build the site first (unless skip_build is True)
    if not skip_build:
        console.print("[bright_blue]>>> Building site...[/bright_blue]")
        if not build_site():
            show_critical_error("Build failed", "Could not build the site for export")
            return False
    else:
        # Check if _site exists
        site_dir = Path("_site")
        if not site_dir.exists():
            show_critical_error("No site found", "No _site directory found. Run build first or remove --skip-build flag")
            return False
    
    # Check if _site directory exists
    site_dir = Path("_site")
    if not site_dir.exists():
        show_critical_error("No site found", "No _site directory found. Run build first.")
        return False
    
    console.print(f"[bright_blue]>>> Exporting site to: {export_path.absolute()}[/bright_blue]")
    
    try:
        # Create the export directory if it doesn't exist
        export_path.mkdir(parents=True, exist_ok=True)
        
        # Copy all files from _site to export_path
        for item in site_dir.iterdir():
            if item.is_file():
                # Copy individual files
                dest_file = export_path / item.name
                shutil.copy2(item, dest_file)
                console.print(f"[bright_blue]>>> Copied: {item.name}[/bright_blue]")
            elif item.is_dir():
                # Copy directories recursively
                dest_dir = export_path / item.name
                if dest_dir.exists():
                    # Remove existing directory and replace it
                    shutil.rmtree(dest_dir)
                    console.print(f"[bright_blue]>>> Replaced directory: {item.name}[/bright_blue]")
                else:
                    console.print(f"[bright_blue]>>> Copied directory: {item.name}[/bright_blue]")
                shutil.copytree(item, dest_dir)
        
        console.print(f"[bold bright_green]✓ Site exported successfully![/bold bright_green]")
        console.print(f"[dim]>>> Export location: {export_path.absolute()}[/dim]")
        
        # Show what was exported
        exported_files = list(export_path.rglob("*"))
        file_count = len([f for f in exported_files if f.is_file()])
        dir_count = len([d for d in exported_files if d.is_dir()])
        
        console.print(f"[dim]>>> Exported {file_count} files and {dir_count} directories[/dim]")
        
        return True
        
    except PermissionError as e:
        show_critical_error("Permission denied", f"Cannot write to {export_path}: {e}")
        return False
    except Exception as e:
        show_critical_error("Export failed", f"Unexpected error during export: {e}")
        return False
