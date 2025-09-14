# sssstatic/converter.py
"""
Converter module for SSSStatic - handles YAML to HTML conversion
"""


def parse_markdown_links(text):
    """Parse markdown-style links [text](url) in a string."""
    import re
    # Pattern to match [text](url) format
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)
        return f'<code><a href="{link_url}" target="_blank" rel="noopener noreferrer">{link_text}</a></code>'
    
    return re.sub(link_pattern, replace_link, text)


def convert_to_html(data, key=None, in_list_item=False):
    """Recursively convert YAML data to HTML."""
    if isinstance(data, dict):
        html = ""
        for k, v in data.items():
            # Skip system tags (underscore-prefixed) and reserved tags
            if k.startswith('_') or k in ["site"]:
                continue

            if in_list_item:
                # Inside a list item, make it more compact
                if isinstance(v, str):
                    if v.startswith(('http://', 'https://')):
                        html += f'<strong>{k.replace("_", " ").title()}:</strong> <a href="{v}">{v}</a><br>\n'
                    else:
                        html += f'<strong>{k.replace("_", " ").title()}:</strong> {parse_markdown_links(v)}<br>\n'
                else:
                    html += f'<strong>{k.replace("_", " ").title()}:</strong> {convert_to_html(v, k, in_list_item)}<br>\n'
            else:
                # Top-level sections
                html += f"<section>\n<h2>{k.replace('_', ' ').title()}</h2>\n"
                html += convert_to_html(v, k, False)
                html += "</section>\n"
        return html

    elif isinstance(data, list):
        html = "<ol>\n"
        for item in data:
            html += "<li>"
            # Parse item to extract main term and description
            if isinstance(item, str):
                # Check for markdown links first
                if '[' in item and '](' in item and ')' in item:
                    # Contains markdown link, parse it
                    html += parse_markdown_links(item)
                # Handle format like "Python (automation and AI tools)"
                elif '(' in item and ')' in item:
                    parts = item.split('(', 1)
                    main_term = parts[0].strip()
                    description = '(' + parts[1].strip()
                    html += f"<code>{main_term}</code> <dim>{description}</dim>"
                else:
                    html += f"<code>{item}</code>"
            else:
                html += convert_to_html(item, key, True)
            html += "</li>\n"
        html += "</ol>\n"
        return html

    elif isinstance(data, str):
        # Check if it looks like a URL
        if data.startswith(('http://', 'https://')):
            return f'<a href="{data}">{data}</a>'
        # Parse markdown links
        return parse_markdown_links(data)

    else:
        return str(data)
