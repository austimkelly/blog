import yara

# Define the YARA rule as a string
yara_rule = """
rule DetectWindowsBatchCommands {
    strings:
        $cmd1 = "cmd.exe /c"
        $cmd2 = "powershell.exe -c"
        $cmd3 = "start cmd.exe /c"
    condition:
        $cmd1 or $cmd2 or $cmd3
}
"""

# Compile the YARA rule
compiled_rule = yara.compile(source=yara_rule)

def detect_match_with_yara(file_path):
    # Open the file and read its content
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Perform the YARA scan on the file content
    matches = compiled_rule.match(data=file_content)

    # Check if there are any matches
    if matches:
        print(f"Match found based on the YARA rule in file: {file_path}")
        for match in matches:
            print(f"Matched rule: {match.rule}")
    else:
        print(f"No match found based on the YARA rule in file: {file_path}")

# Example usage:
file_path = "./test_file.txt"  # Replace this with the actual file path
detect_match_with_yara(file_path)
