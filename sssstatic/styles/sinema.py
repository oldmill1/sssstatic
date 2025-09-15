# sssstatic/styles/sinema.py
"""
Sinema styles module for SSSStatic - contains CSS styles for sinema component
"""


def get_sinema_styles():
    """Return CSS styles for sinema component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Sinema Section - Minimal Terminal Display */
        .sinema-section {
            margin: 0; 
            padding: 0;
            background: transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            border-left: none !important;
            padding-left: 0 !important;
        }
        
        .sinema-section::before {
            display: none !important;
        }
        
        .sinema-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            width: 100%;
        }
        
        .sinema-content-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0;
        }
        
        /* Terminal Section */
        .sinema-terminal-section {
            width: 100%;
            max-width: 800px;
            display: flex;
            justify-content: center;
        }
        
        .sinema-terminal-container {
            width: 100%;
            background: transparent;
            border-radius: 0;
            padding: 0;
            box-shadow: none;
            position: relative;
        }
        
        /* OS X Tiger Traffic Light Buttons */
        .sinema-traffic-lights {
            position: absolute;
            top: 0.75rem;
            left: 0.75rem;
            display: flex;
            gap: 8px;
            z-index: 10;
        }
        
        .sinema-traffic-light {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            position: relative;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .sinema-traffic-light:hover {
            transform: scale(1.1);
        }
        
        .sinema-traffic-light.red {
            background: linear-gradient(135deg, #ff5f56 0%, #ff3b30 50%, #d70015 100%);
            box-shadow: 
                0 1px 3px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.4),
                inset 0 -1px 0 rgba(0, 0, 0, 0.2);
        }
        
        .sinema-traffic-light.yellow {
            background: linear-gradient(135deg, #ffbd2e 0%, #ff9500 50%, #ff8c00 100%);
            box-shadow: 
                0 1px 3px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.4),
                inset 0 -1px 0 rgba(0, 0, 0, 0.2);
        }
        
        .sinema-traffic-light.green {
            background: linear-gradient(135deg, #27ca3f 0%, #30d158 50%, #34c759 100%);
            box-shadow: 
                0 1px 3px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.4),
                inset 0 -1px 0 rgba(0, 0, 0, 0.2);
        }
        
        /* Glossy aqua glass effect */
        .sinema-traffic-light::before {
            content: '';
            position: absolute;
            top: 1px;
            left: 1px;
            right: 1px;
            height: 50%;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.6) 0%, rgba(255, 255, 255, 0.1) 100%);
            border-radius: 50%;
            pointer-events: none;
        }
        
        /* Subtle inner glow */
        .sinema-traffic-light::after {
            content: '';
            position: absolute;
            top: 2px;
            left: 2px;
            right: 2px;
            bottom: 2px;
            background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.3) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }
        
        
        .sinema-terminal-screen {
            background: #1a1a1a;
            border-radius: 8px;
            padding: 1.5rem;
            padding-top: 2.5rem;
            min-height: 400px;
            position: relative;
            overflow: hidden;
            border: 1px solid #333;
            /* Vintage CRT curved glass effect */
            transform: perspective(800px) rotateX(2deg);
            box-shadow: 
                inset 0 0 20px rgba(0, 0, 0, 0.3),
                inset 0 0 40px rgba(0, 0, 0, 0.1),
                0 0 30px rgba(0, 0, 0, 0.2),
                0 8px 16px rgba(0, 0, 0, 0.4);
        }
        
        /* Glassmorphic glare effect */
        .sinema-terminal-screen::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(
                ellipse 300px 200px at 30% 20%,
                rgba(255, 255, 255, 0.08) 0%,
                rgba(255, 255, 255, 0.04) 40%,
                rgba(255, 255, 255, 0.02) 70%,
                transparent 100%
            );
            border-radius: 8px;
            pointer-events: none;
            z-index: 1;
        }
        
        .sinema-terminal-content {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 19px;
            line-height: 1.4;
            color: #4ade80;
            position: relative;
            z-index: 2;
            /* Vintage CRT text glow */
            text-shadow: 
                0 0 3px #4ade80,
                0 0 6px rgba(74, 222, 128, 0.3),
                0 0 9px rgba(74, 222, 128, 0.1);
        }
        
        .sinema-terminal-line {
            opacity: 0;
            animation: sinema-typewriter 0.1s ease-in-out forwards;
            margin-bottom: 0.5rem;
        }
        
        .sinema-terminal-text {
            display: inline-block;
            text-shadow: 0 0 3px #4ade80;
        }
        
        /* Terminal cursor */
        .sinema-terminal-line:last-child::after {
            content: '_';
            animation: sinema-cursor 1s infinite;
            color: #4ade80;
            text-shadow: 0 0 3px #4ade80;
        }
        
        /* Animations */
        @keyframes sinema-typewriter {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes sinema-cursor {
            0%, 50% {
                opacity: 1;
            }
            51%, 100% {
                opacity: 0;
            }
        }
        
        /* Vintage CRT scanlines and curved glass effect */
        .sinema-terminal-screen::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 1px,
                    rgba(74, 222, 128, 0.03) 1px,
                    rgba(74, 222, 128, 0.03) 2px
                ),
                radial-gradient(
                    ellipse at center,
                    transparent 0%,
                    rgba(0, 0, 0, 0.1) 70%,
                    rgba(0, 0, 0, 0.2) 100%
                );
            pointer-events: none;
            animation: sinema-scanlines 0.1s linear infinite;
            border-radius: 8px;
        }
        
        @keyframes sinema-scanlines {
            0% {
                transform: translateY(0);
            }
            100% {
                transform: translateY(2px);
            }
        }
        
        /* Responsive design */
        @media (max-width: 1024px) {
            .sinema-container {
                padding: 1.5rem;
            }
            
            .sinema-terminal-container {
                padding: 0;
            }
            
            .sinema-terminal-screen {
                min-height: 350px;
                padding: 1.25rem;
            }
        }
        
        @media (max-width: 768px) {
            .sinema-container {
                padding: 1rem;
            }
            
            .sinema-terminal-container {
                padding: 0;
            }
            
            .sinema-terminal-screen {
                min-height: 300px;
                padding: 1rem;
            }
            
            .sinema-terminal-content {
                font-size: 14px;
            }
        }
        
        @media (max-width: 480px) {
            .sinema-container {
                padding: 0.75rem;
            }
            
            .sinema-terminal-container {
                padding: 0;
            }
            
            .sinema-terminal-screen {
                min-height: 250px;
                padding: 0.75rem;
            }
            
            .sinema-terminal-content {
                font-size: 13px;
            }
        }
    """
