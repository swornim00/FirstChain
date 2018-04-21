import blockchain

class Validate:
    def isValid(self,chain):
        for index in range(1,len(chain)-1):
            if(chain[index+1] != chain[index]):
                return "The Chain is polluted"
    
        return "The Chain is Perfect"