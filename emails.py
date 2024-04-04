info = {
  'nome': ['João', 'Paula', 'Maria'],
  'telefone': ['99887766', '94578899', '98564321'],
  'email': ['oqibz@example.com', 'xcvkp@example.com', 'tugrp@example.com']
}

def Visual(separador = '.'):
  print(separador * 25)
  print(separador * 25)



for i in range(len(info['nome'])):
  print(f"Nome: {info['nome'][i]}")
  print(f"Telefone: {info['telefone'][i]}")
  print(f"Email: {info['email'][i]}")
  Visual()
