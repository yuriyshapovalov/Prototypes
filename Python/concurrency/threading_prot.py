# Threading for concurrent exceution
import threading as th
import time

def main():
    print("Thread-based parallelism\n")

    y = th.active_count()
    print("threading.active_count() = {}".format(y))

    y = th.current_thread()
    print("threading.current_thread() = {}".format(y))

    y = th.get_ident
    print("threading.get_ident() = {}".format(y))

    y = th.enumerate()
    print("threading.enumerate() = {}".format(y))

    print("\nThread-local data")

    x = th.local()
    x.var = 1
    print("x.var = threading.local() = {} (local for thread)".format(x))

    print("\nThread object")
    
    print("z = threading.Thread(target = func)")
    
    z = th.Thread(target = fn_thread)
    print("z.start()")
    z.start()
    print("z.name = {}".format(z.name))

    z.setName("MySimpleThread")
    print("z.SetName('MySimpleThread')")

    y = z.getName()
    print("z.GetName() = {}".format(y))

    print("z.ident = {}".format(z.ident))

    print("z.is_alive() = {}".format(z.is_alive()))

    print("z.daemon = {}".format(z.daemon))

    z.join()
    print("Thread finished")

    print("\nLock Object")

def fn_thread():
    print("\tFrom thread ... ")
    for i in range(1, 4):
        print("\t{}".format(i))
        time.sleep(1)

if __name__ == '__main__':
    main()
