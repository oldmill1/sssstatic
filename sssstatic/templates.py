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


def generate_hero_banner_html(config):
    """Generate HTML for hero banner component."""
    hero_html = ""
    
    # Check for _hero_banner configuration
    if '_hero_banner' not in config:
        return ""
    
    hero_config = config['_hero_banner']
    if not isinstance(hero_config, dict):
        return ""
    
    # Hero section
    hero_image_url = hero_config.get('hero_image', 'https://dummyimage.com/600x400/007AFF/ffffff&text=hello+(again)')
    
    # Check if it's a local image (not starting with http/https)
    if not hero_image_url.startswith(('http://', 'https://')):
        hero_image_url = f"assets/{hero_image_url}"
    
    hero_headline = hero_config.get('headline', 'Build. Ship. Wow.')
    hero_subtitle = hero_config.get('subtitle', 'A strategy as simple as great software.')
    hero_link = hero_config.get('link', '')
    
    # Process subtitle to make sssstatic a link if link is provided
    if hero_link and 'sssstatic' in hero_subtitle.lower():
        # Replace sssstatic with a link
        hero_subtitle = re.sub(
            r'\bsssstatic\b', 
            f'<a href="{hero_link}" target="_blank" rel="noopener noreferrer">sssstatic</a>', 
            hero_subtitle, 
            flags=re.IGNORECASE
        )
    
    # Three columns
    columns = hero_config.get('columns', [])
    if not columns:
        # Default columns if none specified
        columns = [
            {
                'title': 'Build.',
                'description': 'Creative developers, meet your match.',
                'image': 'https://dummyimage.com/300x200/10B981/ffffff&text=Build',
                'color': '10B981'
            },
            {
                'title': 'Ship.',
                'description': 'We rewrote the book on deployment.',
                'image': 'https://dummyimage.com/300x200/F59E0B/ffffff&text=Ship',
                'color': 'F59E0B'
            },
            {
                'title': 'Wow.',
                'description': "It's okay, you don't have to say anything.",
                'image': 'https://dummyimage.com/300x200/8B5CF6/ffffff&text=Wow',
                'color': '8B5CF6'
            }
        ]
    
    # Generate hero content
    hero_html = f'''    <!-- Hero Banner Section -->
    <section class="hero-banner">
        <div class="hero-content">
            <div class="hero-image">
                <img src="{hero_image_url}" alt="Software Screenshot" />
            </div>
            <div class="hero-text">
                <h2 class="hero-headline">{hero_headline}</h2>
                <p class="hero-subtitle">{hero_subtitle}</p>
            </div>
        </div>
        
        <div class="three-columns">
'''
    
    # Generate three columns
    for column in columns:
        title = column.get('title', '')
        description = column.get('description', '')
        image_url = column.get('image', 'https://dummyimage.com/300x200/cccccc/ffffff&text=Column')
        
        hero_html += f'''            <div class="column">
                <div class="column-image">
                    <img src="{image_url}" alt="{title}" />
                </div>
                <h3 class="column-title">{title}</h3>
                <p class="column-description">{description}</p>
            </div>
'''
    
    hero_html += '''        </div>
    </section>
'''
    
    return hero_html


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

    # Generate hero banner HTML if _hero_banner exists
    hero_banner_html = generate_hero_banner_html(config)
    
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
{header_html}    {image_html}
    {hero_banner_html}
    {cards_html}
    {content_html}
{footer_html}</body>
</html>"""

    return html
