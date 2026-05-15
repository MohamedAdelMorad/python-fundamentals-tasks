# ============================================================
# TASK SOLUTIONS - Complete Implementation
# ============================================================

import random

# ─────────────────────────────────────────────
# 1. Phonebook Manager
# ─────────────────────────────────────────────

phonebook = {}

def add_contact(name, phone):
    phonebook[name] = phone
    print(f"✅ Contact '{name}' added.")

def search_contact(name):
    if name in phonebook:
        print(f"📞 {name}: {phonebook[name]}")
    else:
        print(f"❌ '{name}' not found.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"🗑️ '{name}' deleted.")
    else:
        print(f"❌ '{name}' not found.")

def run_phonebook():
    print("\n===== Phonebook Manager =====")
    add_contact("Ahmed", "01012345678")
    add_contact("Sara", "01098765432")
    search_contact("Ahmed")
    search_contact("Mona")
    delete_contact("Sara")
    print("Phonebook:", phonebook)


# ─────────────────────────────────────────────
# 2. Student Exam Scores
# ─────────────────────────────────────────────

def compute_averages(scores_dict):
    return {name: sum(scores) / len(scores) for name, scores in scores_dict.items()}

def run_student_scores():
    print("\n===== Student Exam Scores =====")
    students = {"Ahmed": [80, 90, 85], "Sara": [70, 95, 88]}
    averages = compute_averages(students)
    for name, avg in averages.items():
        print(f"{name}: {avg:.2f}")


# ─────────────────────────────────────────────
# 3. Find Maximum in Matrix
# ─────────────────────────────────────────────

def find_max_in_matrix(matrix):
    max_val = matrix[0][0]
    max_row, max_col = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_row, max_col = i, j
    return max_val, max_row, max_col

def run_matrix_max():
    print("\n===== Find Maximum in Matrix =====")
    matrix = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]
    print("Matrix:")
    for row in matrix:
        print(row)
    val, r, c = find_max_in_matrix(matrix)
    print(f"Max Value: {val} at position (row={r}, col={c})")


# ─────────────────────────────────────────────
# 4. Transpose of Matrix
# ─────────────────────────────────────────────

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

def run_transpose():
    print("\n===== Transpose of Matrix =====")
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print("Original:")
    for row in matrix:
        print(row)
    trans = transpose(matrix)
    print("Transposed:")
    for row in trans:
        print(row)


# ─────────────────────────────────────────────
# 5. Remove Duplicates from List
# ─────────────────────────────────────────────

def remove_duplicates(lst):
    seen = []
    result = []
    for item in lst:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

def run_remove_duplicates():
    print("\n===== Remove Duplicates =====")
    original = [1, 2, 2, 3, 1, 4]
    print(f"Original : {original}")
    print(f"No Dupes : {remove_duplicates(original)}")


# ─────────────────────────────────────────────
# 6. Factorial Using Recursion + Combinations
# ─────────────────────────────────────────────

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def run_factorial():
    print("\n===== Factorial & Combinations =====")
    n, r = 6, 2
    print(f"factorial({n}) = {factorial(n)}")
    print(f"C({n}, {r}) = {combination(n, r)}")


# ─────────────────────────────────────────────
# 7. Banking System
# ─────────────────────────────────────────────

accounts = {}
next_account_number = 1001

def create_account(name, initial_deposit):
    global next_account_number
    if initial_deposit < 0:
        print("❌ Initial deposit cannot be negative.")
        return
    acc_num = str(next_account_number)
    accounts[acc_num] = {"name": name, "balance": initial_deposit}
    print(f"✅ Account created for {name}. Account #: {acc_num}")
    next_account_number += 1
    return acc_num

def deposit(account, amount):
    if account not in accounts:
        print("❌ Account not found.")
        return
    if amount <= 0:
        print("❌ Deposit amount must be positive.")
        return
    accounts[account]["balance"] += amount
    print(f"✅ Deposited ${amount:.2f}. New balance: ${accounts[account]['balance']:.2f}")

def withdraw(account, amount):
    if account not in accounts:
        print("❌ Account not found.")
        return
    if amount <= 0:
        print("❌ Withdrawal amount must be positive.")
        return
    if accounts[account]["balance"] < amount:
        print("❌ Insufficient funds.")
        return
    accounts[account]["balance"] -= amount
    print(f"✅ Withdrew ${amount:.2f}. New balance: ${accounts[account]['balance']:.2f}")

def check_balance(account):
    if account not in accounts:
        print("❌ Account not found.")
        return
    info = accounts[account]
    print(f"💰 {info['name']} (#{account}) Balance: ${info['balance']:.2f}")

def run_banking():
    print("\n===== Banking System =====")
    acc = create_account("Mohamed", 500)
    deposit(acc, 200)
    withdraw(acc, 100)
    withdraw(acc, 1000)
    check_balance(acc)


# ─────────────────────────────────────────────
# 8. Event Ticket Booking with Group Discount
# ─────────────────────────────────────────────

TICKET_PRICES = {"VIP": 150, "Regular": 80, "Balcony": 50}

