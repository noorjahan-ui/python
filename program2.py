def word_replace(str):
    replace=str[0]
    str=str.replace(replace,'$')
    str=replace+str[1:9:]
    return str
str=input("enter the word:")
print(word_replace(str))


