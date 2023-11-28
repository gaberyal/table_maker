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
        if self.is_empty():
            return(self.name + " is empty")
        st = "{}\n".format(self.name)
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
        if self.datas == [] or len(self.datas) == 1:
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
        if len(self.datas) == 0:
            return False
        
        elif values == []:
            return False
        
        elif len(values) != len(self.datas[0]):
            raise IndexError("You added too many values ({} instead of {})".format(len(values), len(self.datas[0])))
        
        self.datas.append(values)
        self.update()

    def find(self, key, match_case = True):
        if self.is_empty():
            return None
        
        if not match_case:
            key = key.lower()

        
        tmp_table = Table("temporary")
        tmp_table.make_head(self.head)
        for line in self.datas:
            for value in line:

                if not match_case:
                    value = value.lower()
                if value == key:
                    if not line == self.datas[0]:
                        tmp_table.add_values(line)

        return tmp_table
    
    def remove_line(self, index):
        if index == 1:
            raise IndexError("Can not delete the head of the table")
        
        elif index < 1 or index > len(self.datas):
            raise IndexError("Index out of range")
        
        self.datas.pop(index-1)
        self.update()

        return self

t = Table(name = "test")
head = ["id", "name", "skin", "elo"]
t.make_head(head)

# values = []

# for v in values:
#     t.add_values(v)

t.add_values(["djsur", "gabe", "!RyalTikbalang", "2000"])
t.add_values(["shcbn", "kurisu", "!KurisuCloud", "900"])
t.add_values(["poxlf", "patryk", "!PatrickSkin", "1500"])
t.add_values(["qsert", "ez", "!ezPrv1", "1900"])
t.add_values(["chxnd", "", "4chan", "600"])
t.add_values(["pftns", "TEWWW V2", "gabe", "200"])
t.add_values(["xxddh", "SU EMA", "obama", "800"])
t.add_values(["qshyz", "KRIS :)", "hook", "1400"])
t.add_values(["djsur", "arab", "!arabMax", "1300"])
t.add_values(["tarze", "SPARTAN", "!JacksonSpartan", "700"])

print(t)
print("is empty:", t.is_empty())
print("height :", t.height, "width :", t.width)
