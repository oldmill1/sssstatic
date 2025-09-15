# sssstatic/components/topbar.py
"""
TopBar component for SSSStatic - dark mode navigation bar
"""


def generate_topbar_html(config):
    """Generate TopBar HTML - dark mode navigation with CTA button."""
    from ..site_builder import extract_pages, extract_anchor_links
    
    pages = extract_pages(config)
    anchor_links = extract_anchor_links(config)
    
    # Get TopBar configuration
    topbar_config = config.get('_topbar', {})
    site_name = topbar_config.get('title', config.get('site', {}).get('name', 'My Site'))
    cta_text = topbar_config.get('cta', 'Contact')
    cta_link = topbar_config.get('link', '#')
    title_font = topbar_config.get('titleFont', None)
    
    topbar_html = '    <div class="topbar">\n'
    topbar_html += '        <div class="topbar-container">\n'
    
    # Add brand/title on the left
    topbar_html += f'            <a href="index.html" class="topbar-brand">{site_name}</a>\n'
    
    # Add navigation links in the middle
    # Prioritize anchor links over pages if both exist
    if anchor_links:
        topbar_html += '            <nav class="topbar-nav">\n'
        topbar_html += '                <ul class="topbar-list">\n'
        
        # Add anchor links
        for link in anchor_links:
            link_name = link.get('name', 'Untitled')
            scroll_to = link.get('scrollTo', '')
            topbar_html += f'                    <li class="topbar-item"><a href="#{scroll_to}" class="topbar-link anchor-link" data-scroll-to="{scroll_to}">{link_name}</a></li>\n'
        
        topbar_html += '                </ul>\n'
        topbar_html += '            </nav>\n'
    elif pages:
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
    from .button import generate_button_html
    anchor_link = cta_link.startswith('#')
    topbar_html += '            <div class="topbar-cta-wrapper">\n'
    topbar_html += '                '
    topbar_html += generate_button_html(cta_text, cta_link, 'cta', 'default', 'small', 'lightning', anchor_link)
    topbar_html += '\n            </div>\n'
    
    topbar_html += '        </div>\n'
    topbar_html += '    </div>\n'
    
    return topbar_html
