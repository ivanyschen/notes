# Factory Worker Analogy to Blocking/Non-blocking I/O

## Blocking I/O

- A worker works on a work bench.
- While supplies are short, the worker just do nothing but waits.
- **Blocking I/O** refers to threads that **will wait** for I/O operations to finish.

## Non-blocking I/O

- While supplies are short, the worker will suspend the current job and works on another job that can be done first.
- Non-blocking I/O refers to threads that **will not wait** for I/O operations to finish.

## References

[1]: [Explain non-blocking I/O like I’m five](https://blog.codecentric.de/en/2019/04/explain-non-blocking-i-o-like-im-five/)

