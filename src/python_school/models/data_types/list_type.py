class list_type:
    def __init__(self, values=None):
        self.values = [] if values is None else list(values)

    def append(self, value):
        self.values.append(value)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

    def __delitem__(self, index):
        del self.values[index]

    def __iter__(self):
        return iter(self.values)

    def __repr__(self):
        return f"list({self.values})"

    def __str__(self):
        return str(self.values)
        
    def extend(self, iterable):
        self.values.extend(iterable)

    def insert(self, index, value):
        self.values.insert(index, value)

    def remove(self, value):
        self.values.remove(value)

    def pop(self, index=-1):
        return self.values.pop(index)

    def clear(self):
        self.values.clear()

    def index(self, value, start=0, end=None):
        return self.values.index(value, start, end if end is not None else len(self.values))

    def count(self, value):
        return self.values.count(value)

    def sort(self, key=None, reverse=False):
        self.values.sort(key=key, reverse=reverse)

    def reverse(self):
        self.values.reverse()

    def copy(self):
        return list_type(self.values.copy())

    def __add__(self, other):
        if isinstance(other, list_type):
            return list_type(self.values + other.values)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return list_type(self.values * n)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __contains__(self, value):
        return value in self.values

    def __eq__(self, other):
        if isinstance(other, list_type):
            return self.values == other.values
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, list_type):
            return self.values != other.values
        return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, list_type):
            return self.values < other.values
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, list_type):
            return self.values <= other.values
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, list_type):
            return self.values > other.values
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, list_type):
            return self.values >= other.values
        return NotImplemented
        
    def __iadd__(self, other):
        if isinstance(other, list_type):
            self.values += other.values
            return self
        return NotImplemented

    def __imul__(self, n):
        if isinstance(n, int):
            self.values *= n
            return self
        return NotImplemented
        
    def __hash__(self):
        return hash(tuple(self.values))
        
    @classmethod
    def from_tuple(cls, data_tuple):
        return cls(list_type(data_tuple))

    @classmethod
    def from_set(cls, data_set):
        return cls(list_type(data_set))

    @classmethod
    def from_dict_keys(cls, data_dict):
        return cls(list_type(data_dict.keys()))

    @classmethod
    def from_dict_values(cls, data_dict):
        return cls(list_type(data_dict.values()))

    @classmethod
    def from_dict_items(cls, data_dict):
        return cls([item for item in data_dict.items()])

    def to_tuple(self):
        return tuple(self.values)

    def to_set(self):
        return set(self.values)

    def to_dict(self):
        # This conversion is ambiguous for a general list,
        # but if the list contains (key, value) pairs, it can work.
        # We'll assume it's a list of 2-element iterables.
        try:
            return dict(self.values)
        except TypeError:
            raise TypeError("Cannot convert list to dictionary unless elements are (key, value) pairs.")

    def filter(self, func):
        return list_type(filter(func, self.values))

    def map(self, func):
        return list_type(map(func, self.values))

    def reduce(self, func, initializer=None):
        from functools import reduce
        if initializer is None:
            return reduce(func, self.values)
        else:
            return reduce(func, self.values, initializer)

    def all(self):
        return all(self.values)

    def any(self):
        return any(self.values)

    def min(self):
        return min(self.values)

    def max(self):
        return max(self.values)

    def sum(self):
        return sum(self.values)

    def average(self):
        if not self.values:
            raise ValueError("Cannot calculate average of an empty list")
        return sum(self.values) / len(self.values)
    def find_all(self, value):
        return list_type([i for i, x in enumerate(self.values) if x == value])

    def count_if(self, func):
        return sum(1 for x in self.values if func(x))

    def group_by(self, key_func):
        from collections import defaultdict
        grouped = defaultdict(list_type)
        for item in self.values:
            grouped[key_func(item)].append(item)
        return dict(grouped)

    def flatten(self):
        # Flattens a list of lists into a single list
        flattened = []
        for item in self.values:
            if isinstance(item, (list_type, list_type)): # Check for both built-in list and custom list
                flattened.extend(item)
            else:
                flattened.append(item)
        return list_type(flattened)

    def unique(self):
        seen = set()
        result = []
        for item in self.values:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return list_type(result)

    def chunk(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Chunk size must be a positive integer")
        return list_type([list_type(self.values[i:i + size]) for i in range(0, len(self.values), size)])

    def prepend(self, value):
        self.values.insert(0, value)

    def get(self, index, default=None):
        try:
            return self.values[index]
        except IndexError:
            return default

    def swap(self, index1, index2):
        if 0 <= index1 < len(self.values) and 0 <= index2 < len(self.values):
            self.values[index1], self.values[index2] = self.values[index2], self.values[index1]
        else:
            raise IndexError("List index out of range")

    def sample(self, k=1):
        import random
        return list_type(random.sample(self.values, k))
    
    def shuffle(self):
        import random
        random.shuffle(self.values)

    def rotate(self, n=1):
        if not self.values:
            return
        n = n % len(self.values)
        self.values = self.values[-n:] + self.values[:-n]

    def split_at(self, index):
        if not 0 <= index <= len(self.values):
            raise IndexError("Split index out of range")
        return list_type(self.values[:index]), list_type(self.values[index:])

    def is_empty(self):
        return len(self.values) == 0

    def first(self, default=None):
        return self.values[0] if self.values else default

    def last(self, default=None):
        return self.values[-1] if self.values else default

    def join(self, separator=""):
        return separator.join(map(str, self.values))

    def difference(self, other):
        if isinstance(other, list_type):
            return list_type(set(self.values) - set(other.values))
        return NotImplemented

    def intersection(self, other):
        if isinstance(other, list_type):
            return list_type(set(self.values) & set(other.values))
        return NotImplemented

    def union(self, other):
        if isinstance(other, list_type):
            return list_type(set(self.values) | set(other.values))
        return NotImplemented

    def symmetric_difference(self, other):
        if isinstance(other, list_type):
            return list_type(set(self.values) ^ set(other.values))
        return NotImplemented
        
    def is_sorted(self, key=None, reverse=False):
        if len(self.values) < 2:
            return True
        
        # Create a temporary list to sort and compare
        temp_values = list_type(self.values)
        temp_values.sort(key=key, reverse=reverse)
        
        return self.values == temp_values
        

    def find_duplicates(self):
        from collections import Counter
        counts = Counter(self.values)
        return list_type([item for item, count in counts.items() if count > 1])

    def mode(self):
        from collections import Counter
        if not self.values:
            raise ValueError("Cannot find mode of an empty list")
        counts = Counter(self.values)
        max_count = max(counts.values())
        return list_type([item for item, count in counts.items() if count == max_count])

    def median(self):
        if not self.values:
            raise ValueError("Cannot find median of an empty list")
        sorted_values = sorted(self.values)
        n = len(sorted_values)
        if n % 2 == 1:
            return sorted_values[n // 2]
        else:
            mid1 = sorted_values[n // 2 - 1]
            mid2 = sorted_values[n // 2]
            return (mid1 + mid2) / 2

    def variance(self):
        if not self.values:
            raise ValueError("Cannot calculate variance of an empty list")
        n = len(self.values)
        if n == 1:
            return 0.0 # Variance of a single element is 0
        avg = self.average()
        return sum((x - avg) ** 2 for x in self.values) / (n - 1) # Sample variance

    def std_dev(self):
        import math
        if not self.values:
            raise ValueError("Cannot calculate standard deviation of an empty list")
        return math.sqrt(self.variance())

    def power_set(self):
        from itertools import chain, combinations
        s = list_type(self.values)
        return list_type([list_type(combo) for i in range(len(s) + 1) for combo in combinations(s, i)])

    def permutations(self):
        from itertools import permutations
        return list_type([list_type(p) for p in permutations(self.values)])

    def combinations(self, r):
        from itertools import combinations
        return list_type([list_type(c) for c in combinations(self.values, r)])
        
    def combinations_with_replacement(self, r):
        from itertools import combinations_with_replacement
        return list_type([list_type(c) for c in combinations_with_replacement(self.values, r)])

    def get_methods(self):
        return list_type([
            self.append, self.extend, self.insert, self.remove, self.pop,
            self.clear, self.index, self.count, self.sort, self.reverse,
            self.copy, self.to_tuple, self.to_set, self.to_dict, self.filter,
            self.map, self.reduce, self.all, self.any, self.min, self.max,
            self.sum, self.average, self.find_all, self.count_if, self.group_by,
            self.flatten, self.unique, self.chunk, self.prepend, self.get,
            self.swap, self.sample, self.shuffle, self.rotate, self.split_at,
            self.is_empty, self.first, self.last, self.join, self.difference,
            self.intersection, self.union, self.symmetric_difference, self.is_sorted,
            self.find_duplicates, self.mode, self.median, self.variance, self.std_dev,
            self.power_set, self.permutations, self.combinations, self.combinations_with_replacement
        ])
        
if __name__ == "__main__":
    my_list = list_type([1, 2, 3, 4, 5])
    print(f"Original list: {my_list}")

    my_list.append(6)
    print(f"After append(6): {my_list}")

    my_list.extend([7, 8])
    print(f"After extend([7, 8]): {my_list}")

    my_list.insert(0, 0)
    print(f"After insert(0, 0): {my_list}")

    print(f"Length of list: {len(my_list)}")
    print(f"Element at index 3: {my_list[3]}")

    my_list[3] = 99
    print(f"After my_list[3] = 99: {my_list}")

    del my_list[0]
    print(f"After del my_list[0]: {my_list}")

    print(f"Index of 7: {my_list.index(7)}")
    print(f"Count of 99: {my_list.count(99)}")

    my_list.remove(99)
    print(f"After remove(99): {my_list}")

    popped_value = my_list.pop()
    print(f"Popped value: {popped_value}, List after pop: {my_list}")

    my_list.sort()
    print(f"After sort(): {my_list}")

    my_list.reverse()
    print(f"After reverse(): {my_list}")

    copied_list = my_list.copy()
    print(f"Copied list: {copied_list}")

    new_list = list_type([10, 11])
    added_list = my_list + new_list
    print(f"my_list + new_list: {added_list}")

    multiplied_list = my_list * 2
    print(f"my_list * 2: {multiplied_list}")

    print(f"Is 5 in my_list? {5 in my_list}")

    print(f"Is my_list equal to copied_list? {my_list == copied_list}")

    my_list.clear()
    print(f"After clear(): {my_list}")

    # Test additional methods
    test_list = list_type([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10])
    print(f"\nTest list for advanced methods: {test_list}")

    print(f"List to tuple: {test_list.to_tuple()}")
    print(f"List to set: {test_list.to_set()}")

    filtered_list = test_list.filter(lambda x: x % 2 == 0)
    print(f"Filtered (even numbers): {filtered_list}")

    mapped_list = test_list.map(lambda x: x * 2)
    print(f"Mapped (x * 2): {mapped_list}")

    sum_reduced = test_list.reduce(lambda x, y: x + y)
    print(f"Reduced (sum): {sum_reduced}")

    print(f"All elements true? {test_list.all()}")
    print(f"Any elements true? {test_list.any()}")
    print(f"Min element: {test_list.min()}")
    print(f"Max element: {test_list.max()}")
    print(f"Sum of elements: {test_list.sum()}")
    print(f"Average of elements: {test_list.average()}")

    print(f"Find all occurrences of 5: {test_list.find_all(5)}")
    print(f"Count if x > 5: {test_list.count_if(lambda x: x > 5)}")

    group_list = list_type([{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}, {'id': 1, 'name': 'C'}])
    grouped_by_id = group_list.group_by(lambda x: x['id'])
    print(f"Grouped by 'id': {grouped_by_id}")

    nested_list = list_type([1, list_type([2, 3]), 4, list_type([5, 6])])
    print(f"Flattened list: {nested_list.flatten()}")

    unique_list = list_type([1, 2, 2, 3, 4, 4, 5])
    print(f"Unique elements: {unique_list.unique()}")

    chunked_list = test_list.chunk(3)
    print(f"Chunked list (size 3): {chunked_list}")

    test_list.prepend(0)
    print(f"After prepend(0): {test_list}")

    print(f"Get element at index 5: {test_list.get(5)}")
    print(f"Get element at index 100 (with default): {test_list.get(100, 'Not Found')}")

    swap_list = list_type([1, 2, 3, 4])
    swap_list.swap(0, 3)
    print(f"After swap(0, 3): {swap_list}")

    sample_list = test_list.sample(3)
    print(f"Sample 3 elements: {sample_list}")

    shuffle_list = list_type([1, 2, 3, 4, 5])
    shuffle_list.shuffle()
    print(f"Shuffled list: {shuffle_list}")

    rotate_list = list_type([1, 2, 3, 4, 5])
    rotate_list.rotate(2)
    print(f"Rotated list by 2: {rotate_list}")

    split1, split2 = test_list.split_at(5)
    print(f"Split at index 5: {split1}, {split2}")

    print(f"Is test_list empty? {test_list.is_empty()}")
    empty_list = list_type([])
    print(f"Is empty_list empty? {empty_list.is_empty()}")

    print(f"First element of test_list: {test_list.first()}")
    print(f"Last element of test_list: {test_list.last()}")

    join_list = list_type(['a', 'b', 'c', 'd'])
    print(f"Joined list with '-': {join_list.join('-')}")

    list_a = list_type([1, 2, 3, 4])
    list_b = list_type([3, 4, 5, 6])
    print(f"List A: {list_a}, List B: {list_b}")
    print(f"Difference (A - B): {list_a.difference(list_b)}")
    print(f"Intersection (A & B): {list_a.intersection(list_b)}")
    print(f"Union (A | B): {list_a.union(list_b)}")
    print(f"Symmetric Difference (A ^ B): {list_a.symmetric_difference(list_b)}")

    sorted_list = list_type([1, 2, 3, 4, 5])
    unsorted_list = list_type([1, 3, 2, 4, 5])
    print(f"Is sorted_list sorted? {sorted_list.is_sorted()}")
    print(f"Is unsorted_list sorted? {unsorted_list.is_sorted()}")

    dup_list = list_type([1, 2, 2, 3, 4, 4, 4, 5])
    print(f"Duplicates in {dup_list}: {dup_list.find_duplicates()}")

    mode_list = list_type([1, 2, 2, 3, 3, 3, 4])
    print(f"Mode of {mode_list}: {mode_list.mode()}")

    median_list_odd = list_type([1, 2, 3, 4, 5])
    median_list_even = list_type([1, 2, 3, 4, 5, 6])
    print(f"Median of {median_list_odd}: {median_list_odd.median()}")
    print(f"Median of {median_list_even}: {median_list_even.median()}")

    var_list = list_type([1, 2, 3, 4, 5])
    print(f"Variance of {var_list}: {var_list.variance()}")
    print(f"Standard Deviation of {var_list}: {var_list.std_dev()}")

    power_set_list = list_type([1, 2, 3])
    print(f"Power set of {power_set_list}: {power_set_list.power_set()}")

    permutations_list = list_type([1, 2, 3])
    print(f"Permutations of {permutations_list}: {permutations_list.permutations()}")

    combinations_list = list_type([1, 2, 3, 4])
    print(f"Combinations of {combinations_list} (r=2): {combinations_list.combinations(2)}")
    print(f"Combinations with replacement of {combinations_list} (r=2): {combinations_list.combinations_with_replacement(2)}")
    # Test class methods for creating lists from other data types
    print("\n--- Class Method Tests ---")
    tuple_data = (10, 20, 30)
    list_from_tuple = list_type.from_tuple(tuple_data)
    print(f"List from tuple {tuple_data}: {list_from_tuple}")

    set_data = {100, 200, 300}
    list_from_set = list_type.from_set(set_data)
    print(f"List from set {set_data}: {list_from_set}")

    dict_data = {'a': 1, 'b': 2, 'c': 3}
    list_from_dict_keys = list_type.from_dict_keys(dict_data)
    print(f"List from dict keys {dict_data}: {list_from_dict_keys}")
    list_from_dict_values = list_type.from_dict_values(dict_data)
    print(f"List from dict values {dict_data}: {list_from_dict_values}")
    list_from_dict_items = list_type.from_dict_items(dict_data)
    print(f"List from dict items {dict_data}: {list_from_dict_items}")
    

    