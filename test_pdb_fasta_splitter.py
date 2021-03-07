#!/usr/bin/env python3
# test_pdb_fasta_splitter.py

import pytest
from pdb_fasta_splitter import get_fh, _check_size_of_lists, get_header_and_sequence_lists

header = ["E", "F", "G"]
sequence = ["AGCT", "TGCG", "ACTTT"]

def test_get_fh_4_IOError():
    """
    Tests if get_fh raises IOError
    """
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")

def test_get_gh_4_ValueError():
    """
    Tests if get_fh raises ValueError
    """
    with pytest.raises(ValueError):
        get_fh("does_not_exist.txt", ."rr")


def test__check_size_of_lists():
    """
    Tests if _check_size_of_lists works correctly
    """
    assert _check_size_of_lists(header, sequence) == True
    assert _check_size_of_lists(header[1:3], sequence) == True, "Problem on test__check_size_of_lists"

def test_get_header_and_sequence_lists():
    """
    Tests if get_header_and_sequence_lists works correctly
    """
    assert 
