# sssstatic/components/sly.py
"""
Sly component for SSSStatic - displays content with image and text in two columns
"""


def generate_sly_html(config):
    """Generate HTML for sly section with image and text content."""
    sly_data = config.get('_sly')
    
    if not sly_data:
        return ""
    
    # Extract sly configuration
    title = sly_data.get('title', '')
    subtitle = sly_data.get('subtitle', '')
    description = sly_data.get('description', '')
    paragraph = sly_data.get('paragraph', '')
    image_path = sly_data.get('image', '')
    scroll_id = sly_data.get('scrollId', '')
    
    if not title:
        return ""
    
    # Build the sly HTML
    section_id = f' id="{scroll_id}"' if scroll_id else ''
    sly_html = f'    <section class="sly-section"{section_id}>\n'
    sly_html += '        <div class="sly-container">\n'
    sly_html += '            <div class="sly-content-wrapper">\n'
    
    # Left side - Image
    if image_path:
        sly_html += '                <div class="sly-image-section">\n'
        sly_html += '                    <div class="sly-image-block">\n'
        sly_html += f'                        <img src="assets/{image_path}" alt="{title}" class="sly-image">\n'
        sly_html += '                    </div>\n'
        sly_html += '                </div>\n'
    
    # Right side - Text content
    sly_html += '                <div class="sly-text-section">\n'
    
    # Header
    sly_html += '                    <div class="sly-header">\n'
    if subtitle:
        sly_html += f'                        <p class="sly-subtitle">{subtitle}</p>\n'
    
    if title:
        sly_html += f'                        <h1 class="sly-main-title">{title}</h1>\n'
    sly_html += '                    </div>\n'
    
    # Description
    if description:
        sly_html += '                    <div class="sly-description">\n'
        sly_html += f'                        <p class="sly-description-text">{description}</p>\n'
        sly_html += '                    </div>\n'
    
    # Paragraph
    if paragraph:
        sly_html += '                    <div class="sly-paragraph">\n'
        sly_html += f'                        <p class="sly-paragraph-text">{paragraph}</p>\n'
        sly_html += '                    </div>\n'
    
    sly_html += '                </div>\n'
    sly_html += '            </div>\n'
    sly_html += '        </div>\n'
    sly_html += '    </section>\n'
    
    return sly_html
