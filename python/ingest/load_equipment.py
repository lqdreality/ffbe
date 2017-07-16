import sys
from ingest.Ingestors import load_equipment

def main() :
    #infile = sys.argv[1]
    infile = '/home/chrism/ffbe/data/equipment.json'
    load_equipment(infile)

if __name__ == '__main__' :
    main()
