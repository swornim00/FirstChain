import blockchain,validate

Chain = blockchain.BlockChain()

Chain.CreateBlock("This is another Chain")

Chain.ShowBlocks()
validate = validate.Validate()
print(validate.isValid(Chain.chain))