# Bash

- Bash variables are **untyped**

    Unlike many other programming languages, Bash does **not** segregate its variables by "type." Essentially, Bash variables are **character strings**, but, depending on context, Bash permits arithmetic operations and comparisons on variables. The determining factor is **whether the value of a variable contains only digits**.

- Why the output is `{1..5}` instead of number 1 to number 5 printed in each line?

    ```bash
      a_range={1..5}
      for item in $a_range
      do
          echo $item
      done
    ```

    The order of expansions is: brace expansion; tilde expansion, parameter and variable expansion, arithmetic expansion, and command substitution (done in a left-to-right fashion); word splitting; and filename expansion.