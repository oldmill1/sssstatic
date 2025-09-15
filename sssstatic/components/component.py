# sssstatic/components/component.py
"""
Generic component for SSSStatic - renders raw HTML from config
"""


def generate_component_html(config):
    """Generate HTML for generic component with raw HTML content or text components."""
    component_data = config.get('_component')
    
    if not component_data:
        return ""
    
    # Import text component generator
    from .text import generate_text_html
    
    # Check if it's a dict with content array or html property
    if isinstance(component_data, dict):
        # Check for content array (array of _text components)
        content_array = component_data.get('content', [])
        html_content = component_data.get('html', '')
        
        if content_array and isinstance(content_array, list):
            # Generate HTML from text components
            text_htmls = []
            for text_config in content_array:
                if isinstance(text_config, dict) and '_text' in text_config:
                    # Create a temporary config for the text component
                    temp_config = text_config
                    text_html = generate_text_html(temp_config)
                    if text_html:
                        text_htmls.append(text_html)
            
            if text_htmls:
                # Build the component HTML with text components (no extra wrapper needed)
                component_html = ''
                for text_html in text_htmls:
                    # Add each text component directly
                    component_html += text_html + '\n'
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
