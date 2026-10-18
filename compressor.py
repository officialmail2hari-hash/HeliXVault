"""
===========================================================
Module : Compression Engine
Project: AI-Assisted DNA Data Archival System

Description:
------------
Compresses and decompresses raw bytes using gzip.

Workflow:
Raw Bytes
    ↓
Compressed Bytes
    ↓
Decompressed Bytes

Author: Hari
===========================================================
"""

import gzip
from typing import Dict


def compress_data(raw_bytes: bytes) -> bytes:
    """
    Compress raw bytes using gzip.

    Parameters
    ----------
    raw_bytes : bytes

    Returns
    -------
    bytes
        Compressed data
    """
    return gzip.compress(raw_bytes)


def decompress_data(compressed_bytes: bytes) -> bytes:
    """
    Decompress gzip-compressed bytes.

    Parameters
    ----------
    compressed_bytes : bytes

    Returns
    -------
    bytes
        Original data
    """
    return gzip.decompress(compressed_bytes)


def compression_statistics(original: bytes,
                           compressed: bytes) -> Dict:
    """
    Generate compression statistics.
    """

    original_size = len(original)
    compressed_size = len(compressed)

    ratio = compressed_size / original_size

    saved = ((original_size - compressed_size)
             / original_size) * 100

    return {
        "original_size": original_size,
        "compressed_size": compressed_size,
        "compression_ratio": ratio,
        "space_saved": saved
    }


def display_compression_statistics(stats: Dict) -> None:

    print("\n========== COMPRESSION ==========")
    print(f"Original Size     : {stats['original_size']} bytes")
    print(f"Compressed Size   : {stats['compressed_size']} bytes")
    print(f"Compression Ratio : {stats['compression_ratio']:.2f}")
    print(f"Space Saved       : {stats['space_saved']:.2f}%")
    print("=================================\n")


if __name__ == "__main__":

    sample = b"Hello DNA Storage! " * 100

    compressed = compress_data(sample)

    decompressed = decompress_data(compressed)

    stats = compression_statistics(sample, compressed)

    display_compression_statistics(stats)

    print("Verification:", sample == decompressed)