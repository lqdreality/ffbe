from ffbe.ingest.Ingestors import *

EQUIPMENT_FILE = '/home/chrism/ffbe/data/ffbe/equipment.json'
UNIT_FILE = '/home/chrism/ffbe/data/ffbe/units.json'
PCKL_FILE = '/home/chrism/ffbe/data/equipment.pkl'
TMR_FILE = '/home/chrism/ffbe/data/tmr_equipment.txt'

write_tmr_equipment_file(UNIT_FILE, TMR_FILE)

load_equipment(EQUIPMENT_FILE, pckl=PCKL_FILE)
