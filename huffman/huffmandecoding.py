from huffman.huffmancoding import HuffmanCoding

class HuffmanDecoding:
    """
    Clase HuffmanDecoding
    Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        pass

    def decode(self, text, tree):
        """
        Decodifica un texto en base a un árbol de Huffman.
        :param text: texto a decodificar
        :param tree: árbol de Huffman
        :return: texto decodificado
        """
        text_decoded = ""
        arbol = tree
        for i in text:
            if i == "0":
                arbol = arbol.get_left()
            else:
                arbol = arbol.get_right()
            if arbol.get_llave().get_value() is not None:
                text_decoded += arbol.get_llave().get_value()
                arbol = tree
        return text_decoded

code = HuffmanCoding()
texto_codificado = code.encode("Hola mundo como esta mi gente linda")
decode = HuffmanDecoding()

texto_decodificado = decode.decode(texto_codificado, code.get_tree())
print(texto_decodificado)
