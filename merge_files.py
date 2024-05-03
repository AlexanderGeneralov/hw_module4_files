

from operator import itemgetter

files = ["1.txt", "2.txt", "3.txt"]

def merge_files(files, file_to_write): # function to mearege files content and files information to one file
    res_list = [] # to store dicts with each file information
    
    for file in files: # iterate over each file in list of files
        counter = 0 # to store number of lines in file
        tmp_dict = {} # to store file information
        file_content = "" # to store file content
        with open(file, encoding='utf-8') as f:
            for l in f:
                counter += 1
                file_content += l
        tmp_dict = {"file_name" : file, "line_numbers" : counter, "file_content" : file_content} # add file inormation and file content into dict
        res_list.append(tmp_dict) # add dict to list of dicts
    res_list = sorted(res_list, key=itemgetter("line_numbers")) # sort list of dicts by dict key 
    
    with open(file_to_write, 'w') as f:
        for res in res_list: # iterate over list of dicts
            f.write(f"{res['file_name']}\n{res['line_numbers']}\n{res['file_content']}\n") # write data from dict into file
    
    return file_to_write
    
def print_file(file):
    with open(file) as f:
        print(f.read())
        
print_file(merge_files(files, "res.txt"))