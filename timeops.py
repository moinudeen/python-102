import time
 
#----------------------------------------------------------------------
def fast():
    """"""
    print("I run fast!")
 
#----------------------------------------------------------------------
def slow():
    """"""
    time.sleep(2)
    print("I run slow!")
 
#----------------------------------------------------------------------
def medium():
    """"""
    time.sleep(0.5)
    print("I run a little slowly...")
 
#----------------------------------------------------------------------
def main():
    """"""
    fast()
    slow()
    medium()
    for i in range(5):
        medium()
 
if __name__ == '__main__':
    main()
