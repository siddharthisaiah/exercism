from textwrap import wrap

def proteins(strand):
    codon_map = {'AUG' : 'Methionine', 'UUU' : 'Phenylalanine', 'UUC': 'Phenylalanine',
                 'UUA' : 'Leucine', 'UUG' : 'Leucine', 'UCU' : 'Serine', 'UCC' : 'Serine',
                 'UCA' : 'Serine', 'UCG' : 'Serine', 'UAU' : 'Tyrosine', 'UAC' : 'Tyrosine',
                 'UGU' : 'Cysteine', 'UGC' : 'Cysteine', 'UGG' : 'Tryptophan', 'UAA' : 'stop',
                 'UAG' : 'stop', 'UGA' : 'stop' }

    strand = wrap(strand, 3)

    trans = []
    for codon in strand:
        if codon_map[codon] == 'stop':
            break
        trans.append(codon_map[codon])
    return trans


