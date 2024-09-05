def reverse_string(s):
  reversed_string = ''
  for i in range(len(s) - 1, -1, -1):
    reversed_string += s[i]
  return reversed_string

# Exemplo de uso:
string = input("Digite uma string: ")
reversed_string = reverse_string(string)
print(f"String original: {string}")
print(f"String invertida: {reversed_string}")