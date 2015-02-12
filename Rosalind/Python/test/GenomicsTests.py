# Genomic tests

import genomics
import unittest

class TestGenomics(unittest.TestCase):
	dnaSeq = "acgttgtaccttac"

	def setUp(self):
		pass

	def countNucleobasesTest(self):
		result = genomic.countNucleobases(dnaSeq)
		self.assertEqual(result['A'], 3)
		self.assertEqual(result['C'], 4)
		self.assertEqual(result['G'], 2)
		self.assertEqual(result['T'], 5)
