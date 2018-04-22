import blockchain

class Validate:
    def isValid(self,chain):
        for index in range(1,len(chain)):
            if(chain[index].previousHash != chain[index-1].hash):
                return "The Chain is polluted"
            else:
                return "The Chain is Perfect"