# sssstatic/styles/__init__.py
"""
Styles package for SSSStatic - contains modular CSS style components
"""

from .cards import get_card_styles
from .spotlight import get_spotlight_styles
from .widescreen_spotlight import get_widescreen_spotlight_styles
from .pinterest import get_pinterest_styles
from .showcase import get_showcase_styles

__all__ = ['get_card_styles', 'get_spotlight_styles', 'get_widescreen_spotlight_styles', 'get_pinterest_styles', 'get_showcase_styles']
