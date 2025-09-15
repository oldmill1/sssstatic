# sssstatic/styles/topbar.py
"""
TopBar styles module for SSSStatic - contains CSS styles for dark mode topbar
"""


def get_topbar_styles(config=None):
    """Return CSS styles for TopBar component with responsive colors."""
    from .type import get_font_styles
    
    # Get custom font and size from topbar config
    custom_font = None
    topbar_size = 'small'  # default size
    if config and '_topbar' in config:
        custom_font = config['_topbar'].get('titleFont', None)
        topbar_size = config['_topbar'].get('size', 'small')
    
    # Determine colors based on color mode
    if config and 'site' in config:
        color_mode = config['site'].get('colorMode', 'dark')
        if color_mode == 'light':
            topbar_bg = '#f8f9fa'  # Light mode background
            topbar_border = '#e1e8ed'  # Light mode border
            topbar_text = '#24292f'  # Light mode text
            topbar_text_hover = '#1a1a1a'  # Light mode text hover
            topbar_link = '#656d76'  # Light mode link
            topbar_link_hover = '#24292f'  # Light mode link hover
            topbar_cta_bg = '#24292f'  # Light mode CTA background
            topbar_cta_bg_hover = '#1a1a1a'  # Light mode CTA hover
            topbar_cta_border = '#656d76'  # Light mode CTA border
        else:  # dark mode or any other value defaults to dark
            topbar_bg = 'var(--body-bg-color)'  # Use same background as site
            topbar_border = '#333'  # Dark mode border
            topbar_text = '#ffffff'  # Dark mode text
            topbar_text_hover = '#f0f0f0'  # Dark mode text hover
            topbar_link = '#cccccc'  # Dark mode link
            topbar_link_hover = '#ffffff'  # Dark mode link hover
            topbar_cta_bg = '#1a1a1a'  # Dark mode CTA background
            topbar_cta_bg_hover = '#333333'  # Dark mode CTA hover
            topbar_cta_border = '#333'  # Dark mode CTA border
    else:
        # Default to dark mode if no config provided
        topbar_bg = 'var(--body-bg-color)'
        topbar_border = '#333'
        topbar_text = '#ffffff'
        topbar_text_hover = '#f0f0f0'
        topbar_link = '#cccccc'
        topbar_link_hover = '#ffffff'
        topbar_cta_bg = '#1a1a1a'
        topbar_cta_bg_hover = '#333333'
        topbar_cta_border = '#333'
    
    # Define size variables based on topbar_size
    if topbar_size == 'large':
        container_height = '90px'
        brand_font_size = 'var(--font-size-3xl)'
        brand_letter_spacing = '1px'
        cta_padding = '1rem 2rem'
        cta_font_size = 'var(--font-size-lg)'
        container_padding = '0 2.5rem'
    elif topbar_size == 'medium':
        container_height = '80px'
        brand_font_size = 'var(--font-size-2xl)'
        brand_letter_spacing = '0.75px'
        cta_padding = '0.875rem 1.75rem'
        cta_font_size = 'var(--font-size-base)'
        container_padding = '0 2rem'
    else:  # small (default)
        container_height = '70px'
        brand_font_size = 'var(--font-size-xl)'
        brand_letter_spacing = '0.5px'
        cta_padding = '0.75rem 1.5rem'
        cta_font_size = 'var(--font-size-base)'
        container_padding = '0 2rem'
    
    return get_font_styles() + f"""
        /* TopBar Styles - Responsive Color Mode Navigation */
        .topbar {{
            background: {topbar_bg};
            border-bottom: 1px solid {topbar_border};
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            width: 100vw;
        }}
        
        .topbar-container {{
            max-width: 100%;
            margin: 0 auto;
            padding: {container_padding};
            display: flex;
            justify-content: space-between;
            align-items: center;
            min-height: {container_height};
            gap: 2rem;
        }}
        
        .topbar-brand {{
            font-family: {f'"{custom_font}", ' if custom_font else ''}var(--font-primary);
            font-size: {brand_font_size};
            font-weight: var(--font-weight-bold);
            color: {topbar_text};
            text-decoration: none;
            letter-spacing: {brand_letter_spacing};
            margin: 0;
            transition: color 0.2s ease;
            flex-shrink: 0;
        }}
        
        .topbar-brand:hover {{
            color: {topbar_text_hover};
            text-decoration: none;
        }}
        
        .topbar-nav {{
            display: flex;
            flex: 1;
            justify-content: center;
        }}
        
        .topbar-cta-wrapper {{
            display: flex;
            align-items: center;
        }}
        
        .topbar-list {{
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            gap: 2rem;
            align-items: center;
        }}
        
        .topbar-item {{
            margin: 0;
        }}
        
        .topbar-link {{
            color: {topbar_link};
            text-decoration: none;
            font-family: var(--font-primary);
            font-size: var(--font-size-base);
            font-weight: var(--font-weight-normal);
            transition: color 0.2s ease;
            padding: 0.5rem 0;
        }}
        
        .topbar-link:hover {{
            color: {topbar_link_hover};
            text-decoration: none;
        }}
        
        .topbar-cta {{
            background: {topbar_cta_bg};
            color: {topbar_text};
            text-decoration: none;
            border-radius: 8px;
            padding: {cta_padding};
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-primary);
            font-size: {cta_font_size};
            font-weight: var(--font-weight-medium);
            transition: all 0.2s ease;
            border: 1px solid {topbar_cta_border};
            flex-shrink: 0;
        }}
        
        .topbar-cta:hover {{
            background: {topbar_cta_bg_hover};
            color: {topbar_text};
            text-decoration: none;
        }}
        
        .topbar-cta-icon {{
            font-size: 1.1em;
        }}
        
        .topbar-cta-text {{
            font-weight: var(--font-weight-medium);
        }}
        
        /* Responsive design */
        @media (max-width: 1024px) {{
            .topbar-container {{
                padding: 0 1.5rem;
            }}
            
            .topbar-list {{
                gap: 1.5rem;
            }}
        }}
        
        @media (max-width: 768px) {{
            .topbar-container {{
                padding: 0 1rem;
                flex-wrap: wrap;
                gap: 1rem;
                min-height: auto;
                padding-top: 1rem;
                padding-bottom: 1rem;
            }}
            
            .topbar-brand {{
                font-size: {brand_font_size if topbar_size == 'small' else 'var(--font-size-lg)'};
                order: 1;
                flex: 1;
                text-align: left;
            }}
            
            .topbar-nav {{
                order: 3;
                width: 100%;
                justify-content: center;
            }}
            
            .topbar-list {{
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }}
            
            .topbar-cta-wrapper {{
                order: 2;
            }}
            
            .topbar-cta {{
                padding: {cta_padding if topbar_size == 'small' else '0.5rem 1rem'};
                font-size: {cta_font_size if topbar_size == 'small' else 'var(--font-size-sm)'};
            }}
            
            .topbar-link {{
                font-size: var(--font-size-sm);
            }}
        }}
        
        @media (max-width: 480px) {{
            .topbar-container {{
                flex-direction: column;
                gap: 0.75rem;
            }}
            
            .topbar-brand {{
                order: 1;
                text-align: center;
                width: 100%;
            }}
            
            .topbar-nav {{
                order: 2;
            }}
            
            .topbar-list {{
                gap: 0.75rem;
            }}
            
            .topbar-cta-wrapper {{
                order: 3;
                align-self: center;
            }}
        }}
    """
