
# LAB 8: Log File Analyzer

# Initialize counters for errors and warnings
total_count = 0

# Open the application log file and read entries one at a time
with open("application.log", "r") as file:

    # Print the report heading
    print("ERROR REPORT")
    print("----------------------------------------")

    # Process each log entry
    for line in file:

        # Extract the timestamp using slicing
        timestamp = line[:19]

        # Search for error and warning entries
        if "error" in line.lower() or "warning" in line.lower():

            # Standardize severity labels
            line = line.replace("error", "ERROR")
            line = line.replace("warning", "WARNING")

            # Also use find() to locate severity labels
            error_position = line.find("ERROR")
            warning_position = line.find("WARNING")

            # Split the entry into separate fields
            fields = line.split("|")

            # Remove unnecessary whitespace
            fields = [field.strip() for field in fields]

            # Use the extracted timestamp and cleaned fields
            timestamp = line[:19]

            # Identify the severity
            severity = fields[1]
            message = fields[2]

            # Include only ERROR and WARNING entries
            if severity in ["ERROR", "WARNING"]:

                # Combine fields using join()
                formatted_entry = " - ".join(
                    [timestamp, severity, message]
                )

                # Display the formatted entry
                print(formatted_entry)

                # Update the total count
                total_count += 1

# Display the final summary
print()
print("Total errors and warnings:", total_count)
