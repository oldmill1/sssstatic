# 📝 SSSStatic Configuration Guide

Writing a config file for sssstatic is incredibly simple - just write YAML and watch your site come to life! Here's everything you need to know.

## 🎯 The Basics

Your `_config.yml` file is the heart of your site. It's just YAML with a few special features:

- **System settings** start with `_` (like `_colorMode`, `_title`)
- **Everything else** becomes your website content
- **Lists** become ordered lists
- **Objects** become sections with headings
- **URLs** automatically become clickable links

## 🔧 Special Components (Underscore Components)

SSSStatic includes several special components that start with `_` to control site structure and appearance. These components are processed specially and don't appear as regular content sections.

### Available Components:

| Component | Purpose | Required Fields | Optional Fields |
|-----------|---------|----------------|-----------------|
| `_colorMode` | Set site color mode | `"dark"` or `"light"` | - |
| `_title` | Override main heading | Custom title text | - |
| `_footer` | Add site footer | `headline` | - |
| `_card` | Display project cards | `name`, `url`, `description`, `status` | - |
| `_spotlight` | Featured image section | `image` | `title`, `subtitle`, `description`, `buttons` |

## 🏗️ Site Structure

### Basic Site Info

```yaml
# SSSStatic Configuration
site:
  name: "Your Name"              # Used as page title
  theme: "Midnight Serene"        # Theme name (for future use)
_colorMode: "dark"               # "dark" or "light"
_title: "Your Custom Title"       # Override the main heading
```

### Footer

```yaml
_footer:
  headline: "Find me on social media!"
```

## ✨ Spotlight Section

Create a stunning featured image section with optional text overlay:

```yaml
_spotlight:
  image: "hero-image.jpg"         # Local image in assets/ folder
  title: "Welcome to My Site"
  subtitle: "Building amazing things with code"
  description: "This is a featured section that highlights your main content"
  buttons:
    - text: "Get Started"
      url: "https://github.com/you/project"
      style: "primary"
    - text: "Learn More"
      url: "/about"
      style: "secondary"
```

**Image Tips:**
- Put local images in your `assets/` folder
- Local images are automatically prefixed with `assets/`
- Remote images (starting with `http://` or `https://`) work as-is
- Large images are automatically sized for optimal display

**Button Styles:**
- `primary` - Main call-to-action button
- `secondary` - Secondary action button

## 🃏 Project Cards

Showcase your projects with beautiful cards:

```yaml
_card:
  - name: "My Awesome Project"
    url: "https://github.com/you/project"
    description: "What this project does"
    status: "active"              # active, experimental, complete, on hold, development, archived
    
  - name: "Another Project"
    url: "https://github.com/you/another"
    description: "Another cool project"
    status: "experimental"
```

**Status Options:**
- `active` - Green badge
- `experimental` - Orange badge  
- `complete` - Purple badge
- `on hold` - Gray badge
- `development` - Orange badge
- `archived` - Red badge

## 📝 Content Sections

Any other YAML structure becomes your website content:

```yaml
about_me:
  languages:
    - "Python (automation and AI tools)"
    - "TypeScript (when types matter)"
    - "Swift (for iOS development)"
    
  spoken_languages:
    - "English (native)"
    - "Spanish (conversational)"
    
  countries_travelled:
    - "United States (New York, Los Angeles, San Francisco)"
    - "Canada (Toronto, Vancouver)"
    - "Japan (Tokyo, Kyoto, Osaka)"
```

This automatically becomes:
- **Section headings** from object keys (`about_me`, `languages`, etc.)
- **Ordered lists** from arrays
- **Styled content** with proper typography

## 🖼️ Adding Images

### Local Images
1. Put your images in the `assets/` folder
2. Reference them by filename in your config
3. They're automatically copied to `_site/assets/` during build

```yaml
_hero_banner:
  hero_image: "my-photo.jpg"  # Looks for assets/my-photo.jpg
```

### Remote Images
Use full URLs for external images:

```yaml
_hero_banner:
  hero_image: "https://example.com/image.jpg"
```

## 🎨 Themes

Choose between two beautiful built-in themes:

