# sssstatic/styles/pinterest.py
"""
Pinterest masonry layout styles module for SSSStatic - contains CSS styles for Pinterest components
"""


def get_pinterest_styles():
    """Return CSS styles for Pinterest masonry layout components."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Pinterest Masonry Container */
        .pinterest-container {
            column-count: 6;
            column-gap: 1px;
            margin: 0;
            padding: 0;
            width: 100%;
            max-width: none;
            max-height: 66vh;
            overflow: hidden;
            line-height: 0;
            background: black;
        }
        
        /* Pinterest Item */
        .pinterest-item {
            break-inside: avoid;
            margin-bottom: 1px;
            display: inline-block;
            width: 100%;
            background: transparent;
            border: none;
            border-radius: 2px;
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: none;
            position: relative;
        }
        
        .pinterest-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        
        /* Pinterest Link */
        .pinterest-link {
            display: block;
            text-decoration: none;
            color: inherit;
            width: 100%;
            height: 100%;
        }
        
        .pinterest-link:hover {
            text-decoration: none;
            color: inherit;
        }
        
        /* Pinterest Image Container */
        .pinterest-image-container {
            position: relative;
            width: 100%;
            overflow: hidden;
            background: transparent;
        }
        
        /* Pinterest Image */
        .pinterest-image {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.3s ease;
            object-fit: cover;
            border-radius: 2px;
            max-width: 100%;
        }
        
        .pinterest-item:hover .pinterest-image {
            transform: scale(1.02);
        }
        
        /* Responsive adjustments */
        @media (max-width: 1200px) {
            .pinterest-container {
                column-count: 5;
            }
        }
        
        @media (max-width: 900px) {
            .pinterest-container {
                column-count: 4;
            }
        }
        
        @media (max-width: 600px) {
            .pinterest-container {
                column-count: 3;
            }
        }
        
        @media (max-width: 400px) {
            .pinterest-container {
                column-count: 2;
            }
        }
        
        /* Full-width override for Pinterest container */
        .pinterest-container {
            margin-left: calc(-50vw + 50%);
            margin-right: calc(-50vw + 50%);
            width: 100vw;
            max-width: 100vw;
            box-sizing: border-box;
        }
        
        /* Adjust padding for mobile */
        @media (max-width: 768px) {
            .pinterest-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    """
