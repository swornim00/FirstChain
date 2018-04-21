import blockchain,validate

Chain = blockchain.BlockChain()

Chain.CreateBlock("This is another Chain")

for block in Chain.chain:
    print("Index:%d"%block.index)
    print("Hash:",block.hash)
    print("Previous Hash:", block.previousHash)
    print("Data:",block.data)
    print("======================================================")

validate = validate.Validate()
print(validate.isValid(Chain.chain))