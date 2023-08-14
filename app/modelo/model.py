class model:
    def __init__(self) -> None:
        import spacy
        self.nlp = spacy.load("es_core_news_sm")
        import es_core_news_sm
        self.nlp = es_core_news_sm.load()
    
       
    def get_entidades(self, texto):
        """
        Obtiene las entidades de una sola oracion
        params: texto
        return: diccionario con la oracion y las entidades  
        """
        doc = self.nlp(texto)
        output = {"oración": texto, "entidades": {}}
        for ent in doc.ents:
            output["entidades"][ent.text] = ent.label_
        return output
    
    def get_lista(self, lista):
        """
        Obtiene las entidades de una lista de oraciones.
        params: lista de oraciones
        return: lista de entidades por oracion
        """
        resultado =  []
        for e in lista:
            ent = self.get_entidades(e)
            resultado.append(ent)

        return resultado

'''
m = model()
texto = [
 "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
 "San Francisco considera prohibir los robots de entrega en la acera."
 ]

s = m.get_lista(texto)
print(s)
'''