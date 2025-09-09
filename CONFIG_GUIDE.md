# 📝 SSSStatic Configuration Guide

Writing a config file for sssstatic is incredibly simple - just write YAML and watch your site come to life! Here's everything you need to know.

## 🎯 The Basics

Your `_config.yml` file is the heart of your site. It's just YAML with a few special features:

- **System settings** start with `_` (like `_theme`, `_title`)
- **Everything else** becomes your website content
- **Lists** become ordered lists
- **Objects** become sections with headings
- **URLs** automatically become clickable links

## 🔧 Special Components (Underscore Components)

SSSStatic includes several special components that start with `_` to control site structure and appearance. These components are processed specially and don't appear as regular content sections.

### Available Components:

| Component | Purpose | Required Fields | Optional Fields |
|-----------|---------|----------------|-----------------|
| `_theme` | Set site theme | `"dark"` or `"light"` | - |
| `_title` | Override main heading | Custom title text | - |
| `_footer` | Add site footer | `headline` | - |
| `_hero_banner` | Create hero section | `hero_image`, `headline`, `subtitle` | `link`, `columns` |
| `_card` | Display project cards | `name`, `url`, `description`, `status` | - |
| `_multi_line_title` | Movie-style title layout | `title`, `sub_title` | - |
| `_image` | Add header image | `name`, `alt` | - |

## 🏗️ Site Structure

### Basic Site Info

```yaml
# SSSStatic Configuration
site_name: "Your Name"           # Used as page title
_theme: "dark"                   # "dark" or "light"
_title: "Your Custom Title"       # Override the main heading
```

### Footer

```yaml
_footer:
  headline: "Find me on social media!"
```

## 🎨 Hero Banner

Create a stunning hero section with an image and three feature columns:

```yaml
_hero_banner:
  hero_image: "your-image.png"    # Local image in assets/ folder
  headline: "Welcome to My Site"
  subtitle: "Building amazing things with code"
  columns:
    - title: "Feature 1"
      description: "What this feature does"
      image: "https://example.com/image1.jpg"  # Or local image
    - title: "Feature 2" 
      description: "Another cool feature"
      image: "feature2.png"  # Local images auto-prefixed with assets/
    - title: "Feature 3"
      description: "Third amazing feature"
      image: "https://example.com/image3.jpg"
```

**Image Tips:**
- Put local images in your `assets/` folder
- Local images are automatically prefixed with `assets/`
- Remote images (starting with `http://` or `https://`) work as-is
- Large images are automatically sized for optimal display

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
_theme: "dark"   # GitHub-inspired dark theme (default)
_theme: "light"  # Clean, minimal light theme
```

## 📋 Complete Component Reference

### `_theme` - Site Theme
Controls the overall visual appearance of your site.

```yaml
_theme: "dark"   # Default: GitHub-inspired dark theme
_theme: "light" # Clean, minimal light theme
```

**Features:**
- Dark theme: GitHub-inspired colors with syntax highlighting
- Light theme: Clean, professional appearance
- Automatically applies consistent styling across all components

### `_title` - Custom Page Title
Override the default page title (which uses `site_name`).

```yaml
_title: "the professional portfolio of a self-made software engineer"
```

**Usage:**
- Sets both the HTML `<title>` tag and the main `<h1>` heading
- If not provided, falls back to `site_name`
- Supports any text content

### `_footer` - Site Footer
Add a footer section to your site.

```yaml
_footer:
  headline: "~find me on skool soon~"
```

**Fields:**
- `headline` (required): Text to display in the footer

### `_hero_banner` - Hero Section
Create a prominent hero section with image and feature columns.

```yaml
_hero_banner:
  hero_image: "sssstatic_img.png"    # Local image in assets/ folder
  headline: "This website is fast."
  subtitle: "Because it was made with sssstatic"
  link: "https://github.com/oldmill1/sssstatic"  # Optional: makes "sssstatic" clickable
  columns:                           # Optional: three feature columns
    - title: "cmtmsg"
      description: "AI-assisted commit messages"
      image: "https://dummyimage.com/300x200/10B981/ffffff&text=cmtmsg"
    - title: "douglas"
      description: "Chain AI's together. The response is the input."
      image: "https://dummyimage.com/300x200/F59E0B/ffffff&text=douglas"
    - title: "svelte-pi"
      description: "Boilerplate generator for Svelte fans"
      image: "https://dummyimage.com/300x200/8B5CF6/ffffff&text=svelte-pi"
