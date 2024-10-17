import random

def palavras(palavra: str):
   palavraembaralhada = random.shuffle(palavra)
   print(palavraembaralhada)
   return ''.join(palavra)


palavras("Alek")