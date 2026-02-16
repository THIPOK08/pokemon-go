types = [
  'Grass','Ice','Posion','Rock','Fire','Dragon','Dark','Electic',
  'Ground','Water','Flying','Fairy','Steel','Normal','Ghost',
  'Bug','Psychic','Fighting'
]

from pokemon.models import Type
from pokemon.extensions import db
def create_pokemon_types():
  for type in types:
    pt = Type(name=type)
    db.session.add(pt)
    db.session.commit()