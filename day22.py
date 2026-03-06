# Day 22 – Simple log analyzer (count INFO / WARNING / ERROR from a log file)

def analyze_log(file_path):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.upper()
                if "ERROR" in line:
                    counts["ERROR"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "INFO" in line:
                    counts["INFO"] += 1

    except FileNotFoundError:
        print("Log file not found.")
        return

    print("\nLog Summary:")
    for level, count in counts.items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    path = input("Enter log file path: ")
    analyze_log(path)