"""Bisection algorithms."""

from typing import List, Callable, TypeVar, Union, Any

T = TypeVar('T')

def insort_right(a: List[T], x: T, lo: int = 0, hi: Union[int, None] =None, key:Union[Callable[[T], Any], None] = None) -> None:
    """Insert item x in list a, and keep it sorted assuming map(key, a) is sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if not key is None:
        lo = bisect_right(a, key(x), lo, hi, key)
        a.insert(lo, x)
        return

    lo = bisect_right(a, x, lo, hi)
    a.insert(lo, x)

def bisect_right(a: Union[List[T], None], x: T, lo: int = 0, hi: Union[int, None] = None, key:Union[Callable[[T], Any], None] = None) -> int:
    """Return the index where to insert item key(x) in list map(key, a), assuming map(key, a) is sorted.

    The return value i is such that all e in a[:i] have key(e) <= x, and all e in
    a[i:] have key(e) > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    If a is None, a is considered list(range(lo, hi)).
    """

    if a is None:
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            raise ValueError('hi must given if a is None')
        if key is None:
            raise ValueError('key must given if a is None')
        while lo < hi:
            mid = (lo+hi)//2
            if x < key(mid): hi = mid
            else: lo = mid+1
        return lo

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    
    if not key is None:
        while lo < hi:
            mid = (lo+hi)//2
            if x < key(a[mid]): hi = mid
            else: lo = mid+1
        return lo

    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo

def insort_left(a: List[T], x: T, lo: int = 0, hi: Union[int, None] = None, key:Union[Callable[[T], Any], None] = None) -> None:
    """Insert item x in list a, and keep it sorted assuming map(key, a) is sorted.

    If x is already in a, insert it to the left of the leftmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if not key is None:
        lo = bisect_left(a, key(x), lo, hi, key)
        a.insert(lo, x)
        return

    lo = bisect_left(a, x, lo, hi)
    a.insert(lo, x)


def bisect_left(a: Union[List[T], None], x: T, lo: int = 0, hi: Union[int, None] = None, key:Union[Callable[[T], Any], None] = None) -> int:
    """Return the index where to insert item key(x) in list map(key, a), assuming map(key, a) is sorted.

    The return value i is such that all e in a[:i] have key(e) < x, and all e in
    a[i:] have key(e) >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    If a is None, a is considered list(range(lo, hi)).
    """

    if a is None:
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            raise ValueError('hi must given if a is None')
        if key is None:
            raise ValueError('key must given if a is None')
        while lo < hi:
            mid = (lo+hi)//2
            if key(mid) < x: lo = mid+1
            else: hi = mid
        return lo

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)

    if not key is None:
        while lo < hi:
            mid = (lo+hi)//2
            if key(a[mid]) < x: lo = mid+1
            else: hi = mid
        return lo

    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo


# Create aliases
bisect = bisect_right
insort = insort_right
