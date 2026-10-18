"""
=========================================================
HeliXVault Mapping Optimizer
Finds the best Binary -> DNA mapping
=========================================================
"""

from itertools import permutations

message = "HELIXVAULT"

# Convert to binary
binary = "".join(format(ord(c), "08b") for c in message)

bases = ["A", "C", "G", "T"]

best_score = None
best_mapping = None
best_sequence = None


def analyse(sequence):

    length = len(sequence)

    gc = (sequence.count("G") + sequence.count("C")) / length * 100

    longest = 1
    current = 1

    for i in range(1, length):
        if sequence[i] == sequence[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return gc, longest


for perm in permutations(bases):

    mapping = {
        "00": perm[0],
        "01": perm[1],
        "10": perm[2],
        "11": perm[3]
    }

    dna = ""

    for i in range(0, len(binary), 2):
        dna += mapping[binary[i:i + 2]]

    gc, longest = analyse(dna)

    score = abs(gc - 50) + longest * 5

    if best_score is None or score < best_score:

        best_score = score
        best_mapping = mapping
        best_sequence = dna

print("\n========== BEST RESULT ==========\n")

print("Mapping")

for k, v in best_mapping.items():
    print(f"{k} -> {v}")

gc, longest = analyse(best_sequence)

print("\nDNA")

print(best_sequence)

print("\nLength:", len(best_sequence))
print("GC % :", round(gc, 2))
print("Longest Homopolymer:", longest)

print("\nScore:", round(best_score, 2))