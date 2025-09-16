# sssstatic/site_builder.py
"""
Builder module for SSSStatic - orchestrates the site build process
"""

import yaml
from pathlib import Path
from .display import console, show_critical_error
from .templates import generate_site_html
from .yaml_to_html import convert_to_html
from .theme_styles import get_global_css


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
    """Copy assets folder to _site if it exists, and copy stickers from sssstatic/stickers."""
    import shutil

    # Create assets directory in _site
    assets_dest = Path("_site") / "assets"
    assets_dest.mkdir(exist_ok=True)
    
    # Copy assets folder if it exists
    assets_src = Path("assets")
    if assets_src.exists() and assets_src.is_dir():
        # Copy all files from assets to _site/assets
        for item in assets_src.iterdir():
            if item.is_file():
                shutil.copy2(item, assets_dest / item.name)
            elif item.is_dir():
                dest_dir = assets_dest / item.name
                if dest_dir.exists():
                    shutil.rmtree(dest_dir)
                shutil.copytree(item, dest_dir)
        console.print("[bright_blue]>>> Copied assets folder[/bright_blue]")
    
    # Copy stickers from sssstatic/stickers to assets/stickers
    stickers_src = Path("sssstatic") / "stickers"
    stickers_dest = assets_dest / "stickers"
    
    if stickers_src.exists() and stickers_src.is_dir():
        stickers_dest.mkdir(exist_ok=True)
        
        # Copy all PNG files from stickers source to assets/stickers
        for sticker_file in stickers_src.glob("*.png"):
            # Use the filename without extension as the sticker name
            sticker_name = sticker_file.stem
            dest_file = stickers_dest / f"{sticker_name}.png"
            shutil.copy2(sticker_file, dest_file)
            console.print(f"[bright_blue]>>> Copied sticker: {sticker_name}.png[/bright_blue]")
    
    return True


def generate_css_file(config, dev_mode=False):
    """Generate styles.css file in assets folder."""
    # Create assets directory in _site
    assets_dir = Path("_site") / "assets"
    assets_dir.mkdir(exist_ok=True)

    # In dev mode, reload modules to pick up changes
    if dev_mode:
        import importlib
        import sys
        
        # Reload all style and component modules
        modules_to_reload = [
            # Style modules
            'sssstatic.styles.sinema',
            'sssstatic.styles.cards',
            'sssstatic.styles.widescreen_spotlight',
            'sssstatic.styles.pinterest',
            'sssstatic.styles.showcase',
            'sssstatic.styles.slick',
            'sssstatic.styles.sizzle',
            'sssstatic.styles.sly',
            'sssstatic.styles.map',
            'sssstatic.styles.topbar',
            'sssstatic.styles.type',
            'sssstatic.theme_styles',
            # Component modules
            'sssstatic.components.sinema',
            'sssstatic.components.cards',
            'sssstatic.components.widescreen_spotlight',
            'sssstatic.components.pinterest',
            'sssstatic.components.showcase',
            'sssstatic.components.slick',
            'sssstatic.components.sizzle',
            'sssstatic.components.sly',
            'sssstatic.components.map',
            'sssstatic.components.row',
            'sssstatic.components.column',
            'sssstatic.components.component',
            'sssstatic.components.page_header',
            'sssstatic.components.image',
            'sssstatic.components.topbar',
            'sssstatic.components.stickers',
            'sssstatic.styles.stickers',
            'sssstatic.templates'
        ]
        
        for module_name in modules_to_reload:
            try:
                if module_name in sys.modules:
                    importlib.reload(sys.modules[module_name])
                    console.print(f"[dim]>>> Reloaded module: {module_name}[/dim]")
                else:
                    # Import the module first, then reload it
                    __import__(module_name)
                    importlib.reload(sys.modules[module_name])
                    console.print(f"[dim]>>> Imported and reloaded module: {module_name}[/dim]")
            except Exception as e:
                console.print(f"[dim red]>>> Failed to reload {module_name}: {e}[/dim red]")

    # Get global CSS with config for conditional styling
    css_content = get_global_css(config)

    # Write CSS file
    css_file = assets_dir / "styles.css"
    css_file.write_text(css_content, encoding='utf-8')

    console.print("[bright_blue]>>> Generated styles.css[/bright_blue]")
    return True


