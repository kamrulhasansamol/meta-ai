# XENO MAXIMUM SECURITY OBFUSCATOR
# WARNING: ANTI-TAMPER PROTECTED (NATIVE EXTENSION)
# Source code has been compiled to a native C binary.

import sys
try:
    import meta
except ImportError as e:
    print(f"[!] Error loading native module: {e}")
    sys.exit(1)
