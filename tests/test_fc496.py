import pytest
from uhfs_v22 import FC496AtomV22

def test_atom_packing():
    atom = FC496AtomV22()
    data = atom.pack()
    assert len(data) == 64
