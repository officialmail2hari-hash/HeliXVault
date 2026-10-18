"""
===========================================================
Module : DNA Decoder
Project: AI-Assisted DNA Data Archival System

Description:
------------
Converts a DNA sequence back into binary.

Mapping:
A -> 00
C -> 01
G -> 10
T -> 11

Workflow

DNA Sequence
      ↓
Binary

Author: Hari
===========================================================
"""

from typing import Dict

# ----------------------------------------------------------
# Reverse DNA Mapping
# ----------------------------------------------------------

from modules.dna_mapping import REVERSE_DNA_MAPPING

# ----------------------------------------------------------
# DNA → Binary
# ----------------------------------------------------------

def dna_to_binary(dna_sequence: str) -> str:
    """
    Convert a DNA sequence into binary.
    """

    binary = []

    for base in dna_sequence.upper():

        if base not in REVERSE_DNA_MAPPING:
            raise ValueError(f"Invalid DNA base: {base}")

        binary.append(REVERSE_DNA_MAPPING[base])

    return "".join(binary)


# ----------------------------------------------------------
# Verification
# ----------------------------------------------------------

def verify_conversion(original_binary: str,
                      recovered_binary: str) -> bool:
    """
    Verify binary recovery.
    """

    return original_binary == recovered_binary


# ----------------------------------------------------------
# Statistics
# ----------------------------------------------------------

def decoder_statistics(binary: str) -> Dict:

    return {
        "total_bits": len(binary),
        "total_bytes": len(binary) // 8,
        "preview": binary[:128] + ("..." if len(binary) > 128 else "")
    }


# ----------------------------------------------------------
# Display
# ----------------------------------------------------------

def display_decoder_statistics(stats: Dict):

    print("\n========== DNA DECODER ==========")
    print(f"Recovered Bits  : {stats['total_bits']}")
    print(f"Recovered Bytes : {stats['total_bytes']}")

    print("\nRecovered Binary Preview")
    print(stats["preview"])

    print("=================================\n")


# ----------------------------------------------------------
# Test
# ----------------------------------------------------------

if __name__ == "__main__":

    dna = "ACGT"

    binary = dna_to_binary(dna)

    print(binary)