def find_peptide_lengths(rna_sequence):
    stop_codons = {'UAA', 'UAG', 'UGA'}

    peptide_lengths = []

    start = 0

    while start < len(rna_sequence) - 2:
        for i in range(start, len(rna_sequence) - 2, 3):
            codon = rna_sequence[i:i + 3]
            if codon in stop_codons:
                peptide_lengths.append(i - start)
                start = i + 3
                break

    print(' '.join(map(str, peptide_lengths)))

rna_sequence = input().strip()
find_peptide_lengths(rna_sequence)
