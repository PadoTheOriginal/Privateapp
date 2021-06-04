from encrypt import encryption

if __name__ == "__main__":
    from time import time
    from statistics import mean
    e = encryption()
    while True:
        Input = input("INPUT:")
        times = []
        for i in range(1, 10001):
            start = time()
            encrypted = e.encrypt(Input)
            end = time()
            times.append(end - start)
        
        print(mean(times))