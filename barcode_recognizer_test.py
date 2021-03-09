"""
Fichero con los test unitarios del reconocedor de códigos de barras.
"""

import unittest
import cv2
from barcode_recognizer import Code39Recognizer

class TestBarcodeRecognizer(unittest.TestCase):
    """
    Test unitarios de los reconocedores de códigos de barras.
    """

    def test_recognition(self):
        """
        Prueba el sistema de reconicimiento.
        """
        barcode = cv2.imread("code39.png")
        recognizer = Code39Recognizer()
        result = recognizer.recognize(barcode,0,0,100,100)
        self.assertEqual(result, "12345abc")

if __name__ == '__main__':
    unittest.main()
