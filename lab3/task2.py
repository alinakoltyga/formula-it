# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, delimiter=','):
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    common_participants = participants1.intersection(participants2)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common_participants)

participants_first_group_default = "Иванов,Петров,Сидоров"
participants_second_group_default = "Петров,Сидоров,Смирнов"

common_participants_default = find_common_participants(participants_first_group_default, participants_second_group_default)
print("Общие участники (по умолчанию):", common_participants_default)