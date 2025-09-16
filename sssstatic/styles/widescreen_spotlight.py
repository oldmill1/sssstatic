# sssstatic/styles/widescreen_spotlight.py
"""
Widescreen Spotlight styles module for SSSStatic - contains CSS styles for widescreen spotlight component
Inspired by Apple TV+ poster design
"""


def get_widescreen_spotlight_styles():
    """Return CSS styles for widescreen spotlight component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Widescreen Spotlight Section - True full-screen hero */
        .widescreen-spotlight-section {
            margin: 0;
            padding: 0;
            position: relative;
            border-radius: 0;
            overflow: hidden;
            min-height: 100vh;
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            margin-right: calc(-50vw + 50%);
        }
        
        /* Full-bleed background image */
        .widescreen-background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }
        
        /* Widescreen Image - full bleed */
        .widescreen-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .widescreen-background:hover .widescreen-image {
            transform: scale(1.02);
        }
        
        /* Floating content overlay */
        .widescreen-content-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 2;
            display: flex;
            align-items: center;
            padding: 4rem;
            background: linear-gradient(to bottom, transparent 0%, transparent 60%, rgba(0, 0, 0, 0.3) 100%);
        }
        
        /* Layout variations for text positioning */
        .widescreen-layout-right .widescreen-content-overlay {
            justify-content: flex-end;
        }
        
        .widescreen-layout-left .widescreen-content-overlay {
            justify-content: flex-start;
        }
        
        /* Content */
        .widescreen-content {
            max-width: 600px;
            width: 100%;
        }
        
        /* Widescreen Title - Dynamic font family */
        .widescreen-title {
            font-family: var(--widescreen-font-family, 'Original Surfer'), -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 5rem;
            font-weight: 400;
            margin: 0 0 1rem 0;
            color: var(--widescreen-text-color, #ffffff);
            letter-spacing: -0.02em;
            line-height: 0.9;
            text-shadow: 0 2px 20px rgba(0, 0, 0, 0.5);
        }
        
        /* Widescreen Subtitle */
        .widescreen-subtitle {
            font-family: var(--widescreen-font-family, -apple-system), BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.5rem;
            font-weight: 600;
            margin: 0 0 1.5rem 0;
            color: var(--widescreen-text-color, #ffffff);
            letter-spacing: -0.01em;
            text-shadow: 0 1px 10px rgba(0, 0, 0, 0.5);
        }
        
        /* Widescreen Description - Dynamic font family */
        .widescreen-description {
            font-family: var(--widescreen-font-family, 'Inter'), -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.5rem;
            font-weight: 500;
            margin: 0 0 2.5rem 0;
            color: var(--widescreen-text-color, #ffffff);
            line-height: 1.4;
            text-shadow: 0 2px 15px rgba(0, 0, 0, 0.6);
            max-width: 500px;
            letter-spacing: -0.01em;
        }
        
        /* Call-to-action buttons - Integrated with widescreen content */
        .widescreen-content .sss-button-group {
            margin-top: 2rem;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .widescreen-content .sss-button-group-center {
            justify-content: flex-start;
        }
        
        .widescreen-content .sss-button-group-left {
            justify-content: flex-start;
        }
        
        .widescreen-content .sss-button-group-right {
            justify-content: flex-start;
        }
        
        .widescreen-button {
            align-items: center;
            background-color: initial;
            background-image: linear-gradient(rgba(179, 132, 201, .84), rgba(57, 31, 91, .84) 50%);
            border-radius: 42px;
            border-width: 0;
            box-shadow: rgba(57, 31, 91, 0.24) 0 2px 2px,rgba(179, 132, 201, 0.4) 0 8px 12px;
            color: #FFFFFF;
            cursor: pointer;
            display: flex;
            font-family: 'Work Sans', sans-serif;
            font-size: 18px;
            font-weight: 700;
            justify-content: center;
            letter-spacing: .04em;
            line-height: 16px;
            margin: 0;
            padding: 18px 18px;
            text-align: center;
            text-decoration: none;
            text-shadow: rgba(255, 255, 255, 0.4) 0 0 4px,rgba(255, 255, 255, 0.2) 0 0 12px,rgba(57, 31, 91, 0.6) 1px 1px 4px,rgba(57, 31, 91, 0.32) 4px 4px 16px;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            vertical-align: baseline;
            transition: all 0.3s ease;
        }
        
        .widescreen-button-primary {
            background-image: linear-gradient(rgba(179, 132, 201, .84), rgba(57, 31, 91, .84) 50%);
        }
        
        .widescreen-button-primary:hover {
            background-image: linear-gradient(#B384C9, #391F5B 50%);
            transform: translateY(-2px);
        }
        
        .widescreen-button-secondary {
            background: transparent;
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: none;
            text-shadow: none;
        }
        
        .widescreen-button-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-1px);
        }
        
        /* Add lightning bolt icon for primary button */
        .widescreen-button-primary::after {
            content: "⚡";
            font-size: 18px;
            margin-left: 8px;
        }
        
        @media (min-width: 768px) {
            .widescreen-button {
                font-size: 21px;
                padding: 18px 34px;
            }
            
            .widescreen-button-primary::after {
                font-size: 21px;
            }
        }
        
        /* Responsive adjustments - maintain full-screen */
        @media (max-width: 1024px) {
            .widescreen-spotlight-section {
                min-height: 100vh;
            }
            
            .widescreen-content-overlay {
                padding: 3rem 2rem;
            }
            
            .widescreen-title {
                font-size: 3.5rem;
            }
            
            .widescreen-layout-right .widescreen-content-overlay,
            .widescreen-layout-left .widescreen-content-overlay {
                justify-content: center;
            }
        }
        
        @media (max-width: 768px) {
            .widescreen-spotlight-section {
                margin: 0;
                border-radius: 0;
                min-height: 100vh;
            }
            
            .widescreen-content-overlay {
                padding: 2rem 1.5rem;
            }
            
            .widescreen-title {
                font-size: 2.5rem;
            }
            
            .widescreen-subtitle {
                font-size: 1.25rem;
            }
            
            .widescreen-description {
                font-size: 1.25rem;
            }
            
            .widescreen-content .sss-button-group {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.75rem;
            }
            
            .widescreen-button {
                width: auto;
                max-width: 250px;
            }
        }
        
        @media (max-width: 480px) {
            .widescreen-spotlight-section {
                border-radius: 0;
                min-height: 100vh;
            }
            
            .widescreen-content-overlay {
                padding: 1.5rem 1rem;
            }
            
            .widescreen-title {
                font-size: 2rem;
            }
            
            .widescreen-subtitle {
                font-size: 1.125rem;
            }
            
            .widescreen-description {
                font-size: 1.125rem;
            }
        }
    """
