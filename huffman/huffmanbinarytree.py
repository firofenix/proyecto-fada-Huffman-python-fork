class HuffmanBinaryTree:
    """
    Clase que implementa un árbol binario de Huffman
    Autor:Kevin Andres Acosta Rengifo
    """
    def __init__(self, key, left, right):
        """
        Constructor de la clase
        """
        self.llave = key
        self.left = left
        self.right = right

    def get_number_key(self):
        """
        Retorna el valor de la llave,
        si es un string retorna -1, si es un
        numero retorna el numero.
        """
        if self.get_llave().get_value() is None:
            return self.get_llave().get_key()
        else:
            return -1

    def get_left(self):
        """
    Retorna el hijo izquierdo del arbol.
    """
        return self.left

    def get_right(self):
        """
    Retorna el hijo derecho del arbol.
    """
        return self.right

    def get_llave(self):
        if self.llave is None:
            return None
        else:
            return self.llave


class Node:
    """
    Clase que implementa un nodo
    """
    def __init__(self, key, value):
        """
        Constructor de la clase
        """
        self.key = key
        self.value = value

    def get_key(self):
        numero = self.key
        return numero

    def get_value(self):
        # retorna el valor del nodo
        letra = self.value
        return letra