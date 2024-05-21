import os
import argparse


def print_tree(startpath, show_files=True, file_extension=None, prefix=''):
    items = sorted(os.listdir(startpath))
    for index, item in enumerate(items):
        path = os.path.join(startpath, item)
        if index == len(items) - 1:
            connector = '└── '
            new_prefix = prefix + '    '
        else:
            connector = '├── '
            new_prefix = prefix + '│   '

        if os.path.isdir(path):
            print(prefix + connector + item)
            print_tree(path, show_files, file_extension, new_prefix)
        elif show_files:
            if file_extension:
                if item.endswith(file_extension):
                    print(prefix + connector + item)
            else:
                print(prefix + connector + item)


def main():
    parser = argparse.ArgumentParser(description='Display a directory tree.')
    parser.add_argument('directory', metavar='DIR', type=str, nargs='?', default='.',
                        help='Directory to display tree for (default: current directory)')
    parser.add_argument('-f', '--files', action='store_true',
                        help='Include files in the tree')
    parser.add_argument('-e', '--extension', type=str,
                        help='Filter files by extension (e.g., .txt)')

    args = parser.parse_args()
    print_tree(args.directory, show_files=args.files, file_extension=args.extension)


if __name__ == "__main__":
    main()
