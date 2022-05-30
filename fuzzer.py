import sys
import random

testcase='Canon.jpg'
def get_bytes(filename):
    with open(filename,'rb') as f:
        return bytearray(f.read())
def create_new(data):
    with open("mutated.jpg","wb+") as f:
        f.write(data)
data=get_bytes(testcase)
# for idx,item in enumerate(data):
#     print(item)
#     if idx==10:
#         break
create_new(data)
def flip(data):
    chosen_indexs=[]
    indexes=range(4,(len(data)-4))
    num_of_flips=int((len(data)-4)*.01)
    counter=0
    while counter<num_of_flips:
        chosen_indexs.append(random.choice(indexes))
        counter+=1
    print(f"Number of indexes chosen:{str(len(chosen_indexs))}")
    print(f"Indexes chosen:{str(chosen_indexs)}")
    for x in chosen_indexs:
        current=data[x]
        current=bin(current).replace("0b","")
        current="0"*(8-len(current))+current
        indexes=range(0,8)
        picked_index=random.choice(indexes)
        new_number=[]
        for i in current:
            new_number.append(i)
        if new_number[picked_index]=="1":
            new_number[picked_index]="0"
        else:
            new_number[picked_index]="1"
        current=''
        for i in new_number:
            current+=i
        print(current)
        current=int(current,2)
        data[x]=current
        print(data[x])
#flip(data)
