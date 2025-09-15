# sssstatic/styles/sslogan.py
"""
SSlogan styles for SSSStatic - CSS for typography-based content display
"""


def get_sslogan_styles():
    """Return CSS styles for sslogan component."""
    from .type import get_font_styles
    return get_font_styles() + """
/* SSlogan Component Styles */
.sslogan-section {
    width: 100%;
    padding: 1.5rem 1rem;
    margin: 0;
    background: transparent;
}

.sslogan-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0;
}

.sslogan-content {
    text-align: left;
    line-height: 1.6;
}

/* Typography Hierarchy */
.sslogan-heading {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-color, #ffffff);
    margin: 0 0 1.5rem 0;
    line-height: 1.2;
    letter-spacing: -0.02em;
    font-family: var(--heading-font, 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.sslogan-subheading {
    font-size: 1.5rem;
    font-weight: 500;
    color: var(--text-color);
    margin: 0 0 1.25rem 0;
    line-height: 1.3;
    letter-spacing: -0.01em;
    font-family: var(--heading-font, 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.sslogan-paragraph {
    font-size: 1.125rem;
    font-weight: 400;
    color: var(--text-secondary, #e1e8ed);
    margin: 0 0 1.5rem 0;
    line-height: 1.7;
    font-family: var(--body-font, 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.sslogan-paragraph:last-child {
    margin-bottom: 0;
}

/* Responsive Design */
@media (min-width: 768px) {
    .sslogan-section {
        padding: 2rem 1.5rem;
    }
    
    .sslogan-heading {
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    
    .sslogan-subheading {
        font-size: 1.75rem;
        margin-bottom: 1.5rem;
    }
    
    .sslogan-paragraph {
        font-size: 1.25rem;
        margin-bottom: 1.75rem;
    }
}

@media (min-width: 1024px) {
    .sslogan-section {
        padding: 2.5rem 2rem;
    }
    
    .sslogan-container {
        max-width: 900px;
    }
    
    .sslogan-heading {
        font-size: 3.5rem;
        margin-bottom: 2.5rem;
    }
    
    .sslogan-subheading {
        font-size: 2rem;
        margin-bottom: 2rem;
    }
    
    .sslogan-paragraph {
        font-size: 1.375rem;
        margin-bottom: 2rem;
    }
}

/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
    .sslogan-heading {
        color: var(--text-color);
    }
    
    .sslogan-subheading {
        color: var(--text-color);
    }
    
    .sslogan-paragraph {
        color: var(--text-secondary);
    }
}

/* Focus states for accessibility */
.sslogan-heading:focus,
.sslogan-subheading:focus {
    outline: 2px solid var(--accent-color, #80b6cc);
    outline-offset: 2px;
    border-radius: 4px;
}

/* Smooth transitions */
.sslogan-heading,
.sslogan-subheading,
.sslogan-paragraph {
    transition: color 0.2s ease-in-out;
}
"""