def extract_pages(config):
    """Extract _page components from config and return them as separate page configs."""
    pages = []
    
    # Look for _page entries in the config
    for key, value in config.items():
        if key == '_page':
            if isinstance(value, list):
                # Multiple pages
                for page_config in value:
                    if isinstance(page_config, dict) and '_name' in page_config:
                        pages.append(page_config)
            elif isinstance(value, dict) and '_name' in value:
                # Single page
                pages.append(value)
    
    return pages


def extract_anchor_links(config):
    """Extract _anchorLinks components from config and return them as anchor link configs."""
    anchor_links = []
    
    # Look for _anchorLinks entries in the config
    for key, value in config.items():
        if key == '_anchorLinks':
            if isinstance(value, list):
                # Multiple anchor links
                for link_config in value:
                    if isinstance(link_config, dict) and 'name' in link_config and 'scrollTo' in link_config:
                        anchor_links.append(link_config)
            elif isinstance(value, dict) and 'name' in value and 'scrollTo' in value:
                # Single anchor link
                anchor_links.append(value)
    
    return anchor_links


def generate_page_html(page_config, base_config):
    """Generate HTML for a specific page using only its own config."""
    from .templates import generate_site_html
    from .yaml_to_html import convert_to_html
    
    # Create a minimal config for this page - inherit site config and _page for navigation
    page_merged_config = {
        'site': base_config.get('site', {}),
        '_page': base_config.get('_page', [])  # Include _page for navigation generation
    }
    # Add _topbar if it exists in base config
    if '_topbar' in base_config:
        page_merged_config['_topbar'] = base_config['_topbar']
    # Add the page's own configuration
    page_merged_config.update(page_config)
    
    # Generate content from page data (excluding system tags)
    # Skip content generation for pages too - only process underscore components
    content_html = ""
    
    # Generate the complete HTML for this page
    return generate_site_html(page_merged_config, content_html)


def build_site(dev_mode=False):
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

    # Extract pages from config
    pages = extract_pages(config)
    
    # Generate content from all data except system tags, reserved fields, and _page
    # Only process known content components - ignore any non-standard components
    content_data = {k: v for k, v in config.items()
                    if not k.startswith('_') and k not in ['site'] and k != '_page'}
    
    # For now, we'll skip content generation entirely since we only want underscore components
    # This ensures non-standard components are completely ignored
    content_html = ""

    # Create output directory
    output_dir = Path("_site")
    output_dir.mkdir(exist_ok=True)

    # Copy assets folder if it exists (this creates _site/assets)
    copy_assets()

    # Generate CSS file in assets folder
    generate_css_file(config, dev_mode)

    # Generate main index.html
    # Create a config that includes all necessary components for template generation
    template_config = dict(config)  # Start with full config
    
    html = generate_site_html(template_config, content_html, dev_mode)
    output_file = output_dir / "index.html"
    output_file.write_text(html, encoding='utf-8')
    console.print(f"[bright_blue]>>> Generated index.html[/bright_blue]")

    # Generate individual pages
    for page in pages:
        page_name = page.get('_name', 'untitled').lower().replace(' ', '_')
        page_html = generate_page_html(page, config)
        page_file = output_dir / f"{page_name}.html"
        page_file.write_text(page_html, encoding='utf-8')
        console.print(f"[bright_blue]>>> Generated {page_name}.html[/bright_blue]")

    console.print(f"[bold bright_green]✓ Site built successfully![/bold bright_green]")
    console.print(f"[dim]>>> Output: {output_dir.absolute()}[/dim]")
    console.print(f"[dim]>>> Styles: {output_dir / 'assets' / 'styles.css'}[/dim]")

    return True


