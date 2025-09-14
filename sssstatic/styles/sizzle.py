# sssstatic/styles/sizzle.py
"""
Sizzle styles module for SSSStatic - contains CSS styles for sizzle component
"""


def get_sizzle_styles():
    """Return CSS styles for sizzle component."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Sizzle Process Section - Full width background with centered content */
        .sizzle-section {
            margin-bottom: 0;
            padding: 3rem 0;
            background: #fafafa;
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            margin-right: calc(-50vw + 50%);
        }
        
        .sizzle-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            color: #374151;
        }
        
        /* Override dark theme for sizzle section */
        .sizzle-section * {
            color: inherit;
        }

        /* Process section */
        .sizzle-container .process-section {
            text-align: center;
        }

        /* Header styles */
        .sizzle-container .header {
            margin-bottom: 60px;
        }

        .sizzle-container .subtitle {
            color: #3b82f6;
            font-size: 18px;
            font-weight: 500;
            margin-bottom: 10px;
        }

        .sizzle-container .main-title {
            font-size: 48px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .sizzle-container .description {
            font-size: 18px;
            color: #6b7280;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }

        /* Process steps grid */
        .sizzle-container .process-steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 40px;
            margin-top: 40px;
        }

        .sizzle-container .step {
            text-align: center;
            padding: 20px;
            border-radius: 12px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .sizzle-container .step:hover {
            background-color: #fff;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }

        .sizzle-container .step-icon {
            font-size: 48px;
            margin-bottom: 20px;
            display: block;
        }

        .sizzle-container .step-title {
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 15px;
            line-height: 1.3;
        }

        .sizzle-container .step-description {
            font-size: 16px;
            color: #6b7280;
            line-height: 1.6;
            max-width: 300px;
            margin: 0 auto;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .sizzle-section {
                padding: 2rem 0;
            }
            
            .sizzle-container {
                padding: 0 1rem;
            }
            
            .sizzle-container .main-title {
                font-size: 36px;
            }
            
            .sizzle-container .subtitle {
                font-size: 16px;
            }
            
            .sizzle-container .description {
                font-size: 16px;
                padding: 0 10px;
            }
            
            .sizzle-container .process-steps {
                grid-template-columns: 1fr;
                gap: 30px;
                margin-top: 30px;
            }
            
            .sizzle-container .step {
                padding: 15px;
            }
            
            .sizzle-container .step-icon {
                font-size: 40px;
                margin-bottom: 15px;
            }
            
            .sizzle-container .step-title {
                font-size: 20px;
                margin-bottom: 12px;
            }
            
            .sizzle-container .step-description {
                font-size: 15px;
            }
        }

        @media (max-width: 480px) {
            .sizzle-section {
                padding: 1.5rem 0;
            }
            
            .sizzle-container {
                padding: 0 0.75rem;
            }
            
            .sizzle-container .main-title {
                font-size: 28px;
            }
            
            .sizzle-container .subtitle {
                font-size: 14px;
            }
            
            .sizzle-container .description {
                font-size: 14px;
            }
            
            .sizzle-container .step-icon {
                font-size: 36px;
            }
            
            .sizzle-container .step-title {
                font-size: 18px;
            }
            
            .sizzle-container .step-description {
                font-size: 14px;
            }
        }

        /* Tablet landscape */
        @media (min-width: 769px) and (max-width: 1024px) {
            .sizzle-container .process-steps {
                grid-template-columns: repeat(2, 1fr);
                gap: 35px;
            }
        }

        /* Large screens */
        @media (min-width: 1025px) {
            .sizzle-container .process-steps {
                grid-template-columns: repeat(4, 1fr);
                gap: 30px;
            }
            
            .sizzle-container .step-description {
                max-width: 250px;
            }
        }
    """
