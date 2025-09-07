# sssstatic/templates.py
"""
Templates module for SSSStatic - contains all file templates
"""


def get_config_template(project_name):
    """Return the _config.yml template content."""
    return f"""# SSSStatic Configuration
site_name: "{project_name}"
"""


def generate_site_html(config, content_html):
    """Generate complete HTML page from config and content HTML."""
    site_name = config.get('site_name', 'My Site')

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
