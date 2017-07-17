from Character import *
from Equipment import *


c = Character()
e = HandWeapon()
e.etype = 'Spear'
c.equip(e)
print(c.equipment)
