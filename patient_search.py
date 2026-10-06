import sqlite3


# ============================================================
# CONNECT DATABASE
# ============================================================

connection = sqlite3.connect("securehealth.db")
cursor = connection.cursor()


# ============================================================
# PATIENT SEARCH
# ============================================================

print("\n" + "=" * 65)
print("             SECUREHEALTH PATIENT SEARCH")
print("=" * 65)

print("\nEnter Patient ID or Patient Name")

search = input("\nSearch: ").strip()


# ============================================================
# SEARCH DATABASE
# ============================================================

cursor.execute("""
SELECT
    patient_id,
    name,
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
WHERE patient_id = ?
   OR LOWER(name) = LOWER(?)
""", (
    search.upper(),
    search
))


patient = cursor.fetchone()


# ============================================================
# DISPLAY
# ============================================================

if patient:

    print("\n" + "=" * 65)
    print("                  PATIENT RECORD")
    print("=" * 65)

    print(f"\nPatient ID      : {patient[0]}")
    print(f"Name            : {patient[1]}")
    print(f"Age             : {patient[2]}")
    print(f"Gender          : {patient[3]}")
    print(f"Blood Group     : {patient[4]}")
    print(f"Phone           : {patient[5]}")
    print(f"Diagnosis       : {patient[6]}")
    print(f"Doctor          : {patient[7]}")
    print(f"Department      : {patient[8]}")
    print(f"Medical History : {patient[9]}")
    print(f"Allergies       : {patient[10]}")

    print("\n" + "=" * 65)


else:

    print("\n❌ Patient record not found.")


connection.close()