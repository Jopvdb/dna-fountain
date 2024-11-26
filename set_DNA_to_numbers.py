def dna_to_int_array(dna_string):
    """
    Converts a DNA string (A, T, C, G) into a list of integers (0, 1, 2, 3).
    """
    translation = {'A': 0, 'T': 3, 'C': 1, 'G': 2}
    return [translation[base] for base in dna_string]

def process_dna_file(input_file, output_file):
    """
    Reads a file with DNA sequences, converts them to integer arrays,
    and writes the result to an output file as one long string.
    """
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Create a list to store the converted DNA sequences
    converted_lines = []

    for line in lines:
        # Skip any lines that are not DNA sequences (e.g., header lines starting with '>')
        if line.startswith(">"):
            converted_lines.append(line.strip())  # Include headers without conversion
        else:
            # Strip newlines and any spaces, convert DNA to integer array
            dna_string = line.strip()
            int_array = dna_to_int_array(dna_string)
            converted_lines.append("".join(map(str, int_array)))  # Concatenate integers into one long string

    # Write the converted data to the output file
    with open(output_file, 'w') as outfile:
        for converted_line in converted_lines:
            outfile.write(f"{converted_line}\n")

if __name__ == "__main__":
    # Example input and output file paths
    input_file = "encoded_dna.txt"  # Your input file with DNA sequences
    output_file = "encoded_dna_nmbr.txt"  # The file where converted sequences will be saved

    # Process the input file and create the output file
    process_dna_file(input_file, output_file)
    print(f"Conversion completed. Check the output file: {output_file}")

process_dna_file('encoded_dna.txt', 'encoded_dna_nmbr.txt')



