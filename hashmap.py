'''
Author: Tate Thomas
CS 2420
Project 6: Dictionaries

HashMap Class:

    Specifically built for human pyramid lab.

    Methods:

    __init__(*args): Takes 0 or more key-value pairs, raises a KeyError if an odd number of arguments
        are passed.
    get(key): returns value if found, raises a KeyError otherwise.
    set(key, value): inserts a key-value pair into the HashMap.
    remove(key): removes an key-value pair out of the HashMap, ignores if not found.
    clear(): deletes all values and resets the HashMap to its original capacity.
    capacity(): returns the current capacity.
    size(): returns the current amount of key-value pairs in the HashMap.
    keys(): returns a list of the keys in the HashMap.
'''


class HashMap:
    '''HashMap Class:

    Methods:
    get(key)
    set(key, value)
    remove(key)
    clear()
    capacity()
    size()
    keys()
    '''


    _default_cap = 7


    def __init__(self, *args):
        '''Takes 0 or more key-value pairs for initialization'''

        self._table = []
        self._capacity = self._default_cap   # allocated space
        self._size = 0    # number of items
        self._load_factor = .8
        self.clear()

        if (len(args) % 2) == 0:
            i = 1
            while i < len(args):
                self.set(args[i-1], args[i])
                i += 2
        else:
            raise KeyError("Key given without definition.")


    def get(self, key):
        '''Returns the value associated with the given key, raises a KeyError if not found'''

        hash_val = self._hash(key)
        n = 1

        while self._table[hash_val][0] != key:
            if self._table[hash_val][0] is None:
                raise KeyError(f"{key} is not in dictionary")
            hash_val = self._hash(key, n)
            n += 1
        return self._table[hash_val][1]


    def set(self, key, value):
        '''Sets a key-value pair into the HashMap'''

        hash_val = self._hash(key)
        n = 1

        while not ((self._table[hash_val][0] is None) or (self._table[hash_val][0] is False)):
            hash_val = self._hash(key, n)
            n += 1

        self._table[hash_val][0] = key
        self._table[hash_val][1] = value
        self._size += 1

        if (self._size / self._capacity) >= self._load_factor:
            self._rehash()

        return self


    def remove(self, key):
        '''Removes a key-value pair if found, ignores otherwise'''

        try:
            value = self.get(key)
            val_index = self._table.index([key, value])
            self._table[val_index] = [False, None]
            self._size -= 1
        except KeyError:
            pass

        return self


    def clear(self):
        '''Resets the HashMap to its initial empty state'''

        self._table = []
        self._capacity = self._default_cap
        for _ in range(self._capacity):
            self._table.append([None, None])
        self._size = 0


    def capacity(self):
        '''Returns the current capacity'''

        return self._capacity


    def size(self):
        '''Returns the current size of the HashMap'''

        return self._size


    def keys(self):
        '''Returns a list of the keys currently in the HashMap'''

        key_list = []
        for pair in self._table:
            if pair[0] is not None:
                key_list.append(pair[0])
        return key_list


    def _hash(self, tup, n = 0):
        '''Hashes a tuple and returns the value'''

        return ((tup[0] * 3) + (tup[1] * 2) + (n * 19)) % self._capacity


    def _rehash(self):
        '''Resizes the HashMap by 2k-1, rehashes each value'''

        old_table = self._table
        self._table = []
        self._capacity = (self._capacity * 2) - 1
        self._size = 0

        for _ in range(self._capacity):
            self._table.append([None, None])

        for pair in old_table:
            if not pair[0] is None:
                self.set(pair[0], pair[1])


    def __str__(self):
        '''Returns a string representation of the HashMap'''

        string = "{"
        for pair in self._table:
            if not ((pair[0] is None) or (pair[0] is False)):
                string += f"{pair[0]}: {pair[1]}, "
        if len(string) > 1:
            string = string[:-2] + "}"
        else:
            string += "}"
        return string
