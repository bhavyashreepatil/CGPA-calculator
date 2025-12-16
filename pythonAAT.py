print("----------------------------------------------------------CGPA CALCULATOR-------------------------------------------------------")
sub = {
    "Maths": 4,
    "ETC":3,
    "ESC":3,
}
sub_lab={
    "Chemistry": 4,
    "Python":3,
}
def best_two_cie(cie_marks):
    cie_marks.sort(reverse=True)
    return cie_marks[0] + cie_marks[1]

def grade_point(total_marks):
    if total_marks >= 90:
        return 10
    elif total_marks >= 80:
        return 9
    elif total_marks >= 70:
        return 8
    elif total_marks >= 60:
        return 7
    elif total_marks >= 50:
        return 6
    elif total_marks >= 40:
        return 5
    else:
        return 0


total_credit_points = 0
total_credits = 0

for subject, credit in sub.items():
    print(f"\nEnter marks for {subject}")

    cie1 = float(input("CIE 1 (out of 20): "))
    cie2 = float(input("CIE 2 (out of 20): "))
    cie3 = float(input("CIE 3 (out of 20): "))

    cie_total = best_two_cie([cie1, cie2, cie3])

    aat = float(input("AAT/Quiz (out of 10): "))
    see=float(input("SEE marks (out of 100): "))
    reduced_see= see/2
    total_marks = cie_total + aat +reduced_see

    gp = grade_point(total_marks)

    total_credit_points += gp * credit
    total_credits += credit

    print(f"Best 2 CIE total: {cie_total}")
    print(f"Total Marks: {total_marks}")
    print(f"Grade Point: {gp}")
    print("------------------------------------------------------------------------------------------------------------------------------")
for subject,credit in sub_lab.items():
    print(f"\nEnter marks for {subject}")

    cie1 = float(input("CIE 1 (out of 10): "))
    cie2 = float(input("CIE 2 (out of 10): "))
    cie3 = float(input("CIE 3 (out of 10): "))

    cie_total = best_two_cie([cie1, cie2, cie3])

    aat = float(input("AAT / Quiz (out of 5): "))
    lab=float(input("Enter the lab marks(out of 25): "))
    see=float(input("SEE Marks(out of 100): "))
    reduced_see=see/2
    total_marks = cie_total + aat + lab +reduced_see

    gp = grade_point(total_marks)

    total_credit_points += gp * credit
    total_credits += credit

    print(f"Best 2 CIE total: {cie_total}")
    print(f"Total Marks: {total_marks}")
    print(f"Grade Point: {gp}")
    print("------------------------------------------------------------------------------------------------------------------------------")

sgpa = total_credit_points / total_credits
print("\n-----------------------------")
print(f"SGPA = {sgpa:.2f}")

