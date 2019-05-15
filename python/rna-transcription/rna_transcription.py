def to_rna(dna_strand):

    rna_compl = {
       'G':'C',
       'C':'G',
       'T':'A',
       'A':'U' }

    rna_transcript = ""
    
    try:
        for nucleotide in dna_strand:
            rna_transcript += rna_compl[nucleotide]
    except KeyError:
        raise ValueError("Invalid input")

    return rna_transcript
