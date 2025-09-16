# sssstatic/components/video.py
"""
Video component for SSSStatic
"""


def generate_video_html(config):
    """Generate video HTML if _video is present."""
    video_html = ""
    if '_video' in config:
        video_config = config['_video']
        if isinstance(video_config, dict):
            src = video_config.get('src', '')
            alt = video_config.get('alt', 'Video')
            controls = video_config.get('controls', True)
            autoplay = video_config.get('autoplay', False)
            loop = video_config.get('loop', False)
            muted = video_config.get('muted', False)
            width = video_config.get('width', '')
            height = video_config.get('height', '')
            border_radius = video_config.get('borderRadius', '')
            
            if src:
                # Build video attributes
                attributes = []
                if controls:
                    attributes.append('controls')
                if autoplay:
                    attributes.append('autoplay')
                if loop:
                    attributes.append('loop')
                if muted:
                    attributes.append('muted')
                
                # Build style attributes for width/height/border-radius
                style_parts = []
                if width:
                    style_parts.append(f'width: {width}')
                if height:
                    style_parts.append(f'height: {height}')
                if border_radius:
                    style_parts.append(f'border-radius: {border_radius}')
                
                style_attr = f' style="{"; ".join(style_parts)}"' if style_parts else ''
                attributes_str = ' '.join(attributes)
                
                video_html = f'<div class="video-container"><video src="assets/{src}" alt="{alt}" {attributes_str}{style_attr}></video></div>'
        elif isinstance(video_config, str):
            # Simple string format: just the filename
            video_html = f'<div class="video-container"><video src="assets/{video_config}" controls></video></div>'
    
    return video_html
