[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/O0TbKqdD)
# Final homework &nbsp; <a href="/../../pull/1/checks"><img src="/../status/badges/score.svg?raw=true" alt="Latest score" align="right"/></a>

<!-- The above score badge (a) assumes clusterhack-classbot is configured on repos, and (b) relies on relative link to PRs that is *not* officially supported by GitHub -->

---

> **Warning**
>
> ### You should work **individually** on all problems of this homework assignment, and you may **not** use slip days.

---

## Problems

### Problem 1 [40pts] &mdash; `seq_lib.zip`

Define a function called `zip` (in `seq_lib.py`) which accepts two lists, `s` and `t`, as input arguments, and returns a new list with all pairs of `s` and `t` items (in that order) that have equal indices (in their respective list). Here, "pair" simply means a tuple of length two. The input lists should *not* be modified in any way.  Finally, you should *not* use the built-in `zip` function in order to receive credit.

The above implies that: (a) if the input lists do not have equal lengths, then the returned list will have length equal to that of the shortest list (since the "trailing" elements of the longer list do not have a corresponding element with equal index), (b) if any of the two input lists is empty, then the returned list will be a new empty list. Finally, the type of `s` and `t` items does not matter.

For example, the function call `seq_lib.zip([1,2,3], ['a', 'b'])` should evaluate to `[(1, 'a'), (2, 'b')]`.

**Hint** Note that the desired result is the list containing all $(s[i], t[i])$ tuples over the sequence of common indices $i$, i.e., for $i$ in $0, 1, \ldots, \min(\mathrm{len}(s), \mathrm{len}(t))-1$.


### Problem 2 [60pts] &mdash; `seq_lib.find_period`

Define a function called `find_period` (in `seq_lib.py`) which accepts one argument, `s`, and returns an integer period length if `s` is periodic (see next) or `-1` if `s` is not periodic.  The input argument `s` can be of any sequence-like type (e.g., string, list, tuple, etc). Your function should not modify `s` in any way.

For this problem, we use a simplified definition of *periodic*: we'll say that `s` is *periodic* with period length $1 \le p < \mathrm{len}(s)$ if it's equal to the repetition of it's first $p$ elements. For example, `"abcdabcdabcd"` is periodic (with period length $p=4$) since it's the repetition of `"abcd"` (i.e., it's first 4 elements). Therefore, the call `find_period("abcdabcdabcd")` should evaluate to `4`. However, neither `"abcdef"` nor `"abcdabc"` are periodic (thus, `find_period` on either of those inputs should evaluate to `-1`).

Some clarifications on implications of the above statements/definitions:

* If $p$ is a valid period length, then so are all of it's multiples $2p, 3p, \ldots \le \mathrm{len}(s)/2$. Your function should simply return the smallest period length. For example, `find_period("abababab")` should evaluate to `2` (*not* `4`).
* If we allowed $p = \mathrm{len}(s)$, that would trivially be a valid period length for any `s`. So, we don't. This, in turn, implies that any input of length one cannot be periodic.
* If we allowed $p = 0$, that would trivially be a valid period length if `s` were empty. But, we don't. This, in turn, implies that any empty input cannot be periodic.

**Hints** A simple way to check whether `s` is periodic *with period length equal to `p` (integer)* is with the expression `s[0:p] * (len(s)//p) == s` (why?). Note that this will work on any sequence-like type. The only remaining task after that is to find the *first* (i.e., smallest) integer $p$, for $1\le p \le \mathrm{len}(s)/2$, which satisfies that condition (i.e., it is a period). As soon as you find such a $p$, you can return it. If you fail to find one, then you should return -1.
This task, in turn, is not very different from the `is_periodic(...)` practice problem on Canvas...
