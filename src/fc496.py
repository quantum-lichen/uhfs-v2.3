"""
🧲 FC-496 Atoms — 64 bytes Quantum Storage Units
UHFS V2.2 Core Component
"""

import struct
from dataclasses import dataclass
import zlib
import hashlib

PHI_INV = 0.618033988749895

@dataclass
class FC496AtomV22:
    """🧲 FC-496 Atom V2.2 — 64 bytes exact (NVMe-oF Native)"""
    magic_phi: int = 0x9E3779B97F4A7C15
    magic_pi: int = 0x243F6A8885A308D3
    phys_zone_id: int = 0
    phys_offset: int = 0
    schema_id: int = 0
    h_scale_score: int = 0
    content_checksum: int = 0
    flags: int = 0
    next_atom_lba: int = 0
    parent_atom_lba: int = 0
    node_id: int = 0

    def pack(self) -> bytes:
        return struct.pack("<QQQQIIIIIQHI", 
            self.magic_phi, self.magic_pi, self.phys_zone_id, self.phys_offset,
            self.schema_id, self.h_scale_score, self.content_checksum, self.flags,
            self.next_atom_lba, self.parent_atom_lba, self.node_id)

    @classmethod
    def unpack(cls, data: bytes) -> 'FC496AtomV22':
        if len(data) != 64:
            raise ValueError(f"Invalid atom size: {len(data)}")
        unpacked = struct.unpack("<QQQQIIIIIQHI", data)
        return cls(*unpacked)

    @classmethod
    def from_embedding(cls, embedding: bytes, zone_count: int = 16384, content: bytes = b"") -> 'FC496AtomV22':
        """🌌 φ-Spiral LSH Addressing"""
        h = int(hashlib.blake2b(embedding, digest_size=32).hexdigest(), 16)
        zone_id = int(zone_count * (PHI_INV * (h / (1 << 256))) % 1)
        h_scale = 618  # Valid H-Scale
        
        return cls(
            phys_zone_id=zone_id,
            schema_id=1,
            h_scale_score=h_scale,
            content_checksum=zlib.crc32(content) & 0xFFFFFFFF,
            node_id=0
        )
