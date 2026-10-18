"""
===========================================================
Module : File Reader
Project: AI-Assisted DNA Data Archival System

Description:
------------
This module reads a file from disk and extracts:

• File name
• File extension
• File size
• SHA-256 hash
• Raw bytes

This module performs NO processing on the data.
It simply prepares the file for the next module.

Author: Hari
===========================================================
"""

from pathlib import Path
import hashlib


SUPPORTED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".docx",
    ".png",
    ".jpg",
    ".jpeg",
    ".csv"
}


def calculate_sha256(raw_bytes: bytes) -> str:
    """
    Calculate SHA-256 hash of raw file bytes.

    Parameters
    ----------
    raw_bytes : bytes

    Returns
    -------
    str
        SHA-256 hexadecimal digest
    """
    return hashlib.sha256(raw_bytes).hexdigest()


def read_file(file_path: str) -> bytes:
    """
    Read file as raw bytes.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    bytes
        Raw file bytes
    """
    with open(file_path, "rb") as file:
        return file.read()


def load_file(file_path: str) -> dict:
    """
    Load a file and return all metadata.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    dict
        Dictionary containing metadata and raw bytes.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type '{extension}'. "
            f"Supported types: {sorted(SUPPORTED_EXTENSIONS)}"
        )

    raw_bytes = read_file(file_path)

    metadata = {
        "filename": path.name,
        "filepath": str(path.resolve()),
        "extension": extension,
        "size_bytes": path.stat().st_size,
        "sha256": calculate_sha256(raw_bytes),
        "raw_bytes": raw_bytes
    }

    return metadata


def display_metadata(metadata: dict) -> None:
    """
    Display file metadata in a readable format.

    Parameters
    ----------
    metadata : dict
    """

    print("\n========== FILE INFORMATION ==========")
    print(f"Filename      : {metadata['filename']}")
    print(f"Extension     : {metadata['extension']}")
    print(f"Size          : {metadata['size_bytes']} bytes")
    print(f"SHA-256       : {metadata['sha256']}")
    print(f"Raw Byte Size : {len(metadata['raw_bytes'])} bytes")
    print("======================================\n")


if __name__ == "__main__":

    file_path = input("Enter file path: ")

    try:
        metadata = load_file(file_path)
        display_metadata(metadata)

    except Exception as error:
        print(f"\nError: {error}")