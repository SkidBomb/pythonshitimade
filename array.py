from os import system as sys
from time import sleep as wait

array1 = []

def cls(): sys('clear')
def pause(): input("Press any key to continue...")
def pauseNUL(): input("")

def main():
  cls()
  print("Array Factory Build 2")
  print(array1)
  print("Write in what you want to put in the array. To recite the array one by one, type in '/end'. To remove an item, type '/remove'.")
  reader = input(">>>")
  if reader == '/end':
    cls()
    for i in array1:
      print(i)
  elif reader == '/remove':
    print("What item would you like to remove?")
    removequestion = input(">>>")
    if removequestion in array1:
      array1.remove(removequestion)
      main()
    else:
      cls()
      print("Item does not exist.")
      wait(3)
      main()
  else:
    array1.append(reader)
    main()

if __name__ == '__main__':
  main()