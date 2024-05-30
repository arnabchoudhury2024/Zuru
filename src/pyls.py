from time import strftime, localtime
import pandas as pd
import json
import sys

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def ls_dir(structure_dict, sub_dir = "contents"):
    results = []
    for i in structure_dict.get(sub_dir):
        if not i['name'].startswith('.'):
            results.append(i['name'])
    return results

def ls_dir_all(structure_dict, sub_dir = "contents"):
    results = []
    for i in structure_dict.get(sub_dir):
        results.append(i['name'])
    return results

def ls_dir_list(structure_dict, sub_dir = "contents"):
    results = []
    for i in structure_dict.get(sub_dir):
        if not i['name'].startswith('.'):
            if 'contents' in i:
                type_flag = "dir" #if content is there then list else dir
            else:
                type_flag = "file"
            results.append([i['permissions'], i['size'], i['time_modified'],i['name'],type_flag])    
    return results

def ls_dir_list_rev(results):
    return results[::-1]

def ls_print(results, end_with = None):
    if results:
        for result in results:
            print(result, end = end_with)
        print()

def Sort_result(structure_dict, key_index = 1):
    structure_dict.sort(key = lambda x: x[key_index])
    return structure_dict

def format_list(results):
    if results:
        return [f"{result[0]  : <12}{result[1] : <7}{strftime('%b %d %H:%M', localtime(result[2])) : <15}{result[3] : <10}" for result in results]
    else:
        return []

def sort_by_time(ls_dir_result):
    sorted_ls_dir = Sort_result(ls_dir_result, 2)
    return sorted_ls_dir

def filter_type(structure_list, type_flag):
    if type_flag == 'file' or type_flag =='dir':
        return [result for result in structure_list if result[-1] == type_flag]
    else:
        print(r"error: 'folder' is not a valid filter criteria. Available filters are 'dir' and 'file'")
        
def sub_dir(structure_dict, path_name):
    split_path = path_name.split('/')
    sub_dir_list = []
    for i in range(len(structure_dict.get('contents'))):
        if structure_dict.get('contents')[i]['name'] == split_path[0]:
            if 'contents' in structure_dict.get('contents')[i]:
                sub_dir_list = ls_dir_list(structure_dict.get('contents')[i])
            else:
                res= structure_dict.get('contents')[i]
                sub_dir_list = [[res['permissions'], res['size'], res['time_modified'],res['name'],'file']]
    if len(sub_dir_list) > 0: 
        if len(split_path) > 1:
            for i in range(len(sub_dir_list)):
                if sub_dir_list[i][-2] == split_path[-1]:
                    sub_dir_list[i][-2] = r"./" + path_name
                    return [sub_dir_list[i]]
            print(f"error: cannot access {path_name}: No such file or directory")
            return
    else:
        print(f"error: cannot access {path_name}: No such file or directory")
    return sub_dir_list

def convert_bytes(bytes):
    if bytes < 1024:
        return f"{bytes}"
    elif bytes < 1024**2:
        KB = bytes / 1024
        return f"{KB:.2f}K"
    elif bytes < 1024**3:
        MB = bytes / (1024**2)
        return f"{MB:.2f}M"
    else:
        GB = bytes / (1024**3)
        return f"{GB:.2f}G"

def convert_human_readable_format(structure_list):
    for i in range(len(structure_list)):
        structure_list[i][1] = convert_bytes(structure_list[i][1])
    return structure_list
    
    
       
if __name__ == "__main__":
    structure_dict = read_json_file('src/structure.json')    
    result = []
    if len(sys.argv) == 1:
        ls_print(ls_dir(structure_dict), ' ')
    for i in sys.argv[1:]:
        if i == '-A':
            ls_print(ls_dir_all(structure_dict), ' ')
        elif i == '-l':
            result = ls_dir_list(structure_dict)
        elif i == '-t':
            result = sort_by_time(result)
            if '-r' in sys.argv[1:]:
                result = ls_dir_list_rev(result)
        elif i == '-r':
           result = ls_dir_list_rev(result)
        elif 'filter' in i:
            type_flag = i.split('=')
            result = filter_type(result, type_flag[-1])
        else:
            try:
                result = sub_dir(structure_dict, i)   
                result = convert_human_readable_format(result)
            except Exception as ex:
                print("Not a directory")
    ls_print(format_list(result))