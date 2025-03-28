import os

def read_file(file_path): pass
    
def same(lines1, lines2):
    result = []
    for line1 in lines1:
        for line2 in lines2:
            if line1 == line2:
                result.append(line2)
                break
    return result

def diff(lines1, lines2): pass

def write_to_file(file_path, lines): pass


def main(): 
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    same_output = 'same.txt'
    diff_output = 'diff.txt'
    try:
        lines1 = read_file(file1)
        lines2 = read_file(file2)
        common_lines = same(lines1, lines2)
        diff_lines = diff(lines1, lines2)

        write_to_file(same_output, common_lines)
        write_to_file(diff_output, diff_lines)

    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()