```

**Fields:**
- `hero_image` (required): Image filename or full URL
- `headline` (required): Main hero text
- `subtitle` (required): Supporting text
- `link` (optional): URL that makes "sssstatic" in subtitle clickable
- `columns` (optional): Array of 3 feature items with `title`, `description`, `image`

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

### `_multi_line_title` - Movie-Style Title
Create a cinematic title layout with main title and subtitle.

```yaml
_multi_line_title:
  title: "Ankur Taxali"
  sub_title: "presents"
```

**Fields:**
- `title` (required): Main title text
- `sub_title` (required): Subtitle text

**Styling:**
- Uses movie-style typography with monospace fonts
- Creates a dramatic, cinematic appearance
- Overrides `_title` when both are present

### `_image` - Header Image
Add a header image below the title.

```yaml
_image:
  name: "profile-photo.jpg"
  alt: "Profile photo of the author"
```

**Fields:**
- `name` (required): Image filename in `assets/` folder
- `alt` (required): Alt text for accessibility

**Features:**
- Automatically centers and sizes the image
- Adds hover effects and shadows
- Responsive design for all screen sizes

## 🔄 Component Interactions & Best Practices

### Component Priority
When multiple title components are present, they follow this priority:
1. `_multi_line_title` (highest priority)
2. `_title` 
3. `site_name` (fallback)

### Recommended Combinations
```yaml
# Minimal setup
site_name: "Your Name"
_theme: "dark"
_footer:
  headline: "Find me online!"

# Professional portfolio
site_name: "Your Name"
_theme: "dark"
_title: "Software Engineer & Designer"
_hero_banner:
  hero_image: "hero-photo.jpg"
  headline: "Building the future"
  subtitle: "One line of code at a time"
_card:
  - name: "Project 1"
    url: "https://github.com/you/project1"
    description: "Amazing project description"
    status: "active"
_footer:
  headline: "Let's connect!"

# Cinematic presentation
site_name: "Your Name"
_theme: "dark"
_multi_line_title:
  title: "Your Name"
  sub_title: "presents"
_image:
  name: "profile.jpg"
  alt: "Professional headshot"
_footer:
  headline: "The end"
```

### Component Compatibility
- ✅ `_theme` works with all other components
- ✅ `_footer` works with all other components  
- ✅ `_image` works with `_title` and `_multi_line_title`
- ⚠️ `_title` and `_multi_line_title` conflict (use one or the other)
- ✅ `_hero_banner` and `_card` can be used together
- ✅ All components work with regular content sections

### Performance Tips
- Use local images in `assets/` folder for faster loading
- Keep `_hero_banner` columns to exactly 3 for best layout
- Use descriptive `alt` text for `_image` component
- Choose appropriate status badges for `_card` components

## 📋 Complete Example

Here's a real-world example showing all features:

```yaml
# SSSStatic Configuration
site_name: "Ankur Taxali"
_theme: "dark"

_title: "the professional portfolio of a self-made software engineer"
_footer:
  headline: "~find me on skool soon~"

_hero_banner:
  hero_image: "sssstatic_img.png"
  headline: "This website is fast."
  subtitle: "Because it was made with sssstatic"
  columns:
    - title: "cmtmsg"
      description: "AI-assisted commit messages"
      image: "https://dummyimage.com/300x200/10B981/ffffff&text=cmtmsg"
    - title: "douglas"
      description: "Chain AI's together. The response is the input."
      image: "https://dummyimage.com/300x200/F59E0B/ffffff&text=douglas"
    - title: "svelte-pi"
      description: "Boilerplate generator for Svelte fans"
      image: "https://dummyimage.com/300x200/8B5CF6/ffffff&text=svelte-pi"

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
- **Experiment**: Change `_theme` between "dark" and "light" to see the difference
- **Rapid iteration**: Edit `_site/index.html` directly for quick styling tweaks
- **Clean structure**: Use nested objects to create logical content sections

That's it! SSSStatic makes it incredibly easy to create beautiful, professional websites with just YAML. No HTML, no CSS, no complex build processes - just write your content and watch it come to life! 🎉
