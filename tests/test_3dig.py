from src.numeros.lectura import lee3dig
import unittest


class TestLee3Dig(unittest.TestCase):
    def test_lee3dig(self):
        numeros = range(1000)
        for num in numeros:
            print(lee3dig(num))


if __name__ == '__main__':
    unittest.main()
