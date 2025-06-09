import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0 
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        raw = str(self.index) + str(self.timestamp) + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(raw.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"\n Mining Block {self.index}")
        target = '0' * difficulty
        start_time = time.time()
        attempts = 0

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        elapsed = time.time() - start_time
        print(f"Block {self.index} mined!")
        print(f"Attempts: {attempts}")
        print(f"Time: {elapsed:.2f} seconds")
        print(f"Final Hash: {self.hash}")

difficulty = 4
blockchain = []

genesis = Block(0, "First block - Genesis", "0")
genesis.mine_block(difficulty)
blockchain.append(genesis)

b1 = Block(1, "Some data in block 1", genesis.hash)
b1.mine_block(difficulty)
blockchain.append(b1)

b2 = Block(2, "Another set of data in block 2", b1.hash)
b2.mine_block(difficulty)
blockchain.append(b2)
