import hashlib
import datetime
class Block:
    def __init__(self,index, data, previousHash):
        self.sugar = 0
        self.level = 4
        self.index = index
        self.timestamp = datetime.datetime.now().timestamp()
        self.previousHash = previousHash
        self.data = data
        self.hash = self.mine()
        
    
    def calculateHash(self):
        myHash = hashlib.sha256()
        myHash.update((str(self.index) + str(self.timestamp)+str(self.previousHash) + str(self.data)+ str(self.sugar)).encode())
        return(myHash.hexdigest())

    def mine(self):
        minedHash =''
        print("Mining for Block %s......"%self.index)
        while(minedHash[0:self.level] != "0" * self.level):
            minedHash =self.calculateHash()
            self.sugar +=1
        return minedHash

class BlockChain:
    def __init__(self):
        self.chain = []
        self.CreateInitBlock()

    def CreateInitBlock(self):
        fHash = hashlib.sha256()
        fHash.update(b'firsthash')
        self.chain.append(Block(0,"Hello World!",fHash.hexdigest()))

    def CreateBlock(self,data):
        if(self.chain.append(Block(len(self.chain),data,self.chain[len(self.chain)-1].hash))):
            return True
        else:
            return False

    def ShowBlocks(self):
        for block in self.chain:
            print("Index:%d"%block.index)
            print("Hash:",block.hash)
            print("Previous Hash:", block.previousHash)
            print("Data:",block.data)
            print("======================================================")


