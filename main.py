import subprocess
import sys


print("\n" + "=" * 65)
print("                  SECUREHEALTH")
print("            HEALTHCARE SECURITY SYSTEM")
print("=" * 65)


print("\nSelect Account Type")

print("\n1. Hospital Staff")
print("2. Patient")


account_type = input("\nEnter selection: ").strip()


# ============================================================
# HOSPITAL STAFF
# ============================================================

if account_type == "1":

    print("\n" + "=" * 65)
    print("                    HOSPITAL STAFF")
    print("=" * 65)

    print("\n1. Login")
    print("2. Register")

    choice = input("\nEnter selection: ").strip()

    if choice == "1":

        subprocess.run([
            sys.executable,
            "login.py",
            "staff"
        ])

    elif choice == "2":

        subprocess.run([
            sys.executable,
            "register.py",
            "staff"
        ])

    else:

        print("\nInvalid selection.")


# ============================================================
# PATIENT
# ============================================================

elif account_type == "2":

    print("\n" + "=" * 65)
    print("                       PATIENT")
    print("=" * 65)

    print("\n1. Login")
    print("2. Register")

    choice = input("\nEnter selection: ").strip()

    if choice == "1":

        subprocess.run([
            sys.executable,
            "login.py",
            "patient"
        ])

    elif choice == "2":

        subprocess.run([
            sys.executable,
            "register.py",
            "patient"
        ])

    else:

        print("\nInvalid selection.")


else:

    print("\nInvalid selection.")