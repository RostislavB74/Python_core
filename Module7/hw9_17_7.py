data = [1, 2, 3, 4] 

def all_sub_lists(data):
    short_list=[[]]
    for i in range(len(data)):
        for j in range(len(data)-i):
            short_list.append(data[j:j+i+1])
    return short_list

print(all_sub_lists(data))


# # def all_sub_lists(data):
# #short_list=[]
# #     temp_list=[]
# #     #for j in range(3):
# #     #for i in range(len(data)):
    
# #     #    temp_list.append(data[i])
# #     #new_list.append(temp_list[i])
# #     print(temp_list)
# #     return new_list
    
        
            
# # data=[1,2,3] #[[], [1],[2],[3],[1.2],[2,3],[1,2,3]]
# my_2lvl_list = [1, 2, 3]
# short_list=[[]]
# big_list=[]
# for i in range(len(my_2lvl_list)):
#     for j in range(len(my_2lvl_list)-i):
#         short_list.append(my_2lvl_list[j:j+i+1])
#     #new_list.append(short_list)
# #big_list = new_list
# print(short_list)
# # big_list.append(my_2lvl_list[0:2:])
# # big_list.append(my_2lvl_list[1:3:])
# # big_list.append(my_2lvl_list)
# # print(big_list)
# # for j in range(len(new_list)):
# #     temp_list=[]
# #     temp_list.append(new_list[i])
# #     for j in range(len(my_2lvl_list)):
# #         short_list.append(my_2lvl_list[j])
# #     new_list1.append(short_list)    
# #print(temp_list)     
# # print(new_list)     
# #print(new_list1)