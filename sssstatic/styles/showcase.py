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
        
        /* Call-to-action button - matching primary button style */
        .showcase-button {
            font-family: "myriad-pro", system-ui, -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-weight: 600;
            border-radius: 1.87rem;
            border: 1px solid #012880;
            background-image: linear-gradient(-180deg, #4FC3F7 0%, #2E7D32 100%);
            box-shadow: 0 0.5rem 0.625rem 0 rgba(0,0,0,0.2),
                        0 -0.125rem 0.75rem rgba(25, 118, 210, 1) inset,
                        0 0.375rem 0.125rem rgba(255,255,255, 0.4) inset,
                        0 0.125rem 0.25rem 0 rgba(76, 175, 80, 1) inset;
            color: transparent;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            letter-spacing: 0.0375em;
            line-height: 1;
            margin: 0;
            padding: 0.625rem 2rem;
            text-align: center;
            text-decoration: none;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            vertical-align: baseline;
            position: relative;
            overflow: hidden;
            outline: none;
            transition: all 150ms ease-in-out;
            white-space: nowrap;
        }
        
        .showcase-button:hover {
            filter: brightness(1.1);
            text-decoration: none;
        }
        
        .showcase-button:active {
            transform: scale(.96);
            text-decoration: none;
        }
        
        .showcase-button:focus {
            outline: none;
        }
        
        /* Text styling for showcase button */
        .showcase-button .showcase-button-text {
            color: transparent;
            background-image: linear-gradient(0deg, #81C784 -10%, #FEFAFD 100%);
            -webkit-background-clip: text;
            background-clip: text;
            filter: drop-shadow(0 2px 2px hsla(120, 100%, 20%, 1));
        }
        
        /* Shine effects for showcase button */
        .showcase-button::before {
            content: "";
            display: block;
            height: 0.125rem;
            position: absolute;
            top: 0.25rem;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 2rem);
            background: #fff;
            border-radius: 100%;
            opacity: 0.7;
            background-image: linear-gradient(-270deg, rgba(255,255,255,0.00) 0%, #FFFFFF 20%, #FFFFFF 80%, rgba(255,255,255,0.00) 100%);
        }
        
        .showcase-button::after {
            content: "";
            display: block;
            height: 0.125rem;
            position: absolute;
            bottom: 0.375rem;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 2rem);
            background: #fff;
            border-radius: 100%;
            filter: blur(1px);
            opacity: 0.05;
            background-image: linear-gradient(-270deg, rgba(255,255,255,0.00) 0%, #FFFFFF 20%, #FFFFFF 80%, rgba(255,255,255,0.00) 100%);
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
                font-size: 1rem;
                padding: 0.625rem 2rem;
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
                font-size: 0.9rem;
                padding: 0.5rem 1.5rem;
            }
        }
    """
