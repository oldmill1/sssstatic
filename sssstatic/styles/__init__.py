# sssstatic/styles/__init__.py
"""
Styles package for SSSStatic - contains modular CSS style components
"""

from .widescreen_spotlight import get_widescreen_spotlight_styles
from .pinterest import get_pinterest_styles
from .showcase import get_showcase_styles
from .button import get_button_styles

__all__ = ['get_widescreen_spotlight_styles', 'get_pinterest_styles', 'get_showcase_styles', 'get_button_styles']
