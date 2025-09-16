# sssstatic/components/column.py
"""
Column component for SSSStatic - container for organizing components in columns

COMPONENT PROPERTIES:
====================

_column: array | object
    The column configuration. Can be:
    - Array: List of components to place in separate columns
    - Object: Single component to place in one column

PROPERTIES (when _column is an array):
-------------------------------------
Each array item should be an object containing one component:
- _text: Text component
- _image: Image component
- _button: Button component
- _showcase: Showcase component
- _widescreen_spotlight: Widescreen spotlight component
- _pinterest: Pinterest component
- _slick: Slick component
- _sizzle: Sizzle component
- _sly: Sly component
- _sinema: Sinema component
- _sslogan: Slogan component
- _map: Map component
- _component: Generic component
- _video: Video component

PROPERTIES (when _column is an object):
--------------------------------------
Same component types as above, but for a single column layout.

USAGE EXAMPLES:
===============

1. Single component in a column:
   _column:
     _text:
       content: "This is a single text component in a column"
       style: "heading"

2. Multiple components in separate columns:
   _column:
     - _text:
         content: "First column content"
         style: "body"
     - _text:
         content: "Second column content" 
         style: "body"

3. Mixed component types in columns:
   _column:
     - _text:
         content: "Welcome to our site"
         style: "heading"
     - _image:
         src: "assets/photo.jpg"
         alt: "Description"
     - _button:
         text: "Click me"
         link: "/contact"

4. Complex layout with showcase and text:
   _column:
     - _showcase:
         title: "Our Products"
         items:
           - title: "Product 1"
             description: "Amazing product"
     - _text:
         content: "Learn more about our offerings"
         style: "body"

RENDERED OUTPUT:
===============
- Single component: Wrapped in <div class="column">
- Multiple components: Wrapped in <div class="columns-container"> with individual <div class="column column-N"> elements
- Automatic layout: Flexbox-based responsive column system
- Component support: All SSSStatic component types are supported
"""


def generate_column_html(config):
    """Generate HTML for column section containing other components."""
    column_data = config.get('_column')
    
    if not column_data:
        return ""
    
    # Import all component generators
    from .widescreen_spotlight import generate_widescreen_spotlight_html
    from .pinterest import generate_pinterest_html
    from .showcase import generate_showcase_html
    from .slick import generate_slick_html
    from .sizzle import generate_sizzle_html
    from .sly import generate_sly_html
    from .sinema import generate_sinema_html
    from .sslogan import generate_sslogan_html
    from .map import generate_map_html
    from .component import generate_component_html
    from .text import generate_text_html
    from .video import generate_video_html
    
    # Component mapping for dynamic generation
    component_generators = {
        '_widescreen_spotlight': generate_widescreen_spotlight_html,
        '_pinterest': generate_pinterest_html,
        '_showcase': generate_showcase_html,
        '_slick': generate_slick_html,
        '_sizzle': generate_sizzle_html,
        '_sly': generate_sly_html,
        '_sinema': generate_sinema_html,
        '_sslogan': generate_sslogan_html,
        '_map': generate_map_html,
        '_component': generate_component_html,
        '_text': generate_text_html,
        '_video': generate_video_html,
    }
    
    # Collect all components first to determine layout
    components = []
    
    # Handle different column data structures
    if isinstance(column_data, list):
        # If it's a list, process each item
        for item in column_data:
            if isinstance(item, dict):
                # Each item should be a component
                for component_key, component_config in item.items():
                    if component_key in component_generators:
                        # Create a temporary config with just this component
                        temp_config = {component_key: component_config}
                        component_html = component_generators[component_key](temp_config)
                        if component_html:
                            components.append(component_html)
    elif isinstance(column_data, dict):
        # If it's a dict, process it as a single component
        for component_key, component_config in column_data.items():
            if component_key in component_generators:
                temp_config = {component_key: component_config}
                component_html = component_generators[component_key](temp_config)
                if component_html:
                    components.append(component_html)
    
    if not components:
        return ""
    
    # Determine layout based on number of components
    num_components = len(components)
    
    if num_components == 1:
        # Single component - use regular column
        column_html = '        <div class="column">\n'
        indented_html = '\n'.join('            ' + line for line in components[0].split('\n'))
        column_html += indented_html + '\n'
        column_html += '        </div>\n'
    else:
        # Multiple components - create multiple columns
        column_html = '        <div class="columns-container">\n'
        for i, component_html in enumerate(components):
            column_html += f'            <div class="column column-{i+1}">\n'
            indented_html = '\n'.join('                ' + line for line in component_html.split('\n'))
            column_html += indented_html + '\n'
            column_html += f'            </div>\n'
        column_html += '        </div>\n'
    
    return column_html
