import pytest
from uhfs_v22 import UHFSV22, ACPhi496Codon

def test_uhfs_transmute_full_cycle():
    fs = UHFSV22()
    codon = ACPhi496Codon(0x01, "complete test")
    lba = fs.transmute_codon(codon)
    atom = fs.read_atom(lba)
    
    assert lba >= 0
    assert atom is not None
    assert atom.h_scale_score >= 618
