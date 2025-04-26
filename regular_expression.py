import re


with open("2025-04-26 13_03_02_1_show_ip_interface_brief.txt") as read_file:
    file = read_file.read()


with open("2025-04-26 13_16_22_2_show_running-config.txt") as read_file1:
    file1 = read_file1.read()


pattern = re.compile(r"GigabitEthernet+\d/\d/\d/\d")

pattern1 = re.compile(r"Sat\s...\s\d\d\s\d\d.\d\d.\d\d")

result = pattern.search(string=file)
result1 = pattern.findall(string=file)
result2 = pattern.finditer(string=file)


result3 = pattern1.findall(string=file1)
print(result3)