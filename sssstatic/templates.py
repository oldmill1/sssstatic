# sssstatic/templates.py
"""
Templates module for SSSStatic - contains all file templates
"""


def get_config_template(project_name):
    """Return the _config.yml template content."""
    return f"""# SSSStatic Configuration
site_name: "{project_name}"
"""


def generate_cards_html(config):
    """Generate HTML for _card entries."""
    cards_html = ""
    cards = []

    # Collect all _card entries
    for key, value in config.items():
        if key == '_card':
            if isinstance(value, list):
                cards.extend(value)
            else:
                cards.append(value)

    if not cards:
        return ""

    # Generate cards container
    cards_html = '<div class="cards-container">\n'

    for card in cards:
        if isinstance(card, dict):
            name = card.get('name', 'Untitled')
            url = card.get('url', '#')
            description = card.get('description', 'No description')
            status = card.get('status', 'unknown')

            # Status indicator styling
            status_class = f"status-{status.lower()}"

            cards_html += f'''    <div class="card">
        <div class="card-header">
            <h3 class="card-title">{name}</h3>
            <span class="card-status {status_class}">{status}</span>
        </div>
        <p class="card-description">{description}</p>
        <div class="card-footer">
            <a href="{url}" class="card-link" target="_blank" rel="noopener noreferrer">
                View Project →
            </a>
        </div>
    </div>
'''

    cards_html += '</div>\n'
    return cards_html


def generate_footer_html(config):
    """Generate HTML for footer."""
    footer_html = ""
    
    # Check for _footer configuration
    if '_footer' in config:
        footer_config = config['_footer']
        if isinstance(footer_config, dict):
            headline = footer_config.get('headline', 'explore on 🌎')
        else:
            headline = footer_config
    else:
        # Default footer text
        headline = 'explore on 🌎'
    
    footer_html = f'''    <footer class="site-footer">
        <div class="footer-content">
            <span class="footer-text">{headline}</span>
        </div>
    </footer>
'''
    
    return footer_html


def generate_site_html(config, content_html):
    """Generate complete HTML page from config and content HTML."""
    # Use _title for both title and h1, fall back to site_name if _title not available
    page_title = config.get('_title', config.get('site_name', 'My Site'))

    # Generate header HTML - check for multi-line title first
    header_html = ""
    if '_multi_line_title' in config:
        multi_title = config['_multi_line_title']
        if isinstance(multi_title, dict):
            title_text = multi_title.get('title', page_title)
            subtitle_text = multi_title.get('sub_title', '')
            header_html = f"""    <header class="movie-header">
        <h1 class="movie-title">{title_text}</h1>
        <p class="movie-subtitle">{subtitle_text}</p>
    </header>
"""
    else:
        # Fallback to single line title
        header_html = f"    <h1>{page_title}</h1>\n"

    # Generate image HTML if _image is present
    image_html = ""
    if '_image' in config:
        image_config = config['_image']
        if isinstance(image_config, dict):
            image_name = image_config.get('name', '')
            image_alt = image_config.get('alt', 'Image')
            if image_name:
                image_html = f'<div class="header-image"><img src="assets/{image_name}" alt="{image_alt}"></div>'

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
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header_html}    {image_html}
    {cards_html}
    {content_html}
{footer_html}</body>
</html>"""

    return html
