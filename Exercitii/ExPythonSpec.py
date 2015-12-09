import pdb
import this
import re
import codecs

#pdb.set_trace()

#ex1
def comb_zar():
    return [(i,j) for i in range(7) for j in range(7)]

#print combZar()

#ex2
def dupl_List(list):
    result = []
    [result.append(x) for x in list if x not in result]
    return result

#ex3
companies = [
    ("Pixar", 2),
    ("Disney", 4),
    ("Warner Bros.", 9),
    ("Universal", 5),
    ("Reception", 0),
    ("Studio Ghibli", 8),
    ("DreamWorks", 6),
]

comp_dict= {val:nume for nume, val in companies}
#print compDict

#ex4
lista_comp = [comp_dict.get(key) for key in range(11)]
#print listaComp
#print compDict.keys()
#print dir(compDict)

#ex5
def generate_Indecsi():
    indecs = []
    text = codecs.decode(this.s, 'rot-13')
    text_split = text.split(' ')
    indecsi = [index for index, word in enumerate(text_split) if word == 'better']
    print indecsi

#ex6
class Person(object):
    """docstring for Person"""
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return "{} {}".format(self.nume, self.varsta)

obj_list = [('Mariaescu', 10), ('Ionescu', 20), ('Gigi', 12), ('Anaescu', 50), ('Bebescu', 50)]


def person_factory(obj_list):
  return [Person(n,v) for n, v in obj_list ]


def varsta(lista_persoane):
    #return sorted(([name for name,age in listaPersoane if re.match(r'[a-zA-Z]*escu',name)]))
    return sorted([age for name, age in lista_persoane if name.endswith('escu')])


persons = person_factory(obj_list)
#for p in persons:
#    print p


#ex7
def data_base():
    data_base = {}
    add_person(data_base, 1, 'gigi', 20)
    add_person(data_base, 2, 'bebe', 15)
    print query_database(data_base)
    knows_python(data_base, 1, True)
    print knows_python(data_base, 3, False)
    print data_base

def add_person(data_base, id, name, age):
    data_base[id] = {'name': name, 'age': age}

def query_database(data_base):
    return [person['name'] for person in data_base.values() if person['age'] < 18]

def knows_python(data_base, id, bool):
    if data_base.get(id) == None:
        return "Person {0} doesn't exist".format(id)
    data_base[id]['python'] = bool




def main():
    names = varsta(obj_list)
    print names

    data_base()



if __name__ == '__main__':
    main()








