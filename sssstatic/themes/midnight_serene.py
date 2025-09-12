# sssstatic/themes/midnight_serene.py
"""
Midnight Serene theme - Default dark theme with green accents
"""

def get_header_styles():
    """Return CSS styles for header components in Midnight Serene theme."""
    return """
        /* Header Styles - Midnight Serene Theme */
        .site-header {
            margin-bottom: 2rem;
            padding: 1.5rem 0;
            border-bottom: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0d1117;
            position: relative;
        }
        
        .header-brand {
            font-family: var(--font-primary);
            font-size: var(--font-size-2xl);
            font-weight: var(--font-weight-normal);
            color: #a8e6cf;
            text-decoration: none;
            letter-spacing: 1px;
            margin: 0;
            transition: color 0.2s ease;
        }
        
        .header-brand:hover {
            color: #c7f0db;
            text-decoration: none;
        }
        
        .header-list {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            gap: 2.5rem;
            flex-wrap: wrap;
            align-items: center;
        }
        
        .header-item {
            margin: 0;
        }
        
        .header-link {
            color: #a8e6cf;
            text-decoration: none;
            padding: 0.5rem 0;
            transition: color 0.2s ease;
            font-weight: var(--font-weight-normal);
            font-size: var(--font-size-sm);
            letter-spacing: 0.5px;
            font-family: var(--font-primary);
            position: relative;
        }
        
        .header-link:hover {
            color: #c7f0db;
            text-decoration: none;
            transform: scale(1.05);
        }
        
        .nav-link:active {
            transform: translateY(1px);
        }
        
        /* Responsive navigation */
        @media (max-width: 768px) {
            .site-header {
                flex-direction: column;
                gap: 1rem;
                padding: 1rem 0;
            }
            
            .header-brand {
                font-size: var(--font-size-xl);
                text-align: center;
            }
            
            .header-list {
                gap: 1.5rem;
                justify-content: center;
            }
            
            .header-link {
                font-size: var(--font-size-sm);
            }
        }
    """

def get_global_css():
    """Return global CSS styles for Midnight Serene theme."""
    from ..styles.cards import get_card_styles
    from ..styles.footer import get_footer_styles
    from ..styles.fonts import get_font_styles
    
    return get_font_styles() + """
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
            font-family: var(--font-body);
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
            font-family: var(--font-mono);
            font-size: var(--font-size-4xl);
            font-weight: var(--font-weight-semibold);
            margin: 0;
            padding: 0;
            color: #ffffff;
            line-height: 1.2;
            letter-spacing: 1px;
        }}
        
        .movie-subtitle {{
            font-family: var(--font-mono);
            font-size: var(--font-size-base);
            font-weight: var(--font-weight-normal);
            margin: 0.5rem 0 0 0;
            padding: 0;
            color: rgb(128, 182, 204);
            letter-spacing: 2px;
            text-transform: lowercase;
        }}
        
        /* Fallback h1 for single-line titles */
        h1 {{
            font-family: var(--font-mono);
            font-size: var(--font-size-xl);
            font-weight: var(--font-weight-semibold);
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
                font-size: var(--font-size-3xl);
            }}
            
            .movie-subtitle {{
                font-size: var(--font-size-sm);
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
        
        {get_card_styles()}
        
        {get_footer_styles()}
    """
