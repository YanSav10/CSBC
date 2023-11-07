import unittest
from test_mymath import TestAdd

def my_suite():
    # Створюємо екземпляр TestSuite
    suite = unittest.TestSuite()

    # Додаємо тестовий набір до сукупності
    suite.addTest(unittest.makeSuite(TestAdd))

    # Створюємо екземпляр TestResult для збереження результатів тестів
    result = unittest.TestResult()

    # Створюємо екземпляр TextTestRunner для запуску тестів та виведення результатів
    runner = unittest.TextTestRunner()

    # Запускаємо тестовий набір та виводимо результати
    runner.run(suite)

if __name__ == '__main__':
    my_suite()
