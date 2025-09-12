# sssstatic/styles/__init__.py
"""
Styles package for SSSStatic - contains modular CSS style components
"""

from .navigation import get_navigation_styles, get_light_navigation_styles
from .cards import get_card_styles

__all__ = ['get_navigation_styles', 'get_light_navigation_styles', 'get_card_styles']
