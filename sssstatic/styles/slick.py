# sssstatic/styles/slick.py
"""
Slick styles module for SSSStatic - contains CSS styles for slick component
"""


def get_slick_styles():
    """Return CSS styles for slick component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Slick Section - Two column layout with benefits and image */
        .slick-section {
            margin: 0; 
            padding: 0; /* Remove padding from section - let container handle it */
            background-color: #f8f9fa; /* Default background, can be overridden by bgColor */
            color: #000; /* Default text color, can be overridden by color property */
            width: 100%; /* Ensure full width background */
        }
        
        .slick-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 0; /* Move padding to container so content is constrained but background is full width */
        }
        
        .slick-content-wrapper {
            display: flex;
            align-items: flex-start;
            gap: 60px;
        }
        
        /* Benefits Section */
        .slick-benefits-section {
            flex: 1.5;
            max-width: none;
        }
        
        /* Header styles */
        .slick-header {
            margin-bottom: 50px;
        }
        
        .slick-subtitle {
            color: #3b82f6; /* Keep blue for subtitle, can be overridden if needed */
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 10px;
            letter-spacing: 0.3px;
        }
        
        .slick-main-title {
            font-family: var(--font-display);
            font-size: var(--font-size-5xl);
            font-weight: 700;
            color: inherit; /* Inherit color from parent section */
            line-height: 1.2;
            margin-bottom: 0;
        }
        
        .slick-highlight {
            background-color: #fef08a;
            padding: 2px 6px;
            border-radius: 3px;
            /* Text color can be overridden by highlightColor property */
        }
        
        /* Benefits grid - 2 columns, 3 rows */
        .slick-benefits-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: repeat(3, auto);
            gap: 30px 40px;
        }
        
        /* Image Section */
        .slick-image-section {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }
        
        .slick-image-block {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .slick-phone-image {
            max-width: 80%;
            max-height: 80%;
            object-fit: contain;
            border-radius: 8px;
        }
        
        .slick-benefit-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        
        .slick-benefit-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
            flex-shrink: 0;
            padding: 0; 
            margin: 0;
        }
        
        .slick-benefit-content {
            flex: 1;
        }
        
        .slick-benefit-title {
            font-size: 24px;
            font-weight: 700;
            color: inherit; /* Inherit color from parent section */
            margin-bottom: 8px;
            line-height: 1.3;
        }
        
        .slick-benefit-description {
            font-size: 18px;
            color: inherit; /* Inherit color from parent section */
            line-height: 1.4;
        }
        
        .slick-benefit-description em {
            font-style: italic;
            color: #6b7280;
        }
        
        /* Responsive design */
        @media (max-width: 1024px) {
            .slick-container {
                max-width: 1000px;
                padding: 60px 25px;
            }
            
            .slick-content-wrapper {
                gap: 40px;
            }
            
            .slick-benefits-grid {
                gap: 25px 35px;
            }
            
            .slick-main-title {
                font-size: 34px;
            }
            
            .slick-image-block {
                width: 220px;
                height: 520px;
            }
        }
        
        @media (max-width: 768px) {
            .slick-container {
                padding: 50px 20px;
            }
            
            .slick-content-wrapper {
                flex-direction: column;
                gap: 40px;
            }
            
            .slick-benefits-section {
                max-width: 100%;
            }
            
            .slick-benefits-grid {
                grid-template-columns: 1fr;
                gap: 25px;
            }
            
            .slick-main-title {
                font-size: 30px;
            }
            
            .slick-subtitle {
                font-size: 15px;
            }
            
            .slick-benefit-item {
                gap: 12px;
            }
            
            .slick-benefit-icon {
                font-size: 36px;
            }
            
            .slick-benefit-title {
                font-size: 22px;
            }
            
            .slick-benefit-description {
                font-size: 17px;
            }
            
            .slick-image-block {
                width: 200px;
                height: 480px;
            }
        }
        
        @media (max-width: 480px) {
            .slick-container {
                padding: 40px 15px;
            }
            
            .slick-header {
                margin-bottom: 40px;
            }
            
            .slick-main-title {
                font-size: 26px;
            }
            
            .slick-subtitle {
                font-size: 14px;
            }
            
            .slick-benefits-grid {
                gap: 22px;
            }
            
            .slick-benefit-item {
                gap: 10px;
            }
            
            .slick-benefit-icon {
                font-size: 32px;
            }
            
            .slick-benefit-title {
                font-size: 20px;
            }
            
            .slick-benefit-description {
                font-size: 16px;
            }
            
            .slick-image-block {
                width: 180px;
                height: 420px;
            }
        }
    """
