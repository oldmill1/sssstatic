# SSSStatic Sample Configurations

This directory contains sample `_config.yml` files that demonstrate different ways to use SSSStatic for various types of websites.

## Available Samples

### 1. Personal Portfolio (`personal_portfolio.yml`)
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
- `_hero_banner` - Eye-catching header with call-to-action
- `_multi_line_title` - Dramatic title presentation
- `_card` - Project showcase layout
- `_footer` - Customizable footer with links
- `about_me` - Structured personal/professional information

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
