# sssstatic/builder.py
"""
Builder module for SSSStatic - converts YAML config to HTML
"""

import yaml
from pathlib import Path
from .display import console, show_critical_error


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


def convert_to_html(data, key=None, in_list_item=False):
    """Recursively convert YAML data to HTML."""
    if isinstance(data, dict):
        html = ""
        for k, v in data.items():
            if k == "site_name":  # Skip the reserved site_name
                continue

            if in_list_item:
                # Inside a list item, make it more compact
                if isinstance(v, str):
                    if v.startswith(('http://', 'https://')):
                        html += f'<strong>{k.replace("_", " ").title()}:</strong> <a href="{v}">{v}</a><br>\n'
                    else:
                        html += f'<strong>{k.replace("_", " ").title()}:</strong> {v}<br>\n'
                else:
                    html += f'<strong>{k.replace("_", " ").title()}:</strong> {convert_to_html(v, k, in_list_item)}<br>\n'
            else:
                # Top-level sections
                html += f"<section>\n<h2>{k.replace('_', ' ').title()}</h2>\n"
                html += convert_to_html(v, k, False)
                html += "</section>\n"
        return html

    elif isinstance(data, list):
        html = "<ol>\n"
        for item in data:
            html += "<li>"
            html += convert_to_html(item, key, True)
            html += "</li>\n"
        html += "</ol>\n"
        return html

    elif isinstance(data, str):
        # Check if it looks like a URL
        if data.startswith(('http://', 'https://')):
            return f'<a href="{data}">{data}</a>'
        return data

    else:
        return str(data)


def generate_html(config):
    """Generate complete HTML page from config."""
    site_name = config.get('site_name', 'My Site')

    # Generate content from everything except site_name
    content_data = {k: v for k, v in config.items() if k != 'site_name'}
    content_html = convert_to_html(content_data)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
        }}
        h2 {{
            color: #34495e;
            margin-top: 2rem;
        }}
        ol, ul {{
            margin: 1rem 0;
        }}
        li {{
            margin: 0.5rem 0;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        section {{
            margin: 2rem 0;
        }}
    </style>
</head>
<body>
    <h1>{site_name}</h1>
    {content_html}
</body>
</html>"""

    return html


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
    html = generate_html(config)

    # Create output directory
    output_dir = Path("_site")
    output_dir.mkdir(exist_ok=True)

    # Write HTML file
    output_file = output_dir / "index.html"
    output_file.write_text(html, encoding='utf-8')

    console.print(f"[bold bright_green]✓ Site built successfully![/bold bright_green]")
    console.print(f"[dim]>>> Output: {output_file.absolute()}[/dim]")

    return True
