# sssstatic/styles/sly.py
"""
Sly styles module for SSSStatic - contains CSS styles for sly component
"""


def get_sly_styles():
    """Return CSS styles for sly component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Sly Section - Two column layout with image and text */
        .sly-section {
            margin: 0; 
            padding: 4rem 0;
            background-color: #f8f9fa;
        }
        
        .sly-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        
        .sly-content-wrapper {
            display: flex;
            align-items: center;
            gap: 4rem;
        }
        
        /* Image Section - 30% width */
        .sly-image-section {
            flex: 0 0 30%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .sly-image-block {
            width: 100%;
            max-width: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .sly-image {
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: 12px;
            border: none;
            outline: none;
            display: block;
        }
        
        /* Text Section - 70% width */
        .sly-text-section {
            flex: 0 0 70%;
            padding-left: 1rem;
        }
        
        /* Header styles */
        .sly-header {
            margin-bottom: 2rem;
        }
        
        .sly-subtitle {
            color: #3b82f6;
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 12px;
            letter-spacing: 0.3px;
            text-transform: uppercase;
        }
        
        .sly-main-title {
            font-family: var(--font-display);
            font-size: var(--font-size-5xl);
            font-weight: 700;
            color: #000;
            line-height: 1.2;
            margin-bottom: 0;
        }
        
        /* Description */
        .sly-description {
            margin-bottom: 1.5rem;
        }
        
        .sly-description-text {
            font-size: 20px;
            color: #374151;
            line-height: 1.6;
            font-weight: 500;
        }
        
        /* Paragraph */
        .sly-paragraph {
            margin-bottom: 0;
        }
        
        .sly-paragraph-text {
            font-size: 18px;
            color: #6b7280;
            line-height: 1.7;
        }
        
        /* Responsive design */
        @media (max-width: 1024px) {
            .sly-container {
                padding: 0 1.5rem;
            }
            
            .sly-content-wrapper {
                gap: 3rem;
            }
            
            .sly-main-title {
                font-size: 34px;
            }
            
            .sly-description-text {
                font-size: 19px;
            }
            
            .sly-paragraph-text {
                font-size: 17px;
            }
        }
        
        @media (max-width: 768px) {
            .sly-section {
                padding: 3rem 0;
            }
            
            .sly-container {
                padding: 0 1rem;
            }
            
            .sly-content-wrapper {
                flex-direction: column;
                gap: 2.5rem;
            }
            
            .sly-image-section {
                flex: none;
                width: 100%;
                max-width: 300px;
            }
            
            .sly-text-section {
                flex: none;
                width: 100%;
                padding-left: 0;
                text-align: center;
            }
            
            .sly-main-title {
                font-size: 30px;
            }
            
            .sly-subtitle {
                font-size: 15px;
            }
            
            .sly-description-text {
                font-size: 18px;
            }
            
            .sly-paragraph-text {
                font-size: 16px;
            }
        }
        
        @media (max-width: 480px) {
            .sly-section {
                padding: 2.5rem 0;
            }
            
            .sly-container {
                padding: 0 0.75rem;
            }
            
            .sly-content-wrapper {
                gap: 2rem;
            }
            
            .sly-header {
                margin-bottom: 1.5rem;
            }
            
            .sly-main-title {
                font-size: 26px;
            }
            
            .sly-subtitle {
                font-size: 14px;
            }
            
            .sly-description {
                margin-bottom: 1.25rem;
            }
            
            .sly-description-text {
                font-size: 17px;
            }
            
            .sly-paragraph-text {
                font-size: 15px;
            }
        }
    """
