# 🐍🐍🐍 SSSStatic 🐍🐍🐍

> *The simplest way to build beautiful websites*

Create web-sites that _sell_ with pre-defined templates. 
Just fill in your own content. 

Components available:

## 🎨 Layout Components
- **Header** - Site navigation with brand and page links
- **TopBar** - Dark mode navigation bar with CTA button
- **Page Header** - Page titles and multi-line headers

## 🖼️ Visual Components  
- **Spotlight** - Featured image with overlaid text and buttons
- **Widescreen Spotlight** - Full-bleed background with floating text (Apple TV+ style)
- **Image** - Simple image display component
- **Pinterest** - Masonry layout for image galleries
- **Cards** - Project cards with status indicators

## 📸 Photography Components
- **Showcase** - Multi-step process display with image and call-to-action (supports left/right direction)
- **Sizzle** - Modern process section with steps, icons, and clean styling

## 🎯 Usage
Each component is activated by adding its corresponding key to your `_config.yml`:
- `_header` - Site header navigation
- `_topbar` - Dark navigation bar  
- `_title` - Page title
- `_spotlight` - Hero image section
- `_widescreen_spotlight` - Full-width hero section
- `_image` - Image display
- `_pinterest` - Image gallery
- `_card` - Project cards
- `_showcase` - Photography workflow with image
- `_sizzle` - Modern process section with steps

## 📊 Analytics
Add Google Analytics tracking to your site by including your GA4 measurement ID in the site configuration:

```yaml
site:
  name: "My Website"
  google_analytics: "G-XXXXXXXXXX"  # Your Google Analytics ID
```

The tracking code will be automatically included in all pages of your site.
