def get_max(M):
    max_ = 0
    for L in M:
        for c in L:
            if len(c) > max_:
                max_ = len(c)

    return max_

class Table:
    def __init__(self, name):
        self.name = name
        self.head = []
        self.datas = []
        self.height = len(self.datas)
        self.width = len(self.head)

    def __str__(self):
        st = ""
        m = get_max(self.datas)
        i = 1
        for line in self.datas:
            st = st + ("+" + "-" * m)*len(line) + "+\n"
            for tab in line:
                st = st + "|" + f"{tab}" + " " * (m-len(tab))
                
            st = st + "| " + str(i) + "\n"
            i += 1
        st = st + ("+" + "-" * m)*len(self.datas[0]) + "+\n"

        return st
    
    def is_empty(self):
        if self.datas == []:
            return True
        
        for L in self.datas:
            if L ==  []:
                return True
            
        return False

    def update(self): # pour update la longueure des encadrés en fonction de si la valeur la plus longue a changé (peut etre inutile)
        self.height = len(self.datas)
        self.width = len(self.head)

    def clear(self):
        self.datas = []
        self.update()

    def make_head(self, head:list):
        if not self.is_empty() or head == []:
            return False
        
        else:
            self.clear()
            self.head = head
            self.datas.append(head)
        
        self.update()

    def add_values(self, values:list):
        if self.is_empty():
            return False
        
        elif values == []:
            return False
        
        elif len(values) != len(self.datas[0]):
            raise IndexError("You added too many values ({} instead of {})".format(len(values), len(self.datas[0])))
        
        self.datas.append(values)
        self.update()





import random

t = Table(name = "test")
head = ["id", "name", "skin", "elo"]
t.make_head(head)

values = [
    ["djsur", "gabe", "!RyalTikbalang", "2000"],
    ["shcbn", "kurisu", "!KurisuCloud", "900"],
    ["poxlf", "patryk", "!PatrickSkin", "1500"],
    ["qsert", "ez", "!ezPrv1", "1900"],
    ["chxnd", "", "4chan", "600"],
    ["pftns", "TEWWW V2", "gabe", "200"],
    ["xxddh", "SU EMA", "obama", "800"],
    ["qshyz", "KRIS :)", "hook", "1400"],
    ["djsur", "arab", "!arabMax", "1300"],
    ["tarze", "SPARTAN", "!JacksonSpartan", "700"]
]


for v in values:
    t.add_values(v)


print(t)
print("is empty:", t.is_empty())
print("height :", t.height, "width :", t.width)
