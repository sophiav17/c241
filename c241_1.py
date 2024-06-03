import hashlib
import json
from time import time

class Block:
	def __init__(self) :
		self.chain = []
		self.new_transactions = []
		self.count = 0
		self.new_block(previous_hash = "No previous hash . Since this is teh first block")

	def new_block(self, previous_hash = None) :
		block = {
		    'Block No' : self.count,
		    'timestamp' : time(),
		    'transactions' : self.new_transactions or 'No Transactions First Genesis Block',
		    'gasfee' : 0.1,
		    'previous_hash' : previous_hash,
		}
		self.count = self.count + 1
		self.chain.append(block)

		string_object = json.dumps(block)
		block_string = string_object.encode()

		raw_hash = hashlib.sha256(block_string)
		hex_hash = raw_hash.hexdigest()
		self.chain.append(("Current Hash: ", hex_hash))
		return block

blockchain = Block()

print(blockchain.chain)