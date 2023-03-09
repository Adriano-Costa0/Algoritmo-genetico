import random



import math



produtos = [
    [



        "Geladeiro Dako",



        0.751,
        999.90
    ],
    [



        "Iphone 6",



        0.0000899,



        2199.12
    ],
    [



        "TV 55",



        0.400,



        4346.99
    ],
    [



        "TV 50",



        0.290,



        3999.90
    ],
    [



        "TV 42",



        0.200,



        2999.90
    ],
    [



        "Notebook dell",



        0.00350,



        2499.90
    ],
    [



        "Ventilador Mundial",



        0.496,



        199.90
    ],
    [



        "Microondas Electrolux",



        0.0424,



        308.66
    ],
    [



        "Microondas LG",



        0.0544,
        999.90
    ],
    [



        "Microondas Panasonic",



        0.0319,



        299.29
    ],
    [



        "Geladeira Brastemp",



        0.635,



        849
    ],
    [



        "Geladeira Consul",



        0.870,



        1199.89
    ],
    [

        "Notebook Lenovo",



        0.498,



        1999.90
    ],
    [



        "Notebook Asus",



        0.527,



        9382
    ],
]



class Cromossomo:


    def __init__(self, size):


        self.genes = []


        self.fittest = 0


        self.capacity = 0


        for index in range(size):
            self.genes.append(random.randint(0, 1))

        self.calcWeight()


    def calcWeight(self):
        totalFittest = 0
        totalCapacity = 0

        for index in range(len(self.genes)):
            if self.genes[index] is 1:
                price = produtos[index][2]
                size = produtos[index][1]
                totalCapacity += size
                totalFittest += price / size
        
        self.fittest = totalFittest
        self.capacity = totalCapacity
        
    
