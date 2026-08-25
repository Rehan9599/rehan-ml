import threading
import time



def numbers():
    for x in range(8):
        time.sleep(2)
        print(f"numbers:{x}")
        
        
def alphabets():
    for x in "abcdefg":
        time.sleep(2)
        print(f"alphabets:{x}")
        
        
t=time.time()
t1=threading.Thread(target=numbers)
t2=threading.Thread(target=alphabets)

t1.start()
t2.start()


t1.join()
t2.join()


print(time.time()-t)