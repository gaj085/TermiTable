"""
TermiTable: A CLI-based Table Generator with MySQL-style Output
"""

def print_row_separator(col_widths, char = '-'):
    """Prints a row separator like +-----+------+"""
    for width in col_widths:
        print('+', char * width, sep = '', end = '')
    print('+')


def center_text(text, width):
    """Centers text in a given column width"""
    padding = width - len(text)
    if padding % 2 == 0:
        return ' ' * (padding // 2) + text + ' ' * (padding // 2)
    else:
        return ' ' * ((padding + 1) // 2) + text + ' ' * ((padding - 1) // 2)


def collect_column_info():
    """Collects column names and widths from the user"""
    n = int(input("Enter total number of columns: "))
    column_names = []
    column_widths = []

    print("\nEnter column names and max widths one by one:\n")
    for i in range(n):
        name = input(f"Enter name for column {i + 1}: ")
        max_len = int(input(f"Enter max char width for '{name}': "))
        print()

        column_names.append(name)
        column_widths.append(max(len(name), max_len))

    return column_names, column_widths


def collect_entries(column_names, num_entries):
    """Collects row entries from the user"""
    entries = []
    for i in range(num_entries):
        print(f"\nFilling entry {i + 1}:")
        row = []
        for name in column_names:
            value = input(f"Enter {name}: ")
            row.append(value)
        entries.append(row)
    return entries


def print_table(column_names, column_widths, data_rows):
    """Prints the full table"""
    # Header separator
    print_row_separator(column_widths)

    # Column headers
    print('|', end='')
    for idx, name in enumerate(column_names):
        print(center_text(name, column_widths[idx]), '|', sep = '', end = '')
    print()

    # Header underline
    print_row_separator(column_widths, char = '=')

    # Data rows
    for row in data_rows:
        print('|', end='')
        for idx, val in enumerate(row):
            print(center_text(val, column_widths[idx]), '|', sep = '', end = '')
        print()
        print_row_separator(column_widths)


def main():
    column_names, column_widths = collect_column_info()
    num_entries = int(input("Enter number of entries: "))
    entries = collect_entries(column_names, num_entries)
    print("\nGenerated Table:\n")
    print_table(column_names, column_widths, entries)


if __name__ == "__main__":
    main()
