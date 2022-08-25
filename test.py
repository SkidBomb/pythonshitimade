from os import system as sys
from time import sleep as wait

def cls(): sys("clear")
def pause(): input("Press any key to continue...")
def pauseNUL(): input("")
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    wait(delay)
  print('')

def main():
	cls()
	printt("""
		███████╗██╗░░░██╗░█████╗░██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗
		██╔════╝██║░░░██║██╔══██╗██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║
		█████╗░░██║░░░██║██║░░╚═╝█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║
		██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║
		██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝
		╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░
	""", 0.00001)
	input(">>>")

if __name__ == '__main__':
	main()