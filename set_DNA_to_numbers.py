def dna_to_int_array(dna_string):
    """
    Converts a DNA string (A, T, C, G) into a list of integers (0, 1, 2, 3).
    """
    translation = {'A': 0, 'T': 3, 'C': 1, 'G': 2}
    return [translation[base] for base in dna_string]

def process_dna_file(input_file, output_file):
    """
    Reads a file with DNA sequences, converts them to a continuous string of integers,
    and writes the result to an output file as one long string.
    """
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Initialize a list to store the converted DNA sequences as one big string
    converted_data = ""

    for line in lines:
        # Skip any lines that are not DNA sequences (e.g., header lines starting with '>')
        if not line.startswith(">"):
            # Strip newlines and spaces, convert DNA to integer array
            dna_string = line.strip()
            int_array = dna_to_int_array(dna_string)
            # Append integers as a string to the big string
            converted_data += "".join(map(str, int_array))

    # Write the converted data to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(converted_data)

if __name__ == "__main__":
    # Example input and output file paths
    input_file = "encoded_dna.txt"  # Your input file with DNA sequences
    output_file = "encoded_dna_nmbr.txt"  # The file where converted sequences will be saved

    # Process the input file and create the output file
    process_dna_file(input_file, output_file)
