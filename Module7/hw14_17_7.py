def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:
        key_list=[]
        lines = fh.readlines()
        #lines = [line.rstrip() for line in lines]
        print(lines)
    with open(output_file, 'w') as f2:
        for elem in lines:
            f2.write(f'{lines.index(elem)}: {elem}')

            
            # if line:
            #     if line.find(profession) > 0:
            #         repl_str = line.replace(profession, '')
            #         #print(repl_str)
            #         new_str = repl_str.strip()
            #         new_list.append(new_str)
            #         stroka = " ".join(new_list)
            # else: 
            #     return 
    return
    








source_file='Module7\source_14.txt'
output_file='Module7\output_14.txt'

to_indexed(source_file, output_file)
    
