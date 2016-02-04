from skip_list.skip_list import SkipListSet
from .benchmark import maximise

import sys

def convert_hacker_rank_input_file_to_ours(path, new_path):
    with open(path, "r") as hacker_rank_file, open(new_path, 'w') as new_file:

        num_cases_line = hacker_rank_file.readline()
        num_cases = int(num_cases_line)
        new_file.write(num_cases_line)

        test_data = []
        for _ in range(num_cases):
            size_mod_line = hacker_rank_file.readline()
            size, mod = [int(x) for x in size_mod_line.split()]

            array_line = hacker_rank_file.readline()
            array = [int(x) for x in array_line.split()]

            answer = maximise(SkipListSet, array, mod)

            lines_to_write = [size_mod_line, array_line, str(answer) + "\n"]

            new_file.writelines(lines_to_write)


def main():

    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print("convert_hacker_rank HACKER_RANK_FILE NEW_FILE_PATH")
        return

    if len(sys.argv) < 3:
        print("Error: Need 2 arguments: old_path and new_path")
        return

    hacker_rank_file = sys.argv[1]
    new_file = sys.argv[2]

    convert_hacker_rank_input_file_to_ours(hacker_rank_file, new_file)


if __name__ == '__main__':
    main()
