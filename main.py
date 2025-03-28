
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