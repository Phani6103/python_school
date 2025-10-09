import math

import pytest

from python_school.models.data_types.list_type import list_type


def assert_list_type_contents(instance, expected):
    assert isinstance(instance, list_type)
    assert list(instance) == expected


def test_append_and_index_operations():
    values = list_type([1, 2])
    values.append(3)

    assert len(values) == 3
    assert values[0] == 1
    assert values[2] == 3

    values[1] = 99
    assert values[1] == 99

    del values[1]
    assert list(values) == [1, 3]


def test_copy_creates_independent_instance():
    original = list_type([1, 2, 3])
    clone = original.copy()

    original.append(4)

    assert_list_type_contents(original, [1, 2, 3, 4])
    assert_list_type_contents(clone, [1, 2, 3])
    assert clone is not original


def test_add_multiply_and_equality_semantics():
    seq_a = list_type([1, 2])
    seq_b = list_type([3])

    combined = seq_a + seq_b
    repeated = seq_b * 2

    assert_list_type_contents(combined, [1, 2, 3])
    assert_list_type_contents(repeated, [3, 3])
    assert combined == list_type([1, 2, 3])
    assert repeated != seq_b

    original_seq_a = seq_a
    seq_a += seq_b
    assert seq_a is original_seq_a
    assert_list_type_contents(seq_a, [1, 2, 3])

    original_seq_b = seq_b
    seq_b *= 3
    assert seq_b is original_seq_b
    assert_list_type_contents(seq_b, [3, 3, 3])


def test_average_and_variance_require_values():
    populated = list_type([1, 2, 3, 4])
    assert populated.average() == pytest.approx(2.5)
    assert populated.variance() == pytest.approx(1.6666666666666667)
    assert populated.std_dev() == pytest.approx(math.sqrt(1.6666666666666667))

    empty = list_type()
    with pytest.raises(ValueError):
        empty.average()
    with pytest.raises(ValueError):
        empty.variance()
    with pytest.raises(ValueError):
        empty.std_dev()


def test_group_by_chunks_and_find_duplicates():
    words = list_type(["apple", "ant", "banana", "berry"])
    grouped = words.group_by(lambda item: item[0])

    assert set(grouped.keys()) == {"a", "b"}
    assert_list_type_contents(grouped["a"], ["apple", "ant"])
    assert_list_type_contents(grouped["b"], ["banana", "berry"])

    numbers = list_type(range(5))
    chunks = numbers.chunk(2)
    assert_list_type_contents(chunks[0], [0, 1])
    assert_list_type_contents(chunks[1], [2, 3])
    assert_list_type_contents(chunks[2], [4])

    with pytest.raises(ValueError):
        numbers.chunk(0)

    duplicates = list_type([1, 2, 2, 3, 3, 3]).find_duplicates()
    assert_list_type_contents(duplicates, [2, 3])


def test_dict_and_set_related_utilities():
    kv_pairs = list_type([("a", 1), ("b", 2)])
    assert kv_pairs.to_dict() == {"a": 1, "b": 2}

    with pytest.raises(TypeError):
        list_type([1, 2, 3]).to_dict()

    first, second = list_type([1, 2, 3, 4]).split_at(2)
    assert_list_type_contents(first, [1, 2])
    assert_list_type_contents(second, [3, 4])

    odds = list_type([1, 3, 5, 7])
    evens = list_type([2, 4, 6, 8, 1])

    assert set(odds.difference(evens)) == {3, 5, 7}
    assert set(odds.intersection(evens)) == {1}
    assert set(odds.union(evens)) == {1, 2, 3, 4, 5, 6, 7, 8}
    assert set(odds.symmetric_difference(evens)) == {2, 3, 4, 5, 6, 7, 8}


def test_flatten_unique_and_power_set_behaviour():
    nested = list_type([list_type([1, 2]), list_type([3])])
    flattened = nested.flatten()
    assert_list_type_contents(flattened, [1, 2, 3])

    unique_values = list_type([1, 2, 2, 3, 1]).unique()
    assert_list_type_contents(unique_values, [1, 2, 3])

    power = list_type([1, 2]).power_set()
    assert len(power) == 4
    assert_list_type_contents(power[0], [])
    assert_list_type_contents(power[1], [1])
    assert_list_type_contents(power[2], [2])
    assert_list_type_contents(power[3], [1, 2])


