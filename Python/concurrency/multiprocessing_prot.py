# Process-based parallelism
import multiprocessing as mp

class multiprocessingTest:
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

        print("\nSharing state between processes (Server Process) multithreading.Manager")

        with mp.Manager() as manager:
            d = manager.dict()
            l = manager.list(range(10))


            p = mp.Process(target=fnc5, args=(d, l))
            p.start()
            p.join()

            print(d)
            print(l)

        print("\nUsing a pool of workers")

        with mp.Pool(processes=4) as pool:
            result = pool.apply_async(fnc6, [10])
            print(result.get(timeout=1))
            print(pool.map(fnc6, range(10)))

        print("\nMultiprocessing Reference")
        print("- Process")

        p = mp.Process(target=fnc, args=("new proc",))
        print("multiprocessing.Process(target='func', args=('value')) = {}".format(p))

        p.start()
        print("process.start()")

        print("process.name = {}".format(p.name))

        print("process.is_alive() = {}".format(p.is_alive()))

        print("process.daemon = {}".format(p.daemon))
        
        print("process.exitcode = {}".format(p.exitcode))

        print("process.authkey = {}".format(p.authkey))

        print("process.sentinel = {}".format(p.sentinel))

        p.terminate()
        print("process.terminate()")

        print("\n-Pipes and Queues")

        pipe = mp.Pipe()

        print("queue.qsize() = {}".format(q.qsize()))

        q.put(['1', 43])
        print("queue.put(['1', 43])")

        q.put_nowait(['5', 'Sometext'])
        print("queue.put_nowait(['5', 'Sometext'])")

        print("queue.empty() = {}".format(q.empty()))
        print("queue.full() = {}".format(q.full()))

        print("queue.get() = {}".format(q.get()))
        print("queue.get_nowait() = {}".format(q.get_nowait()))

        print("\nMiscellaneous")

        print("multiprocessing.active_children() = {}".format(mp.active_children()))

        print("multiprocessing.cpu_count() = {}".format(mp.cpu_count()))

        print("multiprocessing.current_process() = {}".format(mp.current_process()))

        print("multiprocessing.freeze_support() = {}".format(mp.freeze_support()))


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

    def fnc5(d, l):
        d[1] = '1'
        d['2'] = 2
        d[0.25] = None
        l.reverse()

    def fnc6(x):
        return x**2

if __name__ == '__main__':
    multiprocessingTest().main()
