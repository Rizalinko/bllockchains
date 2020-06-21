from time import time
import json
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(proof = 100, previous_hash=1)

    def new_block(self, proof, previous_hash = None):
        # Create a block
        block = {'index': len(self.chain)+1, 'timestamp': time(), 'transactions': self.current_transactions,
                 'proof': proof, 'previous hash': previous_hash}

        # Reset transactions
        self.current_transactions = []

        self.chain.append(block)
        return block


    def new_transaction(self, sender, reciever, amount):
        # Creates a new transaction and adds it the block
        self.current_transactions.append({'sender': sender, 'reciever': reciever, 'amount':amount})
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # create hash to link blocks

        # The keys of the dictionary must be sorted, or else the hashes will be inconsistent
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]