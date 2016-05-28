# puffadder
A boiler plate reducing library for Python, inspired by Project Lombok for Java.


## @to_string

Adds a __str__ function to the class that returns all public class attributes in a neatly formatted string.

<table border="0">
<tr>
<td>
Puffadder
</td>
<td>
Vanilla Python
</td>
</tr>
<tr valign="top">
<td>
  <pre lang="python">
@to_string
class Student(object):
  _private_attribute = "This will not be seen"
  name = "Sally"
  age = 22
  full_time = True

>>> john = Student()
>>> john.name = "John"
>>> print(Student())
{name=John, age=22, full_time=True}
  </pre>
</td>
<td>
  <pre lang="python">
class Student(object):
  _private_attribute = "This will not be seen"
  name = "Sally"
  age = 22
  full_time = True

  def __str__(self):
    return "{{name={}, age={}, full_time={}}}"
      .format(self.name, self.age, self.ful_time)

>>> john = Student()
>>> john.name = "John"
>>> print(Student())
{name=John, age=22, full_time=True}
  </pre>
</td>
</tr>
</table>


## @builder

Adds a constructor to the class that sets all public class attributes in the constructor. If a constructor was defined it is run after the generated constructor.

<table border="0">
<tr>
<td>
Puffadder
</td>
<td>
Vanilla Python
</td>
</tr>
<tr valign="top">
<td>
  <pre lang="python">
@builder
class Student(object):
  _private_attribute = "This will not be seen"
  name = "Sally"
  age = 22
  full_time = True

john = Student(
    name="John",
    age=30,
    full_time=False
)
  </pre>
</td>
<td>
  <pre lang="python">
class Student(object):
  _private_attribute = "This will not be seen"
  name = "Sally"
  age = 22
  full_time = True

  def __init__(self, name, age, full_time):
    self.name = name
    self.age = age
    self.full_time = full_time

john = Student(
    name="John",
    age=30,
    full_time=False
)
  </pre>
</td>
</tr>
</table>