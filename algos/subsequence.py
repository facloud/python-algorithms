"""Checks if subseq is a subsequence of seq."""


def is_subsequence(seq, subseq):
    if len(subseq) == 0:
        return True
    if len(seq) < len(subseq):
        return False

    in_subseq = False
    subseq_starts = -1
    j = 0
    for i in range(0, len(seq)):
        if seq[i] == subseq[0]:
            subseq_starts = i
            in_subseq = True

        if in_subseq:
            if seq[i] != subseq[j]:
                return is_subsequence(seq[subseq_starts+1:], subseq)
            j += 1
            if j == len(subseq):
                return True

    return False
