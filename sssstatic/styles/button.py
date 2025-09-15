# sssstatic/styles/button.py
"""
Button styles module for SSSStatic - contains CSS styles for centralized button component

BUTTON TYPES AVAILABLE:

1. BUTTON SIZES:
   - .sss-button-small: Compact button (0.875rem font, 0.5rem padding, 8px radius)
   - .sss-button-medium: Standard button (1rem font, 0.875rem padding, 12px radius) 
   - .sss-button-large: Prominent button (1.125rem font, 1rem padding, 16px radius)

2. BUTTON VARIANTS:
   - .sss-button-primary: Apple-style blue button (#007AFF) - Main action buttons
   - .sss-button-secondary: Transparent with blue border - Secondary actions
   - .sss-button-gradient: Purple gradient with shadow - Premium/featured buttons
   - .sss-button-cta: Dark button (#1a1a1a) - Call-to-action buttons

3. BUTTON ICONS (add after button text):
   - .sss-button-icon-lightning: ⚡ (for energy/action)
   - .sss-button-icon-arrow: → (for navigation/next)
   - .sss-button-icon-star: ★ (for favorites/rating)
   - .sss-button-icon-heart: ♥ (for likes/love)
   - .sss-button-icon-check: ✓ (for success/completion)
   - .sss-button-icon-plus: + (for add/create)
   - .sss-button-icon-minus: - (for remove/delete)

4. BUTTON GROUPS (for multiple buttons):
   - .sss-button-group: Base flex container
   - .sss-button-group-left/center/right: Alignment options
   - .sss-button-group-small/medium/large: Gap spacing (0.5rem/1rem/1.5rem)

USAGE EXAMPLES:
- Primary CTA: "sss-button sss-button-primary sss-button-large sss-button-icon-arrow"
- Secondary action: "sss-button sss-button-secondary sss-button-medium"
- Premium feature: "sss-button sss-button-gradient sss-button-large sss-button-icon-star"
- Compact action: "sss-button sss-button-cta sss-button-small sss-button-icon-plus"

All buttons include hover effects, focus states for accessibility, and responsive behavior.
"""


