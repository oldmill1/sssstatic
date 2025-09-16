[![GitHub Pages](https://img.shields.io/badge/github%20pages-deployed-blue.svg)](https://sssstatic.com)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🚀 Quick Start

Create a `_config.yml` file in your project directory and start building! Here's a complete example showing everything you can create:

```yml
# SSSStatic Configuration - Development Testing
# This is your main configuration file - everything starts here!

# Basic site information
site:
  name: "SSSStatic Dev Server - UPDATED"  # Your site name (appears in browser tab)
  description: "Testing the enhanced dev server functionality with file watching"  # SEO description
  colorMode: "dark"  # "dark" or "light" theme

# TopBar navigation with CTA button
# Creates a sleek dark navigation bar at the top of your site
_topbar:
  title: "sssstatic"  # Your brand name
  titleFont: "Original Surfer"  # Custom Google Font
  cta: "Get Started"  # Call-to-action button text
  link: "#contact"  # Where the CTA button links to
  size: "large"  # Button size: "small", "medium", "large"

# Multiple rows - each row is a separate section
# Rows let you organize content into horizontal sections
_row:
  # First row with two columns
  - _column:
    # Left column: Terminal component for that retro computing feel
    - _sinema:
        title: "SINEMA TERMINAL"
        subtitle: "Vintage Computing Experience"
        terminal_text: "Nice to meet you"  # What appears in the terminal
        boot_delay: 2000  # Animation delay in milliseconds
    
    # Right column: Custom component with multiple text elements
    - _component:
        content:
          # Large heading
          - _text:
              content: "Build this website with SSSStatic"
              spacerTop: "4rem"  # Space above the text
              type: "h1"  # HTML heading level
              size: "xxlarge"  # Text size: "small", "medium", "large", "xlarge", "xxlarge"
              fontWeight: "700"  # Font weight: "300", "400", "500", "600", "700"
              fontFamily: "heading"  # Font family: "primary", "heading", "mono"
              letterSpacing: "tight"  # Letter spacing: "tight", "normal", "wide"
              align: "left"  # Text alignment: "left", "center", "right"
              lineHeight: "small"  # Line height: "small", "medium", "large"
              marginBottom: "1rem"  # Space below the text
          
          # Subheading
          - _text:
              content: "Go live in thirty seconds. 🚀"
              type: "h2"
              size: "large"
              fontWeight: "500"
              fontFamily: "heading"
              align: "left"
              lineHeight: "medium"
              marginBottom: "1rem"
          
          # Paragraph text
          - _text:
              content: "From idea to a beautiful, responsive website in just a few lines of text. Perfect for portfolios, docs, and landing pages."
              type: "p"  # Paragraph
              size: "medium"
              fontWeight: "400"
              fontFamily: "primary"
              align: "left"
              lineHeight: "medium"

  # Second row with four columns
  - _column:
    # Column 1: Open source section with buttons
    - _component:
        content:
          - _text:
              align: "center"
              content: "Open Source"
              type: "h1"
              size: "xlarge"
              weight: "light"
              lineHeight: "small"
          - _text:
              content: "MIT Licensed and free to use. Who knows what you'll build with it."
              type: "p"
              size: "medium"
              weight: "normal"
              lineHeight: "medium"
              paddingBlock: "0.5rem"  # Vertical padding
          
          # Primary button with icon
          - _button:
              align: "left"
              text: "View on GitHub"
              url: "https://github.com/yourusername/sssstatic"
              style: "primary"  # Button style: "primary", "secondary", "outline"
              size: "medium"  # Button size: "small", "medium", "large"
              icon: "star"  # Icon: "star", "lightning", "arrow", etc.
          
          # Link-style button
          - _button:
              align: "left"
              text: "Report an issue"
              url: "https://github.com/yourusername/sssstatic"
              style: "primary"
              variant: "link"  # Button variant: "default", "link"
              size: "medium"

    # Column 2: Sticker component with dark background
    - _component:
        bgColor: "#1B1F23"  # Custom background color
        content:
          # Sticker/emoji component
          - _sticker:
              align: "center"
              name: "rocket"  # Sticker name: "rocket", "computer", "cmoon"
              size: "large"  # Sticker size: "small", "medium", "large"
              position: "center"
          - _text:
              content: "People don't appreciate the value of a good sticker."
              type: "p"
              size: "medium"
              weight: "light"
              lineHeight: "medium"
          - _button:
              align: "left"
              text: "View Sticker Gallary"
              url: "https://github.com/yourusername/sssstatic"
              style: "primary"
              variant: "link"
              size: "medium"

    # Column 3: Another sticker component
    - _component:
        bgColor: "#1B1F23"
        content: 
          - _sticker:
              align: "center"
              name: "computer"
              size: "large"
              position: "center"
          - _text:
              content: "Build in dev server mode for instant gratification. Imagine it. Ship it."
              type: "p"
              size: "medium"
              weight: "light"
              lineHeight: "medium"
          - _button:
              align: "left"
              text: "View Examples"
              url: "https://github.com/yourusername/sssstatic"
              style: "primary"
              variant: "link"
              size: "medium"

    # Column 4: Third sticker component
    - _component:
        bgColor: "#1B1F23"
        content: 
          - _sticker:
              align: "center"
              name: "cmoon"
              size: "large"
              position: "center"
          - _text:
              content: "Build in dev server mode for instant gratification. Imagine it. Ship it."
              type: "p"
              size: "medium"
              weight: "light"
              lineHeight: "medium"
          - _button:
              align: "left"
              text: "View Examples"
              url: "https://github.com/yourusername/sssstatic"
              style: "primary"
              variant: "link"
              size: "medium"

# Showcase component - perfect for explaining features or processes
# Creates a side-by-side layout with image and step-by-step content
_showcase:
  image: "statie.png"  # Image file in your assets folder
  spacerTop: "4rem"  # Space above the section
  direction: "right"  # Image position: "left" or "right"
  title: "Why Static Sites Are Awesome"
  subtitle: "Fast, secure, and reliable"
  
  # Step-by-step process with emojis and descriptions
  steps:
    - emoji: "⚡"
      text: "Lightning Fast Performance"
      description: "No server-side processing means instant page loads and better user experience"
    - emoji: "🔒"
      text: "Enhanced Security"
      description: "No database or server-side code means fewer attack vectors and vulnerabilities"
    - emoji: "💰"
      text: "Cost Effective Hosting"
      description: "Host anywhere for free or pennies - CDNs, GitHub Pages, Netlify, Vercel"
    - emoji: "📈"
      text: "Better SEO & Reliability"
      description: "Faster loading times improve search rankings and uptime is nearly 100%"
  
  # Call-to-action button at the bottom
  button_text: "Get Started Today"
  button_url: "#contact"
  button_size: "large"
```

## 🎨 Available Components

### Layout Components
- **`_topbar`** - Dark navigation bar with brand and CTA button
- **`_row`** - Horizontal sections to organize your content
- **`_column`** - Vertical columns within rows for responsive layouts

### Content Components
- **`_component`** - Flexible container for text, buttons, and stickers
- **`_text`** - Headings, paragraphs, and any text content
- **`_button`** - Call-to-action buttons with icons and styles
- **`_sticker`** - Fun emoji/sticker elements for visual interest

### Special Components
- **`_sinema`** - Retro terminal display for that vintage computing feel
- **`_showcase`** - Side-by-side image and step-by-step content
- **`_pinterest`** - Masonry image galleries

## 🚀 Getting Started

1. **Install SSSStatic**:
   ```bash
   pip install sssstatic
   ```

2. **Create your config**:
   Copy the example above into a `_config.yml` file

3. **Add your assets**:
   Put images in an `assets/` folder

4. **Build your site**:
   ```bash
   sssstatic build
   ```

5. **Preview locally**:
   ```bash
   sssstatic dev
   ```

## 📁 Project Structure

```
your-project/
├── _config.yml          # Your configuration file
├── assets/             # Images and other assets
│   ├── statie.png
│   └── ...
└── _site/              # Generated site (auto-created)
    ├── index.html
    └── assets/
```

## 🎯 Key Features

- **Zero Configuration** - Just write YAML, get beautiful HTML
- **Responsive Design** - All components work on mobile and desktop
- **Dark/Light Themes** - Built-in theme support
- **Custom Fonts** - Google Fonts integration
- **Component-Based** - Mix and match components to build anything
- **Fast Development** - Live reload dev server
- **Static Output** - Deploy anywhere (Netlify, Vercel, GitHub Pages)

## 📊 Analytics

Add Google Analytics tracking to your site:

```yaml
site:
  name: "My Website"
  google_analytics: "G-XXXXXXXXXX"  # Your Google Analytics ID
```

The tracking code will be automatically included in all pages of your site.

---

**That's it!** No complex setup, no build tools, no frameworks. Just write YAML and ship beautiful websites. 🚀