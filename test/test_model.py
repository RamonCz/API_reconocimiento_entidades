import sys
sys.path.append("./app/modelo")

from model import model


m = model()
def test_get_entidades():
    texto =  "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares."
    resultado = {"oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                "entidades": {
                "Apple": "ORG",
                "Reino Unido": "LOC",}
                }
    assert resultado == m.get_entidades(texto)

def test_get_lista():
    texto = [
                    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                    "San Francisco considera prohibir los robots de entrega en la acera."
                    ]
    resultado = [
                {
                "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                "entidades": {
                "Apple": "ORG",
                "Reino Unido": "LOC",}
                },
                {
                "oración": "San Francisco considera prohibir los robots de entrega en la acera.",
                "entidades": {
                "San Francisco": "LOC"}
                }
                ]

    assert resultado == m.get_lista(texto)
