# sssstatic/styles/row.py
"""
Row styles module for SSSStatic - contains CSS styles for row component
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
        }
        
        /* Ensure proper spacing between components in a row */
        .row-section > * + * {
            margin-top: 0;
        }
    """
