# SSSStatic Button Component

A centralized button component system for SSSStatic that provides consistent styling and functionality across all components.

## Overview

The button component consolidates all existing button implementations into a single, reusable system with multiple styles, sizes, and configurations.

## Available Button Styles

### 1. Primary (`primary`)
- **Description**: Custom gradient button with blue-to-green gradient and sophisticated shine effects
- **Use Case**: Main call-to-action buttons
- **Color**: Blue-to-green gradient (#4FC3F7 to #2E7D32) with gradient text effect
- **Hover**: Brightness increase (1.1x) with scale animation on click

### 2. Secondary (`secondary`)
- **Description**: Transparent button with border
- **Use Case**: Secondary actions, cancel buttons
- **Color**: Transparent background, blue border (#007AFF)
- **Hover**: Light blue background with lift effect

### 3. Gradient (`gradient`)
- **Description**: Purple gradient button with shadow
- **Use Case**: Premium actions, sign-ups, downloads
- **Color**: Purple gradient (rgba(179, 132, 201, .84) to rgba(57, 31, 91, .84))
- **Hover**: Solid purple gradient with lift effect

### 4. CTA (`cta`)
- **Description**: Dark CTA button with icon support
- **Use Case**: Navigation CTAs, contact buttons
- **Color**: Dark background (#1a1a1a) with white text
- **Hover**: Darker background (#333333) with lift effect

## Available Button Sizes

- **Small** (`small`): Compact button for tight spaces
- **Medium** (`medium`): Standard button size (default)
- **Large** (`large`): Large button for emphasis

## Available Icons

- `lightning`: ⚡
- `arrow`: →
- `star`: ★
- `heart`: ♥
- `check`: ✓
- `plus`: +
- `minus`: -

## Usage

### Single Button

```python
from sssstatic.components.button import generate_button_html

# Basic primary button
button_html = generate_button_html("Get Started", "https://example.com", "primary")

# Button with icon
button_html = generate_button_html("Contact Us", "/contact", "cta", "medium", "lightning")

# Anchor link button (for smooth scrolling)
button_html = generate_button_html("Scroll to Top", "#top", "primary", "medium", None, True)
```

### Button Groups

```python
from sssstatic.components.button import generate_button_group_html

buttons_config = [
    {"text": "Primary Action", "url": "/primary", "style": "primary"},
    {"text": "Secondary Action", "url": "/secondary", "style": "secondary"},
    {"text": "Learn More", "url": "/learn", "style": "gradient", "icon": "arrow"}
]

# Center-aligned button group
button_group_html = generate_button_group_html(buttons_config, "center", "medium")

# Left-aligned with small gap
button_group_html = generate_button_group_html(buttons_config, "left", "small")

# Right-aligned with large gap
button_group_html = generate_button_group_html(buttons_config, "right", "large")
```

### Button Configuration Options

Each button in a group can have the following properties:

- `text` (str): Button text
- `url` (str): Button URL
- `style` (str): Button style ('primary', 'secondary', 'gradient', 'cta')
- `size` (str): Button size ('small', 'medium', 'large')
- `icon` (str): Icon to display
- `anchor_link` (bool): Whether this is an anchor link for smooth scrolling

## Integration with Existing Components

The button component has been integrated into the following existing components:

### Spotlight Component
- Uses button groups for multiple actions
- Supports both primary and secondary buttons
- Automatically handles anchor links

### Widescreen Spotlight Component
- Uses button groups for hero actions
- Supports gradient and secondary buttons
- Maintains full-screen layout

### Showcase Component
- Uses single gradient buttons for call-to-action
- Supports anchor links for smooth scrolling
- Maintains responsive design

### TopBar Component
- Uses small CTA buttons with lightning icon
- Supports anchor links for navigation
- Maintains responsive topbar layout

## CSS Classes

The button component generates the following CSS classes:

### Base Classes
- `.sss-button`: Base button styling
- `.sss-button-{style}`: Style-specific classes (primary, secondary, gradient, cta)
- `.sss-button-{size}`: Size-specific classes (small, medium, large)
- `.sss-button-icon-{icon}`: Icon-specific classes

### Group Classes
- `.sss-button-group`: Button group container
- `.sss-button-group-{alignment}`: Alignment classes (left, center, right)
- `.sss-button-group-{gap}`: Gap classes (small, medium, large)

### Special Classes
- `.anchor-link`: For smooth scrolling anchor links
- `.disabled`: For disabled button state

## Responsive Design

The button component includes comprehensive responsive design:

- **Mobile (≤768px)**: Buttons stack vertically in groups, full-width on small screens
- **Tablet (≤1024px)**: Maintains horizontal layout with adjusted spacing
- **Desktop (>1024px)**: Full horizontal layout with optimal spacing

## Accessibility Features

- Focus outlines for keyboard navigation
- Proper ARIA attributes
- High contrast colors
- Touch-friendly sizing
- Screen reader friendly text

## Migration from Old Button Implementations

The following old button classes have been replaced:

- `spotlight-button` → `sss-button`
- `widescreen-button` → `sss-button`
- `showcase-button` → `sss-button`
- `topbar-cta` → `sss-button`

All existing functionality is preserved while providing a more consistent and maintainable system.

## Examples

### Hero Section Buttons
```python
hero_buttons = [
    {"text": "Watch Trailer", "url": "/trailer", "style": "gradient", "icon": "star"},
    {"text": "Learn More", "url": "#about", "style": "secondary", "anchor_link": True}
]
```

### Navigation CTA
```python
nav_button = generate_button_html("Sign In", "/login", "cta", "small", "lightning")
```

### Feature Showcase
```python
cta_button = generate_button_html("Get Started Today", "/signup", "gradient", "large")
```

This centralized button system ensures consistency across your SSSStatic site while providing the flexibility to create the exact button experience you need.
