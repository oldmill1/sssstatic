# sssstatic/styles/row.py
"""
Row styles module for SSSStatic - contains CSS styles for row component
Enhanced to support multiple columns and vertical stacking
"""


def get_row_styles():
    """Return CSS styles for row component."""
    return """
        /* Row Section - Container for organizing components */
        .row-section {
            width: 100%;
            margin: 0;
            padding: 0;
            border: none;
            outline: none;
            box-shadow: none;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        /* Responsive row behavior */
        @media (min-width: 768px) {
            .row-section {
                flex-direction: row;
                gap: 2rem;
            }
        }
        
        /* Override nested section styles for row content */
        .row-section section {
            border-left: none !important;
            padding-left: 0 !important;
            margin: 0 !important;
        }
        
        .row-section section::before {
            display: none !important;
        }
        
        /* Row can contain multiple components */
        .row-section > * {
            margin: 0;
            flex: 1;
            min-width: 0; /* Prevents flex items from overflowing */
        }
        
        /* Ensure proper spacing between components in a row */
        .row-section > * + * {
            margin-top: 0;
        }
        
        /* Vertical stacking of multiple rows */
        .row-section + .row-section {
            margin-top: 2rem;
        }
        
        /* Responsive spacing for vertical stacking */
        @media (min-width: 768px) {
            .row-section + .row-section {
                margin-top: 3rem;
            }
        }
        
        /* Support for 4+ columns */
        .row-section .column,
        .row-section .columns-container,
        .row-section .component-section {
            flex: 1;
            min-width: 0;
        }
        
        /* Responsive column behavior */
        @media (max-width: 767px) {
            .row-section {
                flex-direction: column;
            }
            
            .row-section > * {
                flex: none;
                width: 100%;
            }
        }
        
        /* Support for different column counts */
        .row-section[data-columns="2"] > * {
            flex: 1;
        }
        
        .row-section[data-columns="3"] > * {
            flex: 1;
        }
        
        .row-section[data-columns="4"] > * {
            flex: 1;
        }
        
        /* Ensure components within rows don't interfere with layout */
        .row-section .component-section {
            border-left: none !important;
            padding-left: 0 !important;
        }
        
        .row-section .component-section::before {
            display: none !important;
        }
    """