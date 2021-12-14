def listplay(list1):
 new =[]
 new.append(list1[0])
 new.append(list1[-1])
 return new
import random
def main():
 list1 = random.sample(range(50),7)
 print(list1)
 print(listplay(list1))



if __name__ == '__main__':
  main()