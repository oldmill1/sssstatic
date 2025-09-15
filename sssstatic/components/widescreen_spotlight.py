# sssstatic/components/widescreen_spotlight.py
"""
Widescreen Spotlight component for SSSStatic - displays a featured image with text positioned on left or right
Inspired by Apple TV+ poster design
"""


def generate_widescreen_spotlight_html(config):
    """Generate HTML for widescreen spotlight section with configurable text positioning."""
    widescreen_data = config.get('_widescreen_spotlight')
    
    if not widescreen_data:
        return ""
    
    # Extract widescreen spotlight configuration
    if isinstance(widescreen_data, dict):
        image_path = widescreen_data.get('image', '')
        title = widescreen_data.get('title', '')
        subtitle = widescreen_data.get('subtitle', '')
        description = widescreen_data.get('description', '')
        buttons = widescreen_data.get('buttons', [])
        text_position = widescreen_data.get('_textPosition', 'right')  # Default to right
    else:
        # If it's just a string, treat it as the image path
        image_path = widescreen_data
        title = ''
        subtitle = ''
        description = ''
        buttons = []
        text_position = 'right'
    
    if not image_path:
        return ""
    
    # Determine layout direction based on text position
    layout_class = f"widescreen-layout-{text_position}"
    
    # Build the widescreen spotlight HTML - full-bleed background with floating text
    spotlight_html = f'    <section class="widescreen-spotlight-section {layout_class}">\n'
    
    # Full-bleed background image
    spotlight_html += '        <div class="widescreen-background">\n'
    spotlight_html += f'            <img src="assets/{image_path}" alt="{title or "Widescreen spotlight image"}" class="widescreen-image">\n'
    spotlight_html += '        </div>\n'
    
    # Floating text content overlay
    spotlight_html += '        <div class="widescreen-content-overlay">\n'
    spotlight_html += '            <div class="widescreen-content">\n'
    
    if title:
        spotlight_html += f'                <h2 class="widescreen-title">{title}</h2>\n'
    
    if subtitle:
        spotlight_html += f'                <h3 class="widescreen-subtitle">{subtitle}</h3>\n'
    
    if description:
        spotlight_html += f'                <p class="widescreen-description">{description}</p>\n'
    
    # Add buttons if provided
    if buttons:
        from .button import generate_button_group_html
        spotlight_html += '                '
        spotlight_html += generate_button_group_html(buttons, 'center', 'medium')
        spotlight_html += '\n'
    
    spotlight_html += '            </div>\n'
    spotlight_html += '        </div>\n'
    spotlight_html += '    </section>\n'
    
    return spotlight_html
