# sssstatic/styles/type.py
"""
Type module for SSSStatic - centralized font definitions and Google Fonts imports
"""

def get_google_fonts_imports(custom_fonts=None):
    """Return HTML link tags for Google Fonts imports."""
    base_imports = """    <link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;600&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Original+Surfer:wght@400&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">"""
    
    if custom_fonts:
        custom_imports = ""
        for font in custom_fonts:
            if font and font.strip():
                # Format font name for Google Fonts URL (replace spaces with +)
                formatted_font = font.strip().replace(' ', '+')
                custom_imports += f'\n    <link href="https://fonts.googleapis.com/css2?family={formatted_font}:wght@100..900&display=swap" rel="stylesheet">'
        return base_imports + custom_imports
    
    return base_imports


def get_font_families():
    """Return font family definitions as CSS custom properties."""
    return """
        :root {
            /* Primary font families */
            --font-primary: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-heading: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-display: 'Original Surfer', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-byline: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-mono: 'Source Code Pro', 'JetBrains Mono', 'Fira Code', monospace;
            --font-system: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
        }"""


def get_font_sizes():
    """Return font size definitions as CSS custom properties."""
    return """
        :root {
            /* Font sizes */
            --font-size-xs: 0.7rem;
            --font-size-sm: 0.9rem;
            --font-size-base: 1rem;
            --font-size-lg: 1.1rem;
            --font-size-xl: 1.4rem;
            --font-size-2xl: 1.8rem;
            --font-size-3xl: 2.2rem;
            --font-size-4xl: 2.8rem;
            --font-size-5xl: 3.2rem;
        }"""


def get_font_weights():
    """Return font weight definitions as CSS custom properties."""
    return """
        :root {
            /* Font weights */
            --font-weight-normal: 400;
            --font-weight-medium: 500;
            --font-weight-semibold: 600;
            --font-weight-bold: 700;
        }"""


def get_font_styles():
    """Return complete font styles CSS."""
    return f"""{get_font_families()}
{get_font_sizes()}
{get_font_weights()}"""


# Font family constants for easy reference
FONT_PRIMARY = "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_HEADING = "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_DISPLAY = "'Original Surfer', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_BYLINE = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_MONO = "'Source Code Pro', 'JetBrains Mono', 'Fira Code', monospace"
FONT_SYSTEM = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_BODY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace"

# Font size constants
FONT_SIZE_XS = "0.7rem"
FONT_SIZE_SM = "0.9rem"
FONT_SIZE_BASE = "1rem"
FONT_SIZE_LG = "1.1rem"
FONT_SIZE_XL = "1.4rem"
FONT_SIZE_2XL = "1.8rem"
FONT_SIZE_3XL = "2.2rem"
FONT_SIZE_4XL = "2.8rem"
FONT_SIZE_5XL = "3.2rem"

# Font weight constants
FONT_WEIGHT_NORMAL = "400"
FONT_WEIGHT_MEDIUM = "500"
FONT_WEIGHT_SEMIBOLD = "600"
FONT_WEIGHT_BOLD = "700"
