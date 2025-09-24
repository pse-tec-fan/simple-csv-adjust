import sys
import csv
import math
import re

# Tables to check
example_table = [
    [1, "a"], [2, "b"], [3, "c"]
]

    # Separate text, str_id = position before of separation (0 = first string)
def separate_lines(original_str, str_id, fail_result=None):
    try:
        new_str = original_str.splitlines()
        return new_str[str_id]
    except:
        return fail_result

def separate_spaces(original_str, str_id, fail_result=None):
    try:
        new_str = original_str.split()
        return new_str[str_id]
    except:
        return fail_result

def separate_char(original_str, char_str, str_id, fail_result=None):
    try:
        new_str = original_str.split(char_str)
        return new_str[str_id]
    except:
        return fail_result

    # Separate text with regular expression (regex_str = r"regex")
def separate_regex(original_str, regex_str, str_id, fail_result=None):
    try:
        new_str = re.split(regex_str, original_str)
        return new_str[str_id]
    except:
        return fail_result

    # Extract text, char_id = position of character to start (0 = first char, "" = last char)
def extract_to_pos(original_str, start_char, end_char=None, fail_result=None):
    try:
        new_str = original_str[start_char:end_char] if end_char is not None else original_str[start_char:]
        return new_str
    except:
        return fail_result

    # Extract text with regular expression (regex_str = r"regex")
def extract_regex(original_str, regex_str, str_id, fail_result=None):
    try:
        new_str = re.search(regex_str, original_str).group(str_id).strip()
        return new_str
    except:
        return fail_result

    # Replace text (replaced_str = "text")
def direct_replace(original_str, replaced_str, replace_str, fail_result=None):
    try:
        new_str = original_str.replace(replaced_str, replace_str)
        return new_str
    except:
        return fail_result

    # Replace text with regular expression (replaced_str = r"regex")
def regex_replace(original_str, replaced_str, replace_str, fail_result=None):
    try:
        new_str = re.sub(replaced_str, replace_str, original_str)
        return new_str
    except:
        return fail_result

def table_check(value, table, col_index, exact_match=True, fail_result=None):
    for row in table:
        if exact_match and row[0] == value:
            return row[col_index]
        elif not exact_match and row[0] <= value:
            last_match = row[col_index]
    return last_match if not exact_match else fail_result

def condition_check(conditions, default=None):
    for condition, result in conditions:
        if condition:
            return result
    return default

    # Handle input and output filenames
def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "base.csv"
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace(".csv", "_adj.csv")

    # Read input CSV
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        input_headers = reader.fieldnames

    # Show info
    input_headers = [
        "col-1", "col-2", "col-3", "col-4", "col-5"
]
    print("Needed fields on input file: " + input_headers) 

    # Define output headers
    output_headers = [
        "col-a", "col-b", "col-c", "col-d", "col-e", "col-f", "col-g"
]

    # Process rows
    output_rows = []
    for row in rows:
        new_row = {}
        for header in output_headers:
            new_row[header] = ""

        # Direct mappings
        #new_row["col-a"] = row.get("col-1", "")

        # Get ID's
        #new_row["col-b"] = separate_char(row.get("col-2", ""), "/", 2, )

        # Split by space
        #new_row["col-c"] = separate_spaces("a b c d e"), 4, )

        # Split by line
        #new_row["col-d"] = separate_lines(row.get("col-2", ""), 0, )

        # Replace text
        #new_row["col-e"] = direct_replace(row.get("col-3", ""), "example", "ex.", )

        # Extract text
        #new_row["col-f"] = extract_to_pos(row.get("col-4", ""), 10, None, )
        
        # Table search
        #col_5 = row.get("col-5", "")
        #test = condition_check([(col_5 < 1, 1), (col_5 > 3, 3),], col_5)
        #new_row["col-g"] = table_check(test, example_table, 1, True, "error")

        output_rows.append(new_row)

    # Write output CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=output_headers)
        writer.writeheader()
        writer.writerows(output_rows)

if __name__ == "__main__":
    main()

