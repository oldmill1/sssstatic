# sssstatic/styles.py
"""
Styles module for SSSStatic - contains CSS styles for generated sites
"""

from .styles.header import get_header_styles
from .styles.cards import get_card_styles




def get_hero_banner_styles():
    """Return CSS styles for hero banner component."""
    return """
        /* Hero Banner Styles */
        .hero-banner {
            margin: 0 0 1rem 0;
            padding: 0;
        }
        
        .hero-content {
            display: flex;
            align-items: center;
            gap: 3rem;
            margin-bottom: 4rem;
            padding: 2rem 0;
        }
        
        .hero-image {
            flex: 1;
            text-align: center;
        }
        
        .hero-image img {
            max-width: 100%;
            height: auto;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .hero-image img:hover {
            transform: scale(1.02);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
        }
        
        .hero-text {
            flex: 1;
            padding-left: 2rem;
        }
        
        .hero-headline {
            font-family: 'Henny Penny', cursive;
            font-size: 3.5rem;
            font-weight: 400;
            color: #ffffff;
            margin: 0 0 1rem 0;
            line-height: 1.1;
            letter-spacing: 1px;
        }
        
        .hero-subtitle {
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 1.3rem;
            color: #e1e8ed;
            margin: 0;
            line-height: 1.5;
            font-weight: 400;
        }
        
        /* Three Columns Layout */
        .three-columns {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .column {
            text-align: center;
            padding: 1.5rem;
            background: rgba(22, 27, 34, 0.3);
            border: 1px solid rgba(88, 166, 255, 0.1);
            border-radius: 16px;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        
        .column:hover {
            transform: translateY(-4px);
            border-color: rgba(88, 166, 255, 0.3);
            background: rgba(22, 27, 34, 0.5);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        .column-image {
            margin-bottom: 1.5rem;
        }
        
        .column-image img {
            width: 100%;
            max-width: 280px;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }
        
        .column:hover .column-image img {
            transform: scale(1.05);
        }
        
        .column-title {
            font-family: 'Henny Penny', cursive;
            font-size: 2.2rem;
            font-weight: 400;
            color: #ffffff;
            margin: 0 0 1rem 0;
            letter-spacing: 0.5px;
        }
        
        .column-description {
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 1rem;
            color: #e1e8ed;
            margin: 0;
            line-height: 1.6;
            font-weight: 400;
        }
        
        /* Responsive Hero Banner */
        @media (max-width: 1024px) {
            .hero-content {
                flex-direction: column;
                gap: 2rem;
                text-align: center;
            }
            
            .hero-text {
                padding-left: 0;
            }
            
            .hero-headline {
                font-size: 3rem;
            }
            
            .three-columns {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }
        }
        
        @media (max-width: 768px) {
            .hero-banner {
                margin: 0 0 1rem 0;
            }
            
            .hero-content {
                margin-bottom: 3rem;
            }
            
            .hero-headline {
                font-size: 2.5rem;
            }
            
            .hero-subtitle {
                font-size: 1.1rem;
            }
            
            .column {
                padding: 1rem;
            }
            
            .column-title {
                font-size: 1.8rem;
            }
            
            .column-description {
                font-size: 0.95rem;
            }
        }
    """


def get_footer_styles():
    """Return CSS styles for footer component."""
    from .styles.footer import get_footer_styles as _get_footer_styles
    return _get_footer_styles()


