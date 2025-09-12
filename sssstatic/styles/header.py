# sssstatic/styles/header.py
"""
Header styles module for SSSStatic - contains CSS styles for site header
"""


def get_header_styles():
    """Return CSS styles for header components."""
    from .fonts import get_font_styles
    return get_font_styles() + """
        /* Header Styles - Toronto Dating Photos Style */
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


