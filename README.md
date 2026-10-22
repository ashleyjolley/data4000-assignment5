# data4000-assignment5

Conditionals, Loops, Exceptions, and Libraries

This repository contains two Python programs demonstrating conditionals, while loops, exception handling, functions and libraries, and command-line interaction.

Exercise 1: POS Checkout System

File: pos_checkout.py

This program allows a cashier to enter items, prices, and quantities. It validates user input, calculates the subtotal, applies a discount, and determines whether a seed-based perk is available.

Run:

python pos_checkout.py

Example run:

Student key: A
Item name (or DONE): Notebook
Unit price: 20
Quantity: 5
Item name (or DONE): DONE
Seed: 65
Units: 5
Subtotal: $100.00
Discount: 10%
Perk applied: YES
Total: $87.00

Exercise 2: Inventory Reorder Analyzer

File: inventory_spotcheck.py

This program collects SKU inventory counts, identifies products that require reordering, and performs an API spot check using the iTunes Search API.

Install required library:

pip install requests

Run:

python inventory_spotcheck.py

Example run (illustrative API result):

Student key: A
SKU: ITEM001
On hand: 5
SKU: ITEM002
On hand: 20
SKU: DONE
Seed: 65
Threshold: 9
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: drake
Songs returned: 5
API status: OK

The song count and API status depend on the live API response.

Requirements

Python 3.x

requests library

Terminal or VS Code terminal