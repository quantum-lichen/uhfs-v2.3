"""
⚙️ FC-496 ↔ ACΦ-496 Bidirectional Transmuter
UHFS V2.2 Pipeline Core
"""

from acphi.codon import ACPhi496Codon
from .fc496 import FC496AtomV22

def transmute_acphi_to_fc(codon: ACPhi496Codon) -> FC496AtomV22:
    """🔄 ACΦ → FC-496 Transmutation"""
    if not codon.validate():
        raise ValueError("Invalid ACΦ codon")
    
    embedding = codon.to_embedding().tobytes()
    atom = FC496AtomV22.from_embedding(embedding, content=codon.payload)
    atom.schema_id = codon.type
    return atom

def transmute_fc_to_acphi(atom: FC496AtomV22) -> ACPhi496Codon:
    """🔄 FC-496 → ACΦ Reverse Transmutation"""
    try:
        payload = atom.content_checksum.to_bytes(4, 'little').decode('latin1', errors='ignore')
        return ACPhi496Codon(atom.schema_id, payload)
    except Exception as e:
        raise ValueError(f"FC to ACΦ transmutation failed: {e}")
