# sssstatic/templates.py
"""
Templates module for SSSStatic - contains all file templates
"""

from .styles import get_theme_css


def get_config_template(project_name):
    """Return the _config.yml template content."""
    return f"""# SSSStatic Configuration
site_name: "{project_name}"
"""


def generate_site_html(config, content_html):
    """Generate complete HTML page from config and content HTML."""
    site_name = config.get('site_name', 'My Site')
    theme = config.get('theme', 'dark')  # Default to dark theme
    css_styles = get_theme_css(theme)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name}</title>
    <style>{css_styles}
    </style>
</head>
<body>
    <h1>{site_name}</h1>
    {content_html}
</body>
</html>"""

    return html
