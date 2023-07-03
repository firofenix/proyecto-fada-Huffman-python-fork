

class HuffmanBinaryTree:
  """
  Clase que implementa un árbol binario de Huffman
  Autor:<Estudiantes>
  """ 
  def __init__(self):
    """
    Constructor de la clase
    """
    self.key = None
    self.left = None
    self.right = None


  def getNumberKey(self):
    """
    Retorna el valor de la llave, 
    si es un string retorna -1, si es un 
    numero retorna el numero.
    """
    raise NotImplementedError("Aún no implementado")

  def getLeft(self):
    """
    Retorna el hijo izquierdo del arbol.
    """
    raise NotImplementedError("Aún no implementado")
  

  def getRight(self):
    """
    Retorna el hijo derecho del arbol.
    """
    raise NotImplementedError("Aún no implementado")
