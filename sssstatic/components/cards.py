# sssstatic/components/cards.py
"""
Cards component for SSSStatic
"""


def generate_cards_html(config):
    """Generate HTML for _card entries."""
    cards_html = ""
    cards = []

    # Collect all _card entries
    for key, value in config.items():
        if key == '_card':
            if isinstance(value, list):
                cards.extend(value)
            else:
                cards.append(value)

    if not cards:
        return ""

    # Generate cards container
    cards_html = '<div class="cards-container">\n'

    for card in cards:
        if isinstance(card, dict):
            name = card.get('name', 'Untitled')
            url = card.get('url', '#')
            description = card.get('description', 'No description')
            status = card.get('status', 'unknown')

            # Status indicator styling
            status_class = f"status-{status.lower()}"

            cards_html += f'''    <div class="card">
        <div class="card-header">
            <h3 class="card-title">{name}</h3>
            <span class="card-status {status_class}">{status}</span>
        </div>
        <p class="card-description">{description}</p>
        <div class="card-footer">
            <a href="{url}" class="card-link" target="_blank" rel="noopener noreferrer">
                View Project →
            </a>
        </div>
    </div>
'''

    cards_html += '</div>\n'
    return cards_html
