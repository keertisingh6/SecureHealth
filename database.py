import sqlite3
import bcrypt


# ============================================================
# DATABASE CONNECTION
# ============================================================

connection = sqlite3.connect("securehealth.db")
cursor = connection.cursor()


# ============================================================
# STAFF TABLE
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS staff (
    employee_id TEXT PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    role TEXT NOT NULL,
    password_hash TEXT
)
""")


# ============================================================
# PATIENT TABLE
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    gender TEXT,
    blood_group TEXT,
    phone TEXT,
    diagnosis TEXT,
    doctor TEXT,
    department TEXT,
    medical_history TEXT,
    allergies TEXT
)
""")


# ============================================================
# 20 INITIAL PATIENT RECORDS
# ============================================================

patients = [

    ("Aarav Mehta", "aarav@gmail.com", 28, "Male", "B+",
     "9876543210", "Hypertension", "Dr. Ananya",
     "Cardiology", "Family history of hypertension", "None"),

    ("Diya Sharma", "diya@gmail.com", 34, "Female", "O+",
     "9876543211", "Type 2 Diabetes", "Dr. Vikram Rao",
     "Endocrinology", "Diabetes diagnosed in 2022", "Penicillin"),

    ("Rohan Kapoor", "rohan@gmail.com", 45, "Male", "A+",
     "9876543212", "Asthma", "Dr. Ananya",
     "Pulmonology", "Chronic asthma since childhood", "Dust"),

    ("Ananya Singh", "ananya.patient@gmail.com", 22, "Female", "AB+",
     "9876543213", "Migraine", "Dr. Vikram Rao",
     "Neurology", "Recurring migraine episodes", "None"),

    ("Kabir Patel", "kabir@gmail.com", 51, "Male", "B-",
     "9876543214", "High Cholesterol", "Dr. Ananya",
     "Cardiology", "High cholesterol under monitoring", "None"),

    ("Meera Joshi", "meera.patient@gmail.com", 39, "Female", "O-",
     "9876543215", "Thyroid Disorder", "Dr. Vikram Rao",
     "Endocrinology", "Hypothyroidism", "Sulfa drugs"),

    ("Arjun Nair", "arjun@gmail.com", 31, "Male", "A+",
     "9876543216", "Gastritis", "Dr. Ananya",
     "Gastroenterology", "Recurring gastritis", "None"),

    ("Isha Malhotra", "isha@gmail.com", 27, "Female", "B+",
     "9876543217", "Anemia", "Dr. Vikram Rao",
     "General Medicine", "Iron deficiency anemia", "None"),

    ("Vivaan Shah", "vivaan@gmail.com", 63, "Male", "O+",
     "9876543218", "Coronary Artery Disease", "Dr. Ananya",
     "Cardiology", "Previous cardiac episode", "Aspirin"),

    ("Sara Khan", "sara@gmail.com", 29, "Female", "A-",
     "9876543219", "PCOS", "Dr. Vikram Rao",
     "Gynecology", "PCOS under treatment", "None"),

    ("Aditya Verma", "aditya@gmail.com", 42, "Male", "B+",
     "9876543220", "Kidney Stones", "Dr. Ananya",
     "Urology", "Previous kidney stone", "None"),

    ("Nisha Gupta", "nisha@gmail.com", 36, "Female", "O+",
     "9876543221", "Vitamin D Deficiency", "Dr. Vikram Rao",
     "General Medicine", "Low vitamin D levels", "None"),

    ("Dev Rao", "dev@gmail.com", 55, "Male", "AB+",
     "9876543222", "Hypertension", "Dr. Ananya",
     "Cardiology", "Long-term hypertension", "None"),

    ("Riya Desai", "riya@gmail.com", 24, "Female", "B+",
     "9876543223", "Asthma", "Dr. Vikram Rao",
     "Pulmonology", "Exercise-induced asthma", "Pollen"),

    ("Yash Agarwal", "yash@gmail.com", 48, "Male", "A+",
     "9876543224", "Type 2 Diabetes", "Dr. Ananya",
     "Endocrinology", "Diabetes under medication", "None"),

    ("Tanya Roy", "tanya@gmail.com", 33, "Female", "O-",
     "9876543225", "Migraine", "Dr. Vikram Rao",
     "Neurology", "Frequent migraine episodes", "None"),

    ("Kunal Bhat", "kunal@gmail.com", 60, "Male", "B-",
     "9876543226", "Arthritis", "Dr. Ananya",
     "Orthopedics", "Knee arthritis", "NSAIDs"),

    ("Pooja Iyer", "pooja@gmail.com", 41, "Female", "A+",
     "9876543227", "Hypertension", "Dr. Vikram Rao",
     "Cardiology", "Controlled hypertension", "None"),

    ("Manav Sethi", "manav@gmail.com", 26, "Male", "O+",
     "9876543228", "Gastritis", "Dr. Ananya",
     "Gastroenterology", "Acid reflux", "None"),

    ("Sneha Kulkarni", "sneha@gmail.com", 50, "Female", "AB-",
     "9876543229", "Thyroid Disorder", "Dr. Vikram Rao",
     "Endocrinology", "Hypothyroidism", "Penicillin")
]


# ============================================================
# INSERT PATIENTS
# ============================================================

for patient in patients:

    cursor.execute("""
    INSERT OR IGNORE INTO patients
    (
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
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, patient)


# ============================================================
# EXISTING HOSPITAL STAFF
# ============================================================
# These are existing employees who can LOGIN.
# New employees can REGISTER later.

staff_members = [

    (
        "DR1234",
        "Dr. Ananya",
        "ananya@securehealth.com",
        "Cardiology",
        "Doctor",
        "DrAnanya@123"
    ),

    (
        "DR1235",
        "Dr. Vikram Rao",
        "vikram@securehealth.com",
        "Endocrinology",
        "Doctor",
        "Vikram@123"
    ),

    (
        "NU1234",
        "Rahul Sharma",
        "rahul@securehealth.com",
        "Emergency",
        "Nurse",
        "Rahul@123"
    ),

    (
        "HA1234",
        "Priya Mehta",
        "priya@securehealth.com",
        "Hospital Administration",
        "Hospital Administrator",
        "Priya@123"
    ),

    (
        "SA1234",
        "Security Administrator",
        "security@securehealth.com",
        "Cybersecurity",
        "Security Administrator",
        "Security@123"
    )
]


# ============================================================
# CREATE EXISTING STAFF ACCOUNTS
# ============================================================

for employee_id, name, email, department, role, password in staff_members:

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    cursor.execute("""
    INSERT OR IGNORE INTO staff
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
        name,
        email,
        department,
        role,
        password_hash
    ))


# ============================================================
# SAVE DATABASE
# ============================================================

connection.commit()
connection.close()


print("\n" + "=" * 65)
print("              SECUREHEALTH DATABASE READY")
print("=" * 65)
print("\n✓ 20 patient records created")
print("✓ Existing staff accounts created")
print("✓ Staff roles and departments stored")
print("✓ Passwords stored using bcrypt hashing")
print("\nDatabase setup completed successfully.")
print("=" * 65)