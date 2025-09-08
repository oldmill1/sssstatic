# sssstatic/deploy.py
"""
Deployment module for SSSStatic - handles cross-project deployment workflows
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
from rich.console import Console

console = Console()


def show_deploy_header(source_dir, target_dir):
    """Display deployment start message."""
    console.print("")
    console.print("[bold bright_green]╔════════════════════════════════════════════╗[/bold bright_green]")
    console.print("[bold bright_green]║[/bold bright_green] [bold bright_yellow]🚀 SSSStatic DEPLOYMENT STARTED! 🚀[/bold bright_yellow] [bold bright_green]║[/bold bright_green]")
    console.print("[bold bright_green]╚════════════════════════════════════════════╝[/bold bright_green]")
    console.print("")
    console.print(f"[bold bright_cyan]╭─[ DEPLOYMENT INFO ]─────────────────────╮[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Source:[/bold bright_white] [bright_yellow]{source_dir}[/bright_yellow]")
    console.print(f"[bold bright_cyan]│[/bold bright_cyan] [bold bright_white]Target:[/bold bright_white] [bright_yellow]{target_dir}[/bright_yellow]")
    console.print(f"[bold bright_cyan]╰─────────────────────────────────────────╯[/bold bright_cyan]")
    console.print("")


def show_deploy_step(step_name, step_number, total_steps):
    """Display deployment step progress."""
    console.print(f"[bold bright_blue]>>> Step {step_number}/{total_steps}: {step_name}[/bold bright_blue]")


def show_deploy_success():
    """Display deployment success message."""
    console.print("")
    console.print("[bold bright_green]╔════════════════════════════════════════════╗[/bold bright_green]")
    console.print("[bold bright_green]║[/bold bright_green] [bold bright_yellow]✅ DEPLOYMENT COMPLETE! ✅[/bold bright_yellow] [bold bright_green]║[/bold bright_green]")
    console.print("[bold bright_green]╚════════════════════════════════════════════╝[/bold bright_green]")
    console.print("[dim bright_blue]>>> Site successfully deployed and committed![/dim bright_blue]")
    console.print("")


def show_deploy_error(error_msg):
    """Display deployment error message."""
    console.print("")
    console.print("[bold red]╔══════════════════════════════════════════╗[/bold red]")
    console.print("[bold red]║[/bold red] [bold bright_white]🔥 DEPLOYMENT FAILED! 🔥[/bold bright_white] [bold red]║[/bold red]")
    console.print("[bold red]╚══════════════════════════════════════════╝[/bold red]")
    console.print("[bold red]>>> ERROR:[/bold red]", end=" ")
    console.print(error_msg, markup=False)
    console.print("[bold red]>>> MISSION ABORTED[/bold red]")
    console.print("")


def copy_site_to_target(source_dir, target_dir):
    """Copy the built site from source to target directory."""
    source_path = Path(source_dir) / "_site"
    target_path = Path(target_dir)
    
    if not source_path.exists():
        raise FileNotFoundError(f"Source directory '{source_path}' not found. Run 'sssstatic build' first.")
    
    if not target_path.exists():
        raise FileNotFoundError(f"Target directory '{target_path}' not found.")
    
    # Files/directories to preserve (don't overwrite)
    preserve_items = {'.git', '.github', 'CNAME', '.gitignore', 'README.md', 'package.json', 'requirements.txt'}
    
    # Remove only website-related content, preserve other files
    for item in target_path.iterdir():
        if item.name not in preserve_items:
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
    
    # Copy all content from _site to target directory
    for item in source_path.iterdir():
        if item.is_file():
            shutil.copy2(item, target_path)
        elif item.is_dir():
            shutil.copytree(item, target_path / item.name)
    
    console.print(f"[bright_green]>>> Copied site to {target_path}[/bright_green]")
    return True


def run_cmtmsg_deploy(target_dir):
    """Run cmtmsg --confirm in the target directory."""
    original_dir = os.getcwd()
    
    try:
        # Change to target directory
        os.chdir(target_dir)
        
        # Check if this is a git repository
        git_dir = Path(".git")
        if not git_dir.exists():
            raise RuntimeError("Target directory is not a git repository. Please initialize a git repository first or use a different target directory.")
        
        console.print("[bright_green]>>> Using existing git repository[/bright_green]")
        
        # Run cmtmsg --confirm
        result = subprocess.run(
            ["cmtmsg", "--confirm"],
            capture_output=True,
            text=True,
            check=True
        )
        
        console.print("[bright_green]>>> Site deployed with cmtmsg![/bright_green]")
        if result.stdout:
            console.print(f"[dim]>>> {result.stdout.strip()}[/dim]")
        
        return True
        
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"cmtmsg deployment failed: {e.stderr}")
    except FileNotFoundError:
        raise RuntimeError("cmtmsg command not found. Make sure it's installed and in your PATH.")
    finally:
        # Restore original directory
        os.chdir(original_dir)


def deploy_site(target_dir, skip_build=False):
    """Main deployment function - builds site and deploys to target directory."""
    source_dir = os.getcwd()
    target_path = Path(target_dir).resolve()
    
    show_deploy_header(source_dir, target_path)
    
    try:
        # Step 1: Build site (unless skipped)
        if not skip_build:
            show_deploy_step("Building site", 1, 3)
            from .site_builder import build_site
            if not build_site():
                raise RuntimeError("Site build failed")
        
        # Step 2: Copy site to target directory
        show_deploy_step("Copying site to target directory", 2 if not skip_build else 1, 3 if not skip_build else 2)
        copy_site_to_target(source_dir, target_path)
        
        # Step 3: Deploy with cmtmsg
        show_deploy_step("Deploying with cmtmsg", 3 if not skip_build else 2, 3 if not skip_build else 2)
        run_cmtmsg_deploy(target_path)
        
        show_deploy_success()
        return True
        
    except Exception as e:
        show_deploy_error(str(e))
        return False
