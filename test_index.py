import index
import pytest

def test_1():
    assert index.func(2)

def test_2():
    assert not index.func(5)

def test_3():
    assert index.other_func(5) == 15
