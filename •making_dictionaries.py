#making dictionaries
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

new = dict(zip(name, favorite_animal))
print(new)

#Good was is to use isinstance to first test type
def dictionary_maker(x,i):
  new_dict = {}
  if isinstance(x,list) and isinstance(i,list):
      new_dict = dict(zip(x, i))
      return new_dict
  else: 
    return "Insufficient Data"

dictionary_maker(name, favorite_animal)

