# sssstatic/components/showcase.py
"""
Showcase component for SSSStatic - displays an image with a multi-step process and call-to-action

Configuration options:
- image: Image file path (required)
- title: Main heading text
- subtitle: Subheading text  
- steps: List of step objects with emoji, text, and description
- button_text: Call-to-action button text (default: "Get Started Today")
- button_url: Call-to-action button URL (default: "#")
- button_size: Button size - "small", "medium", or "large" (default: "medium")
- direction: Image position - "left" or "right" (default: "left")
- spacerTop: CSS value for top margin (e.g., "1rem", "2em", "20px")
- spacerBottom: CSS value for bottom margin (e.g., "1rem", "2em", "20px")
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
        button_size = showcase_data.get('button_size', 'medium')  # Default to medium
        direction = showcase_data.get('direction', 'left')  # Default to left
        spacer_top = showcase_data.get('spacerTop', '')
        spacer_bottom = showcase_data.get('spacerBottom', '')
    else:
        # If it's just a string, treat it as the image path
        image_path = showcase_data
        title = ''
        subtitle = ''
        steps = []
        button_text = 'Get Started Today'
        button_url = '#'
        button_size = 'medium'  # Default to medium
        direction = 'left'  # Default to left
        spacer_top = ''
        spacer_bottom = ''
    
    if not image_path:
        return ""
    
    # Validate button size
    valid_sizes = ['small', 'medium', 'large']
    if button_size not in valid_sizes:
        button_size = 'medium'  # Fallback to medium if invalid size provided
    
    # Default steps if none provided
    if not steps:
        steps = [
            {'emoji': '👋', 'text': 'Meet your Professional'},
            {'emoji': '⚡', 'text': '1 Hour session for service time'},
            {'emoji': '✨', 'text': 'You get high quality results'}
        ]
    
    # Build the showcase HTML with spacer styles
    spacer_styles = []
    if spacer_top:
        spacer_styles.append(f'margin-top: {spacer_top}')
    if spacer_bottom:
        spacer_styles.append(f'margin-bottom: {spacer_bottom}')
    
    style_attr = f' style="{"; ".join(spacer_styles)}"' if spacer_styles else ''
    showcase_html = f'    <section class="showcase-section"{style_attr}>\n'
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
        from .button import generate_button_html
        anchor_link = button_url.startswith('#')
        showcase_html += '                '
        showcase_html += generate_button_html(button_text, button_url, 'primary', 'default', button_size, None, anchor_link)
        showcase_html += '\n            </div>\n'
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
        from .button import generate_button_html
        anchor_link = button_url.startswith('#')
        showcase_html += '                '
        showcase_html += generate_button_html(button_text, button_url, 'primary', 'default', button_size, None, anchor_link)
        showcase_html += '\n            </div>\n'
    showcase_html += '        </div>\n'
    showcase_html += '    </section>\n'
    
    return showcase_html
