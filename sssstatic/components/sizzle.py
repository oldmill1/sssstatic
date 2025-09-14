# sssstatic/components/sizzle.py
"""
Sizzle component for SSSStatic - displays a process section with steps and modern styling
"""


def generate_sizzle_html(config):
    """Generate HTML for sizzle process section."""
    sizzle_data = config.get('_sizzle')
    
    if not sizzle_data:
        return ""
    
    # Extract sizzle configuration
    if isinstance(sizzle_data, dict):
        subtitle = sizzle_data.get('subtitle', "We're proud to offer a")
        title = sizzle_data.get('title', 'No sweat process.')
        description = sizzle_data.get('description', 'Dating in Bombay shouldn\'t be this complicated yaar. We\'ll handle everything you need to absolutely slay on dating apps.')
        steps = sizzle_data.get('steps', [])
    else:
        # If it's just a string, treat it as the title
        subtitle = "We're proud to offer a"
        title = sizzle_data
        description = 'Dating in Bombay shouldn\'t be this complicated yaar. We\'ll handle everything you need to absolutely slay on dating apps.'
        steps = []
    
    # Default steps if none provided
    if not steps:
        steps = [
            {'icon': '📅', 'title': '1. Book Online', 'description': 'Pick a slot that fits your Bombay hustle. Book up to 6 weeks ahead.'},
            {'icon': '📸', 'title': '2. Get Photographed', 'description': 'No worries if you\'re camera shy! We\'ll teach you how to pose like a pro.'},
            {'icon': '🚀', 'title': '3. Implement', 'description': 'We\'ll help you arrange photos and craft a bio that actually gets you matches.'},
            {'icon': '🧪', 'title': '4. Test & Optimize', 'description': 'We\'ll show you how to track performance and keep optimizing until you\'re getting the matches you deserve.'}
        ]
    
    # Build the sizzle HTML
    sizzle_html = '    <section class="sizzle-section">\n'
    sizzle_html += '        <div class="sizzle-container">\n'
    sizzle_html += '            <section class="process-section">\n'
    sizzle_html += '                <div class="header">\n'
    sizzle_html += f'                    <p class="subtitle">{subtitle}</p>\n'
    sizzle_html += f'                    <h1 class="main-title">{title}</h1>\n'
    sizzle_html += f'                    <p class="description">{description}</p>\n'
    sizzle_html += '                </div>\n'
    sizzle_html += '                \n'
    sizzle_html += '                <div class="process-steps">\n'
    
    # Generate steps
    for step in steps:
        if isinstance(step, dict):
            icon = step.get('icon', '⚡')
            step_title = step.get('title', 'Step')
            step_description = step.get('description', '')
        else:
            icon = '⚡'
            step_title = str(step)
            step_description = ''
        
        sizzle_html += '                    <div class="step">\n'
        sizzle_html += f'                        <div class="step-icon">{icon}</div>\n'
        sizzle_html += f'                        <h3 class="step-title">{step_title}</h3>\n'
        if step_description:
            sizzle_html += f'                        <p class="step-description">{step_description}</p>\n'
        sizzle_html += '                    </div>\n'
    
    sizzle_html += '                </div>\n'
    sizzle_html += '            </section>\n'
    sizzle_html += '        </div>\n'
    sizzle_html += '    </section>\n'
    
    return sizzle_html
