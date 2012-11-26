import time
import sys
import random
import re

def delay(seconds):
    """Seconds delays the program by the int given
    """
    for i in reversed(range(seconds)):
        time.sleep(1)
        sys.stdout.write("\rNext request will be in %d seconds..." %i)
        sys.stdout.flush()


def delay_request(n1, n2):
    """This randomly delays the script by the range of 
    seconds given.
    """
    seconds = random.randrange(n1, n2)
    delay(seconds)
    
def delete_duplicates(lst):
    """When given a list, it removes any duplicates and returns
    a new list.
    """
    seen = set()
    seen_add = seen.add
    return [x for x in lst if x not in seen and not seen_add(x)]

def process_sizes(size_el_list):
    size_list = list()
    for s in size_el_list:
        if len(s)>19 or len(s)<6:
            pass
        else:
            if s[0].isalpha():
                char = s[0]
                s = s.replace(char, ' ')
                s = s.strip()
            s = s[:10]
            s = s.strip()
            if 'ZR' in s:
                s = s.replace('ZR', '/')
            elif 'R' in s:
                s = s.replace('R', '/')
            size_list.append(s)
    return size_list

def process_size(s):
    """From a single size el, this func removes 'R', 'ZR'
    or 'P' from a size element:
    255/40ZR17 to 255/40/17
    Returns a single size.
    """
    if len(s)>19 or len(s)<6:
        pass
    else:
        if s[0].isalpha():
            char = s[0]
            s = s.replace(char, ' ')
            s = s.strip()
        s = s[:10]
        s = s.strip()
        if 'ZR' in s:
            s = s.replace('ZR', '/')
        elif 'R' in s:
            s = s.replace('R', '/')
        elif '-' in s:
            s = s.replace('-', '/')
        return s
         
def process_sizes(size_el_list):
    """Returns a proccessed list.
    """
    size_list = list()
    for s in size_el_list:
        tmp_s = process_size(s)
        if tmp_s is not None:
            size_list.append(tmp_s)
    return size_list

def get_index(word):
    i = 0
    for w in word:
        if w is ' ':
            return i
        else:
            i+=1

def get_size(size, tsl):
    """size is the element var returned from tree2 using
    SINGLE_SIZE_ELEMENT. tsl is the list of sizes returned 
    from tree using SIZE_ELEMENT.
    input: 'TOYO Proxes T1 Sport 255/40ZR/17 98Y XL'
    output:'255/40/17'
    """
    pattern = list()

    for pat in tsl:
        index = get_index(pat)
        pattern.append(pat[:index])
        
    for p in pattern:
        if re.search(p, size):
            psize = process_size(p)
            if psize is None:
                pass
            else:
                return psize
