#!/usr/bin/env python3
import os
import sys
import argparse

VERSION = '0.0.1'
AUTHOR = 'Mauro Baptista - Benja Tech'

COMMON_SKIP_DIRS = {'.git', '.idea', '.vscode', '.DS_Store', '__pycache__', '.pytest_cache', 'node_modules'}

class VersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(f'project-dump {VERSION}')
        print(f'Developed by {AUTHOR}')
        sys.exit(0)

PROFILES = {
    'php': {
        'extensions': ['.php'],
        'skip_dirs': ['vendor', 'node_modules']
    },
    'godot': {
        'extensions': ['.gd'],
        'skip_dirs': ['addons']
    },
    'idf': {
        'extensions': ['.c', '.h', '.cmake', '.projbuild', '.txt'],
        'skip_dirs': ['build', '.git', '.idea', '.vscode', 'managed_components', 'cmake-build-debug-esp-idf']
    }
}

def parse_args():
    parser = argparse.ArgumentParser(
        description='Project Dump - Aggregate project files into a single text file for AI analysis',
        epilog=f'Developed by {AUTHOR}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--version',
        action=VersionAction,
        nargs=0,
        help='Show version information and exit'
    )
    parser.add_argument(
        '--filename',
        default='dump.txt',
        help='Output filename (default: dump.txt)'
    )
    parser.add_argument(
        '--extensions',
        help='Comma-separated list of file extensions to include (e.g., .py,.js,.txt)'
    )
    parser.add_argument(
        '--skip-dirs',
        help='Comma-separated list of directories to skip (e.g., build,.git,node_modules)'
    )
    parser.add_argument(
        '--profile',
        choices=['php', 'godot', 'idf'],
        help='Use a predefined profile (php, godot, or idf)'
    )
    parser.add_argument(
        '--include-hidden-dirs',
        action='store_true',
        help='Include common hidden directories (.git, .idea, .vscode, etc.)'
    )
    parser.add_argument(
        '--include-hidden-files',
        action='store_true',
        help='Include hidden files (files starting with .)'
    )
    parser.add_argument(
        '--ignore-starts-with',
        default='.env',
        help='Comma-separated list of prefixes to ignore (default: .env)'
    )
    parser.add_argument(
        '--ignore-ends-with',
        default='.env',
        help='Comma-separated list of suffixes to ignore (default: .env)'
    )
    
    return parser.parse_args()

def is_text_file(filename, extensions):
    return any(filename.endswith(ext) for ext in extensions) or filename.endswith('Kconfig')

def main():
    args = parse_args()
    
    if args.profile:
        profile = PROFILES[args.profile]
        extensions = set(profile['extensions'])
        skip_dirs = set(profile['skip_dirs'])
    else:
        extensions = set(args.extensions.split(',')) if args.extensions else set()
        skip_dirs = set(args.skip_dirs.split(',')) if args.skip_dirs else set()
    
    if not args.include_hidden_dirs:
        skip_dirs.update(COMMON_SKIP_DIRS)
    
    ignore_starts_with = [p.strip() for p in args.ignore_starts_with.split(',') if p.strip()]
    ignore_ends_with = [p.strip() for p in args.ignore_ends_with.split(',') if p.strip()]
    
    output_filename = args.filename
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk("."):
            if skip_dirs:
                dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
                if file == output_filename:
                    continue
                
                if any(file.startswith(pattern) for pattern in ignore_starts_with):
                    continue
                if any(file.endswith(pattern) for pattern in ignore_ends_with):
                    continue
                
                if not args.include_hidden_files and file.startswith('.'):
                    continue
                
                if not extensions or is_text_file(file, extensions):
                    filepath = os.path.join(root, file)
                    
                    outfile.write(f"\n{'='*20}\nFILE: {filepath}\n{'='*20}\n")
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                            outfile.write("\n")
                    except Exception as e:
                        outfile.write(f"Error reading file: {e}\n")
    
    print(f"Done! Open '{output_filename}' and copy everything to the AI.")

if __name__ == '__main__':
    main()
