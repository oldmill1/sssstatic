# sssstatic/components/sslogan.py
"""
SSlogan component for SSSStatic - displays appealing typography with heading, subheading, and paragraphs
"""


def generate_sslogan_html(config):
    """Generate HTML for sslogan section with typography-based content."""
    sslogan_data = config.get('_sslogan')
    
    if not sslogan_data:
        return ""
    
    # Extract sslogan configuration
    heading = sslogan_data.get('heading', '')
    subheading = sslogan_data.get('subheading', '')
    paragraphs = sslogan_data.get('paragraphs', [])
    
    # Handle paragraphs - can be string or list
    if isinstance(paragraphs, str):
        paragraphs = [paragraphs]
    
    if not heading and not subheading and not paragraphs:
        return ""
    
    # Build the sslogan HTML
    sslogan_html = '    <section class="sslogan-section">\n'
    sslogan_html += '        <div class="sslogan-container">\n'
    sslogan_html += '            <div class="sslogan-content">\n'
    
    # Heading
    if heading:
        sslogan_html += f'                <h1 class="sslogan-heading">{heading}</h1>\n'
    
    # Subheading
    if subheading:
        sslogan_html += f'                <h2 class="sslogan-subheading">{subheading}</h2>\n'
    
    # Paragraphs
    for paragraph in paragraphs:
        if paragraph:
            sslogan_html += f'                <p class="sslogan-paragraph">{paragraph}</p>\n'
    
    sslogan_html += '            </div>\n'
    sslogan_html += '        </div>\n'
    sslogan_html += '    </section>\n'
    
    return sslogan_html
