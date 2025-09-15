# sssstatic/components/component.py
"""
Generic component for SSSStatic - renders raw HTML from config
"""


def generate_component_html(config):
    """Generate HTML for generic component with raw HTML content."""
    component_data = config.get('_component')
    
    if not component_data:
        return ""
    
    # Extract HTML content
    if isinstance(component_data, dict):
        html_content = component_data.get('html', '')
    else:
        # If it's just a string, treat it as HTML
        html_content = str(component_data)
    
    if not html_content:
        return ""
    
    # Build the component HTML
    component_html = '        <div class="component-container">\n'
    component_html += f'            {html_content}\n'
    component_html += '        </div>\n'
    
    return component_html