def get_button_styles():
    """Return CSS styles for button component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* SSS Button Component - Centralized Button Styles */
        
        /* Base button styles */
        .sss-button {
            font-family: "myriad-pro", system-ui, -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-weight: 500;
            border-radius: 1000px;
            border: none;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            letter-spacing: 0.0375em;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            vertical-align: baseline;
            position: relative;
            overflow: hidden;
            outline: none;
        }
        
        /* Button sizes */
        .sss-button-small {
            font-size: 0.875rem;
            padding: 0.5rem 1.5rem;
            min-width: 4em;
        }
        
        .sss-button-medium {
            font-size: 1rem;
            padding: 0.875rem 2rem;
            min-width: 6em;
        }
        
        .sss-button-large {
            font-size: 1.125rem;
            padding: 1rem 2.5rem;
            min-width: 6em;
        }
        
        /* Override button sizes to use custom padding for gradient buttons */
        .sss-button-default.sss-button-small,
        .sss-button-warning.sss-button-small,
        .sss-button-success.sss-button-small,
        .sss-button-neutral.sss-button-small {
            padding: 0.375rem 1rem;
            font-size: 0.875rem;
        }
        
        .sss-button-default.sss-button-medium,
        .sss-button-warning.sss-button-medium,
        .sss-button-success.sss-button-medium,
        .sss-button-neutral.sss-button-medium {
            padding: 0.5rem 1.5rem;
            font-size: 1rem;
        }
        
        .sss-button-default.sss-button-large,
        .sss-button-warning.sss-button-large,
        .sss-button-success.sss-button-large,
        .sss-button-neutral.sss-button-large {
            padding: 0.625rem 2rem;
            font-size: 1.125rem;
        }
        
        /* Link button sizes */
        .sss-button-link.sss-button-small {
            padding: 0.125rem 0.375rem;
            font-size: 0.875rem;
        }
        
        .sss-button-link.sss-button-medium {
            padding: 0.25rem 0.5rem;
            font-size: 1rem;
        }
        
        .sss-button-link.sss-button-large {
            padding: 0.375rem 0.75rem;
            font-size: 1.125rem;
        }
        
        /* Legacy primary button - maps to default for backward compatibility */
        .sss-button-primary.sss-button-small {
            padding: 0.375rem 1rem;
            font-size: 0.875rem;
        }
        
        .sss-button-primary.sss-button-medium {
            padding: 0.5rem 1.5rem;
            font-size: 1rem;
        }
        
        .sss-button-primary.sss-button-large {
            padding: 0.625rem 2rem;
            font-size: 1.125rem;
        }
        
        /* Primary button - Custom button-7 design with variants */
        .sss-button-primary {
            touch-action: manipulation;
            cursor: pointer;
            position: relative;
            padding: 0.5rem 1.5rem;
            border-radius: 1.87rem;
            line-height: 1;
            font-size: 1rem;
            font-weight: 600;
            transition: all 150ms ease-in-out;
            white-space: nowrap;
            
            border: 1px solid #012880;
            background-image: linear-gradient(-180deg, #4FC3F7 0%, #2E7D32 100%);
            box-shadow: 0 0.5rem 0.625rem 0 rgba(0,0,0,0.2),
                        0 -0.125rem 0.75rem rgba(25, 118, 210, 1) inset,
                        0 0.375rem 0.125rem rgba(255,255,255, 0.4) inset,
                        0 0.125rem 0.25rem 0 rgba(76, 175, 80, 1) inset;
        }
        
        .sss-button-primary:hover {
            filter: brightness(1.1);
            text-decoration: none;
        }
        
        .sss-button-primary:active {
            transform: scale(.96);
            text-decoration: none;
        }
        
        .sss-button-primary:focus {
            outline: none;
        }
        
        /* Primary button variants */
        .sss-button-primary.sss-button-variant-default {
            /* Default blue-green gradient - already defined above */
        }
        
        .sss-button-primary.sss-button-variant-warning {
            border: 1px solid #D84315;
            background-image: linear-gradient(-180deg, #FF7043 0%, #D84315 100%);
            box-shadow: 0 0.5rem 0.625rem 0 rgba(0,0,0,0.2),
                        0 -0.125rem 0.75rem rgba(211, 47, 47, 1) inset,
                        0 0.375rem 0.125rem rgba(255,255,255, 0.4) inset,
                        0 0.125rem 0.25rem 0 rgba(255, 87, 34, 1) inset;
        }
        
        .sss-button-primary.sss-button-variant-success {
            border: 1px solid #1B5E20;
            background-image: linear-gradient(-180deg, #66BB6A 0%, #2E7D32 100%);
            box-shadow: 0 0.5rem 0.625rem 0 rgba(0,0,0,0.2),
                        0 -0.125rem 0.75rem rgba(27, 94, 32, 1) inset,
                        0 0.375rem 0.125rem rgba(255,255,255, 0.4) inset,
                        0 0.125rem 0.25rem 0 rgba(76, 175, 80, 1) inset;
        }
        
        .sss-button-primary.sss-button-variant-neutral {
            border: 1px solid #424242;
            background-image: linear-gradient(-180deg, #E0E0E0 0%, #9E9E9E 100%);
            box-shadow: 0 0.5rem 0.625rem 0 rgba(0,0,0,0.2),
                        0 -0.125rem 0.75rem rgba(66, 66, 66, 1) inset,
                        0 0.375rem 0.125rem rgba(255,255,255, 0.4) inset,
                        0 0.125rem 0.25rem 0 rgba(158, 158, 158, 1) inset;
        }
        
        .sss-button-primary.sss-button-variant-link {
            border: none;
            background: transparent;
            box-shadow: none;
            color: #81C4F7;
            text-decoration: none;
            padding: 0;
            border-radius: 0;
            font-weight: 500;
            display: inline;
            text-align: left;
        }
        
        .sss-button-primary.sss-button-variant-link:hover {
            color: #1976D2;
            text-decoration: none;
            background: transparent;
            filter: none;
            transform: none;
        }
        
        .sss-button-primary.sss-button-variant-link:active {
            color: #0D47A1;
            transform: none;
        }
        
        .sss-button-primary.sss-button-variant-link:focus {
            outline: 1px solid #4FC3F7;
            outline-offset: 1px;
        }
        
        /* Text styling for primary button variants */
        .sss-button-primary .sss-button-text {
            color: transparent;
            background-image: linear-gradient(0deg, #81C784 -10%, #FEFAFD 100%);
            -webkit-background-clip: text;
            background-clip: text;
            filter: drop-shadow(0 2px 2px hsla(120, 100%, 20%, 1));
        }
        
        .sss-button-primary.sss-button-variant-warning .sss-button-text {
            background-image: linear-gradient(0deg, #FFAB91 -10%, #FEFAFD 100%);
            filter: drop-shadow(0 2px 2px hsla(14, 100%, 20%, 1));
        }
        
        .sss-button-primary.sss-button-variant-success .sss-button-text {
            background-image: linear-gradient(0deg, #A5D6A7 -10%, #FEFAFD 100%);
            filter: drop-shadow(0 2px 2px hsla(120, 100%, 20%, 1));
        }
        
        .sss-button-primary.sss-button-variant-neutral .sss-button-text {
            background-image: linear-gradient(0deg, #F5F5F5 -10%, #424242 100%);
            filter: drop-shadow(0 2px 2px hsla(0, 0%, 20%, 1));
        }
        
        .sss-button-primary.sss-button-variant-link .sss-button-text {
            color: inherit;
            background: none;
            -webkit-background-clip: unset;
            background-clip: unset;
            filter: none;
            text-decoration: inherit;
        }
        
        /* Shine effects for primary button variants (except link) */
        .sss-button-primary:not(.sss-button-variant-link)::before,
        .sss-button-primary.sss-button-variant-default::before,
        .sss-button-primary.sss-button-variant-warning::before,
        .sss-button-primary.sss-button-variant-success::before,
        .sss-button-primary.sss-button-variant-neutral::before {
            content: "";
            display: block;
            height: 0.125rem;
            position: absolute;
            top: 0.25rem;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 1.5rem);
            background: #fff;
            border-radius: 100%;
            
            opacity: 0.7;
            background-image: linear-gradient(-270deg, rgba(255,255,255,0.00) 0%, #FFFFFF 20%, #FFFFFF 80%, rgba(255,255,255,0.00) 100%);
        }
        
        .sss-button-primary:not(.sss-button-variant-link)::after,
        .sss-button-primary.sss-button-variant-default::after,
        .sss-button-primary.sss-button-variant-warning::after,
        .sss-button-primary.sss-button-variant-success::after,
        .sss-button-primary.sss-button-variant-neutral::after {
            content: "";
            display: block;
            height: 0.125rem;
            position: absolute;
            bottom: 0.375rem;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 1.5rem);
            background: #fff;
            border-radius: 100%;
            
            filter: blur(1px);
            opacity: 0.05;
            background-image: linear-gradient(-270deg, rgba(255,255,255,0.00) 0%, #FFFFFF 20%, #FFFFFF 80%, rgba(255,255,255,0.00) 100%);
        }
        
        /* Adjust shine effects for different button sizes */
        .sss-button-primary.sss-button-small::before,
        .sss-button-primary.sss-button-small::after,
        .sss-button-primary.sss-button-variant-default.sss-button-small::before,
        .sss-button-primary.sss-button-variant-default.sss-button-small::after,
        .sss-button-primary.sss-button-variant-warning.sss-button-small::before,
        .sss-button-primary.sss-button-variant-warning.sss-button-small::after,
        .sss-button-primary.sss-button-variant-success.sss-button-small::before,
        .sss-button-primary.sss-button-variant-success.sss-button-small::after,
        .sss-button-primary.sss-button-variant-neutral.sss-button-small::before,
        .sss-button-primary.sss-button-variant-neutral.sss-button-small::after {
            width: calc(100% - 1rem);
        }
        
        .sss-button-primary.sss-button-large::before,
        .sss-button-primary.sss-button-large::after,
        .sss-button-primary.sss-button-variant-default.sss-button-large::before,
        .sss-button-primary.sss-button-variant-default.sss-button-large::after,
        .sss-button-primary.sss-button-variant-warning.sss-button-large::before,
        .sss-button-primary.sss-button-variant-warning.sss-button-large::after,
        .sss-button-primary.sss-button-variant-success.sss-button-large::before,
        .sss-button-primary.sss-button-variant-success.sss-button-large::after,
        .sss-button-primary.sss-button-variant-neutral.sss-button-large::before,
        .sss-button-primary.sss-button-variant-neutral.sss-button-large::after {
            width: calc(100% - 2rem);
        }
        
        /* Secondary button - Sophisticated gradient with shine effects */
        .sss-button-secondary {
            background: linear-gradient(rgba(160, 160, 160, 0.625), rgba(255, 255, 255, 0.625));
            color: #ffffff;
            border: none;
            position: relative;
            overflow: hidden;
            box-shadow: 0 0.375em 0.5em rgba(0, 0, 0, 0.2), 
                        0 0.125em 0.125em rgba(0, 0, 0, 0.3),  
                        inset 0 0.25em 0.25em rgba(0, 0, 0, 0.4),
                        inset 0 0.375em 0.5em 0.25em #BBBBBB;
        }
        
        .sss-button-secondary:hover {
            transform: translateY(-1px);
            box-shadow: 0 0.5em 0.6em rgba(0, 0, 0, 0.25), 
                        0 0.15em 0.15em rgba(0, 0, 0, 0.35),  
                        inset 0 0.25em 0.25em rgba(0, 0, 0, 0.4),
                        inset 0 0.375em 0.5em 0.25em #BBBBBB;
        }
        
        .sss-button-secondary:focus,
        .sss-button-secondary:active {
            box-shadow: 0 0.375em 0.5em rgba(0, 0, 0, 0.2), 
                        0 0.125em 0.125em rgba(0, 0, 0, 0.3),  
                        inset 0 0.25em 0.25em rgba(0, 0, 0, 0.4),
                        inset 0 0.375em 0.5em 0.25em #BBBBBB,
                        0 0 0.5em rgba(0, 0, 0, 0.25);
        }
        
        /* Top shine effect for secondary button */
        .sss-button-secondary::before {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            height: 33%;
            background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.3));
            width: calc(100% - 0.875em);
            border-radius: 2em 2em 0.5em 0.5em;
            top: 5%;
            filter: blur(1px);
            z-index: 2;
        }
        
        /* Bottom glow effect for secondary button */
        .sss-button-secondary::after {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            height: 33%;
            background: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.5));
            width: calc(100% - 1.25em);
            border-radius: 0.75em;
            bottom: 10%;
            filter: blur(3px);
        }
        
        /* Text styling for secondary button */
        .sss-button-secondary .sss-button-text {
            position: relative;
            top: -1px;
            z-index: 1;
            letter-spacing: 0.0375em;
            -webkit-text-stroke-width: 0.025em;
            -webkit-text-stroke-color: #000000;
            text-shadow: 0 0.25em 0.2em rgba(0, 0, 0, 0.25);
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
            outline: none;
        }
        
        .sss-button-gradient:focus {
            outline: none;
        }
        
        .sss-button-cta:focus {
            outline: none;
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
