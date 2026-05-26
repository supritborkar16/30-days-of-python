# Python `random` Module Documentation

The `random` module in Python is used whenever you need randomness in your program.

This includes things like:

- Games
- Password generators
- Simulations
- Random selections
- Shuffling data

Python makes all of this easy using the built-in `random` module.

---

# Importing the Module

```python
import random
```

---

# Why Use the `random` Module?

Without this module, generating random values manually would be difficult.

The `random` module gives us ready-to-use functions for:

- Random numbers
- Random choices
- Random shuffling
- Random floating-point values

---

# Commonly Used Functions

---

## 1. `random.randint()`

Returns a random integer between two numbers.

```python
import random

number = random.randint(1, 10)

print(number)
```

### Example Output

```text
7
```

### Important Note

Both numbers are included.

```python
random.randint(1, 10)
```

can return:

```text
1 or 10
```

---

## 2. `random.choice()`

Selects one random item from a list, string, or tuple.

```python
colors = ["red", "blue", "green"]

print(random.choice(colors))
```

### Example Output

```text
blue
```

---

## 3. `random.shuffle()`

Shuffles items inside a list.

```python
cards = [1, 2, 3, 4, 5]

random.shuffle(cards)

print(cards)
```

### Example Output

```text
[3, 1, 5, 2, 4]
```

### Important Note

`shuffle()` changes the original list directly.

---

## 4. `random.random()`

Returns a random decimal number between `0.0` and `1.0`.

```python
print(random.random())
```

### Example Output

```text
0.5839201
```

---

## 5. `random.uniform()`

Returns a random floating-point number between two values.

```python
print(random.uniform(1, 5))
```

### Example Output

```text
3.42
```

---

# Real Example: Dice Roller

```python
import random

dice = random.randint(1, 6)

print("You rolled:", dice)
```

---

# Real Example: Random Password Character

```python
import random
import string

characters = string.ascii_letters + string.digits

print(random.choice(characters))
```

---

# Real Example: Shuffle a Deck of Cards

```python
import random

cards = ["A", "K", "Q", "J"]

random.shuffle(cards)

print(cards)
```

---

# Best Practices

## Don't Use `random` for Security

The `random` module is fine for:

- Games
- Practice projects
- Simulations

But not for:

- Banking systems
- Cryptography
- Real authentication systems

For secure randomness, use:

```python
import secrets
```

instead.

---

# Summary

| Function | Purpose |
|----------|---------|
| `randint()` | Random integer |
| `choice()` | Random item |
| `shuffle()` | Shuffle list |
| `random()` | Random decimal |
| `uniform()` | Random decimal in range |

---

# Final Thoughts

The `random` module is one of the most fun modules in Python.

It’s beginner-friendly and immediately useful in projects like:

- Mini games
- Password generators
- Lottery systems
- Random quote generators
- Card games

Once you start building projects, you’ll probably use it everywhere.