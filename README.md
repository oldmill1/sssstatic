# 🐍🐍🐍Static Site Generator🐍🐍🐍

- 🐍**Simple**: Just write YAML
- 🐍 **Themed**: Built-in dark and light themes
- 🐍 **Dev-friendly**: Built-in dev server
- 🐍 **Responsive**: Clean, modern styling out of the box

## Set-up

```bash
pip install -e .
```

## Quick Start

### 1. Create a new project

```bash
sssstatic create new
```

### 2. Edit your `_config.yml`

```yaml
# SSSStatic Configuration
site_name: "My Awesome Site"
_theme: "dark"  # or "light"

about:
  name: "Your Name"
  bio: "What you do"
  location: "Where you are"

projects:
  - name: "Cool Project"
    url: "https://github.com/you/project"
    description: "What it does"
    status: "active"

contact:
  email: "you@example.com"
  github: "https://github.com/you"
```

### 3. Build and serve

```bash
sssstatic dev  # builds and starts dev server
# or separately:
sssstatic build
sssstatic serve
```

## Commands

### `sssstatic create new`

Creates a new project with initial `_config.yml` file.

### `sssstatic build`

Builds the static site from `_config.yml` into `_site/` directory.

### `sssstatic serve [options]`

Starts development server to preview the site.

Options:

- `-p, --port PORT` - Port to serve on (default: 8000)
- `-d, --directory DIR` - Directory to serve (default: _site)

### `sssstatic dev [options]`

Builds the site and starts dev server in one command.

Options:

- `-p, --port PORT` - Port to serve on (default: 8000)
- `-d, --directory DIR` - Directory to serve (default: _site)

## Configuration

### System Tags

System configuration uses underscore prefix and won't appear in content:

- `_theme`: "dark" or "light" (default: dark)

### Reserved Fields

- `site_name`: Used as page title and main heading

### Content Structure

Any other YAML structure becomes HTML content:

- **Objects** → Sections with headings
- **Lists** → Ordered lists
- **URLs** → Automatic links
- **Nested data** → Proper HTML hierarchy

## Themes

Two built-in themes:

- **Dark**: GitHub-inspired dark theme (default)
- **Light**: Clean, minimal light theme

Set theme in your config:

```yaml
_theme: "light"  # or "dark"
```

## Development

```bash
# Install in development mode
pip install -e .

# Quick development workflow
sssstatic dev  # builds and serves
# Edit _site/index.html directly for quick tweaks
# Or edit _config.yml and re-run sssstatic dev
```

## File Structure

```
your-project/
├── _config.yml      # Your site configuration
└── _site/           # Generated HTML (created by build)
    └── index.html   # Your website
```

## Requirements

- Python 3.6+
- PyYAML
- Rich (for pretty terminal output)

## License

Free software - see source for details.