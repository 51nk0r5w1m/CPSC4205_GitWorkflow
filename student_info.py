name = "Carley Fant"
email = "fant_carley@colstate.view.usg.edu"
major = "Information Technology"
graduation_year = 2026
hometown = "Atlanta"
interest = "AppSec/DevSecOps/Identity"
title = "STUDENT INFORMATION CARD"

width = 50          # inside width
inner = width - 2   # accounts for the 1 space on each side inside the box

print("┌" + "─" * width + "┐")
print("│" + title.center(width) + "│")
print("├" + "─" * width + "┤")
print(f"│ {'>>[Name]: ' + name:<{inner}} │")
print(f"│ {'>>[Major]: ' + major:<{inner}} │")
print(f"│ {'>>[Email]: ' + email:<{inner}} │")
print(f"│ {'>>[Graduation Year]: ' + str(graduation_year):<{inner}} │")
print(f"│ {'>>[Hometown]: ' + hometown:<{inner}} │")
print(f"│ {'>>[Interest]: ' + interest:<{inner}} │")
print("└" + "─" * width + "┘")
