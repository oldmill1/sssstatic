# sssstatic/styles/sieve.py
"""
Sieve styles for SSSStatic - CSS for typography-based content display
"""


def get_sieve_styles():
    """Return CSS styles for sieve component."""
    from .type import get_font_styles
    return get_font_styles() + """
/* Sieve Component Styles */
.sieve-section {
    width: 100%;
    padding: 3rem 1rem;
    margin: 0;
    background: transparent;
}

.sieve-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0;
}

.sieve-content {
    text-align: left;
    line-height: 1.6;
}

/* Typography Hierarchy */
.sieve-heading {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-color, #ffffff);
    margin: 0 0 1.5rem 0;
    line-height: 1.2;
    letter-spacing: -0.02em;
    font-family: var(--heading-font, 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.sieve-subheading {
    font-size: 1.5rem;
    font-weight: 500;
    color: #ffffff;
    margin: 0 0 1.25rem 0;
    line-height: 1.3;
    letter-spacing: -0.01em;
    font-family: var(--heading-font, 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.sieve-paragraph {
    font-size: 1.125rem;
    font-weight: 400;
    color: var(--text-secondary, #e1e8ed);
    margin: 0 0 1.5rem 0;
    line-height: 1.7;
    font-family: var(--body-font, 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.sieve-paragraph:last-child {
    margin-bottom: 0;
}

/* Responsive Design */
@media (min-width: 768px) {
    .sieve-section {
        padding: 4rem 2rem;
    }
    
    .sieve-heading {
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    
    .sieve-subheading {
        font-size: 1.75rem;
        margin-bottom: 1.5rem;
    }
    
    .sieve-paragraph {
        font-size: 1.25rem;
        margin-bottom: 1.75rem;
    }
}

@media (min-width: 1024px) {
    .sieve-section {
        padding: 5rem 2rem;
    }
    
    .sieve-container {
        max-width: 900px;
    }
    
    .sieve-heading {
        font-size: 3.5rem;
        margin-bottom: 2.5rem;
    }
    
    .sieve-subheading {
        font-size: 2rem;
        margin-bottom: 2rem;
    }
    
    .sieve-paragraph {
        font-size: 1.375rem;
        margin-bottom: 2rem;
    }
}

/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
    .sieve-heading {
        color: #ffffff;
    }
    
    .sieve-subheading {
        color: #ffffff;
    }
    
    .sieve-paragraph {
        color: #e1e8ed;
    }
}

/* Focus states for accessibility */
.sieve-heading:focus,
.sieve-subheading:focus {
    outline: 2px solid var(--accent-color, #80b6cc);
    outline-offset: 2px;
    border-radius: 4px;
}

/* Smooth transitions */
.sieve-heading,
.sieve-subheading,
.sieve-paragraph {
    transition: color 0.2s ease-in-out;
}
"""
