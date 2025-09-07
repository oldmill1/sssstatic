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
            gap: 2rem;
            margin: 3rem 0;
        }
        
        /* Individual Card */
        .card {
            background: linear-gradient(135deg, var(--card-bg) 0%, rgba(22, 27, 34, 0.8) 100%);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 12px var(--card-shadow);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(88, 166, 255, 0.3), transparent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px var(--card-shadow-hover);
            border-color: var(--card-border-hover);
        }
        
        .card:hover::before {
            opacity: 1;
        }
        
        /* Card Header */
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            gap: 1rem;
        }
        
        .card-title {
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            margin: 0;
            color: var(--card-title);
            line-height: 1.3;
            flex: 1;
            letter-spacing: -0.01em;
            transition: color 0.3s ease;
        }
        
        .card:hover .card-title {
            color: #79c0ff;
        }
        
        /* Status Badges */
        .card-status {
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 0.7rem;
            font-weight: 600;
            padding: 0.4rem 0.9rem;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            white-space: nowrap;
            flex-shrink: 0;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .card:hover .card-status {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        
        .status-active {
            background: linear-gradient(135deg, #10b981, #059669);
            color: #ffffff;
        }
        
        .status-experimental {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #ffffff;
        }
        
        .status-complete {
            background: linear-gradient(135deg, #8b5cf6, #7c3aed);
            color: #ffffff;
        }
        
        .status-on\\ hold {
            background: linear-gradient(135deg, #6b7280, #4b5563);
            color: #ffffff;
        }
        
        .status-development {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #ffffff;
        }
        
        .status-archived {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            color: #ffffff;
        }
        
        .status-unknown {
            background: linear-gradient(135deg, var(--status-unknown-bg), #3c4043);
            color: var(--status-unknown-text);
        }
        
        /* Card Description */
        .card-description {
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: var(--card-description);
            margin: 0 0 2rem 0;
            line-height: 1.7;
            font-size: 1rem;
            font-weight: 400;
            transition: color 0.3s ease;
        }
        
        .card:hover .card-description {
            color: #e1e8ed;
        }
        
        /* Card Footer */
        .card-footer {
            margin-top: auto;
        }
        
        .card-link {
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: inline-flex;
            align-items: center;
            color: var(--card-link);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            padding: 0.75rem 1.5rem;
            border-radius: 12px;
            background: linear-gradient(135deg, var(--card-link-bg), rgba(88, 166, 255, 0.05));
            border: 1px solid var(--card-link-border);
            position: relative;
            overflow: hidden;
            letter-spacing: 0.3px;
        }
        
        .card-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(88, 166, 255, 0.1), transparent);
            transition: left 0.5s ease;
        }
        
        .card-link:hover {
            background: linear-gradient(135deg, var(--card-link-bg-hover), rgba(88, 166, 255, 0.15));
            color: var(--card-link-hover);
            text-decoration: none;
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(88, 166, 255, 0.2);
            border-color: rgba(88, 166, 255, 0.4);
        }
        
        .card-link:hover::before {
            left: 100%;
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
            font-family: 'Source Code Pro', monospace;
            font-size: 1.4rem;
            font-weight: 600;
            text-align: center;
            margin: 2rem 0 3rem 0;
            padding: 0;
            color: #58a6ff;
            line-height: 1.4;
            letter-spacing: 1px;
        }}
        
        @keyframes gradientShift {{
            0%, 100% {{
                background-position: 0% 50%;
            }}
            50% {{
                background-position: 100% 50%;
            }}
        }}
        
        @keyframes pulse {{
            0%, 100% {{
                opacity: 0.6;
                transform: translateX(-50%) scaleX(1);
            }}
            50% {{
                opacity: 1;
                transform: translateX(-50%) scaleX(1.2);
            }}
        }}
        
        @keyframes shimmer {{
            0%, 100% {{
                opacity: 0.3;
                transform: translateX(-50%) scaleX(0.8);
            }}
            50% {{
                opacity: 0.8;
                transform: translateX(-50%) scaleX(1.2);
            }}
        }}
        
        h2 {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #ffffff;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 2.5rem;
            font-weight: 600;
            letter-spacing: -0.02em;
        }}
        
        section {{
            margin: 1.5rem 0;
            padding: 0.5rem;
            background-color: transparent;
            border-radius: 0;
            border: none;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        
        section section {{
            margin: 1rem 0;
            padding: 1.5rem;
            background-color: #161b22;
            border-radius: 12px;
            border: 1px solid #30363d;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }}
        
        section section h2 {{
            margin-top: 0;
            margin-bottom: 1rem;
            font-size: 1.8rem;
        }}
        
        ol, ul {{
            margin: 1rem 0;
            padding-left: 0;
            list-style: none;
        }}
        
        li {{
            margin: 0.8rem 0;
            line-height: 1.6;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #e1e8ed;
            font-size: 1.1rem;
            font-weight: 400;
        }}
        
        ol li {{
            counter-increment: item;
        }}
        
        ol li::before {{
            content: counter(item) ". ";
            color: #58a6ff;
            font-weight: 600;
            font-size: 1.1rem;
            margin-right: 1rem;
        }}
        
        ol {{
            counter-reset: item;
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
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #2c3e50;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 2.5rem;
            font-weight: 600;
            letter-spacing: -0.02em;
        }}
        
        section {{
            margin: 1.5rem 0;
            padding: 0.5rem;
            background-color: transparent;
            border-radius: 0;
            border: none;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        
        section section {{
            margin: 1rem 0;
            padding: 1.5rem;
            background-color: #f8f9fa;
            border-radius: 12px;
            border: 1px solid #e9ecef;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}
        
        section section h2 {{
            margin-top: 0;
            margin-bottom: 1rem;
            font-size: 1.8rem;
        }}
        
        ol, ul {{
            margin: 1rem 0;
            padding-left: 0;
            list-style: none;
        }}
        
        li {{
            margin: 0.8rem 0;
            line-height: 1.6;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #333;
            font-size: 1.1rem;
            font-weight: 400;
        }}
        
        ol li {{
            counter-increment: item;
        }}
        
        ol li::before {{
            content: counter(item) ". ";
            color: #3498db;
            font-weight: 600;
            font-size: 1.1rem;
            margin-right: 1rem;
        }}
        
        ol {{
            counter-reset: item;
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
