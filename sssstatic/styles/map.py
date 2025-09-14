# sssstatic/styles/map.py
"""
Map styles module for SSSStatic - contains CSS styles for map components
"""


def get_map_styles():
    """Return CSS styles for map components."""
    return """
        /* Map Container */
        .map-container {
            width: 100vw;
            height: 100vh;
            padding: 0;
            position: relative;
            margin-left: calc(-50vw + 50%);
            margin-right: calc(-50vw + 50%);
        }

        #map {
            width: 100%;
            height: 100%;
            filter: 
                hue-rotate(200deg) 
                saturate(0.6) 
                brightness(1.1) 
                contrast(0.9);
        }

        /* Custom pastel map styling */
        .leaflet-tile {
            filter: 
                hue-rotate(180deg) 
                saturate(0.7) 
                brightness(1.2) 
                contrast(0.8);
        }

        /* Override specific map elements with pastel colors */
        .leaflet-container {
            background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
        }

        /* Custom pastel styling for map tiles */
        .leaflet-tile-pane {
            opacity: 0.9;
        }

        /* Custom larger marker styling */
        .custom-marker {
            background: transparent;
            border: none;
        }

        .marker-pin {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #ff6b35, #e55a2b);
            border: 4px solid #ffffff;
            border-radius: 50% 50% 50% 0;
            transform: rotate(-45deg);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4), 0 0 0 2px rgba(255, 107, 53, 0.2);
            position: relative;
            transition: all 0.3s ease;
        }

        .marker-pin:hover {
            transform: rotate(-45deg) scale(1.1);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5), 0 0 0 3px rgba(255, 107, 53, 0.3);
        }

        .marker-pin::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 18px;
            height: 18px;
            background: #ffffff;
            border-radius: 50%;
            transform: translate(-50%, -50%) rotate(45deg);
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Apple CarPlay-style overlay layer */
        .overlay-layer {
            position: absolute;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            pointer-events: auto;
        }

        .overlay-content {
            background: linear-gradient(135deg, 
                rgba(60, 70, 80, 0.85) 0%, 
                rgba(80, 90, 100, 0.8) 50%, 
                rgba(60, 70, 80, 0.85) 100%);
            backdrop-filter: blur(20px) saturate(1.1);
            border-radius: 20px;
            padding: 48px 40px;
            box-shadow: 
                0 12px 40px rgba(0, 0, 0, 0.3),
                0 0 0 1px rgba(255, 255, 255, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.2);
            min-width: 500px;
            max-width: 600px;
            text-align: left;
            position: relative;
            overflow: hidden;
        }

        .overlay-content::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(255, 255, 255, 0.3) 20%, 
                rgba(255, 255, 255, 0.5) 50%, 
                rgba(255, 255, 255, 0.3) 80%, 
                transparent 100%);
            z-index: 1;
        }

        .overlay-content::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, 
                rgba(255, 255, 255, 0.03) 0%, 
                transparent 30%, 
                transparent 70%, 
                rgba(255, 255, 255, 0.01) 100%);
            pointer-events: none;
            z-index: 0;
        }

        .business-name {
            color: #ffffff;
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 42px;
            font-weight: 800;
            letter-spacing: -0.8px;
            line-height: 1.1;
            margin-bottom: 16px;
            position: relative;
            z-index: 2;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }

        .business-tagline {
            color: #e5e7eb;
            font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 22px;
            font-weight: 500;
            letter-spacing: 0.3px;
            line-height: 1.3;
            margin-bottom: 20px;
            opacity: 0.9;
            position: relative;
            z-index: 2;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
        }

        .business-location {
            color: #d1d5db;
            font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 20px;
            font-weight: 400;
            letter-spacing: 0.2px;
            line-height: 1.4;
            margin-bottom: 24px;
            opacity: 0.8;
            position: relative;
            z-index: 2;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        }

        .business-contact {
            color: #ffffff;
            font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 22px;
            font-weight: 600;
            letter-spacing: 0.4px;
            line-height: 1.3;
            position: relative;
            z-index: 2;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
        }

        .phone-number {
            color: #60a5fa;
            font-weight: 700;
            text-decoration: none;
            cursor: pointer;
            transition: color 0.2s ease;
        }

        .phone-number:hover {
            color: #93c5fd;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .map-container {
                height: 100vh;
            }
            
            .overlay-content {
                min-width: 300px;
                max-width: 400px;
                padding: 32px 24px;
            }
            
            .business-name {
                font-size: 32px;
            }
            
            .business-tagline {
                font-size: 18px;
            }
            
            .business-location {
                font-size: 16px;
            }
            
            .business-contact {
                font-size: 18px;
            }
        }

        @media (max-width: 480px) {
            .map-container {
                height: 100vh;
            }
            
            .overlay-content {
                min-width: 280px;
                max-width: 320px;
                padding: 24px 20px;
            }
            
            .business-name {
                font-size: 28px;
            }
            
            .business-tagline {
                font-size: 16px;
            }
            
            .business-location {
                font-size: 14px;
            }
            
            .business-contact {
                font-size: 16px;
            }
        }
    """
