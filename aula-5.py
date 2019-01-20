import hashlib
import binascii

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

def idTransaction(transaction):
    inputContents = ""
    outputContents = ""
    for inpt in transaction.inputs:
        inputContents += (inpt.outputId + inpt.outputIndex)
    for output in transaction.outputs:
        outputContents += (output.address + output.amount)
    return hashlib.sha256((str(inputContents) + str(outputContents)).encode('utf-8')).hexdigest()
