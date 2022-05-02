'''bloom.py defines a bloom filter which is an
approximate set membership data structure. You
will implement a full bloom filter in this module 
'''
import array
import binascii
import random

class Bloom(object):

	def __init__(self, m,k, seed=0):
		'''Creates a bloom filter of size m with k 
		   independent hash functions.
		'''

		self.array = array.array('B', [0] * m)
		self.hashes = self.generate_hashes(m,k,seed)


	#TODO
	def generate_hashes(self, m, k, seed):
		'''Generate *k* independent linear hash functions 
		   each with the range 0,...,m. 

		   m: the range of the hash functions
		   k: the number of hash functions
		   seed: a random seed that controls which A/B linear 
		   parameters are used.

		   The output of this function should be a list of functions
		'''
		random.seed(seed)

		#TODO

		raise ValueError('Not Implemented')
		


	def put(self, item):
		'''Add a string to the bloom filter, returns void
		'''
		#TODO

	def contains(self, item):
		'''Test to see if the bloom filter could possibly
		contain the string (true (possibly)), false (definitely).
		'''
		#TODO