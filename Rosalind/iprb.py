# Mendel's First Law
# http://rosalind.info/problems/iprb/
import sys
import unittest

class iprb:
	def main(self, hom_dom, het, hom_rec):

		total = hom_dom + het + hom_rec

		p_hom_dom = hom_dom / total
		p_het = het / total
		p_hom_rec = hom_rec / total

		prob = 1
		prob -= p_hom_rec * ((hom_rec-1)/(total-1))
		prob -= 2 * p_hom_rec * (het / (total - 1) * 0.5)
		prob -= p_het * ((het - 1) / (total-1)) * 0.25
		return prob

class Test(unittest.TestCase):
	def setUp(self):
		self.hom_dom = 2
		self.het = 2
		self.hom_dom = 2
		self.result = 0.78333

	def test_mendel_first_law(self):
		self.assertAlmostEqual(
			self.result,
			self.iprb().main(self.hom_dom, het, hom_rec),
			places=5)

if __name__ == '__main__':
	hom_dom = int(sys.argv[1])
	het = int(sys.argv[2])
	hom_rec = int(sys.argv[3])
	if hom_dom == 0 or het == 0 or hom_rec == 0:
		raise Exception("ERROR: Incorrect parameters")
	result = iprb().main(hom_dom, het, hom_rec)
	print(result)