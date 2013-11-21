# Threading for concurrent exceution
import threading as th

def main():
    
    y = th.active_count()
    print("threading.active_count() = {}".format(y))

    y = th.current_thread()
    print("threading.current_thread() = {}".format(y))

    y = th.get_ident
    print("threading.get_ident() = {}".format(y))

if __name__ == '__main__':
    main()
