# Student Information Card
# This program displays a formatted profile card using box-drawing characters.
# It prints student details such as name, major, email, graduation year,
# hometown, and areas of interest in a clean, readable layout using boxdrawing characters.

# -------------------------------
# Student personal information
# -------------------------------

name = "Carley Fant"
email = "fant_carley@colstate.view.usg.edu"
major = "Information Technology"
graduation_year = 2026
hometown = "Atlanta"
interest = "AppSec/DevSecOps/Identity"

# -------------------------------
# Card configuration
# -------------------------------
# Title displayed at the top of the card

title = "STUDENT INFORMATION CARD"

width = 50          # inside width
inner = width - 2   # accounts for the 1 space on each side inside the box

# -------------------------------
# Output the formatted card
# -------------------------------

# Print top border
print("┌" + "─" * width + "┐")

# Print centered title
print("│" + title.center(width) + "│")

# Print divider line
print("├" + "─" * width + "┤")

# Print each labeled field with padding for alignment
print(f"│ {'>>[Name]: ' + name:<{inner}} │")
print(f"│ {'>>[Major]: ' + major:<{inner}} │")
print(f"│ {'>>[Email]: ' + email:<{inner}} │")
print(f"│ {'>>[Graduation Year]: ' + str(graduation_year):<{inner}} │")
print(f"│ {'>>[Hometown]: ' + hometown:<{inner}} │")
print(f"│ {'>>[Interest]: ' + interest:<{inner}} │")

# Print bottom border
print("└" + "─" * width + "┘")
