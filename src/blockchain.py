import hashlib
import datetime
class Block:
    def __init__(self,index, data, previousHash):
        self.index = index
        self.timestamp = datetime.datetime.now().timestamp()
        self.previousHash = previousHash
        self.data = data
        myHash = hashlib.sha256()
        myHash.update((str(self.index) + str(self.timestamp)+str(previousHash) + str(data)).encode())
        self.hash = myHash.hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.CreateInitBlock()

    def CreateInitBlock(self):
        fHash = hashlib.sha256()
        fHash.update(b'firsthash')
        self.chain.append(Block(0,"Hello World!",fHash.hexdigest()))

    def CreateBlock(self,data):
        self.chain.append(Block(len(self.chain),data,self.chain[len(self.chain)-1].hash))
    
