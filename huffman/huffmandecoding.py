# from huffman.huffmancoding import HuffmanCoding
class HuffmanDecoding:
    """
    Clase HuffmanDecoding
    Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
    Autor: kevin Andres Acosta Rengifo,
           Rodolfo Leon Bolanos Florez
    Version: 2
    """
    def __init__(self):
        pass

    @staticmethod
    def decode(text, tree):
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


"""coding = HuffmanCoding()
encoded = coding.encode("un mundo mejor se crea ayudando a los demás, apoya a tu projimo")
tree = coding.get_tree()
print(coding.get_table())

decoding = HuffmanDecoding()
decoded = decoding.decode(encoded, tree"""