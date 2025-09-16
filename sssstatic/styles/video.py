# sssstatic/styles/video.py
"""
Video styles for SSSStatic
"""


def get_video_css():
    """Return CSS styles for video component."""
    return """
/* Video Component Styles */
.video-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2rem 0;
    padding: 1rem;
}

.video-container video {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    background-color: #000;
}

/* Responsive video sizing */
@media (max-width: 768px) {
    .video-container {
        margin: 1rem 0;
        padding: 0.5rem;
    }
    
    .video-container video {
        border-radius: 4px;
    }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    .video-container video {
        box-shadow: 0 4px 12px rgba(255, 255, 255, 0.1);
    }
}
"""
