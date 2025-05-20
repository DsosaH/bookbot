def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = list(text.lower())
    dic = {}
    for character in characters:
       if character in dic:
           dic[character] += 1
       else:
           dic[character] = 1
    return dic

def sort_on(dict):
    return dict["num"]

def get_sorted(dict):
    dic_list = []
    for key in dict:
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = dict[key]
        dic_list.append(new_dic)
    dic_list.sort(reverse=True, key=sort_on) 
    return dic_list
