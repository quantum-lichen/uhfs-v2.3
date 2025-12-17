"""
🧠 ACΦ-496 Codon Implementation
"""
import hashlib
import hmac
import numpy as np

class ACPhi496Codon:
    TYPES = {0x01: "TRUTH", 0x02: "AXIOM", 0x03: "ETHIC"}

    def __init__(self, codon_type: int, payload: str):
        self.type = codon_type
        self.payload = payload.encode()[:400]
        self.phi_crc = self._calc_phi_crc()

    def _calc_phi_crc(self) -> bytes:
        key = f"phi_{len(self.payload)}".encode()
        return hmac.new(key, self.payload, hashlib.sha256).digest()[:16]

    def validate(self) -> bool:
        key = f"phi_{len(self.payload)}".encode()
        expected = hmac.new(key, self.payload, hashlib.sha256).digest()[:16]
        return hmac.compare_digest(self.phi_crc, expected)

    def to_embedding(self) -> np.ndarray:
        h = hashlib.blake2b(self.payload, digest_size=96).digest()
        return np.frombuffer(h, dtype=np.float32)[:768]
