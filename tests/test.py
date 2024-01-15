import argparse

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f"Content successfully written to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Read and write to a file")
    subparsers = parser.add_subparsers(help="Subcommands", dest="command")

    # Subparser for the 'read' command
    read_parser = subparsers.add_parser('read', help='Read content from a file')
    read_parser.add_argument('filename', help='Name of the file to read')
    read_parser.set_defaults(func=read_file)

    # Subparser for the 'write' command
    write_parser = subparsers.add_parser('write', help='Write content to a file')
    write_parser.add_argument('filename', help='Name of the file to write to')
    write_parser.add_argument('content', help='Content to write to the file')
    write_parser.set_defaults(func=write_file)

    args = parser.parse_args()
    print(args.filename)
if __name__ == '__main__':
    main()
