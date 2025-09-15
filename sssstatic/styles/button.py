# sssstatic/styles/button.py
"""
Button styles module for SSSStatic - contains CSS styles for centralized button component
"""


def get_button_styles():
    """Return CSS styles for button component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* SSS Button Component - Centralized Button Styles */
        
        /* Base button styles */
        .sss-button {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-weight: 500;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            letter-spacing: -0.01em;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            vertical-align: baseline;
            position: relative;
            overflow: hidden;
        }
        
        /* Button sizes */
        .sss-button-small {
            font-size: 0.875rem;
            padding: 0.5rem 1rem;
            border-radius: 8px;
        }
        
        .sss-button-medium {
            font-size: 1rem;
            padding: 0.875rem 2rem;
        }
        
        .sss-button-large {
            font-size: 1.125rem;
            padding: 1rem 2.5rem;
            border-radius: 16px;
        }
        
        /* Primary button - Apple-style blue */
        .sss-button-primary {
            background: #007AFF;
            color: #ffffff;
            border: none;
        }
        
        .sss-button-primary:hover {
            background: #0056CC;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 122, 255, 0.3);
        }
        
        /* Secondary button - Transparent with border */
        .sss-button-secondary {
            background: transparent;
            color: #007AFF;
            border: 1px solid #007AFF;
        }
        
        .sss-button-secondary:hover {
            background: rgba(0, 122, 255, 0.1);
            transform: translateY(-2px);
        }
        
        /* Gradient button - Purple gradient with shadow */
        .sss-button-gradient {
            background-color: initial;
            background-image: linear-gradient(rgba(179, 132, 201, .84), rgba(57, 31, 91, .84) 50%);
            border-radius: 42px;
            border-width: 0;
            box-shadow: rgba(57, 31, 91, 0.24) 0 2px 2px,rgba(179, 132, 201, 0.4) 0 8px 12px;
            color: #FFFFFF;
            font-weight: 700;
            letter-spacing: .04em;
            text-shadow: rgba(255, 255, 255, 0.4) 0 0 4px,rgba(255, 255, 255, 0.2) 0 0 12px,rgba(57, 31, 91, 0.6) 1px 1px 4px,rgba(57, 31, 91, 0.32) 4px 4px 16px;
        }
        
        .sss-button-gradient:hover {
            background-image: linear-gradient(#B384C9, #391F5B 50%);
            transform: translateY(-2px);
        }
        
        /* CTA button - Dark with icon */
        .sss-button-cta {
            background: #1a1a1a;
            color: #ffffff;
            border: 1px solid #333;
            font-weight: 500;
        }
        
        .sss-button-cta:hover {
            background: #333333;
            transform: translateY(-1px);
        }
        
        /* Button icons */
        .sss-button-icon {
            font-size: 1.1em;
            display: inline-flex;
            align-items: center;
        }
        
        .sss-button-text {
            font-weight: inherit;
        }
        
        /* Icon-specific styles */
        .sss-button-icon-lightning::after {
            content: "⚡";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        .sss-button-icon-arrow::after {
            content: "→";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        .sss-button-icon-star::after {
            content: "★";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        .sss-button-icon-heart::after {
            content: "♥";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        .sss-button-icon-check::after {
            content: "✓";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        .sss-button-icon-plus::after {
            content: "+";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        .sss-button-icon-minus::after {
            content: "-";
            font-size: 1.1em;
            margin-left: 0.5rem;
        }
        
        /* Button group styles */
        .sss-button-group {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
        }
        
        .sss-button-group-left {
            justify-content: flex-start;
        }
        
        .sss-button-group-center {
            justify-content: center;
        }
        
        .sss-button-group-right {
            justify-content: flex-end;
        }
        
        .sss-button-group-small {
            gap: 0.5rem;
        }
        
        .sss-button-group-medium {
            gap: 1rem;
        }
        
        .sss-button-group-large {
            gap: 1.5rem;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .sss-button-group {
                flex-direction: column;
                align-items: center;
            }
            
            .sss-button-group-left,
            .sss-button-group-right {
                justify-content: center;
            }
            
            .sss-button {
                width: 100%;
                max-width: 300px;
            }
            
            .sss-button-small {
                max-width: 200px;
            }
            
            .sss-button-large {
                max-width: 350px;
            }
        }
        
        @media (max-width: 480px) {
            .sss-button-medium {
                font-size: 0.9rem;
                padding: 0.75rem 1.5rem;
            }
            
            .sss-button-large {
                font-size: 1rem;
                padding: 0.875rem 2rem;
            }
        }
        
        /* Focus styles for accessibility */
        .sss-button:focus {
            outline: 2px solid #007AFF;
            outline-offset: 2px;
        }
        
        .sss-button-gradient:focus {
            outline-color: #B384C9;
        }
        
        .sss-button-cta:focus {
            outline-color: #ffffff;
        }
        
        /* Disabled state */
        .sss-button:disabled,
        .sss-button.disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none !important;
        }
        
        .sss-button:disabled:hover,
        .sss-button.disabled:hover {
            transform: none;
            box-shadow: none;
        }
    """
