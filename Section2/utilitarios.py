def ler_string(s):
  return s

def ler_num(f):
  return f*f

def nome_contrario(s):
  return s[::-1]

def palindromo(s):
  if(s == s[::-1]):
    return True
  else:
    return False