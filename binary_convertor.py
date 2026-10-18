"""
===========================================================
Module : Binary Converter
Project: AI-Assisted DNA Data Archival System

Description:
------------
Converts raw bytes into binary and binary back into bytes.

Workflow:
Raw Bytes
    ↓
Binary String
    ↓
Raw Bytes

Author: Hari
===========================================================
"""

from typing import Dict


def bytes_to_binary(raw_bytes: bytes) -> str:
    """
    Convert raw bytes into a continuous binary string.

    Parameters
    ----------
    raw_bytes : bytes

    Returns
    -------
    str
        Binary string.
    """
    return "".join(format(byte, "08b") for byte in raw_bytes)


def binary_to_bytes(binary_string: str) -> bytes:
    """
    Convert binary string back into raw bytes.

    Parameters
    ----------
    binary_string : str

    Returns
    -------
    bytes
    """

    # Binary length must be divisible by 8
    if len(binary_string) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8.")

    byte_array = bytearray()

    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        byte_array.append(int(byte, 2))

    return bytes(byte_array)


def binary_statistics(binary_string: str) -> Dict:
    """
    Generate statistics about the binary data.

    Parameters
    ----------
    binary_string : str

    Returns
    -------
    dict
    """

    total_bits = len(binary_string)
    ones = binary_string.count("1")
    zeros = binary_string.count("0")

    return {
        "total_bits": total_bits,
        "total_bytes": total_bits // 8,
        "ones": ones,
        "zeros": zeros,
        "preview": binary_string[:128] + ("..." if total_bits > 128 else "")
    }


def display_binary_statistics(stats: Dict) -> None:
    """
    Display binary statistics.
    """

    print("\n========== BINARY INFORMATION ==========")
    print(f"Total Bits   : {stats['total_bits']}")
    print(f"Total Bytes  : {stats['total_bytes']}")
    print(f"Number of 1s : {stats['ones']}")
    print(f"Number of 0s : {stats['zeros']}")
    print("\nBinary Preview")
    print(stats["preview"])
    print("========================================\n")


if __name__ == "__main__":

    sample = b"Hello DNA"

    print("Original Bytes:")
    print(sample)

    binary = bytes_to_binary(sample)

    stats = binary_statistics(binary)

    display_binary_statistics(stats)

    recovered = binary_to_bytes(binary)

    print("Recovered Bytes:")
    print(recovered)

    print("\nVerification:", sample == recovered)