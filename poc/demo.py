#!/usr/bin/env python3
from uhfs_v22 import UHFSV22, ACPhi496Codon

fs = UHFSV22()
codon = ACPhi496Codon(0x01, "Demo codon")
lba = fs.transmute_codon(codon)
print(f"🎮 Demo LBA: {lba}")
