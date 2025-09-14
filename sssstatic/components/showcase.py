# sssstatic/components/showcase.py
"""
Showcase component for SSSStatic - displays an image with a multi-step process and call-to-action
"""


def generate_showcase_html(config):
    """Generate HTML for showcase section with image and steps."""
    showcase_data = config.get('_showcase')
    
    if not showcase_data:
        return ""
    
    # Extract showcase configuration
    if isinstance(showcase_data, dict):
        image_path = showcase_data.get('image', '')
        title = showcase_data.get('title', '')
        subtitle = showcase_data.get('subtitle', '')
        steps = showcase_data.get('steps', [])
        button_text = showcase_data.get('button_text', 'Get Started Today')
        button_url = showcase_data.get('button_url', '#')
        direction = showcase_data.get('direction', 'left')  # Default to left
    else:
        # If it's just a string, treat it as the image path
        image_path = showcase_data
        title = ''
        subtitle = ''
        steps = []
        button_text = 'Get Started Today'
        button_url = '#'
        direction = 'left'  # Default to left
    
    if not image_path:
        return ""
    
    # Default steps if none provided
    if not steps:
        steps = [
            {'emoji': '👋', 'text': 'Meet your Professional'},
            {'emoji': '⚡', 'text': '1 Hour session for service time'},
            {'emoji': '✨', 'text': 'You get high quality results'}
        ]
    
    # Build the showcase HTML
    showcase_html = '    <section class="showcase-section">\n'
    showcase_html += f'        <div class="showcase-container showcase-{direction}">\n'
    
    # Generate image and content based on position
    if direction == 'right':
        # Image first (right side)
        showcase_html += '            <div class="showcase-image">\n'
        showcase_html += f'                <img src="assets/{image_path}" alt="{title or "Professional"}" class="showcase-img">\n'
        showcase_html += '            </div>\n'
        
        # Content second (left side)
        showcase_html += '            <div class="showcase-content">\n'
        if title:
            showcase_html += f'                <h2 class="showcase-title">{title}</h2>\n'
        if subtitle:
            showcase_html += f'                <h3 class="showcase-subtitle">{subtitle}</h3>\n'
        
        # Steps
        if steps:
            showcase_html += '                <div class="showcase-steps">\n'
            for i, step in enumerate(steps, 1):
                if isinstance(step, dict):
                    emoji = step.get('emoji', '⚡')
                    text = step.get('text', f'Step {i}')
                    description = step.get('description', '')
                else:
                    emoji = '⚡'
                    text = str(step)
                    description = ''
                
                showcase_html += f'                    <div class="showcase-step">\n'
                showcase_html += f'                        <span class="step-emoji">{emoji}</span>\n'
                showcase_html += f'                        <div class="step-content">\n'
                showcase_html += f'                            <span class="step-text">{text}</span>\n'
                if description:
                    showcase_html += f'                            <span class="step-description">{description}</span>\n'
                showcase_html += '                        </div>\n'
                showcase_html += '                    </div>\n'
            showcase_html += '                </div>\n'
        
        # Call-to-action button
        # Check if button URL is an anchor link
        if button_url.startswith('#'):
            scroll_to = button_url[1:]  # Remove the # symbol
            showcase_html += f'                <a href="{button_url}" class="showcase-button anchor-link" data-scroll-to="{scroll_to}">{button_text}</a>\n'
        else:
            showcase_html += f'                <a href="{button_url}" class="showcase-button">{button_text}</a>\n'
        showcase_html += '            </div>\n'
    else:
        # Default: Image first (left side)
        showcase_html += '            <div class="showcase-image">\n'
        showcase_html += f'                <img src="assets/{image_path}" alt="{title or "Professional"}" class="showcase-img">\n'
        showcase_html += '            </div>\n'
        
        # Content container (right side)
        showcase_html += '            <div class="showcase-content">\n'
        if title:
            showcase_html += f'                <h2 class="showcase-title">{title}</h2>\n'
        if subtitle:
            showcase_html += f'                <h3 class="showcase-subtitle">{subtitle}</h3>\n'
        
        # Steps
        if steps:
            showcase_html += '                <div class="showcase-steps">\n'
            for i, step in enumerate(steps, 1):
                if isinstance(step, dict):
                    emoji = step.get('emoji', '⚡')
                    text = step.get('text', f'Step {i}')
                    description = step.get('description', '')
                else:
                    emoji = '⚡'
                    text = str(step)
                    description = ''
                
                showcase_html += f'                    <div class="showcase-step">\n'
                showcase_html += f'                        <span class="step-emoji">{emoji}</span>\n'
                showcase_html += f'                        <div class="step-content">\n'
                showcase_html += f'                            <span class="step-text">{text}</span>\n'
                if description:
                    showcase_html += f'                            <span class="step-description">{description}</span>\n'
                showcase_html += '                        </div>\n'
                showcase_html += '                    </div>\n'
            showcase_html += '                </div>\n'
        
        # Call-to-action button
        # Check if button URL is an anchor link
        if button_url.startswith('#'):
            scroll_to = button_url[1:]  # Remove the # symbol
            showcase_html += f'                <a href="{button_url}" class="showcase-button anchor-link" data-scroll-to="{scroll_to}">{button_text}</a>\n'
        else:
            showcase_html += f'                <a href="{button_url}" class="showcase-button">{button_text}</a>\n'
        showcase_html += '            </div>\n'
    showcase_html += '        </div>\n'
    showcase_html += '    </section>\n'
    
    return showcase_html
