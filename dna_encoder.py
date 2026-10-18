"""
===========================================================
Module : DNA Encoder
Project: AI-Assisted DNA Data Archival System

Description:
------------
Converts binary data into a DNA sequence.

Mapping:
00 -> A
01 -> C
10 -> G
11 -> T

Workflow

Binary
   ↓
DNA Sequence

Author: Hari
===========================================================
"""

from typing import Dict

# ----------------------------------------------------------
# DNA Mapping
# ----------------------------------------------------------

from modules.dna_mapping import DNA_MAPPING

# ----------------------------------------------------------
# Binary → DNA
# ----------------------------------------------------------

def binary_to_dna(binary_string: str) -> str:
    """
    Convert binary string into DNA sequence.
    """

    if len(binary_string) % 2 != 0:
        raise ValueError("Binary length must be divisible by 2.")

    dna = []

    for i in range(0, len(binary_string), 2):
        bits = binary_string[i:i + 2]
        dna.append(DNA_MAPPING[bits])

    return "".join(dna)


# ----------------------------------------------------------
# DNA Statistics
# ----------------------------------------------------------

def dna_statistics(dna_sequence: str) -> Dict:

    total = len(dna_sequence)

    a = dna_sequence.count("A")
    c = dna_sequence.count("C")
    g = dna_sequence.count("G")
    t = dna_sequence.count("T")

    gc = ((g + c) / total) * 100 if total else 0

    return {
        "length": total,
        "A": a,
        "C": c,
        "G": g,
        "T": t,
        "gc_content": gc,
        "preview": dna_sequence[:100] +
        ("..." if total > 100 else "")
    }


# ----------------------------------------------------------
# Display Statistics
# ----------------------------------------------------------

def display_dna_statistics(stats: Dict):

    print("\n========== DNA INFORMATION ==========")
    print(f"Sequence Length : {stats['length']}")
    print(f"A : {stats['A']}")
    print(f"C : {stats['C']}")
    print(f"G : {stats['G']}")
    print(f"T : {stats['T']}")
    print(f"GC Content : {stats['gc_content']:.2f}%")

    print("\nDNA Preview")
    print(stats["preview"])

    print("=====================================\n")


# ----------------------------------------------------------
# Test
# ----------------------------------------------------------

if __name__ == "__main__":

    sample_binary = "00011011"

    dna = binary_to_dna(sample_binary)

    print("DNA:", dna)

    stats = dna_statistics(dna)

    display_dna_statistics(stats)