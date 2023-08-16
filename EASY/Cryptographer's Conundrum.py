text = input()
print(len(text[::3].replace('P',""))+len(text[1::3].replace('E',""))+len(text[2::3].replace('R',"")))


