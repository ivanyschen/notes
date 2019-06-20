# AST

* Python is compiled and interpretive

  * Compiler generates bytecode
  * Interpreter executive bytecode

* Life cycle of a pieces of python code

  ```
  -------------            ------------
  |source code| =========> |parse tree| ==========>
  -------------   parse    ------------  transform 
  
  -----             -----            ----------
  |AST| ==========> |CFG| =========> |bytecode| =========>
  -----  transform  -----    emit    ----------  execute
  
  --------
  |output|
  --------
  ```

* Tools: 

  * `ast` module: build and introspect AST of a piece of code
  * `dis` module: disemble a piece of bytecode
  * `astor`
  * `meta`
  * `codegen`

* Code objects:

  * contain instructions and information to run a piece of code
  * is the internal representation of a piece of code
  * `co_name`: name of the object
  * `co_varnames`: all the names of local variables, including arguments
  * `co_stacksize`: maximal stack size that is computed statically by the compiler
  * `co_consts`
  * `co_argcount`
  * `co_code`: a string represents a sequence of bytecode instructions

* Example:

  ```python
  >>> import ast, dis
  >>> source = 'print("may the source be with you")'
  >>> node = ast.parse(source, mode='exec')
  # remember to use 'exec' as oppose to 'eval' which only allows us to pares expression
  
  # What do we get from ast.parse?
  >>> type(node)
  # a module
  <class '_ast.Module'>
  
  >>> ast.dump(node)
  "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='may the source be with you')], keywords=[]))])"
  # not easy to work w/
  
  >>> compiled = compile(node, '<string>', mode='exec')
  >>> type(compiled)
  <class 'code'>
  
  >>> compiled.co_code
  b'e\x00d\x00\x83\x01\x01\x00d\x01S\x00'
  # not readable for human
  >>> [b for b in compiled.co_code]
  [101, 0, 100, 0, 131, 1, 1, 0, 100, 1, 83, 0]
  # more readable compared to the previous
  
  >>> dis.dis(compiled)
    1           0 LOAD_NAME                0 (print)
                2 LOAD_CONST               0 ('may the source be with you')
                4 CALL_FUNCTION            1
                6 POP_TOP
                8 LOAD_CONST               1 (None)
               10 RETURN_VALUE
  # even more readable
  
  >>> dis.show_code(compiled)
  Name:              <module>
  Filename:          <string>
  Argument count:    0
  Kw-only arguments: 0
  Number of locals:  0
  Stack size:        2
  Flags:             NOFREE
  Constants:
     0: 'may the source be with you'
     1: None
  Names:
     0: print
  ```

* Peephole optimization (Looing around w/o moving your head)

  Example: compiler automatically turns double negative into positive

  ```python
  >>> dis.dis('not a not in b')
    1           0 LOAD_NAME                0 (a)
                2 LOAD_NAME                1 (b)
                4 COMPARE_OP               6 (in)
                6 RETURN_VALUE
  
  >>> dis.dis('a in b')
    1           0 LOAD_NAME                0 (a)
                2 LOAD_NAME                1 (b)
                4 COMPARE_OP               6 (in)
                6 RETURN_VALUE
  ```

* Constant Folding: evaluating constant expressions at compile time as oppose to run time.

--------------------------------

Note: Most content is from the talk by Emily Morehouse-Valcarcel. Original talk: https://www.youtube.com/watch?time_continue=233&v=XhWvz4dK4ng

