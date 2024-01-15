import argparse

def capitalize(text):
    return text.upper()

def main():
    parser = argparse.ArgumentParser(description="Convert text to capital letters and save it to an output file.")
    parser.add_argument("input_file", help="Input text file.")
    parser.add_argument("output_file", help="Output text file.")
    parser.add_argument("--indent", action="store_true", help=("Beginning will be indented by 4 spaces"))
    args = parser.parse_args()

    with open(args.input_file, 'r') as infile:
        text = infile.read()

    processed_text = capitalize(text)

    if args.indent:
        processed_text = "    " + processed_text  

    with open(args.output_file, 'w') as outfile:
        outfile.write(processed_text)

    print(f"Text converted to capital letters. Output saved to {args.output_file}.")

if __name__ == "__main__":
    main()
