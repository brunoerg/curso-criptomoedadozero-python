import hashlib
import binascii
from ecdsa import SigningKey, NIST384p

class Transaction:
    def __init__(self):
        self.id = None
        self.inputs = None
        self.outputs = None

class Output:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Input:
    def __init__(self):
        self.outputId = None
        self.outputIndex = None
        self.signature = None


class UnspentOutput:
    def __init__(self, outputId, outputIndex, address, amount):
        self.outputId = outputId
        self.outputIndex = outputIndex
        self.address = address
        self.amount = amount

class UnspentOutputs:
    def __init__(self):
        self.__listUtxo = []

    def updateListUtxo(self, newList):
        self.__listUtxo = newList
    
    def newUnspentOutputs(self, transactions):
        utxoList = []
        for transaction in transactions:
            for inpt in transaction.inputs:
                utxo = UnspentOutput(transaction.id, inpt.outputId, inpt.outputIndex, inpt.address, inpt.amount)
                utxoList.append(utxo)
        self.updateListUtxo(utxoList)


def findUnspentOutput(outputId, outputIndex, listUnspentOutput):
    for unspentOutput in listUnspentOutput:
        if unspentOutput.outputId == outputId and unspentOutput.outputIndex == outputIndex:
            return True
    return False
    
def transactionId(transaction):
    inputContents = ""
    outputContents = ""
    for inpt in transaction.inputs:
        inputContents += (inpt.outputId + inpt.outputIndex)
    for output in transaction.outputs:
        outputContents += (output.address + output.amount)
    return hashlib.sha256((str(inputContents) + str(outputContents).encode('utf-8')).hexdigest()

                

        


