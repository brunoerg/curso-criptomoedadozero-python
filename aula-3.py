import hashlib
import time
import binascii

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce


class Blockchain:
    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)

    def getLatestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    def generateNextBlock(self, data):
        previousBlock = self.getLatestBlock()
        nextIndex = previousBlock.index + 1
        nextTimestamp = int(round(time.time() * 1000))
        nextPreviousHash = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTimestamp, data,
                         calculateHash(nextIndex, nextPreviousHash, nextTimestamp, data))
        if self.validatingBlock(newBlock) == True:
            self.__chain.append(newBlock)

    def validatingBlock(self, newBlock):
        previousBlock = self.getLatestBlock()
        if previousBlock.index + 1 != newBlock.index:
            return False
        elif previousBlock.hash != newBlock.previousHash:
            return False
        return True

    def hashMatchesDifficulty(self, hash, difficulty):
        hashBinary = binascii.unhexlify(hash)
        requiredPrefix = '0'*int(difficulty)
        return hashBinary.startswith(requiredPrefix)

    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = self.calculateHash(index, previousHash, timestamp, data, difficulty, nonce)
            if self.hashMatchesDifficulty(hash, difficulty):
                block = Block(index, previousHash, timestamp, data, difficulty, nonce)
                return block
            nonce = nonce + 1

def calculateHash(index, previousHash, timestamp, data, difficulty, nonce):
    return hashlib.sha256((str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).encode('utf-8')).hexdigest()
