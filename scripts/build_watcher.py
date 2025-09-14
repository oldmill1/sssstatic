#!/usr/bin/env python3
"""
Build Watcher Script for sssstatic

This script watches for file changes in the sssstatic source directory
and automatically rebuilds the site when changes are detected.

Usage:
    python build_watcher.py --watchDir /path/to/watch --destinationDir /path/to/destination
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class BuildHandler(FileSystemEventHandler):
    """Handler for file system events that triggers builds."""
    
    def __init__(self, destination_dir, watch_dir):
        self.destination_dir = destination_dir
        self.watch_dir = watch_dir
        self.last_build_time = 0
        self.build_cooldown = 2  # seconds to wait between builds
        
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
            
        # Check if the file is a Python file or YAML file
        file_path = Path(event.src_path)
        if file_path.suffix not in ['.py', '.yml', '.yaml']:
            return
            
        # Avoid rapid successive builds
        current_time = time.time()
        if current_time - self.last_build_time < self.build_cooldown:
            return
            
        self.last_build_time = current_time
        self._trigger_build()
    
    def on_created(self, event):
        """Handle file creation events."""
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        if file_path.suffix not in ['.py', '.yml', '.yaml']:
            return
            
        current_time = time.time()
        if current_time - self.last_build_time < self.build_cooldown:
            return
            
        self.last_build_time = current_time
        self._trigger_build()
    
    def _trigger_build(self):
        """Execute the sssstatic build command."""
        print(f"\n🔄 File change detected! Building site...")
        
        try:
            # Change to destination directory and run sssstatic build
            result = subprocess.run(
                ['sssstatic', 'build'],
                cwd=self.destination_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            print(f"✅ Build completed successfully!")
            if result.stdout:
                print(f"Output: {result.stdout}")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Build failed with error:")
            print(f"Error: {e.stderr}")
        except FileNotFoundError:
            print(f"❌ sssstatic command not found. Make sure sssstatic is installed and in PATH.")
        except Exception as e:
            print(f"❌ Unexpected error during build: {e}")


def main():
    """Main function to set up file watching and start the observer."""
    parser = argparse.ArgumentParser(
        description="Watch sssstatic source files and auto-rebuild on changes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python build_watcher.py --watchDir /Users/ataxali/dev/sssstatic/sssstatic --destinationDir /Users/ataxali/dev/jslbombaydating_www
    python build_watcher.py --watchDir /path/to/source --destinationDir /path/to/site
        """
    )
    
    parser.add_argument(
        '--watchDir',
        required=True,
        help='Directory to watch for changes (full path)'
    )
    
    parser.add_argument(
        '--destinationDir',
        required=True,
        help='Destination directory where sssstatic build will be executed (full path)'
    )
    
    args = parser.parse_args()
    
    # Validate paths
    watch_dir = Path(args.watchDir)
    destination_dir = Path(args.destinationDir)
    
    if not watch_dir.exists():
        print(f"❌ Watch directory does not exist: {watch_dir}")
        sys.exit(1)
        
    if not watch_dir.is_dir():
        print(f"❌ Watch path is not a directory: {watch_dir}")
        sys.exit(1)
        
    if not destination_dir.exists():
        print(f"❌ Destination directory does not exist: {destination_dir}")
        sys.exit(1)
        
    if not destination_dir.is_dir():
        print(f"❌ Destination path is not a directory: {destination_dir}")
        sys.exit(1)
    
    print(f"🚀 Starting build watcher...")
    print(f"📁 Watching: {watch_dir}")
    print(f"🎯 Building in: {destination_dir}")
    print(f"⏹️  Press Ctrl+C to stop")
    
    # Set up the file system event handler
    event_handler = BuildHandler(destination_dir, watch_dir)
    observer = Observer()
    observer.schedule(event_handler, str(watch_dir), recursive=True)
    
    # Start watching
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n🛑 Stopping build watcher...")
        observer.stop()
    
    observer.join()
    print(f"👋 Build watcher stopped.")


if __name__ == "__main__":
    main()
