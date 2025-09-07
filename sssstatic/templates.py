# sssstatic/templates.py
"""
Templates module for SSSStatic - contains all file templates
"""


def get_config_template(project_name):
    """Return the _config.yml template content."""
    return f"""# SSSStatic Configuration
site_name: "{project_name}"
"""


def generate_site_html(config, content_html):
    """Generate complete HTML page from config and content HTML."""
    site_name = config.get('site_name', 'My Site')

    # Generate image HTML if _image is present
    image_html = ""
    if '_image' in config:
        image_config = config['_image']
        if isinstance(image_config, dict):
            image_name = image_config.get('name', '')
            image_alt = image_config.get('alt', 'Image')
            if image_name:
                image_html = f'<div class="header-image"><img src="assets/{image_name}" alt="{image_alt}"></div>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name}</title>
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
    <h1>{site_name}</h1>
    {image_html}
    {content_html}
</body>
</html>"""

    return html
