"""6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów."""


days = {'Jan': 31, 'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

for key, value in days.items():

   print (key, value)

def all_unique(days):
    return len(days) == len(set(days))
