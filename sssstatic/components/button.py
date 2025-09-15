# sssstatic/components/button.py
"""
Button component module for SSSStatic - centralized button component
"""


def generate_button_html(text, url='#', style='primary', variant='default', size='medium', icon=None, anchor_link=False):
    """
    Generate HTML for a button component.
    
    Args:
        text (str): Button text
        url (str): Button URL (default: '#')
        style (str): Button style - 'primary', 'secondary', 'gradient', 'cta' (default: 'primary')
        variant (str): Button variant - 'default', 'warning', 'success', 'neutral', 'link' (default: 'default')
        size (str): Button size - 'small', 'medium', 'large' (default: 'medium')
        icon (str): Icon to display (optional)
        anchor_link (bool): Whether this is an anchor link for smooth scrolling (default: False)
    
    Returns:
        str: HTML for the button
    """
    # Handle anchor links
    scroll_to = ''
    if anchor_link and url.startswith('#'):
        scroll_to = url[1:]  # Remove the # symbol
    
    # Build CSS classes
    css_classes = ['sss-button', f'sss-button-{style}', f'sss-button-{size}']
    
    # Add variant class if provided and style is primary
    if style == 'primary' and variant:
        css_classes.append(f'sss-button-variant-{variant}')
    
    # Add anchor link class if needed
    if anchor_link and url.startswith('#'):
        css_classes.append('anchor-link')
    
    # Add icon class if provided
    if icon:
        css_classes.append(f'sss-button-icon-{icon}')
    
    # Join classes
    class_string = ' '.join(css_classes)
    
    # Build data attributes for anchor links
    data_attrs = ''
    if anchor_link and url.startswith('#'):
        data_attrs = f' data-scroll-to="{scroll_to}"'
    
    # Generate HTML
    button_html = f'<a href="{url}" class="{class_string}"{data_attrs}>'
    
    # Add text (icon will be generated via CSS)
    button_html += f'<span class="sss-button-text">{text}</span>'
    
    # Close tag
    button_html += '</a>'
    
    return button_html


def generate_button_group_html(buttons, alignment='center', gap='medium'):
    """
    Generate HTML for a group of buttons.
    
    Args:
        buttons (list): List of button configurations
        alignment (str): Button alignment - 'left', 'center', 'right' (default: 'center')
        gap (str): Gap between buttons - 'small', 'medium', 'large' (default: 'medium')
    
    Returns:
        str: HTML for the button group
    """
    if not buttons:
        return ''
    
    # Build CSS classes for button group
    css_classes = ['sss-button-group', f'sss-button-group-{alignment}', f'sss-button-group-{gap}']
    class_string = ' '.join(css_classes)
    
    button_group_html = f'<div class="{class_string}">\n'
    
    for button in buttons:
        if isinstance(button, dict):
            text = button.get('text', 'Button')
            url = button.get('url', '#')
            style = button.get('style', 'primary')
            variant = button.get('variant', 'default')
            size = button.get('size', 'medium')
            icon = button.get('icon', None)
            anchor_link = button.get('anchor_link', False)
            
            button_html = generate_button_html(text, url, style, variant, size, icon, anchor_link)
            button_group_html += f'    {button_html}\n'
        else:
            # If it's just a string, treat it as button text
            button_html = generate_button_html(button)
            button_group_html += f'    {button_html}\n'
    
    button_group_html += '</div>'
    
    return button_group_html


# Button style mappings for easy reference
BUTTON_STYLES = {
    'primary': 'Primary button style with variants',
    'secondary': 'Transparent button with border',
    'gradient': 'Purple gradient button with shadow',
    'cta': 'Dark CTA button with icon'
}

# Button variant mappings for primary style
BUTTON_VARIANTS = {
    'default': 'Blue-green gradient (default)',
    'warning': 'Orange-red gradient (warning)',
    'success': 'Green gradient (success)',
    'neutral': 'Gray-white gradient (neutral)',
    'link': 'Text-only link-style'
}

BUTTON_SIZES = {
    'small': 'Compact button for tight spaces',
    'medium': 'Standard button size',
    'large': 'Large button for emphasis'
}

BUTTON_ICONS = {
    'lightning': '⚡',
    'arrow': '→',
    'star': '★',
    'heart': '♥',
    'check': '✓',
    'plus': '+',
    'minus': '-'
}
