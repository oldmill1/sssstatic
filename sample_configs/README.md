# SSSStatic Sample Configurations

This directory contains sample `_config.yml` files that demonstrate different ways to use SSSStatic for various types of websites.

## Available Samples

### 1. Card Only Example (`card_only_example.yml`)
A minimal demonstration of the card component featuring:
- Simple card layout with different status badges
- No navigation (card-only focus)
- Multiple card examples with various statuses
- Clean, minimal design

**Best for:** Understanding card component, simple project showcases, component testing

### 2. Personal Portfolio (`personal_portfolio.yml`)
A comprehensive portfolio site for a software developer featuring:
- Hero banner with project showcases
- Multi-line title
- Card layout for projects
- About section with skills and experience
- Links to social media and projects
- Professional footer with contact links

**Best for:** Software developers, engineers, designers, freelancers

### 2. Business/Company (`business_company.yml`)
A corporate website showcasing services and team:
- Professional hero banner
- Services offered
- Team information with leadership
- Client testimonials
- Contact information and social media
- Business-focused footer

**Best for:** Agencies, consulting firms, tech companies, service providers

### 3. Creative/Artist (`creative_artist.yml`)
An artistic portfolio for creative professionals:
- Creative hero banner with visual focus
- Portfolio projects and client work
- Skills and tools used
- Education and achievements
- Artistic influences and inspiration
- Creative footer with personality

**Best for:** Digital artists, graphic designers, illustrators, creative directors

### 4. Minimal Blog (`minimal_blog.yml`)
A clean, content-focused blog site:
- Simple hero without image
- Blog categories and recent posts
- About the author
- Writing and speaking engagements
- Learning and reading lists
- Newsletter signup

**Best for:** Bloggers, writers, educators, thought leaders

### 5. Multi-Page Portfolio (`multi_page_example.yml`)
A comprehensive multi-page portfolio featuring:
- Homepage with hero banner and project cards
- Dedicated About page with personal story
- Projects page showcasing work and technologies
- Contact page with multiple ways to connect
- Blog page for writing and thoughts
- Automatic navigation between all pages

**Best for:** Developers, designers, freelancers who want multiple pages

### 6. Sizzle Component (`sizzle_example.yml`)
A demonstration of the Sizzle component featuring:
- Modern process section with clean styling
- Responsive grid layout for steps
- Hover effects and smooth transitions
- Customizable icons, titles, and descriptions
- Multiple configuration options (simple and advanced)

**Best for:** Understanding the Sizzle component, process workflows, step-by-step guides

### 7. Simple Multi-Page (`simple_multi_page.yml`)
A basic example showing multi-page functionality:
- Minimal homepage content
- Single About page example
- Shows both single page and multiple pages syntax
- Perfect for learning the multi-page feature

**Best for:** Learning multi-page functionality, simple personal sites

### 7. SSSStatic Library Site (`sssstatic_library_site.yml`)
The official SSSStatic library website showcasing:
- Homepage with hero banner highlighting key features
- Documentation page with installation and usage guides
- Examples page showcasing templates and real-world usage
- Community page with support, contributing, and roadmap
- Perfect example of a technical documentation site

**Best for:** Library documentation, technical sites, open source projects

## How to Use These Samples

1. **Copy a sample file** to your project directory:
   ```bash
   cp sample_configs/personal_portfolio.yml _config.yml
   ```

2. **Customize the content** to match your information:
   - Replace names, titles, and descriptions
   - Update URLs and social media links
   - Add your own images and assets
   - Modify the theme if desired

3. **Build your site**:
   ```bash
   sssstatic build
   ```

4. **Preview locally**:
   ```bash
   sssstatic serve
   ```

## Key Features Demonstrated

### Link Support
All samples show how to use markdown-style links `[text](url)` in:
- List items (skills, projects, etc.)
- Footer headlines
- About sections
- Contact information

### Themes
- `light` - Clean, professional look
- `dark` - Modern, sleek appearance

### Components Used
- `_multi_line_title` - Dramatic title presentation
- `_card` - Project showcase layout
- `_footer` - Customizable footer with links
- `about_me` - Structured personal/professional information
- `_page` - Multi-page support for creating additional pages

### Multi-Page Support
SSSStatic now supports multiple pages! Use the `_page` component to create additional pages:

```yaml
# Single page
_page:
  _name: "About"
  _title: "About Me"
  _footer:
    headline: "Learn more about my journey"
  # ... page content

# Multiple pages
_page:
  - _name: "About"
    _title: "About Me"
    # ... page content
  - _name: "Projects"
    _title: "My Projects"
    # ... page content
```

**Features:**
- Automatic navigation between pages
- Each page can have its own title, footer, and content
- Page names become filenames (e.g., "About Me" → `about_me.html`)
- Backward compatible with single-page sites

### Content Organization
- Hierarchical sections with clear headings
- Mix of lists, descriptions, and links
- Professional and personal information balance
- Social media integration

## Customization Tips

1. **Images**: Replace placeholder image URLs with your actual images
2. **Links**: Update all URLs to point to your real profiles and projects
3. **Content**: Tailor the sections to match your specific needs
4. **Theme**: Experiment with `light` and `dark` themes
5. **Footer**: Use the new link support for social media and contact info

## Need Help?

- Check the [Configuration Guide](../CONFIG_GUIDE.md) for detailed documentation
- Look at the [main README](../README.md) for setup instructions
- Review the source code in the `sssstatic/` directory for advanced customization
