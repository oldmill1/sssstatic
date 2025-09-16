# sssstatic/components/widescreen_spotlight.py
"""
Widescreen Spotlight component for SSSStatic - displays a featured image with text positioned on left or right
Inspired by Apple TV+ poster design
"""


def generate_widescreen_spotlight_html(config):
    """
    Generate HTML for widescreen spotlight section with configurable text positioning.
    
    This component creates a full-width hero section with a background image and overlaid text content.
    The text can be positioned on either the left or right side of the image, creating a cinematic
    Apple TV+ style layout.
    
    Configuration Parameters (under '_widescreen_spotlight' key):
    
    Required:
    - image (str): Path to the background image file (relative to assets/ folder)
    
    Optional:
    - title (str): Main heading text displayed prominently
    - subtitle (str): Secondary heading text, smaller than title
    - description (str): Body text/paragraph content
    - buttons (list): Array of button configurations (uses button component)
    - textPosition (str): Position of text overlay - 'left' or 'right' (default: 'right')
    - textColor (str): CSS color for text elements (default: '#ffffff')
    - shiftBg (str): CSS transform value to shift background image (default: '0')
    
    Example configuration:
    _widescreen_spotlight:
      image: "hero-image.jpg"
      title: "Welcome to Our Platform"
      subtitle: "Discover Amazing Features"
      description: "This is a compelling description that explains what your platform offers."
      textPosition: "left"
      textColor: "#ffffff"
      shiftBg: "-20px"
      buttons:
        - text: "Get Started"
          link: "/signup"
          style: "primary"
        - text: "Learn More"
          link: "/about"
          style: "secondary"
    
    Returns:
    - str: HTML markup for the widescreen spotlight section, or empty string if no config
    """
    # Get the widescreen spotlight configuration from the site config
    widescreen_data = config.get('_widescreen_spotlight')
    
    # Return empty string if no widescreen spotlight is configured
    if not widescreen_data:
        return ""
    
    # Extract widescreen spotlight configuration
    # Support both full object config and simple string (image path only)
    if isinstance(widescreen_data, dict):
        # Full configuration object with all options
        image_path = widescreen_data.get('image', '')
        title = widescreen_data.get('title', '')
        subtitle = widescreen_data.get('subtitle', '')
        description = widescreen_data.get('description', '')
        buttons = widescreen_data.get('buttons', [])
        text_position = widescreen_data.get('textPosition', 'right')  # Default to right
        text_color = widescreen_data.get('textColor', '#ffffff')  # Default to white
        shift_bg = widescreen_data.get('shiftBg', '0')  # Default to no shift
    else:
        # If it's just a string, treat it as the image path only
        # This provides backward compatibility for simple configurations
        image_path = widescreen_data
        title = ''
        subtitle = ''
        description = ''
        buttons = []
        text_position = 'right'
        text_color = '#ffffff'
        shift_bg = '0'
    
    # Require at least an image path to render the component
    if not image_path:
        return ""
    
    # Determine layout direction based on text position (left/right)
    # This creates CSS classes like 'widescreen-layout-left' or 'widescreen-layout-right'
    layout_class = f"widescreen-layout-{text_position}"
    
    # Build the widescreen spotlight HTML - full-bleed background with floating text
    # Uses CSS custom properties for dynamic styling (text color and background shift)
    spotlight_html = f'    <section class="widescreen-spotlight-section {layout_class}" style="--widescreen-text-color: {text_color}; --widescreen-shift: {shift_bg};">\n'
    
    # Full-bleed background image container
    # The image will cover the entire section width and can be shifted via CSS transform
    spotlight_html += '        <div class="widescreen-background">\n'
    spotlight_html += f'            <img src="assets/{image_path}" alt="{title or "Widescreen spotlight image"}" class="widescreen-image">\n'
    spotlight_html += '        </div>\n'
    
    # Floating text content overlay positioned over the background image
    # Content is positioned left or right based on textPosition setting
    spotlight_html += '        <div class="widescreen-content-overlay">\n'
    spotlight_html += '            <div class="widescreen-content">\n'
    
    # Add title if provided (main heading)
    if title:
        spotlight_html += f'                <h2 class="widescreen-title">{title}</h2>\n'
    
    # Add subtitle if provided (secondary heading)
    if subtitle:
        spotlight_html += f'                <h3 class="widescreen-subtitle">{subtitle}</h3>\n'
    
    # Add description if provided (body text)
    if description:
        spotlight_html += f'                <p class="widescreen-description">{description}</p>\n'
    
    # Add buttons if provided (integrates with button component)
    if buttons:
        from .button import generate_button_group_html
        spotlight_html += '                '
        # Generate button group with center alignment and medium size
        spotlight_html += generate_button_group_html(buttons, 'center', 'medium')
        spotlight_html += '\n'
    
    # Close content containers
    spotlight_html += '            </div>\n'
    spotlight_html += '        </div>\n'
    spotlight_html += '    </section>\n'
    
    return spotlight_html
