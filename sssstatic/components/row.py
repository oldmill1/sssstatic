# sssstatic/components/row.py
"""
Row component for SSSStatic - container for organizing components in rows/sections
"""


def generate_row_html(config):
    """Generate HTML for row section containing other components."""
    row_data = config.get('_row')
    
    if not row_data:
        return ""
    
    # Import all component generators
    from .cards import generate_cards_html
    from .spotlight import generate_spotlight_html
    from .widescreen_spotlight import generate_widescreen_spotlight_html
    from .pinterest import generate_pinterest_html
    from .showcase import generate_showcase_html
    from .slick import generate_slick_html
    from .sizzle import generate_sizzle_html
    from .sly import generate_sly_html
    from .sinema import generate_sinema_html
    from .sieve import generate_sieve_html
    from .map import generate_map_html
    from .column import generate_column_html
    from .component import generate_component_html
    
    # Component mapping for dynamic generation
    component_generators = {
        '_card': generate_cards_html,
        '_spotlight': generate_spotlight_html,
        '_widescreen_spotlight': generate_widescreen_spotlight_html,
        '_pinterest': generate_pinterest_html,
        '_showcase': generate_showcase_html,
        '_slick': generate_slick_html,
        '_sizzle': generate_sizzle_html,
        '_sly': generate_sly_html,
        '_sinema': generate_sinema_html,
        '_sieve': generate_sieve_html,
        '_map': generate_map_html,
        '_column': generate_column_html,
        '_component': generate_component_html,
    }
    
    row_html = '    <section class="row-section">\n'
    
    # Handle different row data structures
    if isinstance(row_data, list):
        # If it's a list, process each item
        for item in row_data:
            if isinstance(item, dict):
                # Each item should be a component
                for component_key, component_config in item.items():
                    if component_key in component_generators:
                        # Create a temporary config with just this component
                        temp_config = {component_key: component_config}
                        component_html = component_generators[component_key](temp_config)
                        if component_html:
                            row_html += component_html
    elif isinstance(row_data, dict):
        # If it's a dict, process it as a single component
        for component_key, component_config in row_data.items():
            if component_key in component_generators:
                temp_config = {component_key: component_config}
                component_html = component_generators[component_key](temp_config)
                if component_html:
                    row_html += component_html
    
    row_html += '    </section>\n'
    
    return row_html
