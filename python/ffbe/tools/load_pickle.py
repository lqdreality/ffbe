import pickle
def load_pickle(fname) :
    f = open(fname, 'rb')
    data = pickle.load(f)
    f.close()
    return data
