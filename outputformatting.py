# hack for multi-line command
"""
In [8]: help(print)
Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
"""

# documentation: https://docs.python.org/3/tutorial/inputoutput.html

print(1)
print('hello')
print("hello")
x = 10
# formatter string with python expressions in string literal.
print(f'hello {x}')
print(f"hello {x}", end='\n')

# break a list into multi-line
print("\n".join(["1","2"]), end='\n', sep='\n')

