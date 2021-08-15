names = ["SNEJINA", "NADEEM", "GENE", "TOD", "KOSIO", "EMA", "SASHO", "DIMITAR", "MAIA", "ARSLAN", "JIN"]


class Concat:

    index1 = 0
    best_match_count = 0
    best_match = ""
    the_name = ""

    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName

    def __repr__(self):
        return self.best_match

    def func(self):
        first = self.firstName
        second = self.secondName
        index = 0
        i = 1
        while i < len(first):
            try:
                if first[len(first)-i] == second[i-1] or first[len(first) - i] == second[i]:
                    i += 1
                    index += 1
                elif first[len(first)-i] == second[i-2] or first[len(first) - i] == second[i-1]:
                    i += 1
                    index += 1
                else:
                    break
                if index > Concat.index1:
                    Concat.index1 = index
                    Concat.best_match = second
            except:
                break



the_name = names[0]
while the_name:
    for second_name in names:
        if the_name == second_name:
            continue
        else:
            Concat(the_name, second_name).func()

    names.remove(Concat.best_match)
    the_name = Concat.best_match
    Concat.index1 = 0