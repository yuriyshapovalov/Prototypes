# Heap queue algorithm
import heapq as hq

def main():
    a = [1,2,3,4,5,6,7,8]

    hq.heapify(a)
    print("heapq.heapify({})".format(a))

    hq.heappush(a, 9)
    print("heapq.heappush('heap', 9) = {}".format(a))

    hq.heappop(a)
    print("heapq.heappop('heap') = {}".format(a))

    y = hq.heappushpop(a, 16)
    print("heapq.heappushpop('heap', 16) = ({}), {}".format(y, a))

    y = hq.heapreplace(a, 1)
    print("heapq.heapreplace('heap', 1) = ({}), {}".format(y, a))

    y = hq.nlargest(2, enumerate(a))
    print("heapq.nlargest(2, 'heap') = {}".format(y))

    y = hq.nsmallest(2, a)
    print("heapq.nsmallest(2, 'heap') = {}".format(y))
   
    y = hq.merge(a, [94, 34,12,56,83])
    print("heapq.merge('heap', [94, 34,12,56,83]) = {}".format(y))

if __name__ == '__main__':
    main()
