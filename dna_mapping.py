"""
===========================================================
Module : DNA Mapping
Project: AI-Assisted DNA Data Archival System

Description:
------------
Contains the DNA encoding and decoding mappings used
throughout the project.

Author: Hari
===========================================================
"""

# ----------------------------------------------------------
# Binary -> DNA Mapping
# ----------------------------------------------------------

DNA_MAPPING = {
    "00": "A",
    "01": "C",
    "10": "G",
    "11": "T"
}

# ----------------------------------------------------------
# DNA -> Binary Mapping
# ----------------------------------------------------------

REVERSE_DNA_MAPPING = {
    value: key for key, value in DNA_MAPPING.items()
}