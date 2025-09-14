# sssstatic/components/image.py
"""
Image component for SSSStatic
"""


def generate_image_html(config):
    """Generate image HTML if _image is present."""
    image_html = ""
    if '_image' in config:
        image_config = config['_image']
        if isinstance(image_config, dict):
            image_name = image_config.get('name', '')
            image_alt = image_config.get('alt', 'Image')
            if image_name:
                image_html = f'<div class="header-image"><img src="assets/{image_name}" alt="{image_alt}"></div>'
    
    return image_html
