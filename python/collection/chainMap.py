from collections import ChainMap
dic={1:"khan",2:2,3:1}
dic2={7:22,6:"jalalzai",5:1,4:2}
dic3={8:88,9:"karim"}

diclist=ChainMap(dic,dic2,dic3)
print(diclist)

# accessing elements

print("accesing element using key: "+diclist[6])

#adding new dictionary 

dic4={'l':'kaka',"num":799}

print(diclist.new_child(dic4))
print(diclist)