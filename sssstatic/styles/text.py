# sssstatic/styles/text.py
"""
Text component styles for SSSStatic - CSS for configurable text components
"""


def get_text_css():
    """Return CSS styles for text components."""
    return """
/* Text Component Container Styles */
.text-component-container {
    width: 100%;
    margin: 0;
}

/* Text Component Base Styles */
.text-component {
    margin: 0;
    color: var(--text-color);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    padding: 1rem;
    box-sizing: border-box; /* Include padding in width calculation */
}

/* Remove padding when text component is inside a column to avoid double padding */
.column .text-component {
    padding: 0; /* Remove padding when inside column */
}

/* Responsive text component padding */
@media (min-width: 768px) {
    .text-component {
        padding: 1.5rem;
    }
    
    .column .text-component {
        padding: 0; /* Remove padding when inside column */
    }
}

@media (min-width: 1024px) {
    .text-component {
        padding: 2rem;
    }
    
    .column .text-component {
        padding: 0; /* Remove padding when inside column */
    }
}

/* Text Size Variants */
.text-size-small {
    font-size: 0.875rem; /* 14px */
}

.text-size-medium {
    font-size: 1rem; /* 16px */
}

.text-size-large {
    font-size: 1.5rem; /* 24px */
}

.text-size-xlarge {
    font-size: 2rem; /* 32px */
}

.text-size-xxlarge {
    font-size: 2.5rem; /* 40px */
}

.text-size-huge {
    font-size: 3rem; /* 48px */
}

/* Text Weight Variants */
.text-weight-thin {
    font-weight: 300;
}

.text-weight-normal {
    font-weight: 400;
}

.text-weight-bold {
    font-weight: 700;
}

.text-weight-black {
    font-weight: 900;
}

/* Text Line Height Variants */
.text-line-height-small {
    line-height: 1.2;
}

.text-line-height-medium {
    line-height: 1.6;
}

.text-line-height-large {
    line-height: 2.0;
}

/* Emoji Positioning */
.emoji-top {
    font-size: 1.2em;
    margin-bottom: 0.5rem;
    display: block;
}

.text-content {
    display: flex;
    align-items: center;
    gap: 0.25rem;
}

.emoji-left {
    font-size: 1.1em;
    margin-right: 0.25rem;
}

.emoji-right {
    font-size: 1.1em;
    margin-left: 0.25rem;
}

/* Responsive text sizing */
@media (min-width: 768px) {
    .text-size-small {
        font-size: 1rem; /* 16px */
    }
    
    .text-size-medium {
        font-size: 1.125rem; /* 18px */
    }
    
    .text-size-large {
        font-size: 1.75rem; /* 28px */
    }
    
    .text-size-xlarge {
        font-size: 2.25rem; /* 36px */
    }
    
    .text-size-xxlarge {
        font-size: 3rem; /* 48px */
    }
    
    .text-size-huge {
        font-size: 3.5rem; /* 56px */
    }
}

@media (min-width: 1024px) {
    .text-size-small {
        font-size: 1.125rem; /* 18px */
    }
    
    .text-size-medium {
        font-size: 1.25rem; /* 20px */
    }
    
    .text-size-large {
        font-size: 2rem; /* 32px */
    }
    
    .text-size-xlarge {
        font-size: 2.5rem; /* 40px */
    }
    
    .text-size-xxlarge {
        font-size: 3.5rem; /* 56px */
    }
    
    .text-size-huge {
        font-size: 4rem; /* 64px */
    }
}

/* Dark mode text color adjustments */
@media (prefers-color-scheme: dark) {
    .text-component {
        color: #e1e8ed;
    }
}

/* Light mode text color adjustments */
@media (prefers-color-scheme: light) {
    .text-component {
        color: #1a1a1a;
    }
}
"""
