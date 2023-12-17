# (c) 2022- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.unittest import HomeworkModuleTestCase
from .hwtest import autograde as grade

from typing import Callable, Sequence, TypeVar, Tuple


S = TypeVar("S")
T = TypeVar("T")
zip: Callable[[Sequence[S], Sequence[T]], Sequence[Tuple[S,T]]]
unwrap: Callable[[Sequence[Sequence[T]]], Sequence[T]]
find_period: Callable[[Sequence], int]


@grade.max_score(40)
class ZipTests(HomeworkModuleTestCase):
  __scriptname__ = "seq_lib.py"
  __modulename__ = "seq_lib"
  __attrnames__ = [ "zip" ]

  @grade.score(-5)
  def test_empty(self):
    self.assertEqual([], zip([], [1, 2, 3]))
    self.assertEqual([], zip([1, 2, 3], []))
    self.assertEqual([], zip([], []))

  @grade.score(-5)
  def test_empty_not_alias(self):
    with self.assertUnmodified([], [1, 2, 3]) as (arg1, arg2):
      result = zip(arg1, arg2)
      self.assertEqual([], result)
      self.assertIsNot(arg1, result, msg="Function returns first input, not new list")
      self.assertIsNot(arg2, result, msg="Function returns second input, not new list")
    with self.assertUnmodified([1, 2, 3], []) as (arg1, arg2):
      result = zip(arg1, arg2)
      self.assertEqual([], result)
      self.assertIsNot(arg1, result, msg="Function returns first input, not new list")
      self.assertIsNot(arg2, result, msg="Function returns second input, not new list")
    with self.assertUnmodified([], []) as (arg1, arg2):
      result = zip(arg1, arg2)
      self.assertEqual([], result)
      self.assertIsNot(arg1, result, msg="Function returns first input, not new list")
      self.assertIsNot(arg2, result, msg="Function returns second input, not new list")

  @grade.score(-40)
  def test_no_builtin(self):
    with self.assertWithoutBuiltin("zip"):
      zip([1, 2, 3], ['a', 'b', 'c'])  # ..whatever

  @grade.score(-40)
  def test_simple(self):
    with self.assertUnmodified([1, 2, 3], ['a', 'b', 'c']) as (arg1, arg2):
      self.assertEqual([(1, 'a'), (2, 'b'), (3, 'c')], zip(arg1, arg2))

  @grade.score(-15)
  def test_unequal_length(self):
    import builtins
    letters = list("abcdefghijklmnopqrstuvwxyz")
    for n in range(len(letters) + 1):
      with self.assertUnmodified(letters, list(range(n))) as (arg1, arg2):
        expected = list(builtins.zip(arg1, arg2, strict=False))
        result = zip(arg1, arg2)
        self.assertEquals(expected, result)
      # Also check alternate arg order...
      with self.assertUnmodified(list(range(n)), letters) as (arg1, arg2):
        expected = list(builtins.zip(arg1, arg2, strict=False))
        result = zip(arg1, arg2)
        self.assertEquals(expected, result)
    
  @grade.score(-20)
  def test_no_copy(self):
    with self.assertUnmodified([1], ['a']) as (x0, y0), self.assertUnmodified([2], ['b']) as (x1, y1), self.assertUnmodified([x0, x1], [y0, y1]) as (arg1, arg2):
      result = zip(arg1, arg2)
      self.assertEquals([([1], ['a']), ([2], ['b'])], result)
      self.assertIs(x0, result[0][0], msg="Result should contain list elements (refs), not copies")
      self.assertIs(y0, result[0][1], msg="Result should contain list elements (refs), not copies")
      self.assertIs(x1, result[1][0], msg="Result should contain list elements (refs), not copies")
      self.assertIs(y1, result[1][1], msg="Result should contain list elements (refs), not copies")
      # Next checks can't hurt...
      self.assertIs(arg1[0], result[0][0], msg="Input lists should not be modified in any way")
      self.assertIs(arg2[0], result[0][1], msg="Input lists should not be modified in any way")
      self.assertIs(arg1[1], result[1][0], msg="Input lists should not be modified in any way")
      self.assertIs(arg2[1], result[1][1], msg="Input lists should not be modified in any way")



@grade.max_score(60)
class FindPeriodTests(HomeworkModuleTestCase):
  __scriptname__ = "seq_lib.py"
  __modulename__ = "seq_lib"
  __attrnames__ = [ "find_period" ]

  @grade.score(-60)
  def test_simple(self):
    self.assertEqual(3, find_period("abcabcabc"))
    self.assertEqual(-1, find_period("abcdabc"))

  @grade.score(-20)
  def test_empty(self):
    self.assertEqual(-1, find_period(""))
    self.assertEqual(-1, find_period(()))
    self.assertEqual(-1, find_period([]))

  @grade.score(-20)
  def test_no_mutation(self):
    with self.assertUnmodified([1,2,3,1,2,3]) as arg:
      self.assertEqual(3, find_period(arg))

  @grade.score(-20)
  def test_constant(self):
    self.assertEqual(-1, find_period("a"))
    self.assertEqual(1, find_period("aa"))
    self.assertEqual(1, find_period("aaaaaaa"))

  @grade.score(-15)
  def test_non_strings1(self):
    self.assertEqual(-1, find_period((1,)))
    self.assertEqual(1, find_period((1,1,1)))
    self.assertEqual(2, find_period((1,2,1,2,1,2)))
    self.assertEqual(-1, find_period((1,2,1,2,1)))
    with self.assertUnmodified([1]) as arg:
      self.assertEqual(-1, find_period(arg))
    with self.assertUnmodified([1,1,1]) as arg:
      self.assertEqual(1, find_period(arg))
    with self.assertUnmodified([1,2,1,2,1,2]) as arg:
      self.assertEqual(2, find_period(arg))
    with self.assertUnmodified([1,2,1,2,1]) as arg:
      self.assertEqual(-1, find_period(arg))

  @grade.score(-15)
  def test_non_strings2(self):
    with self.assertUnmodified([1]) as inner, self.assertUnmodified([inner, inner, inner]) as arg:
      self.assertEqual(1, find_period(arg))
    with self.assertUnmodified([1], [2]) as (in1, in2), self.assertUnmodified([in1, in2, in1, in2, in1, in2]) as arg:
      self.assertEqual(2, find_period(arg))
    with self.assertUnmodified([1], [2]) as (in1, in2), self.assertUnmodified([in1, in2, in1, in2, in1]) as arg:
      self.assertEqual(-1, find_period(arg))

  @grade.score(-20)
  def test_non_periodc(self):
    self.assertEqual(-1, find_period("a"))
    self.assertEqual(-1, find_period(("ab" * 16)[:-1]))
    self.assertEqual(-1, find_period(("ab" * 16)[1:]))
    self.assertEqual(-1, find_period(("abcde" * 16)[:-1]))
    self.assertEqual(-1, find_period(("abcde" * 16)[1:]))

  @grade.score(-25)
  def test_return_smallest(self):
    self.assertEqual(2, find_period("ab" * 16))
    self.assertEqual(3, find_period("abc" * 16))
    self.assertEqual(5, find_period("abcde" * 16))