def test_permutations_and_combinations():
    items = list_type([1, 2, 3])
    perms = items.permutations()
    assert len(perms) == 6
    assert list_type([1, 2, 3]) in perms
    assert list_type([3, 2, 1]) in perms

    combs = items.combinations(2)
    assert len(combs) == 3
    assert list_type([1, 2]) in combs
    assert list_type([1, 3]) in combs
    assert list_type([2, 3]) in combs

    combs_with_replacement = items.combinations_with_replacement(2)
    assert len(combs_with_replacement) == 6
    assert list_type([1, 1]) in combs_with_replacement
    assert list_type([1, 2]) in combs_with_replacement
    assert list_type([1, 3]) in combs_with_replacement
    assert list_type([2, 2]) in combs_with_replacement
    assert list_type([2, 3]) in combs_with_replacement
    assert list_type([3, 3]) in combs_with_replacement


def test_is_sorted_method():
    assert list_type([1, 2, 3, 4, 5]).is_sorted() is True
    assert list_type([5, 4, 3, 2, 1]).is_sorted(reverse=True) is True
    assert list_type([1, 3, 2, 4, 5]).is_sorted() is False
    assert list_type([]).is_sorted() is True
    assert list_type([1]).is_sorted() is True

    # Test with key
    data = list_type([{'id': 1}, {'id': 3}, {'id': 2}])
    assert data.is_sorted(key=lambda x: x['id']) is False
    data.sort(key=lambda x: x['id'])
    assert data.is_sorted(key=lambda x: x['id']) is True


def test_mode_median_and_statisticalmethods():
    assert list_type([1, 2, 2, 3, 3, 3, 4]).mode() == list_type([3])
    with pytest.raises(ValueError):
        list_type([]).mode()

    assert list_type([1, 2, 3, 4, 5]).median() == 3
    assert list_type([1, 2, 3, 4, 5, 6]).median() == 3.5
    with pytest.raises(ValueError):
        list_type([]).median()
        
def test_from_class_methods():
    assert_list_type_contents(list_type.from_tuple((1, 2, 3)), [1, 2, 3])
    assert_list_type_contents(list_type.from_set({1, 2, 3}), [1, 2, 3])
    assert_list_type_contents(list_type.from_dict_keys({'a': 1, 'b': 2}), ['a', 'b'])
    assert_list_type_contents(list_type.from_dict_values({'a': 1, 'b': 2}), [1, 2])
    assert_list_type_contents(list_type.from_dict_items({'a': 1, 'b': 2}), [('a', 1), ('b', 2)])
    
def test_comparison_operators():
    list1 = list_type([1, 2, 3])
    list2 = list_type([1, 2, 3])
    list3 = list_type([1, 2, 4])
    list4 = list_type([1, 2])

    assert (list1 == list2) is True
    assert (list1 != list3) is True
    assert (list1 < list3) is True
    assert (list1 <= list2) is True
    assert (list3 > list1) is True
    assert (list2 >= list1) is True
    assert (list4 < list1) is True
    assert (list1 > list4) is True

    # Test with non-list_type objects
    assert list1.__eq__([1, 2, 5]) is NotImplemented
    assert list1.__lt__([1, 2, 4]) is NotImplemented


def test_contains_method():
    my_list = list_type([1, 2, 3, 4, 5])
    assert (3 in my_list) is True
    assert (6 in my_list) is False


def test_repr_and_str():
    my_list = list_type([1, 2, 3])
    assert repr(my_list) == "list([1, 2, 3])"
    assert str(my_list) == "[1, 2, 3]"


def test_hash_method():
    list1 = list_type([1, 2, 3])
    list2 = list_type([1, 2, 3])
    list3 = list_type([3, 2, 1])

    assert hash(list1) == hash(list2)
    assert hash(list1) != hash(list3)

    # Test that it can be used in sets/dicts
    s = {list1}
    assert list2 in s
    assert list3 not in s


def test_get_methods():
    my_list = list_type([1, 2])
    methods = my_list.get_methods()

    # Check if some key methods are present
    assert my_list.append in methods
    assert my_list.sort in methods
    assert my_list.average in methods
    assert my_list.power_set in methods
    assert my_list.get_methods not in methods # Should not include itself
    
def test_first_and_last():
    my_list = list_type([1, 2, 3])
    assert my_list.first() == 1
    assert my_list.last() == 3

    empty_list = list_type([])
    assert empty_list.first() is None
    assert empty_list.last() is None
    assert empty_list.first(default=0) == 0
    assert empty_list.last(default=0) == 0


