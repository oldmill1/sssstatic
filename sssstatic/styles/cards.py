# sssstatic/styles/cards.py
"""
Card styles module for SSSStatic - contains CSS styles for card components
"""


def get_card_styles():
    """Return CSS styles for card components."""
    from .type import get_font_styles
    return get_font_styles() + """
        /* Card Container */
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin: 0 0 1rem 0;
        }
        
        /* Individual Card */
        .card {
            background: linear-gradient(135deg, var(--card-bg) 0%, rgba(22, 27, 34, 0.8) 100%);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 12px var(--card-shadow);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(88, 166, 255, 0.3), transparent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px var(--card-shadow-hover);
            border-color: var(--card-border-hover);
        }
        
        .card:hover::before {
            opacity: 1;
        }
        
        /* Card Header */
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            gap: 1rem;
        }
        
        .card-title {
            font-family: var(--font-heading);
            font-size: var(--font-size-xl);
            font-weight: var(--font-weight-bold);
            margin: 0;
            color: var(--card-title);
            line-height: 1.3;
            flex: 1;
            letter-spacing: -0.01em;
            transition: color 0.3s ease;
        }
        
        .card:hover .card-title {
            color: rgb(148, 202, 224);
        }
        
        /* Status Badges */
        .card-status {
            font-family: var(--font-primary);
            font-size: var(--font-size-xs);
            font-weight: var(--font-weight-semibold);
            padding: 0.4rem 0.9rem;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            white-space: nowrap;
            flex-shrink: 0;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .card:hover .card-status {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        
        .status-active {
            background: linear-gradient(135deg, #10b981, #059669);
            color: #ffffff;
        }
        
        .status-experimental {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #ffffff;
        }
        
        .status-complete {
            background: linear-gradient(135deg, #8b5cf6, #7c3aed);
            color: #ffffff;
        }
        
        .status-on\\ hold {
            background: linear-gradient(135deg, #6b7280, #4b5563);
            color: #ffffff;
        }
        
        .status-development {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #ffffff;
        }
        
        .status-archived {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            color: #ffffff;
        }
        
        .status-unknown {
            background: linear-gradient(135deg, var(--status-unknown-bg), #3c4043);
            color: var(--status-unknown-text);
        }
        
        /* Card Description */
        .card-description {
            font-family: var(--font-primary);
            color: var(--card-description);
            margin: 0 0 2rem 0;
            line-height: 1.7;
            font-size: var(--font-size-base);
            font-weight: var(--font-weight-normal);
            transition: color 0.3s ease;
        }
        
        .card:hover .card-description {
            color: #e1e8ed;
        }
        
        /* Card Footer */
        .card-footer {
            margin-top: auto;
        }
        
        .card-link {
            font-family: var(--font-primary);
            display: inline-flex;
            align-items: center;
            color: var(--card-link);
            text-decoration: none;
            font-weight: var(--font-weight-semibold);
            font-size: var(--font-size-sm);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            padding: 0.75rem 1.5rem;
            border-radius: 12px;
            background: linear-gradient(135deg, var(--card-link-bg), rgba(88, 166, 255, 0.05));
            border: 1px solid var(--card-link-border);
            position: relative;
            overflow: hidden;
            letter-spacing: 0.3px;
        }
        
        .card-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(88, 166, 255, 0.1), transparent);
            transition: left 0.5s ease;
        }
        
        .card-link:hover {
            background: linear-gradient(135deg, var(--card-link-bg-hover), rgba(88, 166, 255, 0.15));
            color: var(--card-link-hover);
            text-decoration: none;
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(88, 166, 255, 0.2);
            border-color: rgba(88, 166, 255, 0.4);
        }
        
        .card-link:hover::before {
            left: 100%;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .cards-container {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            
            .card {
                padding: 1.25rem;
            }
            
            .card-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
            
            .card-status {
                align-self: flex-start;
            }
        }
    """
