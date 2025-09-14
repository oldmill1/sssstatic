# sssstatic/styles/spotlight.py
"""
Spotlight styles module for SSSStatic - contains CSS styles for spotlight component
"""


def get_spotlight_styles():
    """Return CSS styles for spotlight component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Spotlight Section - Image flush with top, text overlay */
        .spotlight-section {
            margin: 1rem 0;
            padding: 0;
            position: relative;
            border-radius: 24px;
            overflow: hidden;
        }
        
        /* Image Container - flush with top */
        .spotlight-image-container {
            position: relative;
            width: 100%;
            margin: 0;
            overflow: hidden;
        }
        
        /* Spotlight Image */
        .spotlight-image {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .spotlight-image-container:hover .spotlight-image {
            transform: scale(1.02);
        }
        
        /* Content overlay on top of image */
        .spotlight-content {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            padding: 4rem 2rem 2rem;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            text-align: center;
            z-index: 2;
        }
        
        /* Spotlight Title - Apple-style typography */
        .spotlight-title {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 3.5rem;
            font-weight: 600;
            margin: 0 0 0.5rem 0;
            color: #ffffff;
            letter-spacing: -0.03em;
            line-height: 1.1;
            text-align: center;
        }
        
        /* Spotlight Subtitle */
        .spotlight-subtitle {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin: 0 0 1.5rem 0;
            color: #ffffff;
            letter-spacing: -0.01em;
            text-align: center;
        }
        
        /* Spotlight Description */
        .spotlight-description {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.125rem;
            font-weight: 400;
            margin: 0 auto 2rem;
            color: #ffffff;
            line-height: 1.5;
            max-width: 600px;
            text-align: center;
        }
        
        
        /* Call-to-action buttons (optional) */
        .spotlight-actions {
            margin-top: 2rem;
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .spotlight-button {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1rem;
            font-weight: 500;
            padding: 0.875rem 2rem;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            display: inline-block;
            letter-spacing: -0.01em;
        }
        
        .spotlight-button-primary {
            background: #007AFF;
            color: #ffffff;
        }
        
        .spotlight-button-primary:hover {
            background: #0056CC;
            transform: translateY(-2px);
        }
        
        .spotlight-button-secondary {
            background: transparent;
            color: #007AFF;
            border: 1px solid #007AFF;
        }
        
        .spotlight-button-secondary:hover {
            background: rgba(0, 122, 255, 0.1);
            transform: translateY(-2px);
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .spotlight-section {
                margin: 2rem 0;
                border-radius: 16px;
            }
            
            .spotlight-content {
                padding: 3rem 1.5rem 1.5rem;
            }
            
            .spotlight-title {
                font-size: 2.5rem;
            }
            
            .spotlight-subtitle {
                font-size: 1.25rem;
            }
            
            .spotlight-description {
                font-size: 1rem;
            }
            
            .spotlight-actions {
                flex-direction: column;
                align-items: center;
            }
            
            .spotlight-button {
                width: 100%;
                max-width: 200px;
            }
        }
        
        @media (max-width: 480px) {
            .spotlight-section {
                border-radius: 12px;
            }
            
            .spotlight-content {
                padding: 2rem 1rem 1rem;
            }
            
            .spotlight-title {
                font-size: 2rem;
            }
            
            .spotlight-subtitle {
                font-size: 1.125rem;
            }
            
            .spotlight-description {
                font-size: 0.9rem;
            }
        }
    """
