# Nonce Mining Simulation

This project simulates the core idea behind blockchain mining — finding a valid hash by incrementing a **nonce** until a certain difficulty condition is met (e.g., the hash starts with `"0000"`).

> This helps you understand how computational effort ensures block integrity and why tampering is hard in real blockchains.

---

## What It Does

- Defines a simple `Block` class in Python
- Includes `mine_block(difficulty)` method that simulates mining
- Increments nonce until hash starts with a certain number of `0`s
- Measures and prints:
  - Number of attempts (nonce count)
  - Time taken to mine
  - Final valid hash

---

## How Mining Works

The `mine_block()` method does the heavy lifting:

```python
while not self.hash.startswith('0' * difficulty):
    self.nonce += 1
    self.hash = self.calculate_hash()
