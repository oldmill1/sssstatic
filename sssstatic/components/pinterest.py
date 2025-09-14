# sssstatic/components/pinterest.py
"""
Pinterest masonry layout component for SSSStatic
"""


def generate_pinterest_html(config):
    """Generate HTML for Pinterest-style masonry layout."""
    pinterest_html = ""
    pinterest_items = []

    # Collect all _pinterest entries
    for key, value in config.items():
        if key == '_pinterest':
            if isinstance(value, list):
                pinterest_items.extend(value)
            else:
                pinterest_items.append(value)

    if not pinterest_items:
        return ""

    # Generate Pinterest masonry container
    pinterest_html = '<div class="pinterest-container">\n'

    for item in pinterest_items:
        if isinstance(item, dict):
            # Extract item properties
            image_url = item.get('image', '')
            url = item.get('url', '#')
            
            # Handle local images (prefix with assets/) or use picsum for placeholder images
            if not image_url:
                # Generate optimized dimensions for tight masonry layout
                import random
                # More varied sizes optimized for space efficiency
                size_types = [
                    (random.randint(180, 250), random.randint(300, 450)),  # Tall
                    (random.randint(250, 350), random.randint(180, 250)),  # Wide
                    (random.randint(200, 280), random.randint(200, 280)),  # Square
                    (random.randint(150, 220), random.randint(400, 600)),  # Very tall
                    (random.randint(300, 400), random.randint(150, 220)),  # Very wide
                    (random.randint(180, 250), random.randint(250, 350)),  # Medium tall
                    (random.randint(220, 300), random.randint(180, 250)),  # Medium wide
                ]
                width, height = random.choice(size_types)
                image_url = f"https://picsum.photos/{width}/{height}?random={random.randint(1, 1000)}"
            elif not image_url.startswith(('http://', 'https://')):
                # Local image - prefix with assets/ like spotlight component does
                image_url = f"assets/{image_url}"
            
            # Generate Pinterest item HTML - no captions, just images
            pinterest_html += f'''    <div class="pinterest-item">
        <a href="{url}" class="pinterest-link" target="_blank" rel="noopener noreferrer">
            <div class="pinterest-image-container">
                <img src="{image_url}" alt="" class="pinterest-image" loading="lazy">
            </div>
        </a>
    </div>
'''
        elif isinstance(item, str):
            # Handle simple string format (just image filename)
            image_url = item
            url = '#'
            
            # Handle local images (prefix with assets/) or use picsum for placeholder images
            if not image_url.startswith(('http://', 'https://')):
                # Local image - prefix with assets/ like spotlight component does
                image_url = f"assets/{image_url}"
            
            # Generate Pinterest item HTML - no captions, just images
            pinterest_html += f'''    <div class="pinterest-item">
        <a href="{url}" class="pinterest-link" target="_blank" rel="noopener noreferrer">
            <div class="pinterest-image-container">
                <img src="{image_url}" alt="" class="pinterest-image" loading="lazy">
            </div>
        </a>
    </div>
'''

    pinterest_html += '</div>\n'
    return pinterest_html
