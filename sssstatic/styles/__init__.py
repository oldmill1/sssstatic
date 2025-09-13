# sssstatic/styles/__init__.py
"""
Styles package for SSSStatic - contains modular CSS style components
"""

from .header import get_header_styles
from .cards import get_card_styles
from .spotlight import get_spotlight_styles

__all__ = ['get_header_styles', 'get_card_styles', 'get_spotlight_styles']
