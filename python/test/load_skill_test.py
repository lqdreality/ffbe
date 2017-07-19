import operator
import sys
from Search import find_skills
from ingest.Ingestors import load_skills

def main() :
    # Load in equipment data
    infile = sys.argv[1]
    slist = load_skills(infile, verbose=True)

if __name__ == '__main__' :
    main()
