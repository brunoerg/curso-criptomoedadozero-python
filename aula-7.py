from ecdsa import SigningKey, NIST384p

def createSigningKeys():
    return SigningKey.generate(curve=NIST384p)


def signingInput(transaction, inputIndex, listUnspentOutput, privateKey):
    inpt = transaction.inputs[inputIndex]
    data = transaction.id
    verifyingUtxo = findUnspentOutput(inpt.outputId, inpt.outputIndex, listUnspentOutput)
    refAddress = verifyingUtxo.address
    return privateKey.sign(data)

def validatingInputs(input, transaction, unspentOutputs):
    for utxo in unspentOutputs:
        if utxo.outputId == input.outputId and utxo.outputIndex == input.outputIndex:
            address = utxo.address
            key = address.get_verifying_key()
            return key.verify(input.signature, transaction.id)
    return False

def validatingTransactionId(id, transaction):
    return (transactionId(transaction) == id)
