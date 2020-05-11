from bitarray import bitarray
from pickle_hash import hash_code_hex
import pickle
import hashlib
import math


class BloomFilter():

    def __init__(self, total_items, false_positive_rate):
        ''' 
        below are the varibles that calculated using probability equations
         based on the input item size and false positive rate
         all calculation equations referenced from the University Texas
         as well as https://hur.st/bloomfilter/?n=4000&p=1.0E-1&m=&k= site
        '''
        self.false_positive_rate = false_positive_rate
        self.bitarray_size = self.calcualte_bitarray_size(
            total_items, false_positive_rate)
        self.hashes = self.calcualte_hashs(self.bitarray_size, total_items)
        self.bit_array = bitarray(self.bitarray_size)
        self.bit_array.setall(0)

    # calculte how many hashes will be apply to the new bloom filter
    #  base on the the input item sizes and the false positive rate

    def calcualte_hashs(self, bitarray_size, item_size):
        h = (bitarray_size/item_size) * math.log(2)
        return int(h)

    def calcualte_bitarray_size(self, items, false_positive_rate):
        m = -(items * math.log(false_positive_rate))/(math.log(2)**2)
        return int(m)

    def is_member(self, item):
        # print("is_member()'s key: ", item)

        # this is for midterm execution env input as bytes
        key = item  


        # this is for test_bloom_filter.py env input as string
        # key = item.encode()  

        
        for i in range(self.hashes):
            newKey = hashlib.md5(key).hexdigest()
            key_in_int = int(newKey, 16)
            positive = key_in_int % self.bitarray_size
            key = newKey.encode()
            if(self.bit_array[positive] == 0):
                return False
        return True

    def add(self, item):

        # key = item
        key = item.encode()
        # print("key: ", key)
        for i in range(self.hashes):
            newKey = hashlib.md5(key).hexdigest()
            # print("newKey: ", newKey)
            key_in_int = int(newKey, 16)
            positive = key_in_int % self.bitarray_size
            self.bit_array[positive] = 1
            key = newKey.encode()
