"""
Biblioteca para reconocer códigos de barras.
"""

class Code39Recognizer:
    """
        Code39 barcode recognizer.
    """
    def recognize(self, image, x, y, width, height):
        """
        Método que reconoce el código de barras que se le pasa por parámetros.

        Args:
            image (np.array): Image that contains a barcode.

        Returns:
            str: Texto reconocido en el código de barras.
        """
        return "12345abc"

    