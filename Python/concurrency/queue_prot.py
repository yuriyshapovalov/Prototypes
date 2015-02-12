# queue - Synchronized queue class
import queue

def main():
    print("Queue object")

    q = queue.Queue()

    y = q.empty()
    print("queue.empty() = {}".format(y))

    y = q.full()
    print("queue.full() = {}".format(y))

    q.put('some text')
    print("queue.put('some text')")

    q.put_nowait(311)
    print("queue.put_nowait(311)")

    y = q.get()
    print("queue.get() = {}".format(y))

    y = q.get_nowait()
    print("queue.get_nowait() = {}".format(y))


if __name__ == '__main__':
    main()
