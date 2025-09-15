# sssstatic/components/text.py
"""
Text component for SSSStatic - renders configurable text with styling options

Available Properties:
- content: (string) The text content to display
- type: (string) HTML element type - "h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "div", etc.
- size: (string) Text size - "small", "medium", "large", "xlarge", "xxlarge", "huge"
- weight: (string) Font weight - "thin", "normal", "bold", "black"
- paddingInline: (string) Horizontal margin - "0", "0.5rem", "1rem", "2rem", etc.
- paddingBlock: (string) Vertical margin - "0", "0.5rem", "1rem", "2rem", etc.
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
    line_height = text_data.get('lineHeight', 'medium')  # small, medium, large
    padding_inline = text_data.get('paddingInline', '0')
    padding_block = text_data.get('paddingBlock', '0')
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
    
    # Build inline styles for padding (use margin instead to avoid bleeding)
    inline_styles = []
    if padding_inline != '0':
        inline_styles.append(f'margin-left: {padding_inline};')
        inline_styles.append(f'margin-right: {padding_inline};')
    if padding_block != '0':
        inline_styles.append(f'margin-top: {padding_block};')
        inline_styles.append(f'margin-bottom: {padding_block};')
    
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
