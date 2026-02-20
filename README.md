## LIST OF GROUP MEMBERS

1. EBUBE EMMANUEL EZEDIMBU (2022514081)
2. CHINECHETAM JACINTA OLIBIE (2022514057)
3. CHUKWUMA EMMANUEL PRINCE (2022514202)
4. EDEM VICTOR CHUKWUEMEKA (2022514133)
5. NNOLUM VIVIAN CHISOM (2022514008)
6. OGBODO FAVOUR CHIMDINDU (2022514051)
7. NWOBU NZUBECHUKWU (2022554059)
8. EKEMEZIE CHIBUIKEM AZUKA (2022514099)
9. UZOMBA MIRACLE (2022514006)
10. MADUKEME-ONYI CHISOMAGA (2022514048)
11. OBI NNAEMEKA EMMANUEL (2022514089)
12. OKOYE MEYANNA ABUNDANCE (2022514141)
13. IHEANYI VALENTINE KELECHI (2022514117)
14. NNAJI KENECHUKWU THANKGOD (2022514168)
15. NWACHUKWU DANIEL CHIBUIKE (2022514175)
16. DUNU CHUKWUEMEKA REX (2022514002)
17. RICHARD KENECHI MICHAEL(2022514179)
18. EZEANYIM NMESOMA (2022514158)
19. DIM-OBINNA DABERECHI (2022514033)
20. ILECHUKWU CHIZOBA (2022514176)
21. ETEKA CLEMENT CHUKWUEMEKA (2022544098)
22. OKEKE EMMANUEL CHIDERA (2022514012)
23. IWOGBE UZOCHUKWU CHIDIEBERE (2022514034)
24. ODIMEGWU VICTOR CHUKWUNWIKE (2022514195)
25. OFFORNEJELU IFUNANYA PRECIOUS (2022514086)
26. OGBU THANKGOD CHIKWUEUCHEYA (2022514010)

## Bank Account Management System (OOP)

### Overview

This is a simple **Bank Account Management System** written in Python for a school OOP assignment. It demonstrates:

- **Abstraction**: `Account` is an abstract base class defining `deposit()`, `withdraw()`, and `calculate_interest()`.
- **Encapsulation**: account details are stored in private attributes and accessed through getter/setter methods.
- **Polymorphism**: the program stores different account objects together and calls the same methods on each.

The program includes two account types:

- `SavingsAccount`: minimum balance rule + earns monthly interest
- `CurrentAccount`: allows overdraft up to a limit + applies overdraft charge when negative

### Project Structure

```text
CSC 461 GROUP 2/
  main.py
  README.md
```

### Requirements

- Python 3.8+ (recommended)
- No external libraries required

### Clone (Git)

If you have a GitHub (or other Git) repository URL for this project, clone it with:

```bash
git clone <REPO_URL>
cd <REPO_FOLDER>
```

If you **don’t** have a repository URL (for example you submitted as a folder), you can skip cloning and just run the files directly.

### Run

```bash
python main.py
```

### Troubleshooting

- If `python` is not recognized on Windows, try: `py main.py`
- If you have multiple Python versions installed, try: `python --version`

### What The Program Does

When you run `main.py`, it:

1. Creates a `SavingsAccount` and a `CurrentAccount`
2. Performs deposits and withdrawals (polymorphically)
3. Rejects invalid transactions using error handling (e.g., negative deposits, withdrawals beyond limits)
4. Applies interest/charges depending on the account type
5. Prints clear account summaries to the terminal
