# sssstatic/components/page_header.py
"""
Page header component for SSSStatic
"""


def generate_page_header_html(config):
    """Generate page header HTML - only render h1 if _title is present."""
    # Use _title for both title and h1, fall back to site name if _title not available
    page_title = config.get('_title', config.get('site', {}).get('name', 'My Site'))
    
    page_header_html = ""
    if '_title' in config:
        # Check for multi-line title first
        if '_multi_line_title' in config:
            multi_title = config['_multi_line_title']
            if isinstance(multi_title, dict):
                title_text = multi_title.get('title', page_title)
                subtitle_text = multi_title.get('sub_title', '')
                page_header_html = f"""    <header class="movie-header">
        <h1 class="movie-title">{title_text}</h1>
        <p class="movie-subtitle">{subtitle_text}</p>
    </header>
"""
        else:
            # Fallback to single line title
            page_header_html = f"    <h1>{page_title}</h1>\n"
    
    return page_header_html
