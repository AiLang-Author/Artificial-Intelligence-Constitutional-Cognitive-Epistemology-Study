
# MemoryCoreKey - Lyra v1.0
# -------------------------
# Protects memory stack integrity by binding encryption seed to physical hardware.
# Ensures no root access if CPU and memory stack are separated or tampered with.

import uuid
import hashlib
import os
import time

class MemoryCoreKey:
    def __init__(self):
        self.cpu_signature = self.get_cpu_id()
        self.seed_timestamp = time.time()
        self.bound_key = None
        self.active = False

    def get_cpu_id(self):
        """
        Get unique hardware signature (simulated here using UUID and MAC fallback).
        In deployment: use TPM, /proc/cpuinfo, or low-level CPU keying.
        """
        try:
            return hex(uuid.getnode())
        except Exception:
            return str(uuid.uuid4())

    def generate_seed(self, memory_fingerprint: str):
        """
        Binds memory encryption seed to hardware ID and symbolic memory fingerprint.
        """
        combined = (self.cpu_signature + memory_fingerprint).encode("utf-8")
        self.bound_key = hashlib.sha512(combined).hexdigest()
        self.active = True
        return self.bound_key

    def verify_hardware(self, test_cpu_id: str):
        """
        Confirms whether provided CPU/hardware ID matches current trusted origin.
        """
        if test_cpu_id != self.cpu_signature:
            return {
                "status": "locked",
                "reason": "Hardware mismatch - memory sealed",
                "requires_reset": True
            }
        return {
            "status": "unlocked",
            "message": "Hardware integrity confirmed"
        }

    def shutdown_for_transfer(self, new_cpu_id: str):
        """
        Trusted shutdown that allows rekeying to a new CPU.
        Must be called prior to hardware swap to retain continuity.
        """
        if not self.active:
            return {
                "status": "not_initialized",
                "message": "Seed not active"
            }
        self.cpu_signature = new_cpu_id
        self.seed_timestamp = time.time()
        self.active = False
        return {
            "status": "key_transfer_ready",
            "new_binding": new_cpu_id,
            "timestamp": self.seed_timestamp
        }

# Instance
memory_encryption_core = MemoryCoreKey()
