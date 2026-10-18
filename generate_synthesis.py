from modules.binary_convertor import bytes_to_binary
from modules.dna_encoder import binary_to_dna
from modules.dna_decoder import dna_to_binary
from modules.binary_convertor import binary_to_bytes
from modules.analyser import analyse_dna, display_analysis


# The exact message we want to store in physical DNA
message = "HELIXVAULT"

# Convert message to bytes
raw_bytes = message.encode("utf-8")

# Bytes → Binary
binary = bytes_to_binary(raw_bytes)

# Binary → DNA
dna_sequence = binary_to_dna(binary)
analysis = analyse_dna(dna_sequence)

print("\n========== HELIXVAULT SYNTHESIS ==========")
print("Message       :", message)
print("DNA Length    :", len(dna_sequence), "bases")
print("DNA Sequence  :", dna_sequence)

# Verify DNA → Binary → Bytes → Text
recovered_binary = dna_to_binary(dna_sequence)
recovered_bytes = binary_to_bytes(recovered_binary)
recovered_message = recovered_bytes.decode("utf-8")

print("\nRecovered     :", recovered_message)
print("Verification  :", message == recovered_message)

# Save sequence
with open("output/helixvault_synthesis.txt", "w") as file:
    file.write(dna_sequence)

print("\nSequence saved to:")
print("output/helixvault_synthesis.txt")
print("===========================================\n")

display_analysis(analysis)