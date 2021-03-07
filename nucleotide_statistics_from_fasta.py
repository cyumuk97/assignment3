#!/usr/bin/env python3
# nucleotide_statistics_from_fasta.py


import sys
import argparse

def get_fh(filename, openfile):
    """
    Opens the file and passes back a file object
    """
    try:
        newfile = open(filename, openfile)
    
    except ValueError as val:
        if len(openfile) > 1:
            print("Wrong argument is passed", val)

    except IOError as io:
        print("File cannot be opened", io)

    newfile.close()

    return newfile

def _check_size_of_lists(header, sequence):
    """
    Compares the sizes of two lists
    """
    if len(sequence) != len(head):
        sys.exit("The size of the sequence list is not equal to that of the header list")

    else:
        return True

def get_header_and_sequence_lists(filehandle):
    """
    Returns two lists: one for sequences and one for headers
    """
    sequence = []
    header = []

    for line in filehandle:
        if re.match('^>', line):
            header.append(line)
        sequence.append(line)

    _check_size_of_lists(header, sequence)
    return sequence, header

def _get_nt_occurrence(character, sequence):
    """
    Calculates the occurrence of a nucleotide in a sequence
    """
    count = 0
    if character in "AGCTN":
        for i, seq in enumerate(sequence):
            if seq == character:
                count += 1

    else:
       sys.exit("Did not code this condition")

    return count

def _get_accession(header):
    """
    Returns the accession number
    """
    return header[1:10]

def print_sequence_stats(header, sequence, filehandle):
    """
    Prints the top line of the output and each sequence's numerical values
    """
    number = 0
    accession = _get_accession(header)
    A = _get_nt_occurrence('A', sequence)
    G = _get_nt_occurrence('G', sequence)
    C = _get_nt_occurrence('C', sequence)
    T = _get_nt_occurrence('T', sequence)
    N = _get_nt_occurrence('N', sequence)
    length = len(sequence)
    GC = (G + C) / length
    
    print(f'Number'\t'Accession'\t"A's"\t"G's"\t"C's"\t"T's"\t"N's"\t'Length'\t'GC%')

    print('\n')
    print(f'{number}\t{accession}\t{A}\t{G}\t{C}\t{T}\t{N}\t{length}\t{GC.1f}')
 
def get_cli_args():
    """
    Gets command line options using argparse
    """
    parser = argparse.ArgumentParser(
            description = 'Give the fasta sequence file name to get the nucleotide statistics')

    parser.add_argument('-i', '--infile',
                        dest = 'INFILE',
                        type = str
                        help = 'Path to the file to open'
                        required = True)

    parser.add_argument('-o', '--outfile',
                        dest = 'OUTFILE',
                        type = str
                        help = 'Path to the file to write'
                        required = True)

    return parser.parse_args()