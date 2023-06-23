import collections

#[Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]
Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#cats_dict=collections.namedtuple("nickname":'nickname', "age":'age', "owner":'owner')
cats=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

def convert_list(cats):
    if isinstance(cats, list):
        cats_list=[]
        for i in cats:
            cats_dict={}
            cats_dict["nickname"]=(i.nickname)
            cats_dict["age"]=(i.age)
            cats_dict["owner"]=(i.owner)
            cats_list.append(cats_dict)
        print(cats_list)
            # print(i.owner)
        

            
        #print(cats.Cat)
        
            
convert_list(cats)
            
        
    