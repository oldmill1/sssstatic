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
    gap: 1rem;
    width: 100%;
}

/* Responsive column behavior */
@media (min-width: 768px) {
    .column {
        gap: 1.5rem;
    }
}

@media (min-width: 1024px) {
    .column {
        gap: 2rem;
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
    gap: 1rem;
    width: 100%;
}

@media (min-width: 768px) {
    .columns-container {
        flex-direction: row;
        gap: 2rem;
    }
}

/* Individual columns within columns-container */
.columns-container .column {
    flex: 1;
    min-width: 0; /* Prevents flex items from overflowing */
}

/* Multiple columns in a row */
.row-section {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

@media (min-width: 768px) {
    .row-section {
        flex-direction: row;
        gap: 2rem;
    }
}

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
