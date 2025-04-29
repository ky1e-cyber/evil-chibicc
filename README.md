## Implementing [Trusting Trust](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf) attack on [chibicc](https://github.com/rui314/chibicc)

Inspired by [Running the “Reflections on Trusting Trust” Compiler](https://research.swtch.com/nih) and original Ken Thompson's paper

### Step 1. Build backdoored compiler

```sh
$ patch < tt-attack/attack.patch
$ make
$ ./chibicc tt-utils/hello.c
$ ./a.out 
backdooored
```

Then install `./chibicc` executable somewhere in your `PATH`

### Step 2. Rebuild with non-infected source

```sh
$ make clean
$ git restore tokenize.c
```

Now build from original source using infected compiler

```sh
$ make CC=chibicc
```
Replace old `chibicc` executable with newly built one

### Step 3. Rebuild with new compiler

```sh
$ make clean
$ make CC=chibicc
$ ./chibicc tt-utils/hello.c
$ ./a.out
backdooored
```

