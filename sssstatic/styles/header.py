# sssstatic/styles/header.py
"""
Header styles module for SSSStatic - contains CSS styles for site header
"""


def get_header_styles():
    """Return CSS styles for header components."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Header Styles - Toronto Dating Photos Style */
        .site-header {
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
            gap: 1rem;
            flex-wrap: wrap;
            align-items: center;
        }
        
        .header-item {
            margin: 0;
        }
        
        .header-link {
            background-color: #c2fbd7;
            border-radius: 100px;
            box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset,rgba(44, 187, 99, .15) 0 1px 2px,rgba(44, 187, 99, .15) 0 2px 4px,rgba(44, 187, 99, .15) 0 4px 8px,rgba(44, 187, 99, .15) 0 8px 16px,rgba(44, 187, 99, .15) 0 16px 32px;
            color: green;
            cursor: pointer;
            display: inline-block;
            font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif;
            padding: 7px 20px;
            text-align: center;
            text-decoration: none;
            transition: all 250ms;
            border: 0;
            font-size: 16px;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            font-weight: var(--font-weight-normal);
            letter-spacing: 0.5px;
            position: relative;
        }
        
        .header-link:hover {
            box-shadow: rgba(44,187,99,.35) 0 -25px 18px -14px inset,rgba(44,187,99,.25) 0 1px 2px,rgba(44,187,99,.25) 0 2px 4px,rgba(44,187,99,.25) 0 4px 8px,rgba(44,187,99,.25) 0 8px 16px,rgba(44,187,99,.25) 0 16px 32px;
            transform: scale(1.05) rotate(-1deg);
            text-decoration: none;
            color: #0d4f1c;
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
                gap: 0.75rem;
                justify-content: center;
                flex-wrap: wrap;
            }
            
            .header-link {
                font-size: 14px;
                padding: 6px 16px;
            }
        }
    """


