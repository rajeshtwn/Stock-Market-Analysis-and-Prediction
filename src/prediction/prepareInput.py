import pandas as pd
from sklearn import preprocessing
from pybrain.datasets import ClassificationDataSet

## to enable put/append/to_hdf by default store in the table format 
pd.set_option('io.hdf.default_format','table')

def load_hdf(filename):
    '''load hdf store. Parameter: hdfstore filename'''
    stockStore = pd.HDFStore('../../data/'+filename,complevel=9,complib='blosc')
    return stockStore
    
def load_data_frame(filename):
    dataframe = pd.read_csv('../../data/'+filename, index_col = 0, parse_dates = True)
    return dataframe

    
def normalize_dataset(dataframe):
    __ = True


def prepare_datasets(lst,dataframe, ratio):
    '''conversion from pandas dataframe to ClassificationDataSet of numpy'''
    alldata = ClassificationDataSet(1,1,nb_classes = 2)
    inp = dataframe[lst]
    for b,c in inp.values:
        if c=='up': c = 0
        elif c == 'down': c = 1
        else: c =2
        alldata.addSample([b],c)
    tstdata_temp, trndata_temp = alldata.splitWithProportion( ratio )
    # to convert supervised datasets to classification datasets
    tstdata = ClassificationDataSet(1, 1, nb_classes=2)
    for n in range(0, tstdata_temp.getLength()):
        tstdata.addSample( tstdata_temp.getSample(n)[0], tstdata_temp.getSample(n)[1] )
    trndata = ClassificationDataSet(1, 1, nb_classes=2)
    for n in range(0, trndata_temp.getLength()):
        trndata.addSample( trndata_temp.getSample(n)[0], trndata_temp.getSample(n)[1])
    trndata._convertToOneOfMany()
    tstdata._convertToOneOfMany()
    return alldata, trndata, tstdata

# if __name__== '__main__':
#     hdfStore = loadHdf('store.h5')
#     df = load_data_frame('signals_nabil')
#     ds = df_to_cds(df)
#     trndata, tstdata = prepare_datasets(ds, 0.25)
