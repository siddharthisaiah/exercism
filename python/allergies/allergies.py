class Allergies(object):

    allergy_key = {
        1   : 'eggs',
        2   : 'peanuts',
        4   : 'shellfish',
        8   : 'strawberries',
        16  : 'tomatoes',
        32  : 'chocolate',
        64  : 'pollen',
        128 : 'cats'
    }
    
    
    def __init__(self, score):
        self.lst = [value for key, value in self.allergy_key.items() if score & key]

        
    def is_allergic_to(self, item):
        return item in self.lst
