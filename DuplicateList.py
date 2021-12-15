def duplicate(ele):
 new = []
 for i in ele:
  if i not in new:
   new.append(i)
 return new

def main():
 number = int(input("please enter number upto list: "))
 ele =[]
 for i in range(number):
     list= int(input())
     ele.append(list)
 print(duplicate(ele))

if __name__ == '__main__':
        main()