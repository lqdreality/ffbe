import operator
import sys
from Search import find_equipment
from ingest.Ingestors import load_equipment

def main() :
    # Load in equipment data
    infile = sys.argv[1]
    elist = load_equipment(infile)

    # Find all Dagger's with ATK >= 100
    e = find_equipment(elist,
                   etypes=['Dagger'], 
                   stats=['ATK'], 
                   operators=[operator.ge], 
                   comp_vals=[100],
                   verbose=True)

    # Find the equipment named holy rod
    e = find_equipment(elist, name='Holy Rod', verbose=True)

    # Find any equipment with ATK >= 30 and MAG >= 20
    e = find_equipment(elist, 
                       stats=['ATK', 'MAG'],
                       operators=[operator.ge, operator.ge],
                       comp_vals=[30, 20],
                       search_all=True,
                       verbose=True)

    # Find a staff with MAG in between 10 and 20
    e = find_equipment(elist,
                       etypes=['Staff'],
                       stats='MAG',
                       operators=[operator.ge, operator.le],
                       comp_vals=[10,20],
                       verbose=True)

    # Find a staff with ATK and MAG >= 10
    e = find_equipment(elist,
                       etypes=['Staff'],
                       stats=['MAG', 'ATK'],
                       operators=operator.gt,
                       comp_vals=10,
                       verbose=True)

if __name__ == '__main__' :
    main()
