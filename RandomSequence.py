#!/usr/bin/env python3
import numpy as np


def get_random_binary(seq_size):
    seq = np.random.randint(2, size=seq_size)
    return seq


def get_random_binary_from_digits(nums_array, seq_size):
    seq = np.random.randint(1, 9, size=seq_size)
    for i in range(seq_size):
        if seq[i] in nums_array:
            seq[i] = 1
        else:
            seq[i] = 0
    return seq
