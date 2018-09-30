#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#from T2018_Practica1_Solution_Skeleton import *
from T2018_Practica1_Skeleton import *


class TestGenKey(unittest.TestCase):

    def test_basic_genkey_1(self):
        # toy example 1, no holes
        num_its = 10
        max_rails, num_holes, max_hole_pos = 3, 0, 0
        for _ in range(num_its):
            key = uoc_railfence_genkey(max_rails, num_holes, max_hole_pos)
            self.assertTrue(2 <= key[0] <= max_rails)

    def test_basic_genkey_2(self):
        # toy example 2, no holes
        num_its = 10
        max_rails, num_holes, max_hole_pos = 15, 0, 0
        for _ in range(num_its):
            key = uoc_railfence_genkey(max_rails, num_holes, max_hole_pos)
            self.assertTrue(2 <= key[0] <= max_rails)

    def test_genkey_with_holes_1(self):
        # a single hole in the first column
        num_its = 10
        max_rails, num_holes, max_hole_pos = 10, 1, 1
        for _ in range(num_its):
            key = uoc_railfence_genkey(max_rails, num_holes, max_hole_pos)
            (num_rails, holes) = key
            self.assertTrue(2 <= num_rails <= max_rails)  # num rails
            self.assertEqual(len(holes), num_holes)  # num holes

            # check hole
            hole = holes[0]
            self.assertTrue(0 <= hole[0] <= num_rails)  # hole rail
            self.assertEqual(hole[1], 0)  # hole column

    def test_genkey_with_holes_2(self):
        # multiple holes
        num_its = 10
        max_rails, num_holes, max_hole_pos = 10, 15, 10
        for _ in range(num_its):
            key = uoc_railfence_genkey(max_rails, num_holes, max_hole_pos)
            (num_rails, holes) = key
            self.assertTrue(2 <= num_rails <= max_rails)  # num rails
            self.assertEqual(len(holes), num_holes)  # num holes

            for hole in holes:
                self.assertTrue(0 <= hole[0] <= num_rails)  # hole rail
                self.assertTrue(0 <= hole[1] <= max_hole_pos)  # hole column

            # no duplicate holes
            for i in range(len(holes)-1):
                self.assertFalse(holes[i] in holes[i+1:])


class TestEncryption(unittest.TestCase):

    def test_basic_encryption_1(self):
        # toy example
        k = (3, [])
        p = 'CRYPTOGRAPHY'
        c = 'CTARPORPYYGH'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_basic_encryption_2(self):
        # longer toy example
        k = (8, [])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATION'
        c = 'CTSEMRSHDUUSMUYIENDQFONPYPAYIOCITHREONRECOPACFHSRANGACITCEUTORTECI'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_basic_encryption_3(self):
        # last letter in the lowest rail
        k = (8, [])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATI'
        c = 'CTSEMRSHDUUSMUYIENDQFONPYPAYIOCITHREONRECOPACFHSRAGACITCEUTRTECI'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_basic_encryption_4(self):
        # last letter in the highest rail
        k = (8, [])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMM'
        c = 'CTSEMRSHDUUSMYIENDQFOPYPAYIOCTHREONREOPACFHSRGACITCEURTEC'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_basic_encryption_5(self):
        # no complete cycle
        k = (8, [])
        p = 'CRYPTO'
        c = 'CRYPTO'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_basic_encryption_6(self):
        # mixing lower and upper case letters
        k = (5, [])
        p = 'CryptographyIsThePracticeAndStudy'
        c = 'CaeeyrrphPcAdyghTrinupoysatdttIcS'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_basic_encryption_7(self):
        # now with spaces and punctuation signs
        k = (5, [])
        p = 'Cryptography is the practice and study of techniques for secure communication!'
        c = 'Catt fq carrp hcidso iurs octyghseacnt tneoeemiipoyi reauyehsfcrmno!t p dc uun'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_encryption_with_holes_1(self):
        # holes do not overlap with text
        k = (3, [(0, 1), (0, 2), (0, 3), (1, 0), (1, 6), (2, 9)])
        p = 'CRYPTOGRAPHY'
        c = 'CTARPORPYYGH'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_encryption_with_holes_2(self):
        # one hole overlaps with text
        k = (3, [(0, 4)])
        p = 'CRYPTOGRAPHY'
        c = 'CRYRPTGAHYOP'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_encryption_with_holes_3(self):
        # two holes overlaps with text
        k = (3, [(0, 4), (0, 4)])
        p = 'CRYPTOGRAPHY'
        c = 'CRYRPTGAHYOP'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_encryption_with_holes_4(self):
        # long example with holes 1
        k = (5, [(3, 13), (0, 33), (1, 20), (2, 19), (2, 12), (3, 4), (2, 22), (3, 30), (0, 5), (2, 30), (0, 4),
                 (4, 12), (1, 1), (2, 27), (3, 28), (4, 19), (0, 25), (3, 2), (0, 11), (4, 28)])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATION'
        c = 'CRSCNTEUNGAITATADFEUSCRUINROPYHISOCQFEEMCOYTHERCEUYHIOSCMAIPPDNROT'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_encryption_with_holes_5(self):
        # long example with holes 2
        k = (2, [(0, 21), (0, 15), (1, 1), (0, 17), (1, 3), (0, 19), (1, 9), (0, 10), (0, 25), (1, 11), (1, 20),
                 (0, 4), (0, 31), (0, 12), (0, 28), (0, 3), (0, 6), (1, 30), (1, 32), (0, 5)])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATI'
        c = 'CRTGAHITERTCADUYFEHIUSOSCRCMUIAIYPORPYSHPACIENSDOTCNQEFREUEOMNCT'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)

    def test_encryption_with_holes_6(self):
        # now with spaces and punctuation signs
        k = (6, [(5, 26), (5, 5), (0, 26), (2, 29), (1, 17), (1, 33), (3, 21), (4, 18), (5, 30), (3, 29), (2, 6),
                 (0, 20), (3, 3), (4, 9), (4, 8), (1, 7), (3, 13), (4, 27), (2, 13), (5, 18)])
        p = 'Cryptography is the practice and study of techniques for secure communication!'
        c = 'Cacdn mnrrpthieuyhirsomo!ygh et t cqoecuios casoeufc ntptyipan fte ueia rd src'
        self.assertEqual(uoc_railfence_encrypt(p, k), c)


