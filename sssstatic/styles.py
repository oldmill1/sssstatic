# sssstatic/styles.py
"""
Styles module for SSSStatic - contains CSS styles for generated sites
"""


def get_dark_theme_css():
    """Return dark theme CSS styles."""
    return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
            line-height: 1.6;
            color: #e1e8ed;
            background-color: #0d1117;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            min-height: 100vh;
        }
        
        h1 {
            color: #f0f6fc;
            border-bottom: 2px solid #30a14e;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            font-weight: 600;
        }
        
        h2 {
            color: #58a6ff;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
            font-weight: 500;
        }
        
        section {
            margin: 2.5rem 0;
            padding: 1.5rem;
            background-color: #161b22;
            border-radius: 8px;
            border: 1px solid #30363d;
        }
        
        ol, ul {
            margin: 1rem 0;
            padding-left: 1.5rem;
        }
        
        li {
            margin: 0.8rem 0;
            line-height: 1.7;
        }
        
        strong {
            color: #f0f6fc;
            font-weight: 600;
        }
        
        a {
            color: #58a6ff;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        
        a:hover {
            color: #79c0ff;
            text-decoration: underline;
        }
        
        br {
            line-height: 2;
        }
        
        /* Add some visual hierarchy */
        li strong {
            display: inline-block;
            min-width: 120px;
        }
        
        /* Improve spacing between list items */
        ol > li {
            margin-bottom: 1.5rem;
            padding: 0.5rem 0;
        }
        
        /* Style for nested content in list items */
        li > br:last-child {
            display: none;
        }
        
        /* Header image styling */
        .header-image {
            text-align: center;
            margin: 2rem 0 3rem 0;
        }
        
        .header-image img {
            max-width: 400px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }
        
        .header-image img:hover {
            transform: scale(1.02);
        }
    """


def get_light_theme_css():
    """Return light theme CSS styles."""
    return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #ffffff;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            min-height: 100vh;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            font-weight: 600;
        }
        
        h2 {
            color: #34495e;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
            font-weight: 500;
        }
        
        section {
            margin: 2.5rem 0;
            padding: 1.5rem;
            background-color: #f8f9fa;
            border-radius: 8px;
            border: 1px solid #e9ecef;
        }
        
        ol, ul {
            margin: 1rem 0;
            padding-left: 1.5rem;
        }
        
        li {
            margin: 0.8rem 0;
            line-height: 1.7;
        }
        
        strong {
            color: #2c3e50;
            font-weight: 600;
        }
        
        a {
            color: #3498db;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        
        a:hover {
            color: #2980b9;
            text-decoration: underline;
        }
        
        br {
            line-height: 2;
        }
        
        /* Add some visual hierarchy */
        li strong {
            display: inline-block;
            min-width: 120px;
        }
        
        /* Improve spacing between list items */
        ol > li {
            margin-bottom: 1.5rem;
            padding: 0.5rem 0;
        }
        
        /* Style for nested content in list items */
        li > br:last-child {
            display: none;
        }
        
        /* Header image styling */
        .header-image {
            text-align: center;
            margin: 2rem 0 3rem 0;
        }
        
        .header-image img {
            max-width: 400px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .header-image img:hover {
            transform: scale(1.02);
        }
    """


def get_theme_css(theme_name="dark"):
    """Get CSS for specified theme."""
    themes = {
        "dark": get_dark_theme_css,
        "light": get_light_theme_css,
    }

    theme_function = themes.get(theme_name, get_dark_theme_css)
    return theme_function()
