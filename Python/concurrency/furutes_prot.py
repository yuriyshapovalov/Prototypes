# concurrent.futures - Launch parallel tasks
import concurrent.futures as ft

def main():
    with ft.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(fnc, 323, 4)
        print(future.result())

        #future = executor.map(fnc, (33, 22))
        #print(future.result())

def fnc(x, y):
    return x**y

if __name__ == '__main__':
    main()
