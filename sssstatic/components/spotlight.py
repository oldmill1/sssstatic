# sssstatic/components/spotlight.py
"""
Spotlight component for SSSStatic - displays a featured image with optional text
"""


def generate_spotlight_html(config):
    """Generate HTML for spotlight section with image."""
    spotlight_data = config.get('_spotlight')
    
    if not spotlight_data:
        return ""
    
    # Extract spotlight configuration
    if isinstance(spotlight_data, dict):
        image_path = spotlight_data.get('image', '')
        title = spotlight_data.get('title', '')
        subtitle = spotlight_data.get('subtitle', '')
        description = spotlight_data.get('description', '')
        buttons = spotlight_data.get('buttons', [])
    else:
        # If it's just a string, treat it as the image path
        image_path = spotlight_data
        title = ''
        subtitle = ''
        description = ''
        buttons = []
    
    if not image_path:
        return ""
    
    # Build the spotlight HTML
    spotlight_html = '    <section class="spotlight-section">\n'
    
    # Image container (starts from top)
    spotlight_html += '        <div class="spotlight-image-container">\n'
    
    # Handle external URLs vs local assets
    if image_path.startswith(('http://', 'https://')):
        image_src = image_path
    else:
        image_src = f"assets/{image_path}"
    
    spotlight_html += f'            <img src="{image_src}" alt="{title or "Spotlight image"}" class="spotlight-image">\n'
    
    # Text content overlaid on image (only if provided)
    if title or subtitle or description:
        spotlight_html += '            <div class="spotlight-content">\n'
        
        if title:
            spotlight_html += f'                <h2 class="spotlight-title">{title}</h2>\n'
        
        if subtitle:
            spotlight_html += f'                <h3 class="spotlight-subtitle">{subtitle}</h3>\n'
        
        if description:
            spotlight_html += f'                <p class="spotlight-description">{description}</p>\n'
        
        # Add buttons if provided
        if buttons:
            spotlight_html += '                <div class="spotlight-actions">\n'
            for button in buttons:
                if isinstance(button, dict):
                    text = button.get('text', 'Button')
                    url = button.get('url', '#')
                    style = button.get('style', 'primary')
                    spotlight_html += f'                    <a href="{url}" class="spotlight-button spotlight-button-{style}">{text}</a>\n'
                else:
                    # If it's just a string, treat it as button text
                    spotlight_html += f'                    <a href="#" class="spotlight-button spotlight-button-primary">{button}</a>\n'
            spotlight_html += '                </div>\n'
        
        spotlight_html += '            </div>\n'
    
    spotlight_html += '        </div>\n'
    spotlight_html += '    </section>\n'
    
    return spotlight_html
