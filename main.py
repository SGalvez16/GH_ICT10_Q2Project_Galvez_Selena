from pyscript import display
from js import document

# ---------- Helper ----------
def safe_float(id):
    value = document.getElementById(id).value
    return float(value) if value else 0


# ---------- Grade Calculator ----------
def calculate_gwa(event):
    fname = document.getElementById("text1").value
    lname = document.getElementById("text2").value

    sci = safe_float("text3") * 5
    eng = safe_float("text4") * 5
    math = safe_float("text5") * 5
    ict = safe_float("text6") * 2
    pe = safe_float("text7") * 1
    fil = safe_float("text8") * 3

    total_units = 5 + 5 + 5 + 2 + 1 + 3
    gwa = (sci + eng + math + ict + pe + fil) / total_units

    result = f"""
Name: {fname} {lname}
----------------------
Science: {sci}
English: {eng}
Math: {math}
ICT: {ict}
PE: {pe}
Filipino: {fil}
----------------------
Final GWA: {gwa:.2f}
"""

    document.getElementById("output").innerText = result.strip()


# ---------- Club Information ----------
clubs = {
    "Tennis Club": {
        "Description": "A club for tennis enthusiasts.",
        "Meeting Time": "Monday 3 PM",
        "Location": "Gym Hall",
        "Advisor": "Mr. De Guzman",
        "Number of Members": 25,
        "Category": "Sports",
    },
    "Math Club": {
        "Description": "A club for math lovers.",
        "Meeting Time": "Tuesday 2 PM",
        "Location": "Room 101",
        "Advisor": "Mrs. Alfaro",
        "Number of Members": 30,
        "Category": "Academic",
    },
    "Music Club": {
        "Description": "A club for students who love music.",
        "Meeting Time": "Wednesday 4 PM",
        "Location": "Music Room",
        "Advisor": "Mr. Ortiz",
        "Number of Members": 20,
        "Category": "Arts",
    },
    "Debate Club": {
        "Description": "A club for debate lovers.",
        "Meeting Time": "Thursday 3 PM",
        "Location": "Room 202",
        "Advisor": "Ms. Jimenez",
        "Number of Members": 15,
        "Category": "Academic",
    },
}

def show_club_info(event):
    selected = document.getElementById("clubs").value

    if selected not in clubs:
        document.getElementById("output").innerText = "Please select a valid club."
        return

    info = clubs[selected]

    result = f"""
{selected}
----------------------
Description: {info['Description']}
Meeting Time: {info['Meeting Time']}
Location: {info['Location']}
Advisor: {info['Advisor']}
Members: {info['Number of Members']}
Category: {info['Category']}
"""

    document.getElementById("output").innerText = result.strip()
