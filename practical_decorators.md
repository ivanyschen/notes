# Practical Decorators

SEE THIS

```python
@mydeco
def add(a, b):
	return a + b
```

THINK THIS

```python
def add(a, b):
	return a + b
add = mydeco(add)
```

## Callable Perspective

```python
def mydeco(func):
	def wrapper(*args, **kwargs):
		return f'{func(*args, **kwargs)}!!!'
	return wrapper
```

callable 1: decorated function `func`

callable 2: decorator `mydeco`

callable 3: the returned `wrapper`

## Time Perspective

```python
def mydeco(func):
	def wrapper(*args, **kwargs):
		return f'{func(*args, **kwargs)}!!!'
	return wrapper
```

Function `mydeco` will be executed only once while we decorating it.

Function that is decorated will be executed whenever it is called.

💡We usually decorate something only once and use it for a while.

## Example: Once per minute

```python
def once_per_minute(func):
	last_invoked = 0
	def wrapper(*args, **kwargs):
		nonlocal last_invoked
		elapsed_time = time.time() - last_invoked
		if elapsed_time < 60:
			raise CalledTooOftenError(f'only {elapsed_time has passed}')
			last_invokded = time.time()
		return func(*args, kwargs)
	return wrapper
				
```

:thinking: how to extend the above to "once per n"?

SEE THIS

```python
@once_per_n_sec(5)
def add(a, b):
	return a + b
```

THINK THIS

```python
def add(a, b):
	return a + b
add = once_per_n(5)(add)
```

💡 4 callables above so I need 3 levels of function

## Example: Once per n

```python
def once_per_n_sec(n):
  	def middle(func):
      	last_invokded = 0
        def wrapper(*args, **kwargs):
          	nonlocal last_invoked
            elapsed_time = time.time() - last_invoked
            if elapsed_time < n:
              	raise CalledTooOftenError(f'Only {elapsed_time} has passed')
            last_invoked = time.time()
        		return func(*args, **kwargs)
        return wrapper
    return middle
```

## Example: Memoization

```python
def memoization(func):
	cache = {}
	def wrapper(*args, **kwargs):
		if args not in cache:
			print(f'caching new value for {func.__name__}')
			cache[t] = func(*args, **kwargs)
			else:
				print(f'Using old value for {func.__name__}')
			retun cache[t]
	return wrapper
```

:thinking:What if `args` is not hashable? What about `kwargs`

💡Pickle!

```
def memoization(func):
	cache = {}
	def wrapper(*args, **kwargs):
		key = (pickle.dumps(args), pickle.dumps(kwargs))
		if key not in cache:
			print(f'caching new value for {func.__name__}{args}')
			cache[args] = func(*args, **kwargs)
		else:
			print(f'Using old value for {func.__name__}{args}')
		retun cache[args]
	return wrapper
```

## Example: Modify/Add Attributes 

```python
def fancy_repr(self):
	return f'I'm a {type(self), with vars {vars(self)}}'
		
def better_repr(c):
	c.__repr__ = fancy_repr
	def wrapper(*args, ** kwargs):
		o = c(*args, **kwargs)
		return o
	return wrapper
		
######-----------------or-----------------######
def another_better_repr(c):
	c.__repr__ = fancy_repr
	return c
```

```python
def obj_birthday(c):
	def wrapper(*args, **kwargs):
		o = c(*args, **kwargs)
		o._created_at = time.time()
		return o
	return wrapper
```

## Note

Original Talk: [Reuven M. Lerner - Practical decorators - PyCon 2019](https://www.youtube.com/watch?v=MjHpMCIvwsY)
