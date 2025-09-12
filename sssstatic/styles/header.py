# sssstatic/styles/header.py
"""
Header styles module for SSSStatic - contains CSS styles for site header
"""


def get_header_styles():
    """Return CSS styles for header components."""
    return """
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
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 1.8rem;
            font-weight: 400;
            color: rgb(128, 182, 204);
            text-decoration: none;
            letter-spacing: 1px;
            margin: 0;
            transition: color 0.3s ease;
        }
        
        .header-brand:hover {
            color: rgb(148, 202, 224);
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
            color: rgb(128, 182, 204);
            text-decoration: none;
            padding: 0.5rem 0;
            transition: all 0.2s ease;
            font-weight: 600;
            font-size: 0.95rem;
            letter-spacing: 0.5px;
            font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            position: relative;
        }
        
        .header-link:hover {
            color: rgb(148, 202, 224);
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
                font-size: 1.5rem;
                text-align: center;
            }
            
            .header-list {
                gap: 1.5rem;
                justify-content: center;
            }
            
            .header-link {
                font-size: 0.9rem;
            }
        }
    """


