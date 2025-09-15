# sssstatic/components/stickers.py
"""
Stickers component for SSSStatic - renders configurable stickers from PNG files

Available Properties:
- name: (string) The sticker name (corresponds to PNG filename in sssstatic/stickers/)
- size: (string) Sticker size - "small", "medium", "large", "xlarge" (default: "medium")
- position: (string) Sticker position - "left", "center", "right" (default: "center")
- opacity: (float) Sticker opacity - 0.0 to 1.0 (default: 1.0)
- rotation: (int) Sticker rotation in degrees (default: 0)
- animation: (string) Animation type - "none", "bounce", "spin", "float", "pulse" (default: "none")

Example Usage:
_sticker:
  name: "rocket"
  size: "large"
  position: "center"
  opacity: 0.8
  rotation: 15
  animation: "bounce"
"""

import os


def generate_sticker_html(config):
    """Generate HTML for sticker component with configurable properties."""
    sticker_data = config.get('_sticker')
    
    if not sticker_data:
        return ""
    
    # Extract sticker properties with defaults
    name = sticker_data.get('name', '')
    size = sticker_data.get('size', 'medium')
    position = sticker_data.get('position', 'center')
    opacity = sticker_data.get('opacity', 1.0)
    rotation = sticker_data.get('rotation', 0)
    animation = sticker_data.get('animation', 'none')
    align = sticker_data.get('align', 'center')  # left, center, right
    
    if not name:
        return ""
    
    # Build CSS classes based on properties
    css_classes = ['sticker-component']
    css_classes.append(f'sticker-size-{size}')
    css_classes.append(f'sticker-position-{position}')
    css_classes.append(f'align-{align}')
    
    if animation != 'none':
        css_classes.append(f'sticker-animation-{animation}')
    
    # Build inline styles for dynamic properties
    inline_styles = []
    
    # Opacity
    if opacity != 1.0:
        inline_styles.append(f'opacity: {opacity};')
    
    # Rotation
    if rotation != 0:
        inline_styles.append(f'transform: rotate({rotation}deg);')
    
    # Background image
    sticker_path = f'/assets/stickers/{name}.png'
    inline_styles.append(f'background-image: url({sticker_path});')
    
    style_attr = f' style="{"; ".join(inline_styles)}"' if inline_styles else ''
    
    # Build the sticker HTML
    sticker_html = f'        <div class="{" ".join(css_classes)}"{style_attr}></div>\n'
    
    return sticker_html


def get_available_stickers():
    """Get list of available sticker names from the stickers directory."""
    stickers_dir = os.path.join(os.path.dirname(__file__), '..', 'stickers')
    
    if not os.path.exists(stickers_dir):
        return []
    
    stickers = []
    for filename in os.listdir(stickers_dir):
        if filename.lower().endswith('.png'):
            # Remove .png extension to get sticker name
            sticker_name = os.path.splitext(filename)[0]
            stickers.append(sticker_name)
    
    return stickers


# Sticker size mappings for easy reference
STICKER_SIZES = {
    'small': '32px x 32px - Small decorative sticker',
    'medium': '64px x 64px - Standard sticker size',
    'large': '128px x 128px - Large prominent sticker',
    'xlarge': '256px x 256px - Extra large sticker for emphasis'
}

# Sticker position mappings
STICKER_POSITIONS = {
    'left': 'Align sticker to the left',
    'center': 'Center the sticker (default)',
    'right': 'Align sticker to the right'
}

# Sticker animation mappings
STICKER_ANIMATIONS = {
    'none': 'No animation (default)',
    'bounce': 'Gentle bouncing animation',
    'spin': 'Continuous rotation',
    'float': 'Floating up and down motion',
    'pulse': 'Pulsing scale animation'
}

