from huffman.huffmanbinarytree import HuffmanBinaryTree
from huffman.huffmanbinarytree import Node

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: Kevin Andres Acosta Rengifo
    Version: <1>
    """
    def __init__(self):
        self.arbol = None
        self.tabla = None
        self.Num_nodos = 0
        self.profundidad = 0
        self.compresion = 0.0

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        # ------------------variables------------------
        text = text.lower()
        frecuencias = dict()
        tamano_texto = len(text)
        # ---------------------------------------------
        for caracter in text:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1

        lista = []
        for key in frecuencias:  # crea una lista de hojas de arbol con los caracteres y sus frecuencias
            lista.append(HuffmanBinaryTree(Node(frecuencias[key], key), None, None))

        def obtener_frecuencia(arbol):
            return arbol.get_llave().get_key()

        self.Num_nodos = len(lista)
        # ordena la lista de hojas de arbol de menor a mayor frecuencia
        while len(lista) > 1:  # crea el arbol de huffman
            lista.sort(key=obtener_frecuencia)
            arbol1 = lista.pop(0)
            arbol2 = lista.pop(0)
            self.Num_nodos += 1
            lista.append(HuffmanBinaryTree(Node(arbol1.get_llave().get_key() + arbol2.get_llave().get_key(), None),
                                           arbol1, arbol2))
        self.arbol = lista[0]  # ya se crea el arbol de huffman

        # aqui voy ya me devuelve el arbol de huffman
        self.tabla = dict()

        def crear_tabla(arbol, codigo):
            if arbol.get_llave().get_value() is not None:
                self.tabla[arbol.get_llave().get_value()] = codigo
                return 0
            else:
                profundidad_left = 0
                profundidad_right = 0
                if arbol.get_left() is not None:
                    profundidad_left = crear_tabla(arbol.get_left(), codigo + "0")

                if arbol.get_right() is not None:
                    profundidad_right = crear_tabla(arbol.get_right(), codigo + "1")

            profundidad_Actual = max(profundidad_left, profundidad_right) + 1
            return profundidad_Actual
        self.profundidad = crear_tabla(self.arbol, "")

        text_coding = ""
        for car in text:

            text_coding += self.tabla[car]  # codificación del texto

        self.compresion = (1 - (len(text_coding) / (tamano_texto * 256))) * 100
        self.compresion = round(self.compresion, 3)  # porcentaje de compresión redondeado a 3 decimales
        return text_coding

    def get_tree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        return self.arbol

    def get_table(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        return self.tabla

    def get_summary(self):
        """
        return: resumen de la codificación en formato string
        """
        return {
           'Porcentaje de compresión': str(self.compresion) + '%',
           'Número de nodos del árbol': self.Num_nodos,
           'Profundidad del árbol': self.profundidad
        }