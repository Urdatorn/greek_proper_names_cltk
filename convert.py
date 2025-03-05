from greek_accentuation.syllabify import add_necessary_breathing

def convert_txt_to_py(txt_filename, py_filename):
    """Converts a text file of proper names into a Python file with a single set."""
    with open(txt_filename, encoding='utf-8') as f:
        names = {add_necessary_breathing(line.strip()) for line in f if line.strip()}

    with open(py_filename, 'w', encoding='utf-8') as f:
        f.write("proper_names = {\n")
        for name in sorted(names):
            f.write(f"    '{name}',\n")
        f.write("}\n")

# Usage
convert_txt_to_py('proper_names.txt', 'proper_names.py')
