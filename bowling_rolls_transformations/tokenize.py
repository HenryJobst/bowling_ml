from typing import List, Any


def tokenize_seq(seq):
    """
    To tokenize the sequence of rolls input from user to single letters.

    Returns:
    -------
    rolls: list
        A list of rolls in the sequence input by the users.
    """
    rolls: List[Any] = [roll for roll in seq]
    return rolls