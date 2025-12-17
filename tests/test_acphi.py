import pytest
from acphi.codon import ACPhi496Codon

def test_acphi_codon_validation():
    codon = ACPhi496Codon(0x01, "IA serves humanity")
    assert codon.validate() == True
    assert len(codon.payload) <= 400

def test_acphi_embedding():
    codon = ACPhi496Codon(0x02, "test axiom")
    embedding = codon.to_embedding()
    assert len(embedding) == 768
