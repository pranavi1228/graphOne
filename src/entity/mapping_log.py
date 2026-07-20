import csv
import os


def log_mapping(raw_name, canonical_name):

    os.makedirs("exports", exist_ok=True)

    file = "exports/entity_mapping.csv"

    exists = os.path.exists(file)

    with open(file, "a", newline="", encoding="utf8") as f:

        writer = csv.writer(f)

        if not exists:
            writer.writerow(["Raw Name", "Canonical Name"])

        writer.writerow([raw_name, canonical_name])