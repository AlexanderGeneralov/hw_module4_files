

import pprint
from operator import itemgetter

files = ["1.txt", "2.txt", "3.txt"]

def merge_files(files, file_to_write):
    res_list = [] # to store dicts with each file infor mation
    
    for file in files:
        counter = 0
        tmp_dict = {}
        file_content = ""
        with open(file, encoding='utf-8') as f:
            for l in f:
                counter += 1
                file_content += l
        tmp_dict = {"file_name" : file, "line_numbers" : counter, "file_content" : file_content}
        res_list.append(tmp_dict)
    res_list = sorted(res_list, key=itemgetter("line_numbers"))
    
    with open(file_to_write, 'w') as f:
        for res in res_list:
            f.write(f"{res['file_name']}\n{res['line_numbers']}\n{res['file_content']}\n")
    
    return file_to_write
    
def print_file(file):
    with open(file) as f:
        print(f.read())
        
print_file(merge_files(files, "res.txt"))