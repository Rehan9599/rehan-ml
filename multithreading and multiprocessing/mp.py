import multiprocessing
import time



def numbers():
    for x in range(8):
        time.sleep(2)
        print(f"numbers:{x}")
        
        
def alphabets():
    for x in "abcdefg":
        time.sleep(2)
        print(f"alphabets:{x}")
        
if __name__ == '__main__':      
    t=time.time()
    p1=multiprocessing.Process(target=numbers)
    p2=multiprocessing.Process(target=alphabets)

    p1.start()
    p2.start()


    p1.join()
    p2.join()


    print(time.time()-t)