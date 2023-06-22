from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    dec_total=0
    getcontext().prec = signs_count
    for elem in number_list:
        dec_total += Decimal(elem)
    print(dec_total)
    length= len(number_list)
    #print(length)
    #print(signs_count)
    #getcontext().prec = signs_count
    dec_aver= Decimal(dec_total)/Decimal(length)
    
    return dec_aver   
print(decimal_average([3, 5, 77, 23, 0.57], 6)) #21.714
print(decimal_average([31, 55, 177, 2300, 1.57], 9)) #512.91400