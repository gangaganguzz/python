import os
import shutil
import hashlib
import logging

# 1. Get folder path
folder_path = input("Enter folder path: ")

if not os.path.isdir(folder_path):
    print("Folder does not exist!")
    exit()

# 2. Dry run option
answer = input("Do you want Dry Run? (yes/no): ").lower()

if answer == "yes":
    dry_run = True
else:
    dry_run = False

# 3. File categories
categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    ".pdf": "Documents",
    ".txt": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",

    ".csv": "Spreadsheets",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",

    ".py": "Python_Files",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives"
}

organized_folders = [
    "Images",
    "Documents",
    "Spreadsheets",
    "Python_Files",
    "Archives",
    "Duplicates",
    "Others"
]

# 4. Scan files including subfolders
files = []

for root, dirs, filenames in os.walk(folder_path):

    # Skip folders created by the organizer
    dirs[:] = [
        folder for folder in dirs
        if folder not in organized_folders
    ]

    for filename in filenames:

        if filename.startswith("."):
            continue

        if filename in ["organizer_report.txt", "organizer.log"]:
            continue

        file_path = os.path.join(root, filename)

        if os.path.isfile(file_path):
            files.append(file_path)

# 5. Calculate storage size
total_size = 0

for file in files:

    try:
        total_size += os.path.getsize(file)

    except OSError:
        print("Unable to calculate size:", file)

# 6. Display preview
print("\n========== PREVIEW ==========")

print("Total files found:", len(files))
print("Total storage:", round(total_size / 1024, 2), "KB")

for file in files:

    extension = os.path.splitext(file)[1].lower()

    category = categories.get(extension, "Others")

    print(os.path.basename(file), "->", category)

# 7. Confirmation
if not dry_run:

    confirm = input(
        "\nDo you want to organize these files? (yes/no): "
    ).lower()

    if confirm != "yes":
        print("Operation cancelled!")
        exit()

# 8. Create folders (only actual run)
if not dry_run:

    for category in organized_folders:

        category_path = os.path.join(folder_path, category)

        os.makedirs(category_path, exist_ok=True)

    # Logging setup
    logging.basicConfig(
        filename=os.path.join(folder_path, "organizer.log"),
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

# 9. Function to calculate file hash
def get_file_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()

# 10. Function to avoid overwriting files
def get_unique_path(destination):

    if not os.path.exists(destination):
        return destination

    folder = os.path.dirname(destination)
    filename = os.path.basename(destination)

    name, extension = os.path.splitext(filename)

    counter = 1

    while True:

        new_name = f"{name}_{counter}{extension}"

        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            return new_path

        counter += 1

# 11. Counters
moved_count = 0
duplicate_count = 0
failed_count = 0

category_count = {}

# Hashes of files already processed
original_hashes = {}

# 12. Process each file
for file in files:

    filename = os.path.basename(file)

    extension = os.path.splitext(filename)[1].lower()

    category = categories.get(extension, "Others")

    try:

        # Check file content
        file_hash = get_file_hash(file)

        # Is it a duplicate?
        if file_hash in original_hashes:

            duplicate_count += 1

            print("\nDuplicate found:", filename)

            if not dry_run:

                destination_folder = os.path.join(
                    folder_path, "Duplicates"
                )

                destination = os.path.join(
                    destination_folder, filename
                )

                destination = get_unique_path(destination)

                shutil.move(file, destination)

                print("Duplicate moved to Duplicates folder")

                logging.info("Duplicate moved: %s", filename)

        else:

            # First time seeing this content
            original_hashes[file_hash] = file

            if not dry_run:

                destination_folder = os.path.join(
                    folder_path, category
                )

                destination = os.path.join(
                    destination_folder, filename
                )

                destination = get_unique_path(destination)

                shutil.move(file, destination)

                # Store new path for future reference
                original_hashes[file_hash] = destination

                print("Moved:", filename, "->", category)

                logging.info(
                    "Moved %s to %s", filename, category
                )

            moved_count += 1

            category_count[category] = (
                category_count.get(category, 0) + 1
            )

    except Exception as error:

        failed_count += 1

        print("Failed:", filename)

        if not dry_run:

            logging.error(
                "Failed to process %s: %s", filename, error
            )

# 13. Final report
print("\n========== FINAL REPORT ==========")

if dry_run:
    print("Mode: DRY RUN (files not moved)")
else:
    print("Mode: ACTUAL ORGANIZATION")

print("Total files scanned:", len(files))
print("Files moved / planned:", moved_count)
print("Duplicates found:", duplicate_count)
print("Failed files:", failed_count)

print("Total storage:", round(total_size / 1024, 2), "KB")

print("\nCategory-wise count:")

for category, count in category_count.items():

    print(category, ":", count)

# 14. Save report (actual run only)
if not dry_run:

    report_path = os.path.join(
        folder_path, "organizer_report.txt"
    )

    with open(report_path, "w") as report:

        report.write("FILE ORGANIZER REPORT\n")
        report.write("====================\n")

        report.write(f"Total files scanned: {len(files)}\n")
        report.write(f"Files moved: {moved_count}\n")
        report.write(f"Duplicates found: {duplicate_count}\n")
        report.write(f"Failed files: {failed_count}\n")

        report.write(
            f"Total storage: {round(total_size / 1024, 2)} KB\n"
        )

        report.write("\nCategory-wise count:\n")

        for category, count in category_count.items():

            report.write(f"{category}: {count}\n")

    print("\nReport saved successfully!")
    print("Log file saved successfully!")

else:

    print("\nDry Run completed.")
    print("No files were moved.")