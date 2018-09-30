#!/usr/bin/env python
# -*- coding: utf-8 -*-


# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
def move_on(info, num_rails):
    if info[0] == 0:
        info[2] = True
    if info[0] == (num_rails - 1):
        info[2] = False
    if info[2]:
        info[0] = info[0] + 1
    if not info[2]:
        info[0] = info[0] - 1
    info[1] = info[1] + 1
    return info

# --------------------------------------------------------------------------
from random import randint


def uoc_railfence_genkey(max_rails=10, num_holes=0, max_hole_pos=100):
    """
    Generates a random key for the modified rail fence cipher. A key is a two-element tuple:
    - the first element is an integer with the number of rails
    - the second element is a list of holes. Each hole is a tuple (rail number, column number)

    :param max_rails: optional parameter (defaults to 10), maximum number of rails.
    :param num_holes: optional parameter (detaults to 0), number of holes to include in the fence.
    :param max_hole_pos: optional parameter (defaults to 100), maximum column value for holes.
    :return:
    """

    key = (None, [])

    # --- IMPLEMENTATION GOES HERE ---
    num_rails = randint(2, max_rails)
    holes = []

    for i in range(num_holes):
        while True:
            rail = randint(0,(num_rails-1))
            column = randint(0,(max_hole_pos-1))
            tupla = (rail, column)
            if tupla not in holes:
                holes.append(tupla)
                break

    key = (num_rails, holes)
    # --------------------------------

    return key


def uoc_railfence_encrypt(message, key):
    """
    Ciphers the message with the key, using the modified rail fence cipher.

    :param message: string, message to cipher (may contain upper and lower case letters, spaces,
        and basic symbols (!, -, and _)
    :param key: rail fence cipher key, as returned by uoc_railfence_genkey
    :return: string, ciphered message
    """

    ciphertext = ''

    # --- IMPLEMENTATION GOES HERE ---
    num_rails = key[0]
    holes = key[1]
    # info[0] = actual_rail
    # info[1] = actual_col
    # info[2] = forward
    info = [0, 0, True]

    table = [[None for x in range(len(message) + len(holes))] for y in range(num_rails)]

    # Fill the holes in the table
    for hole in holes:
        table[hole[0]][hole[1]] = '*'

    for c in message:
        while (table[info[0]][info[1]] == '*'):
            info = move_on(info, num_rails)

        table[info[0]][info[1]] = c
        info = move_on(info, num_rails)

    for row in table:
        for letter in row:
            if letter != '*' and letter is not None:
                ciphertext += letter
    # --------------------------------
    return ciphertext

def uoc_railfence_decrypt(ciphertext, key):
    """
    Deciphers the ciphertext with the key, , using the modified rail fence cipher.
    :param ciphertext: string, message to decipher (may contain upper and lower case letters, spaces,
        and basic symbols (!, -, and _)
    :param key: rail fence cipher key, as returned by uoc_railfence_genkey
    :return: string, deciphered message
    """

    plaintext = ''

    # --- IMPLEMENTATION GOES HERE ---


    # --------------------------------

    return plaintext
