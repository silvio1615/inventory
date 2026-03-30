# 🛒 Product Input & Cost Calculator

A simple Python script that collects product information from the user via the terminal, validates each input, and displays the total cost in a formatted summary line.

---

## 🔄 Flow Diagram

<img width="360" height="912" alt="flowchart" src="https://github.com/user-attachments/assets/7f1f552c-885a-485e-80ab-133f04211290" />

  

---

## ✨ Features

- Collects product name, quantity, and unit price interactively from the terminal
- Validates that quantity is a **positive integer** — retries automatically on bad input
- Validates that price is a **positive float** — retries automatically on bad input
- Uses `try/except` with `ValueError` to handle non-numeric input gracefully
- Calculates total cost (`price × quantity`) and displays a formatted summary

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

No external libraries required.

### Run the script

```bash
python main.py
```

---

## 🖥️ Example Session

```
Enter product name: Laptop
Enter the product quantity: -5
Error: please enter a positive value for the quantity.
Enter the product quantity: abc
Error: please enter a valid number.
Enter the product quantity: 3
Enter the product price: 899.99
Product: Laptop | Quantity: 3 | Unit price: $899.99 | Total cost: $2699.97
```

---

## 🛠️ How It Works

The script uses **boolean flags** (`val_cant`, `val_price`) as loop controllers — a common Python pattern for input validation without breaking the control flow abruptly.

Each validation loop works like this:

1. Flag is set to `True` to enter the loop
2. Inside the loop, the input is attempted inside a `try` block
3. If the conversion fails (`ValueError`), an error message is printed and the loop repeats
4. If the value is negative, an error message is printed and the loop repeats
5. If the value is valid, the flag is set to `False` to exit the loop

Once both inputs are validated, `total_cost` is calculated and printed in a single formatted line using an f-string.

---

## 📋 Variables Reference

| Variable | Type | Description |
|---|---|---|
| `product` | `str` | Name of the product entered by the user |
| `quantity` | `int` | Number of units (must be ≥ 0) |
| `price` | `float` | Unit price (must be ≥ 0) |
| `total_cost` | `float` | Calculated as `price × quantity` |
| `val_cant` | `bool` | Loop flag for quantity validation |
| `val_price` | `bool` | Loop flag for price validation |

---

