import pytest
from utils import arrs


@pytest.fixture
def coll():
    return [[1, 2, 3], 1, "test"]

@pytest.fixture
def coll_1():
    return [[], 0, "test"]
    

def test_get(coll, coll_1):
    assert arrs.get(coll) == 2
    assert arrs.get(coll_1) == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2], 1) == [2]
    assert arrs.my_slice([1, 2, 3, 4], None, 3) == [1, 2, 3]
