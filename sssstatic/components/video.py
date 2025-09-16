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
            zoom = video_config.get('zoom', '')
            
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
                
                # Build style attributes for width/height/zoom
                video_style_parts = []
                if width:
                    video_style_parts.append(f'width: {width}')
                if height:
                    video_style_parts.append(f'height: {height}')
                if zoom:
                    video_style_parts.append(f'transform: scale({zoom})')
                
                # Build container style attributes for border-radius
                container_style_parts = []
                if border_radius:
                    container_style_parts.append(f'border-radius: {border_radius}')
                    container_style_parts.append('overflow: hidden')
                
                video_style_attr = f' style="{"; ".join(video_style_parts)}"' if video_style_parts else ''
                container_style_attr = f' style="{"; ".join(container_style_parts)}"' if container_style_parts else ''
                attributes_str = ' '.join(attributes)
                
                video_html = f'<div class="video-container"{container_style_attr}><video src="assets/{src}" alt="{alt}" {attributes_str}{video_style_attr}></video></div>'
        elif isinstance(video_config, str):
            # Simple string format: just the filename
            video_html = f'<div class="video-container"><video src="assets/{video_config}" controls></video></div>'
    
    return video_html
