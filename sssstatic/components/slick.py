# sssstatic/components/slick.py
"""
Slick component for SSSStatic - displays benefits with icons and an image
"""


def generate_slick_html(config):
    """Generate HTML for slick section with benefits and image."""
    slick_data = config.get('_slick')
    
    if not slick_data:
        return ""
    
    # Extract slick configuration
    subtitle = slick_data.get('subtitle', '')
    title = slick_data.get('title', '')
    highlight_text = slick_data.get('highlight_text', '')
    benefits = slick_data.get('benefits', [])
    image_path = slick_data.get('image', '')
    
    if not benefits:
        return ""
    
    # Build the slick HTML
    slick_html = '    <section class="slick-section">\n'
    slick_html += '        <div class="slick-container">\n'
    slick_html += '            <div class="slick-content-wrapper">\n'
    
    # Left side - Benefits
    slick_html += '                <div class="slick-benefits-section">\n'
    
    # Header
    slick_html += '                    <div class="slick-header">\n'
    if subtitle:
        slick_html += f'                        <p class="slick-subtitle">{subtitle}</p>\n'
    
    if title:
        if highlight_text:
            # Split title and replace highlight_text with highlighted version
            title_parts = title.split(highlight_text)
            if len(title_parts) == 2:
                highlighted_title = f'{title_parts[0]}<span class="slick-highlight">{highlight_text}</span>{title_parts[1]}'
            else:
                highlighted_title = title
        else:
            highlighted_title = title
        slick_html += f'                        <h1 class="slick-main-title">{highlighted_title}</h1>\n'
    slick_html += '                    </div>\n'
    
    # Benefits grid
    slick_html += '                    <div class="slick-benefits-grid">\n'
    for benefit in benefits:
        icon = benefit.get('icon', '✓')
        benefit_title = benefit.get('title', '')
        description = benefit.get('description', '')
        
        slick_html += '                        <div class="slick-benefit-item">\n'
        slick_html += f'                            <div class="slick-benefit-icon">{icon}</div>\n'
        slick_html += '                            <div class="slick-benefit-content">\n'
        if benefit_title:
            slick_html += f'                                <h3 class="slick-benefit-title">{benefit_title}</h3>\n'
        if description:
            slick_html += f'                                <p class="slick-benefit-description">{description}</p>\n'
        slick_html += '                            </div>\n'
        slick_html += '                        </div>\n'
    
    slick_html += '                    </div>\n'
    slick_html += '                </div>\n'
    
    # Right side - Image
    if image_path:
        slick_html += '                <div class="slick-image-section">\n'
        slick_html += '                    <div class="slick-image-block">\n'
        slick_html += f'                        <img src="assets/{image_path}" alt="Slick image" class="slick-phone-image">\n'
        slick_html += '                    </div>\n'
        slick_html += '                </div>\n'
    
    slick_html += '            </div>\n'
    slick_html += '        </div>\n'
    slick_html += '    </section>\n'
    
    return slick_html