class TestDecryption(unittest.TestCase):

    def test_basic_decryption_1(self):
        # toy example
        k = (3, [])
        p = 'CRYPTOGRAPHY'
        c = 'CTARPORPYYGH'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_basic_decryption_2(self):
        # longer toy example
        k = (8, [])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATION'
        c = 'CTSEMRSHDUUSMUYIENDQFONPYPAYIOCITHREONRECOPACFHSRANGACITCEUTORTECI'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_basic_decryption_3(self):
        # last letter in the lowest rail
        k = (8, [])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATI'
        c = 'CTSEMRSHDUUSMUYIENDQFONPYPAYIOCITHREONRECOPACFHSRAGACITCEUTRTECI'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_basic_decryption_4(self):
        # last letter in the highest rail
        k = (8, [])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMM'
        c = 'CTSEMRSHDUUSMYIENDQFOPYPAYIOCTHREONREOPACFHSRGACITCEURTEC'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_basic_decryption_5(self):
        # no complete cycle
        k = (8, [])
        p = 'CRYPTO'
        c = 'CRYPTO'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_basic_decryption_6(self):
        # mixing lower and upper case letters
        k = (5, [])
        p = 'CryptographyIsThePracticeAndStudy'
        c = 'CaeeyrrphPcAdyghTrinupoysatdttIcS'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_basic_decryption_7(self):
        # now with spaces and punctuation signs
        k = (5, [])
        p = 'Cryptography is the practice and study of techniques for secure communication!'
        c = 'Catt fq carrp hcidso iurs octyghseacnt tneoeemiipoyi reauyehsfcrmno!t p dc uun'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_decryption_with_holes_1(self):
        # holes do not overlap with text
        k = (3, [(0, 1), (0, 2), (0, 3), (1, 0), (1, 6), (2, 9)])
        p = 'CRYPTOGRAPHY'
        c = 'CTARPORPYYGH'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_decryption_with_holes_2(self):
        # one hole overlaps with text
        k = (3, [(0, 4)])
        p = 'CRYPTOGRAPHY'
        c = 'CRYRPTGAHYOP'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_decryption_with_holes_3(self):
        # two holes overlaps with text
        k = (3, [(0, 4), (0, 4)])
        p = 'CRYPTOGRAPHY'
        c = 'CRYRPTGAHYOP'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_decryption_with_holes_4(self):
        # long example with holes 1
        k = (5, [(3, 13), (0, 33), (1, 20), (2, 19), (2, 12), (3, 4), (2, 22), (3, 30), (0, 5), (2, 30), (0, 4),
                 (4, 12), (1, 1), (2, 27), (3, 28), (4, 19), (0, 25), (3, 2), (0, 11), (4, 28)])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATION'
        c = 'CRSCNTEUNGAITATADFEUSCRUINROPYHISOCQFEEMCOYTHERCEUYHIOSCMAIPPDNROT'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_decryption_with_holes_5(self):
        # long example with holes 2
        k = (2, [(0, 21), (0, 15), (1, 1), (0, 17), (1, 3), (0, 19), (1, 9), (0, 10), (0, 25), (1, 11), (1, 20),
                 (0, 4), (0, 31), (0, 12), (0, 28), (0, 3), (0, 6), (1, 30), (1, 32), (0, 5)])
        p = 'CRYPTOGRAPHYISTHEPRACTICEANDSUDYOFTECHNIQUESFORSECURECOMMUNICATI'
        c = 'CRTGAHITERTCADUYFEHIUSOSCRCMUIAIYPORPYSHPACIENSDOTCNQEFREUEOMNCT'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)

    def test_decryption_with_holes_6(self):
        # now with spaces and punctuation signs
        k = (6, [(5, 26), (5, 5), (0, 26), (2, 29), (1, 17), (1, 33), (3, 21), (4, 18), (5, 30), (3, 29), (2, 6),
                 (0, 20), (3, 3), (4, 9), (4, 8), (1, 7), (3, 13), (4, 27), (2, 13), (5, 18)])
        p = 'Cryptography is the practice and study of techniques for secure communication!'
        c = 'Cacdn mnrrpthieuyhirsomo!ygh et t cqoecuios casoeufc ntptyipan fte ueia rd src'
        self.assertEqual(uoc_railfence_decrypt(c, k), p)


if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [TestGenKey, TestEncryption, TestDecryption]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)

