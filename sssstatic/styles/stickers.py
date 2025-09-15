# sssstatic/styles/stickers.py
"""
Stickers styles module for SSSStatic - contains CSS styles for sticker component

STICKER TYPES AVAILABLE:

1. STICKER SIZES:
   - .sticker-size-small: 32px x 32px - Small decorative sticker
   - .sticker-size-medium: 64px x 64px - Standard sticker size
   - .sticker-size-large: 128px x 128px - Large prominent sticker
   - .sticker-size-xlarge: 256px x 256px - Extra large sticker for emphasis

2. STICKER POSITIONS:
   - .sticker-position-left: Align sticker to the left
   - .sticker-position-center: Center the sticker (default)
   - .sticker-position-right: Align sticker to the right

3. STICKER ANIMATIONS:
   - .sticker-animation-none: No animation (default)
   - .sticker-animation-bounce: Gentle bouncing animation
   - .sticker-animation-spin: Continuous rotation
   - .sticker-animation-float: Floating up and down motion
   - .sticker-animation-pulse: Pulsing scale animation

USAGE EXAMPLES:
- Standard sticker: "sticker-component sticker-size-medium sticker-position-center"
- Large bouncing sticker: "sticker-component sticker-size-large sticker-animation-bounce"
- Small floating sticker: "sticker-component sticker-size-small sticker-animation-float"

All stickers are background images with transparent backgrounds and include hover effects.
"""


def get_sticker_styles():
    """Return CSS styles for sticker component."""
    return """
        /* SSS Sticker Component - Sticker Styles */
        
        /* Base sticker styles */
        .sticker-component {
            display: inline-block;
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            border: none;
            outline: none;
            cursor: pointer;
            transition: all 0.3s ease;
            vertical-align: middle;
        }
        
        /* Sticker sizes */
        .sticker-size-small {
            width: 32px;
            height: 32px;
        }
        
        .sticker-size-medium {
            width: 64px;
            height: 64px;
        }
        
        .sticker-size-large {
            width: 128px;
            height: 128px;
        }
        
        .sticker-size-xlarge {
            width: 256px;
            height: 256px;
        }
        
        /* Sticker positions */
        .sticker-position-left {
            margin-right: auto;
        }
        
        .sticker-position-center {
            margin-left: auto;
            margin-right: auto;
        }
        
        .sticker-position-right {
            margin-left: auto;
        }
        
        /* Sticker animations */
        .sticker-animation-bounce {
            animation: sticker-bounce 2s infinite;
        }
        
        .sticker-animation-spin {
            animation: sticker-spin 3s linear infinite;
        }
        
        .sticker-animation-float {
            animation: sticker-float 3s ease-in-out infinite;
        }
        
        .sticker-animation-pulse {
            animation: sticker-pulse 2s ease-in-out infinite;
        }
        
        /* Animation keyframes */
        @keyframes sticker-bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        }
        
        @keyframes sticker-spin {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }
        
        @keyframes sticker-float {
            0%, 100% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-15px);
            }
        }
        
        @keyframes sticker-pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
        }
        
        /* Hover effects */
        .sticker-component:hover {
            transform: scale(1.05);
            filter: brightness(1.1);
        }
        
        /* Focus states for accessibility */
        .sticker-component:focus {
            outline: 2px solid #007AFF;
            outline-offset: 2px;
        }
        
        /* Responsive behavior */
        @media (max-width: 768px) {
            .sticker-size-xlarge {
                width: 192px;
                height: 192px;
            }
            
            .sticker-size-large {
                width: 96px;
                height: 96px;
            }
            
            .sticker-size-medium {
                width: 48px;
                height: 48px;
            }
            
            .sticker-size-small {
                width: 24px;
                height: 24px;
            }
        }
        
        /* High contrast mode support */
        @media (prefers-contrast: high) {
            .sticker-component {
                filter: contrast(1.2);
            }
        }
        
        /* Reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            .sticker-component {
                animation: none !important;
                transition: none !important;
            }
            
            .sticker-component:hover {
                transform: none;
            }
        }
    """
