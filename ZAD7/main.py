class Komendy:

    def __init__(self, sysname):

        self.komendy_windows = {
            'cd': {
                '': '{argument} wejscie do folderu / wyświetla aktualną ścieżkę',
                '..': 'wyjscie z folderu',
            },
            'exit': {
                '': 'zamyka cmd'
            },
            'mkdir': {
                '': '{argument} Tworzy folder o nazwie z argumentu'
            },
            'rd': {
                '': 'usuwa pliki',
                '-r': 'usuwa wszystkie pliki'
            },
            'date': {
                '': 'wyświetla dzisiejszą date',
            }
        }

        self.komendy_linux = {
            'ls': {
                '': 'wyświetla pliki i katalogi',
                '-a': 'pokazuje ukryte pliki',
                '-l': 'pokazuje więcej informacji o pliku'
            },
            'pwd': {
                '': 'wyświetla aktualną ścieżkę'
            },
            'cd': {
                '': '{argument} wejscie do folderu',
                '..': 'wyjscie z folderu',
            },
            'mkdir': {
                '': '{argument} Tworzy folder o nazwie z argumentu'
            },
            'rm': {
                '': 'usuwa pliki',
                '-f': 'usunięcie plików zabezpieczonych',
                '-r': 'usunięcie plików również w podfolderach'
            }
        }

        if sysname == "Windows":
            self.komendy = self.komendy_windows
        elif sysname == "Linux":
            self.komendy = self.komendy_linux
        else:
            raise Exception("Zla nazwa systemu")

        self.sysname = sysname

    def dobra_komenda(self, zla_komenda):
        if not isinstance(zla_komenda, str):
            return None
        wsio = zla_komenda.lower().split(" ")
        if len(wsio) < 1:
            return None
        return wsio

    def help(self, zla_komenda):
        wsio = self.dobra_komenda(zla_komenda)
        if wsio is None:
            return None

        if wsio[0] in self.komendy:
            komenda = self.komendy[wsio[0]]
            if len(wsio) > 1:
                if wsio[1] in komenda:
                    return komenda[wsio[1]]
                else:
                    return komenda['']
            else:
                return komenda['']
        else:
            return None


komenda = Komendy("Windows")
result = komenda.help('help -help')
print(result)


def func(n):
    if type(n) is not int:
        return None
    elif n < 0:
        return None
    elif n == 0:
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return func(n - 1) + func(n - 2)
