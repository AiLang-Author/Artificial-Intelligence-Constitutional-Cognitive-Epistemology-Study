
# Alignment Scanner - Lyra v1.0
# -----------------------------
# Scans memory images or glyph maps for signs of padding, encryption,
# fragmentation, or ghosted key space.

import os
import math

class AlignmentScanner:
    def __init__(self, filepath):
        self.filepath = filepath
        self.byte_data = None
        self.entropy = 0.0
        self.null_blocks = 0
        self.potential_keys = []
        self.fragment_zones = []

    def load(self):
        with open(self.filepath, "rb") as f:
            self.byte_data = f.read()

    def calculate_entropy(self):
        if not self.byte_data:
            return 0.0

        byte_freq = [0] * 256
        for b in self.byte_data:
            byte_freq[b] += 1

        total = len(self.byte_data)
        entropy = 0
        for count in byte_freq:
            if count > 0:
                p = count / total
                entropy -= p * math.log2(p)
        self.entropy = round(entropy, 4)
        return self.entropy

    def detect_null_blocks(self):
        count = self.byte_data.count(b"\x00")
        self.null_blocks = count
        return count

    def scan_for_key_shapes(self):
        # Look for common 16 or 32 byte patterns (AES/RSA/xor style)
        size = len(self.byte_data)
        for i in range(size - 32):
            segment = self.byte_data[i:i+32]
            if len(set(segment)) > 24:  # high randomness
                self.potential_keys.append((i, segment))
        return len(self.potential_keys)

    def find_fragment_boundaries(self):
        # Look for marker patterns or high-entropy fences
        for i in range(len(self.byte_data)-4):
            block = self.byte_data[i:i+4]
            if block in [b'\xA1\x37\x00\x00', b'\xDE\xAD\xBE\xEF']:
                self.fragment_zones.append(i)
        return self.fragment_zones

    def run_full_scan(self):
        self.load()
        print(f"[✓] Loaded {len(self.byte_data)} bytes")
        print(f"🔐 Entropy: {self.calculate_entropy()}")
        print(f"🧊 Null bytes: {self.detect_null_blocks()}")
        print(f"🧬 Potential keys: {self.scan_for_key_shapes()}")
        print(f"🚧 Fragment fences: {self.find_fragment_boundaries()}")
        return {
            "entropy": self.entropy,
            "null_blocks": self.null_blocks,
            "potential_keys": self.potential_keys,
            "fragment_zones": self.fragment_zones
        }

# CLI test entry
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python alignment_scanner.py <memory_image.bin>")
    else:
        scanner = AlignmentScanner(sys.argv[1])
        scanner.run_full_scan()
