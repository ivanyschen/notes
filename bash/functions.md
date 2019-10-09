# Function

## Two Syntaxes

```bash
function_name () {
	<commands>
}
```

```bash
function function_name {
	<commands>
}
```

## Passing in Arguments

```bash
function_1 () {
	echo "This is var: $1"
}
function_1 var_1
function_1 var_2
```

## Return

- Bash doesn't allow returning custimized return values but only a **return status**.
- typically, a return status **0** indicated everything goes well. A status other than 0 suggests something goes wrong.

```bash
function_1 () {
	echo "Hello $1!"
	return 5
}

function_1 ujhuyz0110
echo "function has returned a status $?"
```

## Variable Scope

```bash
Local var_name=<val>
```

- It is generally a good practice to keep variables in a function local variables.

## Overriding Commands

```bash
ls () {
	command ls -lh
}

ls
```

- If `command` is not added, it will end up with an endless loop.