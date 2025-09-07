# sssstatic/converter.py
"""
Converter module for SSSStatic - handles YAML to HTML conversion
"""


def convert_to_html(data, key=None, in_list_item=False):
    """Recursively convert YAML data to HTML."""
    if isinstance(data, dict):
        html = ""
        for k, v in data.items():
            if k == "site_name":  # Skip the reserved site_name
                continue

            if in_list_item:
                # Inside a list item, make it more compact
                if isinstance(v, str):
                    if v.startswith(('http://', 'https://')):
                        html += f'<strong>{k.replace("_", " ").title()}:</strong> <a href="{v}">{v}</a><br>\n'
                    else:
                        html += f'<strong>{k.replace("_", " ").title()}:</strong> {v}<br>\n'
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
            html += convert_to_html(item, key, True)
            html += "</li>\n"
        html += "</ol>\n"
        return html

    elif isinstance(data, str):
        # Check if it looks like a URL
        if data.startswith(('http://', 'https://')):
            return f'<a href="{data}">{data}</a>'
        return data

    else:
        return str(data)
