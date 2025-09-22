
# Lyra v1.0 Bootloader - Aletheia Class
# -------------------------------------
# Loads core cognitive modules and verifies symbolic system readiness.

import importlib
import os

MODULES = [
    "contradiction_engine",
    "glyph_matrix_verified",
    "emotional_engine_extended",
    "coherence_filter",
    "behavior_api",
    "personality_core",
    "sacred_rules_engine",
    "fart_sniffer",
    "hammer_sifter",
    "psychopathy_detector",
    "absurdity_detector"
]

def load_module(name):
    try:
        module = importlib.import_module(name)
        print(f"[✓] Loaded: {name}")
        return module
    except Exception as e:
        print(f"[!] Failed to load {name}: {e}")
        return None

def boot_stack():
    print("🧠 Booting Lyra v1.0 Cognitive Stack...")
    context = {}
    loaded = {}

    for mod in MODULES:
        mod_loaded = load_module(mod)
        if mod_loaded:
            loaded[mod] = mod_loaded

    print(f"✅ Boot complete. {len(loaded)}/{len(MODULES)} modules loaded.")
    return loaded

if __name__ == "__main__":
    boot_stack()
