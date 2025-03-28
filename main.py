import os

def read_file(file_path): 
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не знайдено.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())
    
def same(lines1, lines2):
    result = []
    for line1 in lines1:
        for line2 in lines2:
            if line1 == line2:
                result.append(line2)
                break
    return result

def diff(first_file: list[str], second_file: list[str]) -> list[str]:
    unique_lines = []
    file_num = []
    for line in first_file:
        if line not in second_file:
            unique_lines.append(line)
            file_num.append(1)

    for line in second_file:
        if line not in first_file:
            unique_lines.append(line)
            file_num.append(1)
    
    with open("diff.txt", "w", encoding="utf-8") as file:
        for a in range(len(unique_lines)):
            file.write("Унікальний рядок: "+ unique_lines[a] + "    Для файлу "+ str(file_num[a]) + "\n")

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


