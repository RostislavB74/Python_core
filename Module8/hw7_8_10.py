import collections

#[Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]
Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
Cat1 = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#cats_dict=collections.namedtuple("nickname":'nickname', "age":'age', "owner":'owner')
#cats=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats=[{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]
def convert_list(cats):
   
    cats_list=[]
    for i in cats:
        if isinstance(i, tuple):
            cats_dict={}
            cats_dict["nickname"]=(i.nickname)
            cats_dict["age"]=(i.age)
            cats_dict["owner"]=(i.owner)
            cats_list.append(cats_dict)
        if isinstance(i, dict):
            cats2=[]
            cats2=Cat(**i)
            
            cats_list.append(cats2)
           
        
    return cats_list
           
            
print(convert_list(cats))
            
        
    