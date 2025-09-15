# sssstatic/components/sinema.py
"""
Sinema component for SSSStatic - displays a vintage terminal with boot sequence
"""


def generate_sinema_html(config):
    """Generate HTML for sinema section with vintage terminal."""
    sinema_data = config.get('_sinema')
    
    if not sinema_data:
        return ""
    
    # Extract sinema configuration
    title = sinema_data.get('title', 'SINEMA TERMINAL')
    subtitle = sinema_data.get('subtitle', 'Vintage Computing Experience')
    terminal_text = sinema_data.get('terminal_text', 'hello world')
    boot_delay = sinema_data.get('boot_delay', 2000)  # milliseconds
    
    # Build the sinema HTML
    sinema_html = '    <section class="sinema-section">\n'
    sinema_html += '        <div class="sinema-container">\n'
    sinema_html += '            <div class="sinema-content-wrapper">\n'
    
    # Terminal Section
    sinema_html += '                <div class="sinema-terminal-section">\n'
    sinema_html += '                    <div class="sinema-terminal-container">\n'
    sinema_html += '                        <!-- OS X Tiger Traffic Light Buttons -->\n'
    sinema_html += '                        <div class="sinema-traffic-lights">\n'
    sinema_html += '                            <div class="sinema-traffic-light red"></div>\n'
    sinema_html += '                            <div class="sinema-traffic-light yellow"></div>\n'
    sinema_html += '                            <div class="sinema-traffic-light green"></div>\n'
    sinema_html += '                        </div>\n'
    sinema_html += '                        <div class="sinema-terminal-screen">\n'
    sinema_html += '                            <div class="sinema-terminal-content">\n'
    
    # Only show the terminal command (no bootlines)
    terminal_command = f"$ {terminal_text}"
    
    sinema_html += f'                                <div class="sinema-terminal-line" style="animation-delay: 0ms">\n'
    sinema_html += f'                                    <span class="sinema-terminal-text">{terminal_command}</span>\n'
    sinema_html += '                                </div>\n'
    
    sinema_html += '                            </div>\n'
    sinema_html += '                        </div>\n'
    sinema_html += '                    </div>\n'
    sinema_html += '                </div>\n'
    
    sinema_html += '            </div>\n'
    sinema_html += '        </div>\n'
    sinema_html += '    </section>\n'
    
    return sinema_html