```yaml
_colorMode: "dark"   # GitHub-inspired dark theme (default)
_colorMode: "light"  # Clean, minimal light theme
```

## 📋 Complete Component Reference

### `_colorMode` - Site Color Mode
Controls the overall visual appearance of your site.

```yaml
_colorMode: "dark"   # Default: GitHub-inspired dark theme
_colorMode: "light" # Clean, minimal light theme
```

**Features:**
- Dark theme: GitHub-inspired colors with syntax highlighting
- Light theme: Clean, professional appearance
- Automatically applies consistent styling across all components

### `_title` - Custom Page Title
Override the default page title (which uses `site.name`).

```yaml
_title: "the professional portfolio of a self-made software engineer"
```

**Usage:**
- Sets both the HTML `<title>` tag and the main `<h1>` heading
- If not provided, falls back to `site.name`
- Supports any text content

### `_footer` - Site Footer
Add a footer section to your site.

```yaml
_footer:
  headline: "~find me on skool soon~"
```

**Fields:**
- `headline` (required): Text to display in the footer

### `_spotlight` - Featured Image Section
Create a prominent featured image section with optional text overlay and buttons.

```yaml
_spotlight:
  image: "sssstatic_img.png"        # Local image in assets/ folder
  title: "This website is fast."
  subtitle: "Because it was made with sssstatic"
  description: "SSSStatic makes it incredibly easy to create beautiful, professional websites with just YAML."
  buttons:
    - text: "View on GitHub"
      url: "https://github.com/oldmill1/sssstatic"
      style: "primary"
    - text: "Get Started"
      url: "/docs"
      style: "secondary"
```

**Fields:**
- `image` (required): Image filename or full URL
- `title` (optional): Main title text
- `subtitle` (optional): Supporting subtitle text
- `description` (optional): Detailed description text
- `buttons` (optional): Array of button objects with `text`, `url`, `style`

**Button Fields:**
- `text` (required): Button label
- `url` (required): Button link
- `style` (optional): Button style (`primary` or `secondary`)

**Image Handling:**
- Local images: Put in `assets/` folder, reference by filename
- Remote images: Use full URLs starting with `http://` or `https://`
- Images are automatically optimized and responsive

### `_card` - Project Cards
Display project information in styled cards.

```yaml
_card:
  - name: "cmtmsg"
    url: "https://github.com/oldmill1/cmtmsg"
    description: "AI-assisted commit messages"
    status: "active"
  - name: "douglas"
    url: "https://github.com/oldmill1/douglas"
    description: "Chain AI's together. The response is the input."
    status: "experimental"
```

**Fields (per card):**
- `name` (required): Project name
- `url` (required): Project URL
- `description` (required): Project description
- `status` (required): Project status

**Status Options:**
- `active` - Green badge (actively maintained)
- `experimental` - Orange badge (experimental/early stage)
- `complete` - Purple badge (finished project)
- `on hold` - Gray badge (temporarily paused)
- `development` - Orange badge (in active development)
- `archived` - Red badge (no longer maintained)


## 🔄 Component Interactions & Best Practices

### Component Priority
When multiple title components are present, they follow this priority:
1. `_title` (highest priority)
2. `site.name` (fallback)

### Recommended Combinations
```yaml
# Minimal setup
site:
  name: "Your Name"
  theme: "Midnight Serene"
_colorMode: "dark"
_footer:
  headline: "Find me online!"

# Professional portfolio
site:
  name: "Your Name"
  theme: "Midnight Serene"
_colorMode: "dark"
_title: "Software Engineer & Designer"
_spotlight:
  image: "hero-photo.jpg"
  title: "Building the future"
  subtitle: "One line of code at a time"
  description: "Creating innovative solutions with modern technology"
  buttons:
    - text: "View Projects"
      url: "/projects"
      style: "primary"
_card:
  - name: "Project 1"
    url: "https://github.com/you/project1"
    description: "Amazing project description"
    status: "active"
_footer:
  headline: "Let's connect!"

# Featured showcase
site:
  name: "Your Name"
  theme: "Midnight Serene"
_colorMode: "dark"
_title: "Creative Developer"
_spotlight:
  image: "showcase.jpg"
  title: "Your Name"
  subtitle: "Creative Developer"
  description: "Building beautiful digital experiences"
_footer:
  headline: "The end"
```

