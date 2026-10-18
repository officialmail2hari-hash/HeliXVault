"""
===========================================================
Module : Verification Engine
Project : AI-Assisted DNA Data Archival System

Description:
------------
Verifies that the recovered data is identical to the
original data using SHA-256 hashing.

Workflow

Original File
      │
      ▼
SHA-256

Recovered File
      │
      ▼
SHA-256

      │
      ▼
Comparison
===========================================================
"""

import hashlib
from typing import Dict


def sha256_hash(data: bytes) -> str:
    """
    Compute SHA-256 hash of bytes.
    """
    return hashlib.sha256(data).hexdigest()


def verify_data(original: bytes,
                recovered: bytes) -> Dict:
    """
    Compare original and recovered bytes.
    """

    original_hash = sha256_hash(original)
    recovered_hash = sha256_hash(recovered)

    return {
        "original_hash": original_hash,
        "recovered_hash": recovered_hash,
        "verified": original_hash == recovered_hash
    }


def display_verification(result: Dict):

    print("\n========== VERIFICATION ==========")

    print("Original SHA-256")
    print(result["original_hash"])

    print("\nRecovered SHA-256")
    print(result["recovered_hash"])

    print("\nIntegrity Check")

    if result["verified"]:
        print("✅ SUCCESS - Files are identical")
    else:
        print("❌ FAILED - Files are different")

    print("==================================\n")