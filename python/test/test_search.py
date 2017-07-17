import operator
import sys
from Search import find_equipment
from ingest.Ingestors import load_equipment

def main() :
    infile = sys.argv[1]
    elist = load_equipment(infile)
    find_equipment(elist=elist, 
                   etypes=['Dagger'], 
                   stats=['ATK'], 
                   operators=[operator.ge], 
                   comp_vals=[100],
                   search_all=True)

if __name__ == '__main__' :
    main()