### Component Compatibility
- ✅ `_colorMode` works with all other components
- ✅ `_footer` works with all other components  
- ✅ `_spotlight` works with all other components
- ✅ `_card` works with all other components
- ✅ All components work with regular content sections

### Performance Tips
- Use local images in `assets/` folder for faster loading
- Use descriptive alt text for `_spotlight` images
- Choose appropriate status badges for `_card` components
- Keep spotlight content concise for better visual impact

## 📋 Complete Example

Here's a real-world example showing all features:

```yaml
# SSSStatic Configuration
site:
  name: "Ankur Taxali"
  theme: "Midnight Serene"
_colorMode: "dark"

_title: "the professional portfolio of a self-made software engineer"
_footer:
  headline: "~find me on skool soon~"

_spotlight:
  image: "sssstatic_img.png"
  title: "This website is fast."
  subtitle: "Because it was made with sssstatic"
  description: "SSSStatic makes it incredibly easy to create beautiful, professional websites with just YAML."
  buttons:
    - text: "View on GitHub"
      url: "https://github.com/oldmill1/sssstatic"
      style: "primary"
    - text: "Get Started"
      url: "/docs"
      style: "secondary"

_card:
  - name: "cmtmsg"
    url: "https://github.com/oldmill1/cmtmsg"
    description: "AI-assisted commit messages"
    status: "active"

  - name: "douglas"
    url: "https://github.com/oldmill1/douglas"
    description: "Chain AI's together. The response is the input."
    status: "experimental"

  - name: "svelte-pi"
    url: "https://github.com/oldmill1/svelte-pi"
    description: "Boilerplate generator for Svelte fans"
    status: "complete"

  - name: "sssstatic"
    url: "https://github.com/oldmill1/sssstatic"
    description: "Easiest way to make static sites"
    status: "active"

about_me:
  languages:
    - "Python (automation and AI tools)"
    - "TypeScript (when types matter)"
    - "Swift (for iOS development)"
    - "Shell (because automation)"
    - "JavaScript (for the web stuff)"

  spoken_languages:
    - "English (native)"
    - "Hindi (conversational)"
  
  countries_travelled:
    - "Canada (Toronto)"
    - "United States (New York, Los Angeles, Los Vegas, Philadelphia, Washington DC)"
    - "United Kingdom (London)"
    - "France (Paris)"
    - "Germany (Berlin)"
    - "Italy (Rome)"
    - "Netherlands (Amsterdam)"
    - "Guatemala (Antigua, Guatemala City, Lake Atitlan, Tikal)"
    - "Costa Rica (San Jose, Arenal, Monteverde, Manuel Antonio, Tortuguero)"
    - "India (New Delhi, Jaipur, Agra, Varanasi, Mumbai, Goa, Kerala)"
    - "Greece (Athens, Nafplion, Mykonos, Santorini, Crete)"
    - "Egypt (Cairo, Luxor, Aswan, Sharm el-Sheikh, Alexandria)"
```

## 🚀 Quick Start Workflow

1. **Create a new project:**
   ```bash
   sssstatic create new
   ```

2. **Edit your `_config.yml`** with the structure above

3. **Add images** to the `assets/` folder

4. **Build and preview:**
   ```bash
   sssstatic dev  # Builds and starts dev server
   ```

5. **Open** `http://localhost:8000` to see your site!

## 💡 Pro Tips

- **Start simple**: Begin with basic site info and add features gradually
- **Use local images**: They're automatically optimized and responsive
- **Experiment**: Change `_colorMode` between "dark" and "light" to see the difference
- **Rapid iteration**: Edit `_site/index.html` directly for quick styling tweaks
- **Clean structure**: Use nested objects to create logical content sections

That's it! SSSStatic makes it incredibly easy to create beautiful, professional websites with just YAML. No HTML, no CSS, no complex build processes - just write your content and watch it come to life! 🎉
