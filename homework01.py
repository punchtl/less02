t_int = 5
t_float = 1.2
t_list = ['a', '1']
t_tuple = ('b', '2')
t_str = "Привет"
t_dict = {"город": "Москва", "страна": "Россия"}

full_list = [t_int, t_float, t_list, t_tuple, t_str, t_dict]
for i in full_list:
    print(f'{i} это {type(i)}')