def get_dark_theme_css():
    """Return dark theme CSS styles."""
    return f"""
        :root {{
            --card-bg: #161b22;
            --card-border: #30363d;
            --card-shadow: rgba(0, 0, 0, 0.3);
            --card-shadow-hover: rgba(0, 0, 0, 0.5);
            --card-border-hover: rgb(128, 182, 204);
            --card-title: #f0f6fc;
            --card-description: #e1e8ed;
            --card-link: rgb(128, 182, 204);
            --card-link-bg: rgba(88, 166, 255, 0.1);
            --card-link-border: rgba(88, 166, 255, 0.2);
            --card-link-bg-hover: rgba(88, 166, 255, 0.2);
            --card-link-hover: rgb(148, 202, 224);
            --status-unknown-bg: #484f58;
            --status-unknown-text: #f0f6fc;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
            line-height: 1.6;
            color: #f8f9fa;
            background-color: #0d1117;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            min-height: 100vh;
        }}
        
        {get_header_styles()}
        
        /* Minimal typography-focused header */
        .movie-header {{
            text-align: center;
            margin: 3rem 0 4rem 0;
            padding: 0;
        }}
        
        .movie-title {{
            font-family: 'Source Code Pro', monospace;
            font-size: 2.8rem;
            font-weight: 600;
            margin: 0;
            padding: 0;
            color: #ffffff;
            line-height: 1.2;
            letter-spacing: 1px;
        }}
        
        .movie-subtitle {{
            font-family: 'Source Code Pro', monospace;
            font-size: 1rem;
            font-weight: 400;
            margin: 0.5rem 0 0 0;
            padding: 0;
            color: rgb(128, 182, 204);
            letter-spacing: 2px;
            text-transform: lowercase;
        }}
        
        /* Fallback h1 for single-line titles */
        h1 {{
            font-family: 'Source Code Pro', monospace;
            font-size: 1.4rem;
            font-weight: 600;
            text-align: center;
            margin: 2rem 0 1rem 0;
            padding: 0;
            color: rgb(128, 182, 204);
            line-height: 1.4;
            letter-spacing: 1px;
        }}
        
        /* Responsive adjustments */
        @media (max-width: 768px) {{
            .movie-title {{
                font-size: 2.2rem;
            }}
            
            .movie-subtitle {{
                font-size: 0.9rem;
            }}
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
            font-family: 'Henny Penny', cursive;
            color: #ffffff;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 2.8rem;
            font-weight: 400;
            letter-spacing: 0.5px;
        }}
        
        section {{
            margin: 0 0 1rem 0;
            padding: 0.5rem;
            background-color: transparent;
            border-radius: 0;
            border: none;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        
        section section {{
            margin: 0 0 1rem 0;
            padding: 0 0 0 2rem;
            border-left: 1px solid rgba(168, 230, 207, 0.1);
            position: relative;
        }}
        
        section section::before {{
            content: '';
            position: absolute;
            left: -1px;
            top: 0;
            bottom: 0;
            width: 1px;
            background: linear-gradient(180deg, transparent, rgba(168, 230, 207, 0.2), transparent);
            opacity: 0.3;
        }}
        
        section section h2 {{
            font-family: 'Henny Penny', cursive;
            font-size: 1.8rem;
            font-weight: 400;
            color: #ffffff;
            margin: 0 0 0.5rem 0;
            text-align: left;
            letter-spacing: 0.5px;
        }}
        
        section section ol {{
            margin: 0;
            padding: 0;
            list-style: none;
            counter-reset: none;
            max-width: 100%;
        }}
        
        section section li {{
            margin: 0;
            padding: 0;
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 1.1rem;
            font-weight: 400;
            color: #f8f9fa;
            line-height: 1.7;
            position: relative;
            padding-left: 2.5rem;
            transition: all 0.3s ease;
        }}
        
        section section li::before {{
            content: counter(item);
            counter-increment: item;
            position: absolute;
            left: 0;
            top: 0.1rem;
            font-family: 'Henny Penny', cursive;
            font-size: 1.1rem;
            font-weight: 400;
            color: #a8e6cf;
            opacity: 0.8;
            transition: all 0.3s ease;
        }}
        
        section section li:hover {{
            color: #f0f6fc;
            transform: translateX(0.2rem);
        }}
        
        section section li:hover::before {{
            color: #c7f0db;
            opacity: 1;
            transform: scale(1.1);
        }}
        
        section section ol {{
            counter-reset: item;
        }}
        
        /* Inline code styling for list items */
        section section li code {{
            font-family: 'Source Code Pro', 'JetBrains Mono', 'Fira Code', monospace;
            font-size: 0.95em;
            font-weight: 500;
            background: rgba(168, 230, 207, 0.1);
            color: #a8e6cf;
            padding: 0.1em 0.3em;
            border-radius: 4px;
            border: 1px solid rgba(168, 230, 207, 0.2);
            transition: all 0.3s ease;
        }}
        
        section section li:hover code {{
            background: rgba(168, 230, 207, 0.15);
            color: #c7f0db;
            border-color: rgba(168, 230, 207, 0.3);
        }}
        
        /* Link styling for list items - inherits from code styling */
        section section li code a {{
            color: inherit;
            text-decoration: none;
            display: inline;
        }}
        
        section section li code a:hover {{
            color: inherit;
            text-decoration: none;
        }}
        
        /* Dimmed text styling for descriptions */
        section section li dim {{
            color: #8b949e;
            font-style: italic;
            font-weight: 400;
            opacity: 0.8;
            transition: all 0.3s ease;
        }}
        
        section section li:hover dim {{
            color: #a5a5a5;
            opacity: 1;
        }}
        
        /* Responsive adjustments for all sub-sections */
        @media (max-width: 768px) {{
            section section {{
                padding: 0 0 0 1.5rem;
                margin: 0 0 1rem 0;
            }}
            
            section section:last-child {{
                margin-bottom: 0;
            }}
            
            section section h2 {{
                font-size: 1.6rem;
                margin-bottom: 0.5rem;
            }}
            
            section section li {{
                font-size: 1rem;
                line-height: 1.6;
                padding-left: 2rem;
                margin: 0;
            }}
            
            section section li::before {{
                font-size: 0.9rem;
            }}
            
            section section li code {{
                font-size: 0.9em;
                padding: 0.15em 0.3em;
            }}
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
            color: #f8f9fa;
            font-size: 1.1rem;
            font-weight: 400;
        }}
        
        ol li {{
            counter-increment: item;
        }}
        
        ol li::before {{
            content: counter(item) ". ";
            color: #a8e6cf;
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
            color: #a8e6cf;
            text-decoration: none;
            transition: color 0.2s ease;
        }}
        
        a:hover {{
            color: #c7f0db;
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
        
        {get_hero_banner_styles()}
        
        {get_card_styles()}
        
        {get_footer_styles()}
    """




def get_theme_css(theme_name="dark"):
    """Get CSS for specified theme. Only dark theme is supported."""
    return get_dark_theme_css()
