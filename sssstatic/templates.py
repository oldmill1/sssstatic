# sssstatic/templates.py
"""
Templates module for SSSStatic - contains all file templates
"""
import re


def get_config_template(project_name):
    """Return the _config.yml template content."""
    return f"""# SSSStatic Configuration
site:
  name: "{project_name}"
"""


def get_smooth_scroll_script():
    """Return JavaScript for smooth scrolling functionality."""
    return """
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Handle anchor link clicks
    const anchorLinks = document.querySelectorAll('.anchor-link');
    
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const scrollTo = this.getAttribute('data-scroll-to');
            const targetElement = document.getElementById(scrollTo);
            
            if (targetElement) {
                // Smooth scroll to the target element
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
</script>"""


def generate_site_html(config, content_html, dev_mode=False):
    """Generate complete HTML page from config and content HTML."""
    from .components.page_header import generate_page_header_html
    from .components.image import generate_image_html
    from .components.topbar import generate_topbar_html
    from .components.cards import generate_cards_html
    from .components.spotlight import generate_spotlight_html
    from .components.widescreen_spotlight import generate_widescreen_spotlight_html
    from .components.pinterest import generate_pinterest_html
    from .components.showcase import generate_showcase_html
    from .components.slick import generate_slick_html
    from .components.sizzle import generate_sizzle_html
    from .components.sly import generate_sly_html
    from .components.sinema import generate_sinema_html
    from .components.map import generate_map_html
    from .styles.footer import generate_footer_html
    from .styles.type import get_google_fonts_imports
    
    # Use _title for both title and h1, fall back to site name if _title not available
    page_title = config.get('_title', config.get('site', {}).get('name', 'My Site'))

    # Generate header HTML - use TopBar if configured, otherwise no header
    has_topbar = '_topbar' in config
    if has_topbar:
        header_html = generate_topbar_html(config)
    else:
        header_html = ""  # No header component

    # Generate page header HTML - only render h1 if _title is present
    page_header_html = generate_page_header_html(config)

    # Generate image HTML if _image is present
    image_html = generate_image_html(config)
    
    # Generate footer HTML
    footer_html = generate_footer_html(config)

    # Component mapping for dynamic generation
    component_generators = {
        '_card': generate_cards_html,
        '_spotlight': generate_spotlight_html,
        '_widescreen_spotlight': generate_widescreen_spotlight_html,
        '_pinterest': generate_pinterest_html,
        '_showcase': generate_showcase_html,
        '_slick': generate_slick_html,
        '_sizzle': generate_sizzle_html,
        '_sly': generate_sly_html,
        '_sinema': generate_sinema_html,
        '_map': generate_map_html,
    }
    
    # Generate components in the order they appear in the YAML config
    components_html = ""
    for key, value in config.items():
        if key in component_generators:
            component_html = component_generators[key](config)
            if component_html:
                components_html += component_html

    body_class = "has-topbar" if has_topbar else ""
    
    # Check if anchor links are present to add smooth scrolling JavaScript
    has_anchor_links = '_anchorLinks' in config
    
    # Add timestamp to CSS link in dev mode for cache busting
    css_link = "assets/styles.css"
    if dev_mode:
        import time
        timestamp = int(time.time())
        css_link = f"assets/styles.css?v={timestamp}"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
{get_google_fonts_imports()}
    <link rel="stylesheet" href="{css_link}">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
</head>
<body class="{body_class}">
{header_html}{page_header_html}    {image_html}
    {components_html}
    {content_html}
{footer_html}{get_smooth_scroll_script() if has_anchor_links else ''}</body>
</html>"""

    return html
