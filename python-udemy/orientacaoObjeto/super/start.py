class MinhaString(str):
    def upper(self):
        print('Chamou upper')
        return super().upper()

string = MinhaString('Luiz')
print(string.upper())
