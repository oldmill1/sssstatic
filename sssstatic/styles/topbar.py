# sssstatic/styles/topbar.py
"""
TopBar styles module for SSSStatic - contains CSS styles for dark mode topbar
"""


def get_topbar_styles():
    """Return CSS styles for TopBar component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* TopBar Styles - Dark Mode Navigation */
        .topbar {
            background: #1a1a1a;
            border-bottom: 1px solid #333;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            width: 100vw;
        }
        
        .topbar-container {
            max-width: 100%;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            min-height: 70px;
            gap: 2rem;
        }
        
        .topbar-brand {
            font-family: var(--font-primary);
            font-size: var(--font-size-xl);
            font-weight: var(--font-weight-bold);
            color: #ffffff;
            text-decoration: none;
            letter-spacing: 0.5px;
            margin: 0;
            transition: color 0.2s ease;
            flex-shrink: 0;
        }
        
        .topbar-brand:hover {
            color: #f0f0f0;
            text-decoration: none;
        }
        
        .topbar-nav {
            margin-left: auto;
            display: flex;
        }
        
        .topbar-list {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            gap: 2rem;
            align-items: center;
        }
        
        .topbar-item {
            margin: 0;
        }
        
        .topbar-link {
            color: #cccccc;
            text-decoration: none;
            font-family: var(--font-primary);
            font-size: var(--font-size-base);
            font-weight: var(--font-weight-normal);
            transition: color 0.2s ease;
            padding: 0.5rem 0;
        }
        
        .topbar-link:hover {
            color: #ffffff;
            text-decoration: none;
        }
        
        .topbar-cta {
            background: #000000;
            color: #ffffff;
            text-decoration: none;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-primary);
            font-size: var(--font-size-base);
            font-weight: var(--font-weight-medium);
            transition: all 0.2s ease;
            border: 1px solid #333;
            flex-shrink: 0;
        }
        
        .topbar-cta:hover {
            background: #333333;
            color: #ffffff;
            text-decoration: none;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        
        .topbar-cta-icon {
            font-size: 1.1em;
        }
        
        .topbar-cta-text {
            font-weight: var(--font-weight-medium);
        }
        
        /* Responsive design */
        @media (max-width: 1024px) {
            .topbar-container {
                padding: 0 1.5rem;
            }
            
            .topbar-list {
                gap: 1.5rem;
            }
        }
        
        @media (max-width: 768px) {
            .topbar-container {
                padding: 0 1rem;
                flex-wrap: wrap;
                gap: 1rem;
                min-height: auto;
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
            
            .topbar-brand {
                font-size: var(--font-size-lg);
                order: 1;
                flex: 1;
                text-align: left;
            }
            
            .topbar-nav {
                order: 3;
                width: 100%;
                margin-left: 0;
                justify-content: center;
            }
            
            .topbar-list {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .topbar-cta {
                order: 2;
                padding: 0.5rem 1rem;
                font-size: var(--font-size-sm);
            }
            
            .topbar-link {
                font-size: var(--font-size-sm);
            }
        }
        
        @media (max-width: 480px) {
            .topbar-container {
                flex-direction: column;
                gap: 0.75rem;
            }
            
            .topbar-brand {
                order: 1;
                text-align: center;
                width: 100%;
            }
            
            .topbar-nav {
                order: 2;
            }
            
            .topbar-list {
                gap: 0.75rem;
            }
            
            .topbar-cta {
                order: 3;
                align-self: center;
            }
        }
    """
