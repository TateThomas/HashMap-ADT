import sys
import time
from hashmap import HashMap


def weight_on(r, c):

    global calls, cache, cache_hits
    calls += 1

    if c > (r / 2):
        try:
            value = cache.get((r, r-c))
            cache_hits += 1
            return value
        except KeyError:
            return weight_on(r, r-c)

    try:
        value = cache.get((r, c))
        cache_hits += 1
        return value
    except KeyError:
        pass

    if c == 0:
        value = (weight_on(r-1, c) / 2) + 100
        cache.set((r, c), value)
        return value

    value = (weight_on(r-1, c-1) / 2) + (weight_on(r-1, c) / 2) + 200
    cache.set((r, c), value)
    return value


def main():
    global calls, cache, cache_hits
    start = time.perf_counter()
    rows = int(sys.argv[1])
    for row in range(rows):
        string = ""
        for column in range(row + 1):
            string += f"{weight_on(row, column):.2f} "
        print(string)
    end = time.perf_counter()
    duration = end - start
    print(f"\nElapsed time: {duration} seconds")
    print(f"Number of function calls: {calls}")
    print(f"Number of cache hits: {cache_hits}")


calls = 0
cache = HashMap((0, 0), 0.0)
cache_hits = 0


if __name__ == "__main__":
    main()
