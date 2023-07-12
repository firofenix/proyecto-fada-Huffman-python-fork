from huffmanbinarytree import HuffmanBinaryTree
from huffmanbinarytree import node


class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        self.arbol = None
        self.tabla = None

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        text = text.lower()
        frecuencias = dict()
        for caracter in text:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
        lista = []

        for key in frecuencias:  # crea una lista de hojas de arbol con los caracteres y sus frecuencias
            lista.append(HuffmanBinaryTree(node(frecuencias[key], key), None, None))

        def obtener_frecuencia(arbol):
            return arbol.get_llave().get_key()

        # ordena la lista de hojas de arbol de menor a mayor frecuencia
        while len(lista) > 1:  # crea el arbol de huffman
            lista.sort(key=obtener_frecuencia)
            arbol1 = lista.pop(0)
            arbol2 = lista.pop(0)
            lista.append(HuffmanBinaryTree(node(arbol1.get_llave().get_key() + arbol2.get_llave().get_key(), None),
                                           arbol1, arbol2))
        self.arbol = lista[0]

        # aqui voy ya me devuelve el arbol de huffman
        # tarea -> crear la tabla de codificacion
        self.tabla = dict()
        self.tabla_auxiliar(self.arbol, "")
        print(self.tabla)
        texto_codificado = ""
        for caracter in text:
            texto_codificado += self.tabla[caracter]
        print(texto_codificado)
        return texto_codificado



    def get_tree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        raise NotImplementedError("Aún no implementado")

    def get_table(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        raise NotImplementedError("Aún no implementado")

    def get_summary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        raise NotImplementedError("Aún no implementado")


code = HuffmanCoding()
code.encode("Hola mundo como esta mi gente linda")
"""
h: 1
o: 4
l: 2
a: 3
 : 6
m: 3
u: 1
n: 3
d: 2
c: 1
e: 3
s: 1
t: 2
i: 2
g: 1

"""