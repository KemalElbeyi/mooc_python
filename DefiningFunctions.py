def hello(target):
    print(f"Hello {target}")
hello("kemo")

def many_times(text,times):
    i=1
    while i <= times:
        print(text)
        i+=1
many_times("kemo",4)

def hash_square(x):
    for i in range(x):
        print(x*"#")
hash_square(3)

def squared(text,x):
    i = 0
    while i < x:
        print(text[i:x])
        i+=1
        
squared("kemo",3)

def spruce(x):
    for i in range(1,x+1):
        print(" "*(x-i)+"*"*(2*i-1))
    print(" "*(x-1)+"*")
spruce(3)

def greatest_number(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)
greatest_number(0,-4,0)

def same_chars(text,a,b):
    if 0 <= a < len(text) and 0 <= b < len(text):
        return text[a] == text[b]
    else:
        return False
print(same_chars("programmer", 6, 7))

def first_word(text):
    return text.split()[0]

def second_word(text):
    return text.split()[1]

def last_word(text):
    return text.split()[-1]

sentence = "The quick brown fox jumps"
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))
