# sssstatic/styles.py
"""
Styles module for SSSStatic - contains CSS styles for generated sites
"""


def get_card_styles():
    """Return CSS styles for card components."""
    return """
        /* Card Container */
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        /* Individual Card */
        .card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px var(--card-shadow);
            position: relative;
            overflow: hidden;
        }
        
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 25px var(--card-shadow-hover);
            border-color: var(--card-border-hover);
        }
        
        /* Card Header */
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
            gap: 1rem;
        }
        
        .card-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0;
            color: var(--card-title);
            line-height: 1.3;
            flex: 1;
        }
        
        /* Status Badges */
        .card-status {
            font-size: 0.75rem;
            font-weight: 500;
            padding: 0.25rem 0.75rem;
            border-radius: 16px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            white-space: nowrap;
            flex-shrink: 0;
        }
        
        .status-active {
            background: #10b981;
            color: #ffffff;
        }
        
        .status-inactive {
            background: #6b7280;
            color: #ffffff;
        }
        
        .status-development {
            background: #f59e0b;
            color: #ffffff;
        }
        
        .status-archived {
            background: #ef4444;
            color: #ffffff;
        }
        
        .status-unknown {
            background: var(--status-unknown-bg);
            color: var(--status-unknown-text);
        }
        
        /* Card Description */
        .card-description {
            color: var(--card-description);
            margin: 0 0 1.5rem 0;
            line-height: 1.6;
            font-size: 0.95rem;
        }
        
        /* Card Footer */
        .card-footer {
            margin-top: auto;
        }
        
        .card-link {
            display: inline-flex;
            align-items: center;
            color: var(--card-link);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            background: var(--card-link-bg);
            border: 1px solid var(--card-link-border);
        }
        
        .card-link:hover {
            background: var(--card-link-bg-hover);
            color: var(--card-link-hover);
            text-decoration: none;
            transform: translateX(2px);
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .cards-container {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            
            .card {
                padding: 1.25rem;
            }
            
            .card-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
            
            .card-status {
                align-self: flex-start;
            }
        }
    """


def get_dark_theme_css():
    """Return dark theme CSS styles."""
    return f"""
        :root {{
            --card-bg: #161b22;
            --card-border: #30363d;
            --card-shadow: rgba(0, 0, 0, 0.3);
            --card-shadow-hover: rgba(0, 0, 0, 0.5);
            --card-border-hover: #58a6ff;
            --card-title: #f0f6fc;
            --card-description: #e1e8ed;
            --card-link: #58a6ff;
            --card-link-bg: rgba(88, 166, 255, 0.1);
            --card-link-border: rgba(88, 166, 255, 0.2);
            --card-link-bg-hover: rgba(88, 166, 255, 0.2);
            --card-link-hover: #79c0ff;
            --status-unknown-bg: #484f58;
            --status-unknown-text: #f0f6fc;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
            line-height: 1.6;
            color: #e1e8ed;
            background-color: #0d1117;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            min-height: 100vh;
        }}
        
        h1 {{
            color: #f0f6fc;
            border-bottom: 2px solid #30a14e;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            font-weight: 600;
        }}
        
        h2 {{
            color: #58a6ff;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
            font-weight: 500;
        }}
        
        section {{
            margin: 2.5rem 0;
            padding: 1.5rem;
            background-color: #161b22;
            border-radius: 8px;
            border: 1px solid #30363d;
        }}
        
        ol, ul {{
            margin: 1rem 0;
            padding-left: 1.5rem;
        }}
        
        li {{
            margin: 0.8rem 0;
            line-height: 1.7;
        }}
        
        strong {{
            color: #f0f6fc;
            font-weight: 600;
        }}
        
        a {{
            color: #58a6ff;
            text-decoration: none;
            transition: color 0.2s ease;
        }}
        
        a:hover {{
            color: #79c0ff;
            text-decoration: underline;
        }}
        
        br {{
            line-height: 2;
        }}
        
        /* Add some visual hierarchy */
        li strong {{
            display: inline-block;
            min-width: 120px;
        }}
        
        /* Improve spacing between list items */
        ol > li {{
            margin-bottom: 1.5rem;
            padding: 0.5rem 0;
        }}
        
        /* Style for nested content in list items */
        li > br:last-child {{
            display: none;
        }}
        
        /* Header image styling */
        .header-image {{
            text-align: center;
            margin: 2rem 0 3rem 0;
        }}
        
        .header-image img {{
            max-width: 400px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }}
        
        .header-image img:hover {{
            transform: scale(1.02);
        }}
        
        {get_card_styles()}
    """


def get_light_theme_css():
    """Return light theme CSS styles."""
    return f"""
        :root {{
            --card-bg: #ffffff;
            --card-border: #e1e5e9;
            --card-shadow: rgba(0, 0, 0, 0.1);
            --card-shadow-hover: rgba(0, 0, 0, 0.15);
            --card-border-hover: #3498db;
            --card-title: #2c3e50;
            --card-description: #5a6c7d;
            --card-link: #3498db;
            --card-link-bg: rgba(52, 152, 219, 0.1);
            --card-link-border: rgba(52, 152, 219, 0.2);
            --card-link-bg-hover: rgba(52, 152, 219, 0.2);
            --card-link-hover: #2980b9;
            --status-unknown-bg: #95a5a6;
            --status-unknown-text: #ffffff;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #ffffff;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            min-height: 100vh;
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            font-weight: 600;
        }}
        
        h2 {{
            color: #34495e;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
            font-weight: 500;
        }}
        
        section {{
            margin: 2.5rem 0;
            padding: 1.5rem;
            background-color: #f8f9fa;
            border-radius: 8px;
            border: 1px solid #e9ecef;
        }}
        
        ol, ul {{
            margin: 1rem 0;
            padding-left: 1.5rem;
        }}
        
        li {{
            margin: 0.8rem 0;
            line-height: 1.7;
        }}
        
        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
            transition: color 0.2s ease;
        }}
        
        a:hover {{
            color: #2980b9;
            text-decoration: underline;
        }}
        
        br {{
            line-height: 2;
        }}
        
        /* Add some visual hierarchy */
        li strong {{
            display: inline-block;
            min-width: 120px;
        }}
        
        /* Improve spacing between list items */
        ol > li {{
            margin-bottom: 1.5rem;
            padding: 0.5rem 0;
        }}
        
        /* Style for nested content in list items */
        li > br:last-child {{
            display: none;
        }}
        
        /* Header image styling */
        .header-image {{
            text-align: center;
            margin: 2rem 0 3rem 0;
        }}
        
        .header-image img {{
            max-width: 400px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }}
        
        .header-image img:hover {{
            transform: scale(1.02);
        }}
        
        {get_card_styles()}
    """


def get_theme_css(theme_name="dark"):
    """Get CSS for specified theme."""
    themes = {
        "dark": get_dark_theme_css,
        "light": get_light_theme_css,
    }

    theme_function = themes.get(theme_name, get_dark_theme_css)
    return theme_function()
