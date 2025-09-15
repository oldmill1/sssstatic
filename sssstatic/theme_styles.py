# sssstatic/styles.py
"""
Styles module for SSSStatic - contains CSS styles for generated sites
"""

from .styles.topbar import get_topbar_styles
from .styles.cards import get_card_styles
from .styles.spotlight import get_spotlight_styles
from .styles.widescreen_spotlight import get_widescreen_spotlight_styles
from .styles.pinterest import get_pinterest_styles
from .styles.showcase import get_showcase_styles
from .styles.slick import get_slick_styles
from .styles.sizzle import get_sizzle_styles
from .styles.sly import get_sly_styles
from .styles.sinema import get_sinema_styles
from .styles.map import get_map_styles








def get_global_css(config=None):
    """Return global CSS styles with conditional background based on colorMode."""
    from .styles.footer import get_footer_styles
    from .styles.type import get_font_styles
    from .styles.cards import get_card_styles
    from .styles.topbar import get_topbar_styles
    from .styles.spotlight import get_spotlight_styles
    from .styles.widescreen_spotlight import get_widescreen_spotlight_styles
    from .styles.pinterest import get_pinterest_styles
    from .styles.showcase import get_showcase_styles
    from .styles.slick import get_slick_styles
    from .styles.sizzle import get_sizzle_styles
    
    # Determine the background color based on config
    if config and 'site' in config:
        color_mode = config['site'].get('colorMode', 'dark')
        if color_mode == 'light':
            body_bg_color = '#f8f9fa'
        else:  # dark mode or any other value defaults to dark
            body_bg_color = '#000000'  # True dark black color
    else:
        # Default to dark mode if no config provided
        body_bg_color = '#000000'
    
    return get_font_styles() + """
        :root {
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
            --body-bg-color: """ + body_bg_color + """;
        }
        
        body {
            font-family: var(--font-body);
            line-height: 1.6;
            color: #f8f9fa;
            background-color: var(--body-bg-color);
            max-width: 1200px;
            margin: 0 auto;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        /* When TopBar is used, adjust body padding */
        body.has-topbar {
            padding-top: 70px;
        }
        
        """ + get_topbar_styles(config) + """
        
        /* Minimal typography-focused header */
        .movie-header {
            text-align: center;
            margin: 3rem 0 4rem 0;
            padding: 0;
        }
        
        .movie-title {
            font-family: var(--font-mono);
            font-size: var(--font-size-4xl);
            font-weight: var(--font-weight-semibold);
            margin: 0;
            padding: 0;
            color: #ffffff;
            line-height: 1.2;
            letter-spacing: 1px;
        }
        
        .movie-subtitle {
            font-family: var(--font-mono);
            font-size: var(--font-size-base);
            font-weight: var(--font-weight-normal);
            margin: 0.5rem 0 0 0;
            padding: 0;
            color: rgb(128, 182, 204);
            letter-spacing: 2px;
            text-transform: lowercase;
        }
        
        /* Fallback h1 for single-line titles */
        h1 {
            font-family: var(--font-mono);
            font-size: var(--font-size-xl);
            font-weight: var(--font-weight-semibold);
            text-align: center;
            margin: 2rem 0 1rem 0;
            padding: 0;
            color: rgb(128, 182, 204);
            line-height: 1.4;
            letter-spacing: 1px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .movie-title {
                font-size: var(--font-size-3xl);
            }
            
            .movie-subtitle {
                font-size: var(--font-size-sm);
            }
        }
        
        @keyframes gradientShift {
            0%, 100% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                opacity: 0.6;
                transform: translateX(-50%) scaleX(1);
            }
            50% {
                opacity: 1;
                transform: translateX(-50%) scaleX(1.2);
            }
        }
        
        @keyframes shimmer {
            0%, 100% {
                opacity: 0.3;
                transform: translateX(-50%) scaleX(0.8);
            }
            50% {
                opacity: 0.8;
                transform: translateX(-50%) scaleX(1.2);
            }
        }
        
        h2 {
            font-family: var(--font-heading);
            color: #ffffff;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: var(--font-size-4xl);
            font-weight: var(--font-weight-normal);
            letter-spacing: 0.5px;
        }
        
        section {
            margin: 0 0 1rem 0;
            padding: 0.5rem;
            background-color: transparent;
            border-radius: 0;
            border: none;
            font-family: var(--font-system);
        }
        
        section section {
            margin: 0 0 1rem 0;
            padding: 0 0 0 2rem;
            border-left: 1px solid rgba(168, 230, 207, 0.1);
            position: relative;
        }
        
        section section::before {
            content: '';
            position: absolute;
            left: -1px;
            top: 0;
            bottom: 0;
            width: 1px;
            background: linear-gradient(180deg, transparent, rgba(168, 230, 207, 0.2), transparent);
            opacity: 0.3;
        }
        
        section section h2 {
            font-family: var(--font-heading);
            font-size: var(--font-size-2xl);
            font-weight: var(--font-weight-normal);
            color: #ffffff;
            margin: 0 0 0.5rem 0;
            text-align: left;
            letter-spacing: 0.5px;
        }
        
        section section ol {
            margin: 0;
            padding: 0;
            list-style: none;
            counter-reset: none;
            max-width: 100%;
        }
        
        section section li {
            margin: 0;
            padding: 0;
            font-family: var(--font-primary);
            font-size: var(--font-size-lg);
            font-weight: var(--font-weight-normal);
            color: #f8f9fa;
            line-height: 1.7;
            position: relative;
            padding-left: 2.5rem;
            transition: all 0.3s ease;
        }
        
        section section li::before {
            content: counter(item);
            counter-increment: item;
            position: absolute;
            left: 0;
            top: 0.1rem;
            font-family: var(--font-heading);
            font-size: var(--font-size-lg);
            font-weight: var(--font-weight-normal);
            color: #a8e6cf;
            opacity: 0.8;
            transition: all 0.3s ease;
        }
        
        section section li:hover {
            color: #f0f6fc;
            transform: translateX(0.2rem);
        }
        
        section section li:hover::before {
            color: #c7f0db;
            opacity: 1;
            transform: scale(1.1);
        }
        
        section section ol {
            counter-reset: item;
        }
        
        /* Inline code styling for list items */
        section section li code {
            font-family: var(--font-mono);
            font-size: 0.95em;
            font-weight: var(--font-weight-medium);
            background: rgba(168, 230, 207, 0.1);
            color: #a8e6cf;
            padding: 0.1em 0.3em;
            border-radius: 4px;
            border: 1px solid rgba(168, 230, 207, 0.2);
            transition: all 0.3s ease;
        }
        
        section section li:hover code {
            background: rgba(168, 230, 207, 0.15);
            color: #c7f0db;
            border-color: rgba(168, 230, 207, 0.3);
        }
        
        /* Link styling for list items - inherits from code styling */
        section section li code a {
            color: inherit;
            text-decoration: none;
            display: inline;
        }
        
        section section li code a:hover {
            color: inherit;
            text-decoration: none;
        }
        
        /* Dimmed text styling for descriptions */
        section section li dim {
            color: #8b949e;
            font-style: italic;
            font-weight: var(--font-weight-normal);
            opacity: 0.8;
            transition: all 0.3s ease;
        }
        
        section section li:hover dim {
            color: #a5a5a5;
            opacity: 1;
        }
        
        /* Responsive adjustments for all sub-sections */
        @media (max-width: 768px) {
            section section {
                padding: 0 0 0 1.5rem;
                margin: 0 0 1rem 0;
            }
            
            section section:last-child {
                margin-bottom: 0;
            }
            
            section section h2 {
                font-size: var(--font-size-xl);
                margin-bottom: 0.5rem;
            }
            
            section section li {
                font-size: var(--font-size-base);
                line-height: 1.6;
                padding-left: 2rem;
                margin: 0;
            }
            
            section section li::before {
                font-size: var(--font-size-sm);
            }
            
            section section li code {
                font-size: 0.9em;
                padding: 0.15em 0.3em;
            }
        }
        
        ol, ul {
            margin: 1rem 0;
            padding-left: 0;
            list-style: none;
        }
        
        li {
            margin: 0.8rem 0;
            line-height: 1.6;
            font-family: var(--font-system);
            color: #f8f9fa;
            font-size: var(--font-size-lg);
            font-weight: var(--font-weight-normal);
        }
        
        ol li {
            counter-increment: item;
        }
        
        ol li::before {
            content: counter(item) ". ";
            color: #a8e6cf;
            font-weight: var(--font-weight-semibold);
            font-size: var(--font-size-lg);
            margin-right: 1rem;
        }
        
        ol {
            counter-reset: item;
        }
        
        strong {
            color: #f0f6fc;
            font-weight: var(--font-weight-semibold);
        }
        
        a {
            color: #a8e6cf;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        
        a:hover {
            color: #c7f0db;
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
        
        
        """ + get_card_styles() + get_spotlight_styles() + get_widescreen_spotlight_styles() + get_pinterest_styles() + get_showcase_styles() + get_slick_styles() + get_sizzle_styles() + get_sly_styles() + get_sinema_styles() + get_map_styles() + get_footer_styles()




