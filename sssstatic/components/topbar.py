# sssstatic/components/topbar.py
"""
TopBar component for SSSStatic - dark mode navigation bar
"""


def generate_topbar_html(config):
    """Generate TopBar HTML - dark mode navigation with CTA button."""
    from ..site_builder import extract_pages
    
    pages = extract_pages(config)
    
    # Get TopBar configuration
    topbar_config = config.get('_topbar', {})
    site_name = topbar_config.get('title', config.get('site', {}).get('name', 'My Site'))
    cta_text = topbar_config.get('cta', 'Contact')
    cta_link = topbar_config.get('link', '#')
    
    topbar_html = '    <div class="topbar">\n'
    topbar_html += '        <div class="topbar-container">\n'
    
    # Add brand/title on the left
    topbar_html += f'            <a href="index.html" class="topbar-brand">{site_name}</a>\n'
    
    # Add navigation links in the middle
    if pages:
        topbar_html += '            <nav class="topbar-nav">\n'
        topbar_html += '                <ul class="topbar-list">\n'
        
        # Add page links
        for page in pages:
            page_name = page.get('_name', 'Untitled')
            page_filename = page_name.lower().replace(' ', '_') + '.html'
            topbar_html += f'                    <li class="topbar-item"><a href="{page_filename}" class="topbar-link">{page_name}</a></li>\n'
        
        topbar_html += '                </ul>\n'
        topbar_html += '            </nav>\n'
    
    # Add CTA button on the right
    topbar_html += f'            <a href="{cta_link}" class="topbar-cta">\n'
    topbar_html += '                <span class="topbar-cta-icon">⚡</span>\n'
    topbar_html += f'                <span class="topbar-cta-text">{cta_text}</span>\n'
    topbar_html += '            </a>\n'
    
    topbar_html += '        </div>\n'
    topbar_html += '    </div>\n'
    
    return topbar_html
