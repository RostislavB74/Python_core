import csv
filename = '3.csv'
contacts = [
    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
, {
    "name": "Allen ",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
}]
def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=list(contacts[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in contacts:
            writer.writerow(d)    
        
        
            


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        result=[]
        contacts1={}
        reader = csv.DictReader(fh)
        for row in reader:
            
            for keys, value in row.items():
                print (type(row.get(keys)))
                #print (keys, value)
                if keys =='favorite':
                    value = bool(value)
                    contacts1[keys] = value
                    print(keys, type(value))
                else:
                    contacts1[keys] = value
            result.append(contacts1)
        print (contacts1)
        return result



    
        
#write_contacts_to_file(filename, contacts)

print(read_contacts_from_file(filename))
                
            
            
    
