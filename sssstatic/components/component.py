# sssstatic/components/component.py
"""
Generic component for SSSStatic - renders raw HTML from config
"""


def generate_component_html(config):
    """Generate HTML for generic component with raw HTML content or text components."""
    component_data = config.get('_component')
    
    if not component_data:
        return ""
    
    # Import component generators
    from .text import generate_text_html
    from .button import generate_button_html
    
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
                            size = button_config.get('size', 'medium')
                            icon = button_config.get('icon', None)
                            anchor_link = button_config.get('anchor_link', False)
                            
                            button_html = generate_button_html(text, url, style, size, icon, anchor_link)
                            if button_html:
                                content_htmls.append(button_html)
            
            if content_htmls:
                # Build the component HTML with mixed content (no extra wrapper needed)
                component_html = ''
                for content_html in content_htmls:
                    # Add each content component directly
                    component_html += content_html + '\n'
                return component_html
        
        # Fall back to HTML content if no content array
        if html_content:
            component_html = '        <div class="component-container">\n'
            component_html += f'            {html_content}\n'
            component_html += '        </div>\n'
            return component_html
    else:
        # If it's just a string, treat it as HTML
        html_content = str(component_data)
        if html_content:
            component_html = '        <div class="component-container">\n'
            component_html += f'            {html_content}\n'
            component_html += '        </div>\n'
            return component_html
    
    return ""
