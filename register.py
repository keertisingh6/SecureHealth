import sqlite3
import bcrypt
import sys
import re


# ============================================================
# CHECK ACCOUNT TYPE
# ============================================================

if len(sys.argv) < 2:

    print("Please start registration through main.py.")
    exit()


account_type = sys.argv[1]


# ============================================================
# DATABASE
# ============================================================

connection = sqlite3.connect("securehealth.db")
cursor = connection.cursor()


print("\n" + "=" * 65)
print("                  SECUREHEALTH")
print("                ACCOUNT REGISTRATION")
print("=" * 65)


# ============================================================
# STAFF REGISTRATION
# ============================================================

if account_type == "staff":

    print("\nHospital Staff Registration")

    employee_id = input("\nEmployee ID: ").strip().upper()


    # --------------------------------------------------------
    # IDENTIFY ROLE FROM EMPLOYEE ID
    # --------------------------------------------------------

    role_patterns = {

        "DR": "Doctor",

        "NU": "Nurse",

        "HA": "Hospital Administrator",

        "SA": "Security Administrator"
    }


    prefix = employee_id[:2]


    if prefix not in role_patterns:

        print("\n❌ Invalid Employee ID.")
        print("\nValid formats:")
        print("DR1234 - Doctor")
        print("NU1234 - Nurse")
        print("HA1234 - Hospital Administrator")
        print("SA1234 - Security Administrator")

        connection.close()
        exit()


    if not re.fullmatch(
        r"(DR|NU|HA|SA)\d{4}",
        employee_id
    ):

        print("\n❌ Invalid Employee ID format.")
        print("Example: DR1234")

        connection.close()
        exit()


    role = role_patterns[prefix]


    print(f"\nDetected Account Role: {role}")


    # --------------------------------------------------------
    # CHECK WHETHER ID ALREADY EXISTS
    # --------------------------------------------------------

    cursor.execute("""
    SELECT employee_id
    FROM staff
    WHERE employee_id = ?
    """, (employee_id,))


    if cursor.fetchone():

        print("\n❌ Employee ID already registered.")
        print("Please use the Login option.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # NEW EMPLOYEE INFORMATION
    # --------------------------------------------------------

    full_name = input("\nFull Name: ").strip()

    email = input("Official Email: ").strip().lower()

    department = input("Department: ").strip()


    # --------------------------------------------------------
    # EMAIL VALIDATION
    # --------------------------------------------------------

    if not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        email
    ):

        print("\n❌ Invalid email address.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # PASSWORD
    # --------------------------------------------------------

    password = input("Create Password: ")

    confirm_password = input("Confirm Password: ")


    if password != confirm_password:

        print("\n❌ Passwords do not match.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # PASSWORD REQUIREMENTS
    # --------------------------------------------------------

    if len(password) < 8:

        print("\n❌ Password must contain at least 8 characters.")

        connection.close()
        exit()


    if not re.search(r"[A-Z]", password):

        print("\n❌ Password must contain an uppercase letter.")

        connection.close()
        exit()


    if not re.search(r"[a-z]", password):

        print("\n❌ Password must contain a lowercase letter.")

        connection.close()
        exit()


    if not re.search(r"\d", password):

        print("\n❌ Password must contain a number.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # HASH PASSWORD
    # --------------------------------------------------------

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


    # --------------------------------------------------------
    # CREATE NEW STAFF ACCOUNT
    # --------------------------------------------------------

    cursor.execute("""
    INSERT INTO staff
    (
        employee_id,
        full_name,
        email,
        department,
        role,
        password_hash
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        employee_id,
        full_name,
        email,
        department,
        role,
        password_hash
    ))


    connection.commit()


    print("\n" + "=" * 65)
    print("✓ REGISTRATION SUCCESSFUL")
    print("=" * 65)

    print(f"\nEmployee ID : {employee_id}")
    print(f"Name        : {full_name}")
    print(f"Role        : {role}")
    print(f"Department  : {department}")

    print("\nPassword has been securely hashed.")
    print("You can now use the Login option.")


# ============================================================
# PATIENT REGISTRATION
# ============================================================

elif account_type == "patient":

    print("\nPatient Registration")

    full_name = input("\nFull Name: ").strip()

    email = input("Email: ").strip().lower()

    age = input("Age: ").strip()

    gender = input("Gender: ").strip()

    blood_group = input("Blood Group: ").strip()

    phone = input("Phone Number: ").strip()


    # --------------------------------------------------------
    # VALIDATE EMAIL
    # --------------------------------------------------------

    if not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        email
    ):

        print("\n❌ Invalid email address.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # CHECK EMAIL
    # --------------------------------------------------------

    cursor.execute("""
    SELECT patient_id
    FROM patients
    WHERE LOWER(email) = LOWER(?)
    """, (email,))


    if cursor.fetchone():

        print("\n❌ A patient with this email already exists.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # PASSWORD
    # --------------------------------------------------------

    password = input("Create Password: ")

    confirm_password = input("Confirm Password: ")


    if password != confirm_password:

        print("\n❌ Passwords do not match.")

        connection.close()
        exit()


    if len(password) < 8:

        print("\n❌ Password must contain at least 8 characters.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # HASH PASSWORD
    # --------------------------------------------------------

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


    # --------------------------------------------------------
    # CREATE PATIENT RECORD
    # --------------------------------------------------------

    cursor.execute("""
    INSERT INTO patients
    (
        name,
        email,
        age,
        gender,
        blood_group,
        phone
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        full_name,
        email,
        age,
        gender,
        blood_group,
        phone
    ))


    connection.commit()


    patient_id = cursor.lastrowid


    print("\n" + "=" * 65)
    print("✓ PATIENT REGISTRATION SUCCESSFUL")
    print("=" * 65)

    print(f"\nPatient Name : {full_name}")
    print(f"Patient ID   : {patient_id}")

    print("\nAccount created successfully.")
    print("Your Patient ID is generated automatically.")


else:

    print("\nInvalid account type.")


connection.close()