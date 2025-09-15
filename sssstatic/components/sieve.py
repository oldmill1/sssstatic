# sssstatic/components/sieve.py
"""
Sieve component for SSSStatic - displays appealing typography with heading, subheading, and paragraphs
"""


def generate_sieve_html(config):
    """Generate HTML for sieve section with typography-based content."""
    sieve_data = config.get('_sieve')
    
    if not sieve_data:
        return ""
    
    # Extract sieve configuration
    heading = sieve_data.get('heading', '')
    subheading = sieve_data.get('subheading', '')
    paragraphs = sieve_data.get('paragraphs', [])
    
    # Handle paragraphs - can be string or list
    if isinstance(paragraphs, str):
        paragraphs = [paragraphs]
    
    if not heading and not subheading and not paragraphs:
        return ""
    
    # Build the sieve HTML
    sieve_html = '    <section class="sieve-section">\n'
    sieve_html += '        <div class="sieve-container">\n'
    sieve_html += '            <div class="sieve-content">\n'
    
    # Heading
    if heading:
        sieve_html += f'                <h1 class="sieve-heading">{heading}</h1>\n'
    
    # Subheading
    if subheading:
        sieve_html += f'                <h2 class="sieve-subheading">{subheading}</h2>\n'
    
    # Paragraphs
    for paragraph in paragraphs:
        if paragraph:
            sieve_html += f'                <p class="sieve-paragraph">{paragraph}</p>\n'
    
    sieve_html += '            </div>\n'
    sieve_html += '        </div>\n'
    sieve_html += '    </section>\n'
    
    return sieve_html
