t_list = ['1', '2', '3', '4', '5']
if len(t_list) % 2 == 0:
    i = 0
    while i < len(t_list):
        el = t_list[i]
        t_list[i] = t_list[i + 1]
        t_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(t_list) - 1:
        el = t_list[i]
        t_list[i] = t_list[i + 1]
        t_list[i + 1] = el
        i += 2
print(t_list)
