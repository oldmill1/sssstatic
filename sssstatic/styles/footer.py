# sssstatic/styles/footer.py
"""
Footer styles module for SSSStatic - contains CSS styles and HTML generation for footer components
"""


def get_footer_styles():
    """Return CSS styles for footer components."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Clean Footer Styles */
        .site-footer {
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            margin-top: 2rem;
            padding: 4rem 0 0 0;
            background: black;
            position: relative;
        }
        
        .site-footer::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: rgba(88, 166, 255, 0.15);
            box-shadow: 
                0 1px 0 rgba(255, 255, 255, 0.05),
                0 2px 0 rgba(0, 0, 0, 0.1);
        }
        
        .footer-content {
            display: flex;
            justify-content: center;
            align-items: center;
            max-width: 900px;
            margin: 0 auto;
            padding: 0 2rem 4rem 2rem;
        }
        
        .footer-text {
            font-family: var(--font-mono);
            font-size: var(--font-size-lg);
            font-weight: var(--font-weight-normal);
            color: #e1e8ed;
            letter-spacing: 1px;
            text-align: center;
            line-height: 1.4;
            opacity: 0.8;
        }
        
        /* Responsive footer spacing */
        @media (min-width: 768px) {
            .site-footer {
                margin-top: 3rem;
            }
        }
        
        @media (min-width: 1024px) {
            .site-footer {
                margin-top: 4rem;
            }
        }
        
        /* Responsive footer */
        @media (max-width: 768px) {
            .site-footer {
                padding: 3rem 0 0 0;
            }
            
            .footer-content {
                padding: 0 1rem 3rem 1rem;
            }
            
            .footer-text {
                font-size: var(--font-size-base);
                letter-spacing: 0.8px;
            }
        }
    """


def generate_footer_html(config):
    """Generate HTML for footer."""
    from ..yaml_to_html import parse_markdown_links
    
    footer_html = ""
    
    # Check for _footer configuration
    if '_footer' in config:
        footer_config = config['_footer']
        if isinstance(footer_config, dict):
            headline = footer_config.get('headline', 'Made with [SSSStatic](http://sssstatic.com/)')
        else:
            headline = footer_config
    else:
        # Default footer text
        headline = 'Made with [SSSStatic](http://sssstatic.com/)'
    
    # Parse markdown links in the headline
    parsed_headline = parse_markdown_links(headline)
    
    footer_html = f'''    <footer class="site-footer">
        <div class="footer-content">
            <span class="footer-text">{parsed_headline}</span>
        </div>
    </footer>
'''
    
    return footer_html
