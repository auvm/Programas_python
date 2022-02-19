guests = ["john lennon", "emiliano zapata", "porfirio díaz"]
print(f"Hi {guests[0].title()} I invite you to a breakfast.")
print(f"Hi {guests[1].title()} I invite you to a breakfast.")
print(f"Hi {guests[2].title()} I invite you to a breakfast.")

print(f"Oh No! {guests[2].title()} won't came here.")

guests[2] = "tyler joseph"


print(f"Now {guests[2].title()} is invited you my breakfast.")