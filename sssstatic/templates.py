# sssstatic/templates.py
"""
Templates module for SSSStatic - contains all file templates
"""
import re


def get_config_template(project_name):
    """Return the _config.yml template content."""
    return f"""# SSSStatic Configuration
site_name: "{project_name}"
"""


def generate_site_html(config, content_html):
    """Generate complete HTML page from config and content HTML."""
    from .components.page_header import generate_page_header_html
    from .components.image import generate_image_html
    from .components.header import generate_header_html
    from .components.cards import generate_cards_html
    from .styles.footer import generate_footer_html
    
    # Use _title for both title and h1, fall back to site_name if _title not available
    page_title = config.get('_title', config.get('site_name', 'My Site'))

    # Generate header HTML
    header_html = generate_header_html(config)

    # Generate page header HTML - only render h1 if _title is present
    page_header_html = generate_page_header_html(config)

    # Generate image HTML if _image is present
    image_html = generate_image_html(config)
    
    # Generate cards HTML if _card entries exist
    cards_html = generate_cards_html(config)
    
    # Generate footer HTML
    footer_html = generate_footer_html(config)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;600&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fascinate&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Henny+Penny&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header_html}{page_header_html}    {image_html}
    {cards_html}
    {content_html}
{footer_html}</body>
</html>"""

    return html
