#cleaner.py
import regex as re
from patterns import phone,percentages,integer,dec,urls,emails,removespecial


def remove_special(x):
    match =re.sub(removespecial,"",str(x))
    return match

def remove_doublespaces(x):
    x = str(x)
    x = re.sub(r'\s+', ' ', x)
    return x.strip() 

def remove_newline(x):
    x=str(x).replace("\n"," ")
    return x
def remove_tab(x):
    x=str(x).replace("\t"," ")
    return x

def digits(x):
    match = re.search(integer,x)
    if not match:
        return ""
    else:
        return match.group(0)

def decimal(x):
    x=str(x)
    match = re.search(dec,x)
    if not match:
        return ""
    else:
        return match.group(0)

def phonenumber(x):
    x = str(x)
    match = re.search(phone, x)
    if not match:  # No phone number found
        return ""
    
    num = match.group(0)
    if num.startswith("+"):
        return "+" + re.sub(r"\D", "", num)
    else:
        return re.sub(r"\D", "", num)
    
def percentage(x):
    x = str(x).strip()
    match = re.search(percentages, x)
    if match:
        num_str = match.group(0).rstrip('%')
        return float(num_str) / 100
    else:
        try:
            return float(x)
        except ValueError:
            return None
        
def url(x):
    x= str(x)
    match= re.search(urls,x)
    return match.group(0) if match else None

def email (x):
    x=str(x)
    match=re.search(emails,x)
    return match.group(0) if match else None
