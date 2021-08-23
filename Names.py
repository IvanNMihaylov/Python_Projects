names = ["SNEJINA", "GENE", "TOD", "KOSIO", "NADEEM", "EMA", "SASHO", "DIMITAR", "MAIA", "ARSLAN", "JIN"]


class Concat:

    weight = 0
    tail = ""
    dict = {}

    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName


    def func(self):
        first = self.firstName
        second = self.secondName
        tail = ""
        weight = 0
        part = first
        for i in range(len(first)-1):
            if len(first) - 1 > i:
                part = first[((len(first) - 1) - i):]
            if second.startswith(part):
                if Concat.weight < i + 1:
                    weight = i + 1
                    Concat.weight = i + 1
                    tail = second
                    Concat.tail = second
                    Concat.dict[first] = [second, weight]
            elif Concat.weight == 0:
                Concat.dict[first] = [second, weight]


for first_name in names:
    for second_name in names:
        if first_name == second_name:
            continue
        else:
            Concat(first_name, second_name).func()
    Concat.weight = 0

my_dict = Concat.dict
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
sub_str = []
print(my_dict)