def run_ticket_booking():
    print("\n===== Event Ticket Booking =====")

    name = input("Enter your name: ").strip()

    email = input("Enter your email: ").strip()
    if "@" not in email:
        print("❌ Invalid email. Must contain '@'.")
        return

    ticket_type = input("Ticket type (VIP / Regular / Balcony): ").strip().capitalize()
    if ticket_type not in TICKET_PRICES:
        print("❌ Invalid ticket type.")
        return

    try:
        num_tickets = int(input("Number of tickets: "))
    except ValueError:
        print("❌ Invalid number.")
        return

    if num_tickets > 10:
        print("❌ Maximum 10 tickets per person.")
        return

    children_count = 0
    has_children = input("Are there children under 12 in the group? (yes/no): ").strip().lower()
    if has_children == "yes":
        try:
            children_count = int(input(f"How many children (max {num_tickets})? "))
            if children_count > num_tickets:
                print("❌ Children count exceeds total tickets.")
                return
        except ValueError:
            print("❌ Invalid number.")
            return

    early_bird = input("Early bird code (or press Enter to skip): ").strip()
    group_booking = input("Group booking? (yes/no): ").strip().lower()

    price = TICKET_PRICES[ticket_type]
    adult_tickets = num_tickets - children_count
    total = (price * adult_tickets) + (price * 0.5 * children_count)

    print(f"\n{'='*40}")
    print(f"       🎟️  INVOICE - {name}")
    print(f"{'='*40}")
    print(f"Ticket Type   : {ticket_type}")
    print(f"Tickets       : {num_tickets} (Adults: {adult_tickets}, Children: {children_count})")
    print(f"Base Subtotal : ${total:.2f}")

    if children_count > 0:
        child_discount = price * 0.5 * children_count
        print(f"Children Disc.: -${child_discount:.2f} (50% for {children_count} child(ren))")

    early_applied = False
    if early_bird == "EARLY25":
        total *= 0.75
        early_applied = True
        print(f"Early Bird 25%: Applied → ${total:.2f}")

    group_applied = False
    if group_booking == "yes" and num_tickets >= 4:
        total *= 0.88
        group_applied = True
        print(f"Group Disc.12%: Applied → ${total:.2f}")

    total *= 1.07
    print(f"Tax 7%        : Applied")
    print(f"{'='*40}")
    print(f"FINAL TOTAL   : ${total:.2f}")
    print(f"{'='*40}")
    print(f"Thank you, {name}! Enjoy the event! 🎉")


# ─────────────────────────────────────────────
# 9. Restaurant Order System with Membership Card
# ─────────────────────────────────────────────

MENU = {"Burger": 8, "Pizza": 12, "Salad": 6, "Pasta": 10}

def run_restaurant():
    print("\n===== Restaurant Order System =====")
    print("Menu:")
    for item, price in MENU.items():
        print(f"  {item}: ${price}")

    customer_name = input("\nCustomer name: ").strip()

    try:
        age = int(input("Age: "))
    except ValueError:
        print("❌ Invalid age.")
        return

    item = input("Item ordered: ").strip().capitalize()
    if item not in MENU:
        print("❌ Item not on menu.")
        return

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("❌ Invalid quantity.")
        return

    membership = input("Membership card? (yes/no): ").strip().lower()
    special_code = input("Special code (or Enter to skip): ").strip()

    price = MENU[item]
    subtotal = price * quantity

    # Determine best discount (membership 15% vs code 20%)
    discount_rate = 0
    discount_label = "None"

    if membership == "yes":
        discount_rate = 0.15
        discount_label = "Membership 15%"

    if special_code == "WELCOME20":
        if 0.20 > discount_rate:
            discount_rate = 0.20
            discount_label = "Code WELCOME20 (20%)"

    total = subtotal * (1 - discount_rate)

    # Senior discount (stacks on top)
    senior_applied = False
    if age >= 60:
        total *= 0.90
        senior_applied = True

    # Service charge if total before tax > $50
    service_applied = False
    if total > 50:
        total *= 1.10
        service_applied = True

    # Tax 8%
    total *= 1.08

    print(f"\n{'='*40}")
    print(f"       🍽️  RECEIPT - {customer_name}")
    print(f"{'='*40}")
    print(f"Item          : {item} x{quantity}")
    print(f"Subtotal      : ${subtotal:.2f}")
    print(f"Discount      : {discount_label}")
    if senior_applied:
        print(f"Senior Disc.  : 10% (age {age})")
    if service_applied:
        print(f"Service Charge: 10% (order > $50)")
    print(f"Tax 8%        : Applied")
    print(f"{'='*40}")
    print(f"TOTAL         : ${total:.2f}")
    print(f"{'='*40}")
    print(f"Thanks for dining with us, {customer_name}! 😊")


# ─────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────

def main():
    tasks = {
        "1": ("Phonebook Manager",          run_phonebook),
        "2": ("Student Exam Scores",         run_student_scores),
        "3": ("Find Max in Matrix",           run_matrix_max),
        "4": ("Transpose of Matrix",          run_transpose),
        "5": ("Remove Duplicates from List",  run_remove_duplicates),
        "6": ("Factorial & Combinations",     run_factorial),
        "7": ("Banking System",               run_banking),
        "8": ("Event Ticket Booking",         run_ticket_booking),
        "9": ("Restaurant Order System",      run_restaurant),
    }

    print("\n========== TASK RUNNER ==========")
    for key, (name, _) in tasks.items():
        print(f"  {key}. {name}")
    print("  0. Run all non-interactive tasks (1-7)")
    print("=================================")

    choice = input("Choose a task (0-9): ").strip()

    if choice == "0":
        for key in ["1", "2", "3", "4", "5", "6", "7"]:
            tasks[key][1]()
    elif choice in tasks:
        tasks[choice][1]()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()