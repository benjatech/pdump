# Project Dump (pdump)

**Aggregate your project files into a single text file for AI analysis**

Project Dump is a command-line tool that consolidates all your project files into a single text file, making it easy to share your entire codebase with AI assistants like Claude, ChatGPT, or other LLMs for analysis, debugging, or code review.

## Installation

### Option 1: Download Pre-compiled Binary (Recommended)

**Linux/macOS:**
```bash
# Download the binary
wget https://github.com/benjatech/pdump/releases/latest/download/pdump

# Make it executable
chmod +x pdump

# Move to your PATH
sudo mv pdump /usr/local/bin/
```

**Windows:**
Download `pdump.exe` and add it to your PATH.

### Option 2: Install from Source

**Requirements:**
- Python 3.7+

```bash
# Clone the repository
git clone https://github.com/benjatech/pdump.git
cd pdump

# Make the script executable
chmod +x pdump.py

# Copy to your bin directory
cp pdump.py /usr/local/bin/pdump
```

### Option 3: Compile It Yourself

```bash
# Install PyInstaller
pip install pyinstaller

# Compile to standalone executable
pyinstaller --onefile pdump.py

# The binary will be in dist/pdump
sudo cp dist/pdump /usr/local/bin/
```

## Quick Start

```bash
# Dump all files in current directory
pdump

# Use a predefined profile
pdump --profile php

# Specify output filename
pdump --filename my-project.txt

# Include only specific extensions
pdump --extensions .py,.js,.md
```

## Usage

```
pdump [OPTIONS]
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--version` | Show version information | - |
| `--help` | Show help message | - |
| `--filename FILENAME` | Output filename | `dump.txt` |
| `--extensions EXTS` | Comma-separated file extensions (e.g., `.py,.js,.txt`) | All files |
| `--skip-dirs DIRS` | Comma-separated directories to skip | - |
| `--profile PROFILE` | Use predefined profile: `php`, `godot`, or `idf` | - |
| `--include-hidden-dirs` | Include hidden directories (`.git`, `.idea`, etc.) | Excluded |
| `--include-hidden-files` | Include hidden files (files starting with `.`) | Excluded |
| `--ignore-starts-with PATTERNS` | Ignore files starting with patterns | `.env` |
| `--ignore-ends-with PATTERNS` | Ignore files ending with patterns | `.env` |

### Common Exclusions (Default)

By default, these directories are always skipped:
- `.git`
- `.idea`
- `.vscode`
- `.DS_Store`
- `__pycache__`
- `.pytest_cache`
- `node_modules`

Use `--include-hidden-dirs` to include them.

## Examples

### Basic Usage

```bash
# Dump all project files
pdump

# Specify output file
pdump --filename my-codebase.txt
```

### Using Profiles

```bash
# PHP project
pdump --profile php

# Godot game project
pdump --profile godot

# ESP-IDF embedded project
pdump --profile idf
```

### Custom Filters

```bash
# Only Python files
pdump --extensions .py

# Python and JavaScript files
pdump --extensions .py,.js,.jsx

# Skip build and test directories
pdump --skip-dirs build,test,dist

# Include .git directory
pdump --include-hidden-dirs

# Ignore backup and temporary files
pdump --ignore-ends-with .bak,.tmp,.swp
```

### Advanced Examples

```bash
# Python project with comprehensive settings
pdump --extensions .py,.md,.txt \
      --skip-dirs venv,__pycache__,dist,build \
      --filename python-project.txt

# Web project (HTML, CSS, JS)
pdump --extensions .html,.css,.js,.jsx,.tsx \
      --skip-dirs node_modules,dist,build \
      --filename web-app.txt

# Include everything (even hidden files and dirs)
pdump --include-hidden-dirs --include-hidden-files --filename complete-dump.txt
```

## Profiles

### PHP Profile
- **Extensions**: `.php`
- **Skip Dirs**: `vendor`, `node_modules`

```bash
pdump --profile php
```

### Godot Profile
- **Extensions**: `.gd`
- **Skip Dirs**: `addons`

```bash
pdump --profile godot
```

### ESP-IDF Profile
- **Extensions**: `.c`, `.h`, `.cmake`, `.projbuild`, `.txt`
- **Skip Dirs**: `build`, `.git`, `.idea`, `.vscode`, `managed_components`, `cmake-build-debug-esp-idf`

```bash
pdump --profile idf
```

## Output Format

The output file contains all your project files with clear separators:

```
====================
FILE: ./main.py
====================
[file contents here]

====================
FILE: ./utils/helper.py
====================
[file contents here]
```

## Use Cases

-  **Code Review**: Share entire codebase with AI for comprehensive review
-  **Debugging**: Let AI analyze your entire project context
-  **Documentation**: Generate documentation from your codebase
-  **Refactoring**: Get AI suggestions for large-scale refactoring
-  **Learning**: Analyze codebases for educational purposes
-  **AI Training**: Prepare code datasets for fine-tuning

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-profile`)
3. Commit your changes (`git commit -m 'Add new profile'`)
4. Push to the branch (`git push origin feature/new-profile`)
5. Open a Pull Request

## License

MIT License - feel free to use this tool in your projects.

## Author

**Mauro Baptista**  
X: [@carnou](https://x.com/carnou)

## Support

If you find this tool useful, please give it a ⭐ on GitHub!

---

**Version**: 0.0.1  
**Last Updated**: February 2026