def test_join():
    my_list = list_type(['a', 'b', 'c'])
    assert my_list.join('-') == 'a-b-c'
    assert my_list.join('') == 'abc'
    assert list_type([1, 2, 3]).join(',') == '1,2,3'
    assert list_type([]).join(',') == ''
    
def test_shuffle():
    original_list = [1, 2, 3, 4, 5]
    my_list = list_type(original_list.copy())
    my_list.shuffle()
    
    # Check if all original elements are still present
    assert sorted(my_list.values) == sorted(original_list)
    # Check if it's likely shuffled (not guaranteed to be different, but highly probable)
    assert my_list.values != original_list or len(original_list) <= 1

def test_rotate():
    my_list = list_type([1, 2, 3, 4, 5])
    my_list.rotate(2)
    assert_list_type_contents(my_list, [4, 5, 1, 2, 3])

    my_list = list_type([1, 2, 3, 4, 5])
    my_list.rotate(-1) # Rotate left by 1
    assert_list_type_contents(my_list, [2, 3, 4, 5, 1])

    my_list = list_type([1, 2, 3])
    my_list.rotate(0)
    assert_list_type_contents(my_list, [1, 2, 3])

    my_list = list_type([1, 2, 3])
    my_list.rotate(3) # Rotate by length of list
    assert_list_type_contents(my_list, [1, 2, 3])

    empty_list = list_type([])
    empty_list.rotate(5)
    assert_list_type_contents(empty_list, [])

def test_sample():
    my_list = list_type([1, 2, 3, 4, 5])
    sample_k_1 = my_list.sample()
    assert len(sample_k_1) == 1
    assert sample_k_1[0] in my_list.values

    sample_k_3 = my_list.sample(k=3)
    assert len(sample_k_3)== 3
    for item in sample_k_3:
        assert item in my_list.values
    
    # Test k > len(list)
    with pytest.raises(ValueError):
        my_list.sample(k=10)

    # Test k = 0
    sample_k_0 = my_list.sample(k=0)
    assert len(sample_k_0) == 0
    assert_list_type_contents(sample_k_0, [])

def test_is_empty():
    empty_list = list_type([])
    non_empty_list = list_type([1, 2, 3])

    assert empty_list.is_empty() is True
    assert non_empty_list.is_empty() is False
    
def test_get_item_with_slice():
    my_list = list_type([0, 1, 2, 3, 4, 5])
    assert list(my_list[1:4]) == [1, 2, 3]
    assert list(my_list[:3]) == [0, 1, 2]
    assert list(my_list[3:]) == [3, 4, 5]
    assert list(my_list[::2]) == [0, 2, 4]
    assert list(my_list[::-1]) == [5, 4, 3, 2, 1, 0]
    assert list(my_list[:]) == [0, 1, 2, 3, 4, 5]

def test_set_item_with_slice():
    my_list = list_type([0, 1, 2, 3, 4, 5])
    my_list[1:4] = [10, 11, 12]
    assert_list_type_contents(my_list, [0, 10, 11, 12, 4, 5])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    my_list[:2] = [100, 101]
    assert_list_type_contents(my_list, [100, 101, 2, 3, 4, 5])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    my_list[4:] = [200, 201]
    assert_list_type_contents(my_list, [0, 1, 2, 3, 200, 201])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    my_list[::2] = [100, 11, 12]
    assert_list_type_contents(my_list, [100, 1, 11, 3, 12, 5])

    # Test with different length assignment
    my_list = list_type([0, 1, 2, 3, 4, 5])
    my_list[1:4] = [100]
    assert_list_type_contents(my_list, [0, 100, 4, 5])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    my_list[1:2] = [10, 11, 12]
    assert_list_type_contents(my_list, [0, 10, 11, 12, 2, 3, 4, 5])

def test_del_item_with_slice():
    my_list = list_type([0, 1, 2, 3, 4, 5])
    del my_list[1:4]
    assert_list_type_contents(my_list, [0, 4, 5])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    del my_list[:2]
    assert_list_type_contents(my_list, [2, 3, 4, 5])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    del my_list[4:]
    assert_list_type_contents(my_list, [0, 1, 2, 3])

    my_list = list_type([0, 1, 2, 3, 4, 5])
    del my_list[::2]
    assert_list_type_contents(my_list, [1, 3, 5])
    
