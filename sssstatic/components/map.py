# sssstatic/components/map.py
"""
Map component for SSSStatic
"""


def generate_map_html(config):
    """Generate HTML for _map entries."""
    map_config = config.get('_map')
    
    if not map_config:
        return ""
    
    # Extract configuration values with defaults
    business_name = map_config.get('business_name', 'Business Name')
    business_tagline = map_config.get('business_tagline', 'Business Tagline')
    business_location = map_config.get('business_location', 'Business Location')
    business_contact = map_config.get('business_contact', 'Contact Information')
    phone_number = map_config.get('phone_number', '0000000000')
    latitude = map_config.get('latitude', 19.1615)
    longitude = map_config.get('longitude', 72.8562)
    zoom_level = map_config.get('zoom_level', 15)
    scroll_id = map_config.get('scrollId', '')
    
    # Add ID attribute if scrollId is provided
    container_id = f' id="{scroll_id}"' if scroll_id else ''
    
    map_html = f'''    <div class="map-container"{container_id}>
        <div id="map"></div>
        <div class="overlay-layer">
            <div class="overlay-content">
                <div class="business-name">{business_name}</div>
                <div class="business-tagline">{business_tagline}</div>
                <div class="business-location">{business_location}</div>
                <div class="business-contact">{business_contact} <span class="phone-number">{phone_number}</span></div>
            </div>
        </div>
    </div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // Initialize the map centered on the specified coordinates
        const map = L.map('map', {{
            zoomControl: false,
            scrollWheelZoom: false,
            doubleClickZoom: false,
            boxZoom: false,
            keyboard: false,
            dragging: false,
            touchZoom: false
        }}).setView([{latitude}, {longitude}], {zoom_level});
        
        // Add custom pastel-themed map tiles
        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '© OpenStreetMap contributors'
        }}).addTo(map);
        
        // Create a custom larger marker icon
        const customIcon = L.divIcon({{
            className: 'custom-marker',
            html: '<div class="marker-pin"></div>',
            iconSize: [50, 50],
            iconAnchor: [25, 50]
        }});
        
        // Add a marker for the specific address
        L.marker([{latitude}, {longitude}], {{ icon: customIcon }}).addTo(map);
    </script>
'''
    
    return map_html
