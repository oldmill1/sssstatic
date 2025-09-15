# sssstatic/styles/component.py
"""
Component styles for SSSStatic - CSS for generic component containers
"""


def get_component_css():
    """Return CSS styles for component containers."""
    return """
/* Component Container Styles */
.component-container {
    width: 100%;
    padding: 1rem;
    margin: 0;
    box-sizing: border-box;
}

/* Remove padding when component-container is inside a column to avoid double padding */
.column .component-container {
    padding: 0;
}

/* Responsive component behavior */
@media (min-width: 768px) {
    .component-container {
        padding: 1.5rem;
    }
    
    .column .component-container {
        padding: 0;
    }
}

@media (min-width: 1024px) {
    .component-container {
        padding: 2rem;
    }
    
    .column .component-container {
        padding: 0;
    }
}

/* Component content styling */
.component-container h1,
.component-container h2,
.component-container h3,
.component-container h4,
.component-container h5,
.component-container h6 {
    margin-top: 0;
    margin-bottom: 1rem;
    color: var(--text-color);
}

.component-container p {
    margin-bottom: 1rem;
    color: #e1e8ed;
    line-height: 1.6;
}

.component-container a {
    color: rgb(128, 182, 204);
    text-decoration: none;
}

.component-container a:hover {
    color: rgb(148, 202, 224);
    text-decoration: underline;
}
"""
