#!/usr/bin/env python3
# pdb_fasta_splitter.py
"""
This script generates two files with protein sequence and secondary structures
"""
import sys
import re
import argparse


def get_fh(filename, openfile):
    """
    Opens the file and passes back a file object
    """
    try:
        newfile = open(filename, openfile)
        file1 = open("pdb_protein.fasta")
        file2 = open("odb_ss.fasta")
        newfile.close()

    except ValueError as val:
        if len(openfile) > 1:
            print("Wrong argument is passed", val)

    except IOError as error:
        print("File cannot be opened", error)

    return newfile, file1, file2


def _check_size_of_lists(header, sequence):
    """
    Compares the sizes of two lists
    """
    string = "The size of sequence list is not equal to that of header list"
    if len(sequence) != len(header):
        sys.exit(string)

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


def get_cli_args():
    """
    Gets command line options using argparse
    """
    parser = argparse.ArgumentParser(
        description='Give the fasta sequence file name to do the splitting')

    parser.add_argument('-i', '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to the file to open',
                        required=True)

    return parser.parse_args()
