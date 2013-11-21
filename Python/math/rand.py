# random - Generate pseudo-random numbers
import random

def main():
    # Random
    print("Pseudo-random generators functions")
    random.seed()

    y = random.getrandbits(8)
    print("random.getrandbytes(8) = {}".format(y))

    y = random.randrange(0, 100)
    print("random.randrange(0, 100) = {}".format(y))

    y = random.randrange(0, 100, 5)
    print("random.randrange(0, 100, 5) = {}".format(y))

    y = random.randint(200, 300)
    print("random.randint(200, 300) = {}".format(y))

    a = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = random.choice(a)
    print("random.choice({}) = {}".format(a, y))

    random.shuffle(a)
    print("random.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) = {}".format(a))

    y = random.sample(a, 5)
    print("random.sample({}, 5) = {}".format(a, y))

    y = random.random()
    print("random.random() = {}".format(y))

    y = random.uniform(8, 16)
    print("random.uniform(8, 16) = {}".format(y))

if __name__ == '__main__':
    main()
