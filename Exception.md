# Exceptions in Python

### Take advantage of `exc_info`

```python
try:
		...
except FirstException:
		...
except Exception:
		logger.error('This is an exception', exc_info=True)
```

### Raise within Exception (Reraise)

DONT:

```python
try:
		1 / 0
except Exception:
  	raise Exception('This is an exception.') 
```

```
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-4-193771c4d400> in <module>
      1 try:
----> 2     1 / 0
      3 except Exception:

ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Exception                                 Traceback (most recent call last)
<ipython-input-4-193771c4d400> in <module>
      2     1 / 0
      3 except Exception:
----> 4     raise Exception('This is an exception.')
      5
      6

Exception: This is an exception.
```

DO:

```python
try:
		1 / 0
except Exception:
  	print('This is an exception.')
  	raise
```

```
This is an exception.
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-5-786bc080cd46> in <module>
      1 try:
----> 2     1 / 0
      3 except Exception:
      4     print('This is an exception.')
      5     raise

ZeroDivisionError: division by zero
```

###  Raise with direct cause

```python
class MyClassException(Exception):
		pass
		
try:
		1 / 0
exception Exception as e:
		raise MyClassException('Exception in class method') from e
```

```
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-9-822583d64bca> in <module>
      4 try:
----> 5     1 / 0
      6 except Exception as e:

ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

MyClassException                          Traceback (most recent call last)
<ipython-input-9-822583d64bca> in <module>
      5     1 / 0
      6 except Exception as e:
----> 7     raise MyClassException('Exception in class method') from e
      8

MyClassException: Exception in class method
```

### Don't leave `return` in `finally`

```python
def do():
		try:
				1 / 0
		except Exception:
				raise
		finally:
				return
```

```python
do()
# No exception is raised
```

## Resource

[1]: [Exceptional Exceptions - How to properly raise, handle and create them](Exceptional Exceptions - How to properly raise, handle and create them.)

