#Lists <small>4/3</small>

## pop quiz
1. How did you handle y in piglatin?
2. Given fooify(str) -> 'foo', write fooifyPhrase("hello I am") -> "foo0 foo1 foo2"

## Experiment
```python
   >>> [1] + [2]
   [1,2]
   
   >>> [1] + 2
   Error

   >>> x = [1,2]
   >>> y = [3,4]
   >>> print x + y
   [1,2,3,4]

   >>> print x
   [1,2]

   >>> [1,2] + [2,3]
   [1,2,2,3]
```

#Reigning Champ <small>4/4</small>

pit each element against the other one at a time
**make sure to initialize first gladioator at first element not 0**

```python
a="booyakasha"
x = ['B', 0, 0, 'Y', 4, 'K', 4, '$', 'H', 4]

a[0] -> 'b'
x[0] -> 'B'

a[0] = 'g' -> Error not mutable
x[0] = 'G' -> changes the 'B' to 'G'

a[::1] -> 'booyakasha' #whole string
x[::1] -> ['G', 0, 0, 'Y', 4, 'K', 4, '$', 'H', 4] #whole list
a[::2] -> 'boaah' #every other letter
x[::2] -> ['G', 0, 4, 4, 'H'] #every other element
```

to get formal about it, ```x[::n]``` returns all elements whose index mod n = 0

```
>>> x[::3]
['G', 'Y', 4, 4]
>>> x[1::3]
[0, 4, '$']
>>> x[2::3]
[0, 'K', 'H']
>>> x[3::3]
['Y', 4, 4]
```

starts at 1

doesn't add 1 then mod because ```x[3::3] -> ['Y', 4, 4]```

##Negatives
```python
>>> x[::-1]
[4, 'H', '$', 4, 'K', 4, 'Y', 0, 0, 'G']
>>> x[::-2]
[4, '$', 'K', 'Y', 0] #starts at last
>>> x[::2]
['G', 0, 4, 4, 'H']
>>> x
['G', 0, 0, 'Y', 4, 'K', 4, '$', 'H', 4]
```

```python
x[2::] -> [0, 'Y', 4, 'K', 4, '$', 'H', 4] # = x[2:]
```

```python
x[::0] -> Error
```

```
>>> x[:2:]
['G', 0]
>>> x
['G', 0, 0, 'Y', 4, 'K', 4, '$', 'H', 4]
>>> x[:3:]
['G', 0, 0]
>>> x[:4:]
['G', 0, 0, 'Y']
```

##Summary
```x[start:len:mod]``` returns the first len mod'th element starting at start. returns as many as can, no error if len is too big