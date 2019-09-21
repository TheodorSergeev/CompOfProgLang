# -*- coding: utf-8 -*-
"""

Task: implement a function that calculates factorial using tail call.
(https://en.wikipedia.org/wiki/Tail_call)

Example:
    Run this file in your IDE or in command line::

        $ python3 factorial.py

.. _Repository:
   https://github.com/TheodorSergeev/CompOfProgLang

"""

import time
import math


def factorial(num: int) -> int:
    """Computes factorial using tail call.

    Args:
        num (int): Non-negative integer whose factorial is to be calculated.

    Returns:
        int: Factorial of the 'num'.

    Raises:
        ValueError: If `num` is negative.

    """

    if num == 0:
        return 1

    if num < 0:
        raise ValueError("save must be True if recurse is True")

    return num * factorial(num - 1)


def time_function(func, arg):
    """Computes execution time of a function on a given argument.

    Args:
        func: Function to be timed.
        arg: Argument for 'func'.

    Returns:
        ret_val: Return value of 'func' with argument 'arg'.
		float: The 'func' execution time in seconds.

    """

    start = time.time()
    ret_val = func(arg)
    end = time.time()
    return ret_val, (end - start)


for i in range(1, 15):
    fact_tail_call, time_tail_call = time_function(factorial, i)
    fact_math, time_math = time_function(math.factorial, i)

    if fact_tail_call != fact_math:
        raise ValueError("Factorial computed by built-in function differs from the implemented one")

    print("%2d! = %12d   tail call elapsed in %.4f ms   built-in elapsed in %.4f ms" %
          (i, fact_tail_call, time_tail_call * 1000, time_math * 1000))
