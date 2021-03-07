#!/usr/bin/env python3
# test_nucleotide_statistics_from_fasta.py

import pytest
from nucleotide_statistics_from_fasta import _get_nt_occurrence, _get_accession, print_sequence_stats

sequence = "AGCTGCNCTAAATTGCGG"

def test__get_nt_occurrence():
    """
    Tests if _get_nt_occurrence works correctly
    """
    assert _get_nt_occurrence('A', sequence) == 2, "Problem on test__get_nt_occurrence"
    assert _get_nt_occurrence('A', sequence) == 4

def test__get_accession():
    """
    Tests if _get_accession works correctly
    """


def test_print_sequence_stats():
    """
    Tests if print_sequence_stats works correctly
    """

