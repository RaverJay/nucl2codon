#!/usr/bin/env python3
# nucl2codon - python rewrite of https://github.com/theosanderson/Codon2Nucleotide functionality
# SK

def nucl2codon(nucl_pos):
    '''Returns (gene name, codon number) for a nucleotide position on the SARS-CoV-2 genome - or (None, -1) if something goes wrong
    Logic from https://github.com/theosanderson/Codon2Nucleotide
    '''

    # make an int out it
    nucl_pos = int(nucl_pos)

    # fixed gene annotation (yoinked from Codon2Nucleotide, hopefully this is correct for the Wuhan reference)
    genes = {
    'ORF1a': [266, 13467],
    'ORF1b': [13468, 21556],
    'S': [21563, 25385],
    'ORF3a': [25393, 26221],
    'E': [26245, 26473],
    'M': [26523, 27192],
    'ORF6': [27202, 27388],
    'ORF7a': [27394, 27760],
    'ORF7b': [27756, 27888],
    'ORF8': [27894, 28260],
    'N': [28274, 29534],
    'ORF10': [29558, 29675]
    }

    matches = []
    for gene in genes:
        if genes[gene][0] <= nucl_pos <= genes[gene][1]:
            matches.append(gene)
    

    if len(matches) != 1:
        return (None, -1)

    gene = matches[0]
    codon = ((nucl_pos - genes[gene][0]) // 3) + 1
    
    return gene, codon
    
