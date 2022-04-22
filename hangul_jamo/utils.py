from itertools import chain, tee
from typing import Any, Iterator, Optional, Tuple


def consume(iterator: Iterator, n: int, default: Optional[Any] = None) -> Iterator:
    for _ in range(n):
        next(iterator, default)

def ngram(text: str, n: int, pad_left: bool = False, pad_right: bool = False) -> Iterator[Tuple[Optional[str], ...]]:
    if pad_left:
        text = chain([None] * (n - 1), text)
    if pad_right:
        text = chain(text, [None] * (n - 1))

    iterators = tee(text, n)
    for index, iterator in enumerate(iterators):
        consume(iterator, index, default=None)

    return zip(*iterators)
