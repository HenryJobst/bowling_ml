from bowling_rolls_transformations.tokenize import tokenize_seq
import pandas as pd


def transform_symbol(rolls):
    """
    Transform the rolls to scores based on the annotation of the symbols.
    Annotation of the symbols:
        "X" indicates a strike, "/" indicates a spare, "-" indicates a miss,
        and a number indicates the number of pins knocked down in the roll.

    For symbols:
        'X' -> 10
        '-' -> 0
        '/' -> '/' This will be kept the same to differentiate spare from strike.
    For numbers:
        Will transform the number in str to int.

    Parameters:
    -------
    rolls: list of str
        The rolls in a list that is retrieved from the console.

    Returns:
    -------
    rolls: list of str and int
        A list of transformed rolls.

    """
    for i in range(len(rolls)):
        # If it's 'X', it's strike. Set the score to 10.
        if rolls[i] == 'X':
            rolls[i] = 10
        # If it's '-', it's missed. Set the score to 0.
        elif rolls[i] == '-':
            rolls[i] = 0
        # If it's '/', it's spare, keep it for the record.
        elif rolls[i] == '/':
            rolls[i] = 10 - rolls[i - 1]
        else:
            rolls[i] = int(rolls[i])
    return rolls


def fill(seq):
    filled_seq = []
    for i in range(len(seq)):
        filled_seq.append(seq[i])
        if seq[i] == 10 and len(filled_seq) < 18 and len(filled_seq) % 2 != 0:
            filled_seq.append(0)

    seq = filled_seq

    for i in range(21-len(seq)):
        seq.append(0)

    return pd.Series(seq)


def convert(x):
    return fill(transform_symbol(tokenize_seq(x)))

