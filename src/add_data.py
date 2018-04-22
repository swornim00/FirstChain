import blockchain
import validate

def help():
    print("[+] 'input' for inputing the data")
    print("[+] 'list' for listing the blocks")

def inputBlock(chain):
    data_now = input("Enter you data here\n>")
    if(chain.CreateBlock(data_now)):
        print("The Block Successfully added!")
    
def listBlocks(chain):
    Chain.ShowBlocks()


Chain = blockchain.BlockChain()
validate = validate.Validate()

print("Welcome to BlockChain Based Records Keeping System\n")
print("Enter the command")
command = 'input'
while True:
    command = input("\n>")

    if command == 'input':
        inputBlock(Chain)
        print(validate.isValid(Chain.chain))
    elif command == 'list':
        listBlocks(Chain)
    elif command == 'exit':
        break
    else:
        help()

