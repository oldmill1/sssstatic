# sssstatic/styles/column.py
"""
Column styles for SSSStatic - CSS for column layout components
"""


def get_column_css():
    """Return CSS styles for column components."""
    return """
/* Column Component Styles */
.column {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    width: 100%;
    padding: 0.5rem; /* Add padding to prevent text from touching edges */
    box-sizing: border-box; /* Include padding and border in width calculation */
    word-wrap: break-word; /* Break long words */
    word-break: break-word; /* Break words if necessary */
    hyphens: auto; /* Add hyphens for better text breaking */
}

/* Responsive column behavior */
@media (min-width: 768px) {
    .column {
        gap: 0.75rem;
        padding: 0.75rem; /* Increase padding on larger screens */
    }
}

@media (min-width: 1024px) {
    .column {
        gap: 1rem;
        padding: 1rem; /* More padding on desktop */
    }
}

/* Column within row section */
.row-section .column {
    flex: 1;
    min-width: 0; /* Prevents flex items from overflowing */
}

/* Multiple columns container */
.columns-container {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    width: 100%;
    box-sizing: border-box; /* Include padding and border in width calculation */
}

@media (min-width: 768px) {
    .columns-container {
        flex-direction: row;
        gap: 1rem;
    }
}

/* Individual columns within columns-container */
.columns-container .column {
    flex: 1;
    min-width: 0; /* Prevents flex items from overflowing */
    box-sizing: border-box; /* Include padding and border in width calculation */
    word-wrap: break-word; /* Break long words */
    word-break: break-word; /* Break words if necessary */
    hyphens: auto; /* Add hyphens for better text breaking */
}

/* Multiple columns in a row - handled by row styles */

/* Column content spacing */
.column > * {
    margin-bottom: 0;
}

.column > *:last-child {
    margin-bottom: 0;
}

/* Specific column positioning for numbered columns */
.column-1 {
    order: 1;
}

.column-2 {
    order: 2;
}

.column-3 {
    order: 3;
}

.column-4 {
    order: 4;
}
"""
