import sys 
sys.setrecursionlimit(12000)

n = 0 

def python():
    global n
    
    n = n + 1
    
    print("Python", n)
    python()

python()