from importlib.metadata import metadata
from unittest import result

from modules.file_reader import load_file, display_metadata
from modules.binary_convertor import (
    bytes_to_binary,
    binary_to_bytes,
    binary_statistics,
    display_binary_statistics
)
from modules.compressor import (
    compress_data,
    decompress_data,
    compression_statistics,
    display_compression_statistics
)
from modules.dna_encoder import (
    binary_to_dna,
    dna_statistics,
    display_dna_statistics
)
from modules.dna_decoder import (
    dna_to_binary,
    verify_conversion,
    decoder_statistics,
    display_decoder_statistics
)
from modules.verifier import (
    verify_data,
    display_verification
)

from scipy import stats

def main():

    metadata = load_file("sample_files/sample.txt")

    display_metadata(metadata)

    compressed = compress_data(metadata["raw_bytes"])

    stats = compression_statistics(
        metadata["raw_bytes"],
        compressed
    )

    display_compression_statistics(stats)

    decompressed = decompress_data(compressed)

    print(
        "Compression Verification:",
        decompressed == metadata["raw_bytes"]
    )

    binary = bytes_to_binary(compressed)

    dna = binary_to_dna(binary)

    recovered_binary = dna_to_binary(dna)

    decoder_stats = decoder_statistics(recovered_binary)

    display_decoder_statistics(decoder_stats)

    print(
        "DNA Decode Verification:",
        verify_conversion(binary, recovered_binary)
    )

    # DNA -> Binary
    recovered_binary = dna_to_binary(dna)

    # Binary -> Compressed Bytes
    recovered_compressed = binary_to_bytes(recovered_binary)

    # Compressed Bytes -> Original Bytes
    recovered_original = decompress_data(recovered_compressed)

    # Verify
    result = verify_data(
        metadata["raw_bytes"],
        recovered_original
    )

    display_verification(result)

    with open("output/dna_sequence.txt", "w") as file:
        file.write(dna)

    stats = dna_statistics(dna)

    display_dna_statistics(stats)

    binary_stats = binary_statistics(binary)

    display_binary_statistics(binary_stats)

    recovered = binary_to_bytes(binary)

    print(
        "Binary Verification:",
        recovered == compressed
    )


if __name__ == "__main__":
    main()