"""
===========================================================
Module : DNA Sequence Analyser
Project: AI-Assisted DNA Data Archival System

Description:
------------
Analyses a DNA sequence for synthesis suitability.

Author: Hari
===========================================================
"""

from typing import Dict


def analyse_dna(dna_sequence: str) -> Dict:

    dna_sequence = dna_sequence.upper()

    length = len(dna_sequence)

    a = dna_sequence.count("A")
    c = dna_sequence.count("C")
    g = dna_sequence.count("G")
    t = dna_sequence.count("T")

    gc_content = ((g + c) / length) * 100 if length else 0

    # Longest homopolymer
    longest = 1
    current = 1

    for i in range(1, length):
        if dna_sequence[i] == dna_sequence[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return {
        "length": length,
        "A": a,
        "C": c,
        "G": g,
        "T": t,
        "gc_content": gc_content,
        "longest_homopolymer": longest
    }


def display_analysis(result: Dict):

    print("\n========== DNA ANALYSIS ==========")
    print(f"Length              : {result['length']} bases")
    print(f"A Count             : {result['A']}")
    print(f"C Count             : {result['C']}")
    print(f"G Count             : {result['G']}")
    print(f"T Count             : {result['T']}")
    print(f"GC Content          : {result['gc_content']:.2f}%")
    print(f"Longest Homopolymer : {result['longest_homopolymer']}")

    print("\nSynthesis Assessment")

    if 40 <= result["gc_content"] <= 60:
        print("✓ GC content is within the preferred range.")
    else:
        print("⚠ GC content is outside the preferred range.")

    if result["longest_homopolymer"] <= 4:
        print("✓ Homopolymer length is acceptable.")
    else:
        print("⚠ Long homopolymer detected.")

    print("==================================\n")