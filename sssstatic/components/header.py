# sssstatic/components/header.py
"""
Header component for SSSStatic
"""


def generate_header_html(config):
    """Generate header HTML - always shows site name, adds page links if available."""
    from ..site_builder import extract_pages
    
    pages = extract_pages(config)
    
    # Get site name for brand
    site_name = config.get('site', {}).get('name', 'My Site')
    
    header_html = '    <header class="site-header">\n'
    
    # Add brand/title on the left
    header_html += f'        <a href="index.html" class="header-brand">{site_name}</a>\n'
    
    # Only add navigation links if there are pages
    if pages:
        # Add navigation links on the right
        header_html += '        <ul class="header-list">\n'
        
        # Add home link
        header_html += '            <li class="header-item"><a href="index.html" class="header-link">Home</a></li>\n'
        
        # Add page links
        for page in pages:
            page_name = page.get('_name', 'Untitled')
            page_filename = page_name.lower().replace(' ', '_') + '.html'
            header_html += f'            <li class="header-item"><a href="{page_filename}" class="header-link">{page_name}</a></li>\n'
        
        header_html += '        </ul>\n'
    
    header_html += '    </header>\n'
    return header_html
