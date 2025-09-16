# sssstatic/components/text.py
"""
Text component for SSSStatic - renders configurable text with styling options

Available Properties:
- content: (string) The text content to display
- type: (string) HTML element type - "h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "div", etc.
- size: (string) Text size - "small", "medium", "large", "xlarge", "xxlarge", "huge"
- weight: (string) Font weight - "thin", "normal", "bold", "black"
- fontWeight: (string) Specific font weight - "400", "500", "600", "700", etc.
- fontFamily: (string) Font family - "primary", "heading", "display", "byline", "mono", "system"
- letterSpacing: (string) Letter spacing - "tight", "normal", "wide", or specific value like "-0.02em"
- paddingInline: (string) Horizontal margin - "0", "0.5rem", "1rem", "2rem", etc.
- paddingBlock: (string) Vertical margin - "0", "0.5rem", "1rem", "2rem", etc.
- marginBottom: (string) Bottom margin - "0", "0.5rem", "1rem", "2rem", etc.
- spacerTop: (string) Top padding - "0", "0.5rem", "1rem", "2rem", etc.
- spacerBottom: (string) Bottom padding - "0", "0.5rem", "1rem", "2rem", etc.
- lineHeight: (string) Line height - "small", "medium", "large"
- emojiLeft: (string) Optional emoji to display to the left of text
- emojiRight: (string) Optional emoji to display to the right of text
- emojiTop: (string) Optional emoji to display above the text

Example Usage:
_text:
  content: "Hello World"
  type: "h1"
  size: "xlarge"
  weight: "bold"
  paddingBlock: "1rem"
  spacerTop: "2rem"
  spacerBottom: "1rem"
  emojiLeft: "👋"
"""


def generate_text_html(config):
    """Generate HTML for text component with configurable properties."""
    text_data = config.get('_text')
    
    if not text_data:
        return ""
    
    # Extract text properties with defaults
    text_content = text_data.get('content', '')
    element_type = text_data.get('type', 'p')  # Default to paragraph
    size = text_data.get('size', 'medium')  # small, medium, large, xlarge
    weight = text_data.get('weight', 'normal')  # thin, normal, bold
    font_weight = text_data.get('fontWeight', '')  # Specific weight like "500", "600"
    font_family = text_data.get('fontFamily', '')  # primary, heading, display, etc.
    letter_spacing = text_data.get('letterSpacing', '')  # tight, normal, wide, or specific value
    line_height = text_data.get('lineHeight', 'medium')  # small, medium, large
    padding_inline = text_data.get('paddingInline', '0')
    padding_block = text_data.get('paddingBlock', '0')
    margin_bottom = text_data.get('marginBottom', '')
    spacer_top = text_data.get('spacerTop', '')
    spacer_bottom = text_data.get('spacerBottom', '')
    emoji_left = text_data.get('emojiLeft', '')
    emoji_right = text_data.get('emojiRight', '')
    emoji_top = text_data.get('emojiTop', '')
    align = text_data.get('align', 'center')  # left, center, right
    
    if not text_content:
        return ""
    
    # Build CSS classes based on properties
    css_classes = ['text-component']
    css_classes.append(f'text-size-{size}')
    css_classes.append(f'text-weight-{weight}')
    css_classes.append(f'text-line-height-{line_height}')
    css_classes.append(f'align-{align}')
    
    # Add font family class if specified
    if font_family:
        css_classes.append(f'font-family-{font_family}')
    
    # Add letter spacing class if specified
    if letter_spacing:
        css_classes.append(f'letter-spacing-{letter_spacing}')
    
    # Build inline styles for padding and new properties
    inline_styles = []
    if padding_inline != '0':
        inline_styles.append(f'margin-left: {padding_inline};')
        inline_styles.append(f'margin-right: {padding_inline};')
    if padding_block != '0':
        inline_styles.append(f'margin-top: {padding_block};')
        inline_styles.append(f'margin-bottom: {padding_block};')
    if margin_bottom:
        inline_styles.append(f'margin-bottom: {margin_bottom};')
    if spacer_top:
        inline_styles.append(f'padding-top: {spacer_top};')
    if spacer_bottom:
        inline_styles.append(f'padding-bottom: {spacer_bottom};')
    if font_weight:
        inline_styles.append(f'font-weight: {font_weight};')
    if letter_spacing and letter_spacing not in ['tight', 'normal', 'wide']:
        # If it's a specific value like "-0.02em", use it directly
        inline_styles.append(f'letter-spacing: {letter_spacing};')
    
    style_attr = f' style="{"; ".join(inline_styles)}"' if inline_styles else ''
    
    # Build the text content with emojis
    text_with_emojis = ""
    
    # Add top emoji if specified
    if emoji_top:
        text_with_emojis += f'<div class="emoji-top">{emoji_top}</div>'
    
    # Add left emoji, text content, and right emoji
    text_with_emojis += f'<span class="text-content">'
    if emoji_left:
        text_with_emojis += f'<span class="emoji-left">{emoji_left}</span>'
    text_with_emojis += text_content
    if emoji_right:
        text_with_emojis += f'<span class="emoji-right">{emoji_right}</span>'
    text_with_emojis += '</span>'
    
    # Build the component HTML (use text-component-container directly, no extra wrapper)
    component_html = f'        <{element_type} class="{" ".join(css_classes)}"{style_attr}>\n'
    component_html += f'            {text_with_emojis}\n'
    component_html += f'        </{element_type}>\n'
    
    return component_html
