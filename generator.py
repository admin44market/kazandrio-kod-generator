import random
import string

from colorama import Fore, Back, Style
from pyfiglet import Figlet

from colorama import Fore, Back, Style
from pyfiglet import Figlet

figlet = Figlet()

print("=" * 50)
print(Fore.GREEN + Back.BLUE + Style.BRIGHT + figlet.renderText("Kazandrio Kod Generator") + Style.RESET_ALL)
print("=" * 50)
def rastgele_kod_uret(kod_sayisi):


 
  karakterler = string.ascii_letters + string.digits
  
  kodlar = []
 
  for _ in range(kod_sayisi):
    
    kod = "".join(random.choice(karakterler) for _ in range(10))
  
    kodlar.append(kod)

  return kodlar

kod_sayisi = int(input("Kaç tane kod üretilsin? "))

kodlar = rastgele_kod_uret(kod_sayisi)

print("Kodlar:")
for kod in kodlar:
  print(kod)
  
  
