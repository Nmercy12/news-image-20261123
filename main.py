#!/usr/bin/env python3
import os
import shutil
import hashlib
import sys
import struct

def main():
    # Resolve entry.png relative to main.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "entry.png")
    
    if not os.path.exists(source_path):
        print(f"Error: source image not found at {source_path}", file=sys.stderr)
        sys.exit(1)
        
    # Verify PNG dimensions (1024x1024) from header
    with open(source_path, "rb") as f:
        header = f.read(24)
    if len(header) >= 24 and header[:8] == b'\x89PNG\r\n\x1a\n':
        width, height = struct.unpack(">II", header[16:24])
        if width != 1024 or height != 1024:
            print(f"Error: Invalid PNG dimensions {width}x{height} (expected 1024x1024)", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: Invalid PNG signature", file=sys.stderr)
        sys.exit(1)
        
    # Determine output directory
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        output_dir = os.path.join(script_dir, "out")
    
    os.makedirs(output_dir, exist_ok=True)
    dest_path = os.path.join(output_dir, "entry.png")
    
    # Read source bytes and compute SHA-256
    with open(source_path, "rb") as f:
        source_bytes = f.read()
    
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    source_size = len(source_bytes)
    
    # Copy bytes exactly
    shutil.copyfile(source_path, dest_path)
    
    # Verify copy size matches source
    if not os.path.exists(dest_path):
        print(f"Error: destination file not created at {dest_path}", file=sys.stderr)
        sys.exit(1)
        
    with open(dest_path, "rb") as f:
        dest_bytes = f.read()
        
    dest_size = len(dest_bytes)
    dest_sha256 = hashlib.sha256(dest_bytes).hexdigest()
    
    if source_size != dest_size:
        print(f"Error: size mismatch! Source size {source_size} != Dest size {dest_size}", file=sys.stderr)
        sys.exit(1)
        
    if source_sha256 != dest_sha256:
        print(f"Error: SHA-256 mismatch! Source {source_sha256} != Dest {dest_sha256}", file=sys.stderr)
        sys.exit(1)
        
    print(f"Output path: {dest_path}")
    print(f"SHA-256: {source_sha256}")
    print(f"Size: {source_size} bytes")

if __name__ == "__main__":
    main()
