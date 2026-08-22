# XENO MAXIMUM SECURITY OBFUSCATOR
# WARNING: ANTI-TAMPER PROTECTED (NATIVE EXTENSION)
# Source code has been compiled to a native C binary.

import sys
try:
    import main_obfuscated_core
except ImportError as e:
    print(f"[!] Error loading native module: {e}")
    sys.exit(1)
