"""
Check NES ROM Mapper compatibility with JSNES
"""

import sys
import os

def check_mapper(rom_file):
    """Check the mapper number of a NES ROM"""
    try:
        with open(rom_file, 'rb') as f:
            header = f.read(16)

        # Check for iNES header
        if header[0:4] != b'NES\x1a':
            return None, "No iNES header found"

        # Extract mapper number
        mapper_num = (header[6] >> 4) | (header[7] & 0xF0)

        # Check compatibility
        supported_mappers = [0, 1, 2, 3, 4, 7, 66]
        is_supported = mapper_num in supported_mappers

        return mapper_num, is_supported

    except Exception as e:
        return None, str(e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_rom_mapper.py <rom_file>")
        print("\nExample:")
        print("  python check_rom_mapper.py roms/3-Contra.nes")
        sys.exit(1)

    rom_file = sys.argv[1]

    if not os.path.exists(rom_file):
        print(f"❌ File not found: {rom_file}")
        sys.exit(1)

    print(f"Checking: {rom_file}")
    print("-" * 50)

    mapper_num, result = check_mapper(rom_file)

    if mapper_num is None:
        print(f"❌ Error: {result}")
        sys.exit(1)

    print(f"Mapper Number: {mapper_num}")

    if result is True:
        print("✅ Status: SUPPORTED by JSNES")
    elif result is False:
        print("❌ Status: NOT SUPPORTED by JSNES")
        print("\nSupported mappers: 0, 1, 2, 3, 4, 7, 66")
        print("\nSuggestion:")
        print("  Find a ROM version that uses Mapper 2 or Mapper 0")
        print("  These are the most common compatible mappers")
    else:
        print(f"⚠️  Error: {result}")

if __name__ == "__main__":
    main()
