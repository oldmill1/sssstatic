# sssstatic/styles/showcase.py
"""
Showcase styles module for SSSStatic - contains CSS styles for showcase component
"""


def get_showcase_styles():
    """Return CSS styles for showcase component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Showcase Section - Full width background with centered content */
        .showcase-section {
            margin-bottom: 0;
            padding: 3rem 0;
            background: #f8f9fa;
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            margin-right: calc(-50vw + 50%);
        }
        
        .showcase-container {
            display: flex;
            align-items: center;
            gap: 4rem;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        
        /* Right-positioned image layout */
        .showcase-container.showcase-right {
            flex-direction: row-reverse !important;
        }
        
        /* Image container (left side) */
        .showcase-image {
            flex: 0 0 45%;
            position: relative;
        }
        
        .showcase-img {
            width: 100%;
            height: auto;
            border-radius: 16px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .showcase-image:hover .showcase-img {
            transform: scale(1.02);
        }
        
        /* Content container (right side) */
        .showcase-content {
            flex: 1;
            padding-left: 1rem;
        }
        
        /* Adjust padding for right-positioned image */
        .showcase-container.showcase-right .showcase-content {
            padding-left: 0;
            padding-right: 1rem;
        }
        
        /* Showcase Title */
        .showcase-title {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 2.5rem;
            font-weight: 600;
            margin: 0 0 1rem 0;
            color: #2c3e50;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }
        
        /* Showcase Subtitle */
        .showcase-subtitle {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.25rem;
            font-weight: 400;
            margin: 0 0 2rem 0;
            color: #5a6c7d;
            line-height: 1.4;
        }
        
        /* Showcase Steps */
        .showcase-steps {
            margin-bottom: 2.5rem;
        }
        
        .showcase-step {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            padding: 1rem 0;
            border-bottom: 1px solid #e1e8ed;
        }
        
        .showcase-step:last-child {
            border-bottom: none;
            margin-bottom: 0;
        }
        
        .step-emoji {
            font-size: 2rem;
            margin-right: 1rem;
            flex-shrink: 0;
            margin-top: 0.2rem;
        }
        
        .step-content {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        
        .step-text {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.375rem;
            font-weight: 600;
            color: #2c3e50;
            line-height: 1.3;
            margin-bottom: 0.25rem;
        }
        
        .step-description {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 1.125rem;
            font-weight: 400;
            color: #5a6c7d;
            line-height: 1.4;
        }
        
        /* Call-to-action button - matching widescreen button style */
        .showcase-button {
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
            padding: 18px 34px;
            text-align: center;
            text-decoration: none;
            text-shadow: rgba(255, 255, 255, 0.4) 0 0 4px,rgba(255, 255, 255, 0.2) 0 0 12px,rgba(57, 31, 91, 0.6) 1px 1px 4px,rgba(57, 31, 91, 0.32) 4px 4px 16px;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            vertical-align: baseline;
            transition: all 0.3s ease;
        }
        
        .showcase-button:hover {
            background-image: linear-gradient(#B384C9, #391F5B 50%);
            transform: translateY(-2px);
        }
        
        /* Responsive adjustments */
        @media (max-width: 1024px) {
            .showcase-container,
            .showcase-container.showcase-right {
                gap: 3rem;
                padding: 0 1.5rem;
            }
            
            .showcase-image {
                flex: 0 0 40%;
            }
            
            .showcase-title {
                font-size: 2.25rem;
            }
        }
        
        @media (max-width: 768px) {
            .showcase-section {
                margin: 2rem 0;
            }
            
            .showcase-container,
            .showcase-container.showcase-right {
                flex-direction: column;
                gap: 2rem;
                padding: 0 1rem;
            }
            
            .showcase-image {
                flex: none;
                width: 100%;
                max-width: 400px;
                margin: 0 auto;
            }
            
            .showcase-content {
                padding-left: 0;
                padding-right: 0;
                text-align: center;
            }
            
            .showcase-title {
                font-size: 2rem;
            }
            
            .showcase-subtitle {
                font-size: 1.125rem;
            }
            
            .showcase-step {
                justify-content: center;
                text-align: left;
            }
            
            .step-emoji {
                font-size: 1.75rem;
            }
            
            .step-text {
                font-size: 1rem;
            }
            
            .showcase-button {
                width: 100%;
                max-width: 300px;
            }
        }
        
        @media (max-width: 480px) {
            .showcase-container,
            .showcase-container.showcase-right {
                padding: 0 0.75rem;
            }
            
            .showcase-title {
                font-size: 1.75rem;
            }
            
            .showcase-subtitle {
                font-size: 1rem;
            }
            
            .step-emoji {
                font-size: 1.5rem;
                margin-right: 0.75rem;
            }
            
            .step-text {
                font-size: 0.95rem;
            }
            
            .showcase-button {
                font-size: 1rem;
                padding: 0.875rem 1.5rem;
            }
        }
    """
