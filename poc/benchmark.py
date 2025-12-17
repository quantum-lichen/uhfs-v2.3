#!/usr/bin/env python3
import time
from uhfs_v22 import UHFSV22, ACPhi496Codon

def benchmark(n=100000):
    fs = UHFSV22()
    start = time.perf_counter()
    for i in range(n):
        codon = ACPhi496Codon(0x01, f"truth-{i}")
        fs.transmute_codon(codon)
    duration = time.perf_counter() - start
    print(f"📊 {n:,} atoms: {n/duration:,.0f} IOPS")

if __name__ == "__main__":
    benchmark()
