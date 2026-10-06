import sqlite3
import bcrypt
import sys


# ============================================================
# ACCOUNT TYPE
# ============================================================

if len(sys.argv) < 2:

    print("Please start login through main.py.")
    exit()


account_type = sys.argv[1]


# ============================================================
# DATABASE
# ============================================================

connection = sqlite3.connect("securehealth.db")
cursor = connection.cursor()


print("\n" + "=" * 65)
print("                  SECUREHEALTH")
print("            HEALTHCARE SECURITY SYSTEM")
print("=" * 65)


# ============================================================
# STAFF LOGIN
# ============================================================

if account_type == "staff":

    employee_id = input("\nEmployee ID: ").strip().upper()

    password = input("Password: ")


    cursor.execute("""
    SELECT
        employee_id,
        full_name,
        email,
        department,
        role,
        password_hash
    FROM staff
    WHERE employee_id = ?
    """, (employee_id,))


    staff = cursor.fetchone()


    if staff is None:

        print("\n❌ Invalid Employee ID or Password.")

        connection.close()
        exit()


    stored_hash = staff[5]


    # --------------------------------------------------------
    # VERIFY PASSWORD
    # --------------------------------------------------------

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    ):

        print("\n❌ Invalid Employee ID or Password.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # SUCCESS
    # --------------------------------------------------------

    print("\n" + "=" * 65)
    print("✓ AUTHENTICATION SUCCESSFUL")
    print("=" * 65)

    print(f"\nEmployee ID : {staff[0]}")
    print(f"Name        : {staff[1]}")
    print(f"Email       : {staff[2]}")
    print(f"Department  : {staff[3]}")
    print(f"Role        : {staff[4]}")

    print("\n" + "-" * 65)
    print("ROLE-BASED ACCESS")
    print("-" * 65)


    if staff[4] == "Doctor":

        print("✓ Patient medical records")
        print("✓ Medical history")
        print("✓ Patient reports")


    elif staff[4] == "Nurse":

        print("✓ Authorized patient records")
        print("✓ Patient care information")
        print("✗ Restricted administrative controls")


    elif staff[4] == "Hospital Administrator":

        print("✓ Hospital administration")
        print("✓ Staff management")
        print("✗ Restricted medical modifications")


    elif staff[4] == "Security Administrator":

        print("✓ Security monitoring")
        print("✓ Access logs")
        print("✓ Security controls")


# ============================================================
# PATIENT LOGIN
# ============================================================

elif account_type == "patient":

    credential = input("\nName or Email: ").strip()

    password = input("Password: ")


    cursor.execute("""
    SELECT
        patient_id,
        name,
        email,
        age,
        gender,
        blood_group,
        phone,
        diagnosis,
        doctor,
        department,
        medical_history,
        allergies
    FROM patients
    WHERE
        LOWER(name) = LOWER(?)
        OR LOWER(email) = LOWER(?)
    """, (
        credential,
        credential
    ))


    patient = cursor.fetchone()


    if patient is None:

        print("\n❌ Invalid Name/Email or Password.")

        connection.close()
        exit()


    # --------------------------------------------------------
    # PATIENT PASSWORD
    # --------------------------------------------------------
    #
    # For the first version we will create a separate
    # patient_accounts table next.
    #
    # This section currently demonstrates patient record
    # retrieval only.
    # --------------------------------------------------------

    print("\n✓ Patient record located.")

    print("\n" + "=" * 65)
    print("                  PATIENT INFORMATION")
    print("=" * 65)

    print(f"\nPatient ID      : {patient[0]}")
    print(f"Name            : {patient[1]}")
    print(f"Email           : {patient[2]}")
    print(f"Age             : {patient[3]}")
    print(f"Gender          : {patient[4]}")
    print(f"Blood Group     : {patient[5]}")
    print(f"Phone           : {patient[6]}")
    print(f"Diagnosis       : {patient[7]}")
    print(f"Doctor          : {patient[8]}")
    print(f"Department      : {patient[9]}")
    print(f"Medical History : {patient[10]}")
    print(f"Allergies       : {patient[11]}")


else:

    print("\n❌ Invalid account type.")


connection.close()