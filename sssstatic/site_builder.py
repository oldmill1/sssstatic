# sssstatic/site_builder.py
"""
Builder module for SSSStatic - orchestrates the site build process
"""

import yaml
from pathlib import Path
from .display import console, show_critical_error
from .templates import generate_site_html
from .yaml_to_html import convert_to_html


def load_config(config_path):
    """Load and parse the _config.yml file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        show_critical_error("Config file not found", f"Could not find {config_path}")
        return None
    except yaml.YAMLError as e:
        show_critical_error("Invalid YAML syntax", str(e))
        return None


def copy_assets():
    """Copy assets folder to _site if it exists."""
    import shutil

    assets_src = Path("assets")
    if assets_src.exists() and assets_src.is_dir():
        assets_dest = Path("_site") / "assets"
        if assets_dest.exists():
            shutil.rmtree(assets_dest)
        shutil.copytree(assets_src, assets_dest)
        console.print("[bright_blue]>>> Copied assets folder[/bright_blue]")
        return True
    return False


def build_site():
    """Main build function - reads config and generates HTML."""
    config_path = Path("_config.yml")

    if not config_path.exists():
        show_critical_error("No config found", "Run this command in a project directory with _config.yml")
        return False

    console.print("[bright_blue]>>> Loading configuration...[/bright_blue]")
    config = load_config(config_path)
    if not config:
        return False

    console.print("[bright_blue]>>> Generating HTML...[/bright_blue]")

    # Generate content from all data except system tags and reserved fields
    content_data = {k: v for k, v in config.items()
                    if not k.startswith('_') and k not in ['site_name', 'theme']}
    content_html = convert_to_html(content_data)

    # Create output directory
    output_dir = Path("_site")
    output_dir.mkdir(exist_ok=True)

    # Copy assets folder if it exists
    copy_assets()

    # Generate complete HTML using template
    html = generate_site_html(config, content_html)

    # Write HTML file
    output_file = output_dir / "index.html"
    output_file.write_text(html, encoding='utf-8')

    console.print(f"[bold bright_green]✓ Site built successfully![/bold bright_green]")
    console.print(f"[dim]>>> Output: {output_file.absolute()}[/dim]")

    return True
