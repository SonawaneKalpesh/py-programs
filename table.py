def printTable(n):
     for i in range(1, 11): # multiples from 1 to 10 
         print("%d * %d = %d" % (n, i, n * i)) 
if __name__ == "__main__": n = 10 
printTable(n)