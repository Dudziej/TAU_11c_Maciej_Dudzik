import pytest
from main import Komendy
from main import func


class TestClass:
    def test_komendy_bstart(self):
        hasattr(Komendy, 'komendy')

    def test_komendy_astart(self):
        sysname = "Windows"
        komendy = Komendy(sysname)
        hasattr(komendy, 'komendy')

    def test_sysname_windows(self):
        sysname = "Windows"
        komendy = Komendy(sysname)
        assert komendy.sysname == sysname

    def test_sysname_linux(self):
        sysname = "Linux"
        komendy = Komendy(sysname)
        assert komendy.sysname == sysname

    def test_sysname_bad(self):
        sysname = "bad"
        with pytest.raises(Exception):
            Komendy(sysname)

    def test_sysname_liczba(self):
        sysname = 256
        with pytest.raises(Exception):
            Komendy(sysname)

    def test_sysname_tablica(self):
        sysname = [2, 1, 3, 7]
        with pytest.raises(Exception):
            Komendy(sysname)

    def test_sysname_none(self):
        sysname = None
        with pytest.raises(Exception):
            Komendy(sysname)

    def test_sysname_float(self):
        sysname = 4.20
        with pytest.raises(Exception):
            Komendy(sysname)


class TestClassWindows:
    def test_win_exit(self):
        komenda = Komendy("Windows")
        result = komenda.help('exit')
        assert result == 'zamyka cmd'

    def test_win_bad_kom(self):
        komenda = Komendy("Windows")
        result = komenda.help('pieniadzezalas')
        assert result is None

    def test_win_bad_kom_arg(self):
        komenda = Komendy("Windows")
        result = komenda.help('gdzie -sa')
        assert result is None

    def test_win_cd_arg(self):
        komenda = Komendy("Windows")
        result = komenda.help('cd ..')
        assert result == 'wyjscie z folderu'

    def test_win_cd_arg2(self):
        komenda = Komendy("Windows")
        result = komenda.help('cd Desktop')
        assert result == '{argument} wejscie do folderu'

    def test_win_cd_arg_bad_arg(self):
        komenda = Komendy("Windows")
        result = komenda.help('cd .. wololo')
        assert result == 'wyjscie z folderu'

    def test_win_none(self):
        komenda = Komendy("Windows")
        result = komenda.help(None)
        assert result is None


class TestClassLinux:

    def test_linux_rm_arg(self):
        komenda = Komendy("Linux")
        result = komenda.help('rm -f')
        assert result == 'usunięcie plików zabezpieczonych'

    def test_linux_ls(self):
        komenda = Komendy("Linux")
        result = komenda.help('ls')
        assert result == 'wyświetla pliki i katalogi'

    def test_linux_bad_kom_arguments(self):
        komenda = Komendy("Linux")
        result = komenda.help('my -nameis')
        assert result is None

    def test_linux_bad_kom_arg_arg(self):
        komenda = Komendy("Linux")
        result = komenda.help('my -nameis Jeff')
        assert result is None

    def test_linux_int(self):
        komenda = Komendy("Linux")
        result = komenda.help(420)
        assert result is None

    def test_linux_empty(self):
        komenda = Komendy("Linux")
        result = komenda.help("")
        assert result is None

    def test_linux_pwd(self):
        komenda = Komendy("Linux")
        result = komenda.help("pwd")
        assert result == 'wyświetla aktualną ścieżkę'


class TestClassLab7:
    random_num = [(100, None), (-0.420, None),(func, None), ([4, 2, 0], None), (-2.137, None),  (1, 1), (0, 0),
                  (2, 1), (3, 2), (4, 2021), (float('inf'), None), (85, 2137420), ("9", None),
                  (float('-inf'), None)]

    @pytest.mark.parametrize("number,expected", random_num)
    def test_func(number, expected):
        assert func(number) == expected
