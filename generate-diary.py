#!/usr/bin/env python3
"""
Script to automatically generate diary.json from markdown files in Daily folder
"""

import os
import json
import glob

# Get all markdown files in Daily folder
diary_files = glob.glob('Daily/*.md')

# Sort files by date in reverse order (newest first)
diary_files.sort(reverse=True)

# Prepare diary entries list
diary_entries = []

# Process each file
for file_path in diary_files:
    # Extract date from filename
    filename = os.path.basename(file_path)
    date = filename[:-3]  # Remove .md extension
    
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract title from first # header
    title = "Diary Entry - " + date  # Default title
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Create entry dictionary
    entry = {
        "date": date,
        "title": title,
        "filePath": file_path
    }
    
    # Add to entries list
    diary_entries.append(entry)

# Write to diary.json with proper formatting
with open('diary.json', 'w') as f:
    json.dump(diary_entries, f, indent=2, ensure_ascii=False)

# Print success message
print("✅ Diary JSON generated successfully!")
print(f"📋 Found {len(diary_entries)} diary entries")
print("📄 Updated diary.json with all entries sorted by date (newest first)")
print("🎯 Format: Properly formatted JSON with correct indentation")
