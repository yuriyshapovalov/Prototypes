# Process-based parallelism
import multiprocessing as mp

def main():
    print("Multiprocessing (process-based parallelism)")
    
    print("\nCreating process using multiprocessing.Process")
    p = mp.Process(target=fnc, args=('first',))
    print("multiprocessing.Process(target='func', args=()) = {}".format(p))
    p.start()
    p.join()

    print("\nUsing multiprocessing.Queue to communicate between processes")
    q = mp.Queue()
    p = mp.Process(target=fnc1, args=(q, 'second'))
    print("multiprocessing.Queue() = {}".format(q))
    p.start()
    print(q.get())
    p.join()

    print("\nUsing multithreading.Pipe to communicate between precesses")
    parent_conn, child_conn = mp.Pipe()
    p1 = mp.Process(target=fnc2, args=(child_conn, 'third'))
    p1.start()
    print(parent_conn.recv())
    p1.join()

    print("\nMultithreading.Lock for processes synchronization")
    lock = mp.Lock()

    for i in range(0, 10):
        mp.Process(target=fnc3, args=(lock, i)).start()

    print("\nSharing state between processes (Shared Memory) multithreading.Value/Array")
    num = mp.Value('d', 0.0)
    arr = mp.Array('i', range(10))

    p = mp.Process(target=fnc4, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

    print("\nSharing state between processes (Server Process) multithreading.Process/Manager")

def fnc(name):
    print("\tprocess - ", name)

def fnc1(q, name):
    q.put([42, None, 'Hello'])
    print("\tprocess - ", name)

def fnc2(conn, name):
    conn.send([23, 'Some data'])
    print('\tprocess - ', name)

def fnc3(l, i):
    l.acquire()
    print("\tlock process - {}".format(i))
    l.release()

def fnc4(n, a):
    n.value = 3.1415926535898
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    main()
