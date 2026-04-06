# Simple CSV Cleaner - for freelance clients
import csv

# Input and output files
input_file = "dirty_data.csv"
output_file = "clean_data.csv"

with open(input_file, "r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Remove empty rows
clean_rows = [row for row in rows if any(cell.strip() for cell in row)]

# Save clean data
with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(clean_rows)

print("✅ Done! Clean data saved to clean_data.csv")