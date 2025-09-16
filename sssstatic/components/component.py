# sssstatic/components/component.py
"""
Generic component for SSSStatic - renders raw HTML from config

COMPONENT PROPERTIES:
====================

_component: string | object
    The component configuration. Can be:
    - String: Raw HTML content (simple usage)
    - Object: Structured component with properties below

PROPERTIES (when _component is an object):
------------------------------------------

html: string (optional)
    Raw HTML content to render inside the component container
    Example: "<h2>Welcome!</h2><p>This is HTML content</p>"

bgColor: string (optional)
    Background color for the component container
    Format: CSS color value (hex, rgb, rgba, named colors)
    Example: "#f0f0f0", "rgb(240, 240, 240)", "lightblue"
    Default: No background color

content: array (optional)
    Array of child components to render inside the component
    Each item can be one of:
    - _text: Text component
    - _button: Button component  
    - _sticker: Sticker component
    Example: [{"_text": {"content": "Hello", "style": "heading"}}]

USAGE EXAMPLES:
===============

1. Simple HTML string:
   _component: "<p>This is raw HTML content</p>"

2. HTML with background:
   _component:
     html: "<h2>Welcome!</h2><p>This is HTML content</p>"
     bgColor: "#f0f0f0"

3. Content array with text and buttons:
   _component:
     content:
       - _text:
           content: "Get Started Today"
           style: "heading"
       - _text:
           content: "Join thousands of satisfied customers"
           style: "body"
       - _button:
           text: "Sign Up Now"
           url: "/signup"
           style: "primary"
     bgColor: "#e8f4fd"

4. Mixed content with stickers:
   _component:
     content:
       - _text:
           content: "Special Offer!"
           style: "heading"
       - _sticker:
           name: "rocket"
           size: "large"
       - _button:
           text: "Claim Offer"
           url: "/offer"
           style: "success"

RENDERED OUTPUT:
===============
- Single HTML string: Wrapped in <div class="component-container">
- Object with html: Wrapped in <div class="component-container"> with optional background styling
- Object with content: Flexbox container with proper spacing and alignment
- Background colors: Applied with border-radius: 12px and padding: 1rem
"""


def generate_component_html(config):
    """Generate HTML for generic component with raw HTML content or text components."""
    component_data = config.get('_component')
    
    if not component_data:
        return ""
    
    # Import component generators
    from .text import generate_text_html
    from .button import generate_button_html
    from .stickers import generate_sticker_html
    
    # Check if it's a dict with content array or html property
    if isinstance(component_data, dict):
        # Check for content array (array of _text and _button components)
        content_array = component_data.get('content', [])
        html_content = component_data.get('html', '')
        
        if content_array and isinstance(content_array, list):
            # Generate HTML from text and button components
            content_htmls = []
            for content_config in content_array:
                if isinstance(content_config, dict):
                    # Handle _text components
                    if '_text' in content_config:
                        temp_config = content_config
                        text_html = generate_text_html(temp_config)
                        if text_html:
                            content_htmls.append(text_html)
                    
                    # Handle _button components
                    elif '_button' in content_config:
                        button_config = content_config['_button']
                        if isinstance(button_config, dict):
                            # Extract button parameters
                            text = button_config.get('text', 'Button')
                            url = button_config.get('url', '#')
                            style = button_config.get('style', 'primary')
                            variant = button_config.get('variant', 'default')
                            size = button_config.get('size', 'medium')
                            icon = button_config.get('icon', None)
                            anchor_link = button_config.get('anchor_link', False)
                            align = button_config.get('align', 'center')
                            
                            button_html = generate_button_html(text, url, style, variant, size, icon, anchor_link, align)
                            if button_html:
                                content_htmls.append(button_html)
                    
                    # Handle _sticker components
                    elif '_sticker' in content_config:
                        temp_config = content_config
                        sticker_html = generate_sticker_html(temp_config)
                        if sticker_html:
                            content_htmls.append(sticker_html)
            
            if content_htmls:
                # Build the component HTML with proper wrapper
                bg_color = component_data.get('bgColor', '')
                if bg_color:
                    style_attr = f' style="background-color: {bg_color}; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-evenly; align-items: center; gap: 0.5rem; padding: 1rem; min-height: 200px;"'
                else:
                    style_attr = ' style="display: flex; flex-direction: column; justify-content: space-evenly; align-items: center; gap: 0.5rem;"'
                component_html = f'        <div class="component-container"{style_attr}>\n'
                for content_html in content_htmls:
                    # Add each content component with proper indentation
                    indented_html = '\n'.join('            ' + line for line in content_html.split('\n'))
                    component_html += indented_html + '\n'
                component_html += '        </div>\n'
                return component_html
        
        # Fall back to HTML content if no content array
        if html_content:
            # Wrap HTML content in component container
            bg_color = component_data.get('bgColor', '')
            if bg_color:
                style_attr = f' style="background-color: {bg_color}; border-radius: 12px; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 0.5rem; padding: 1rem; min-height: 200px;"'
            else:
                style_attr = ' style="display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 0.5rem;"'
            component_html = f'        <div class="component-container"{style_attr}>\n'
            component_html += f'            {html_content}\n'
            component_html += '        </div>\n'
            return component_html
    else:
        # If it's just a string, treat it as HTML
        html_content = str(component_data)
        if html_content:
            # Wrap HTML content in component container (no bgColor support for string components)
            component_html = '        <div class="component-container">\n'
            component_html += f'            {html_content}\n'
            component_html += '        </div>\n'
            return component_html
    
    return ""
