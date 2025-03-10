 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/XAS_data_reduction'] = NXprocess()
root['/entry/XAS_data_reduction'].attrs['EX_required'] = 'true'
root['/entry/XAS_data_reduction/parameters'] = NXparameters()
root['/entry/XAS_data_reduction/parameters'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxasproc
 
root['/entry/definition'] = NXfield('NXxasproc')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/XAS_data_reduction/program'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/XAS_data_reduction/program'].attrs['type'] = 'NX_CHAR'
root['/entry/XAS_data_reduction/program'].attrs['EX_required'] = 'true'
 
root['/entry/XAS_data_reduction/version'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/XAS_data_reduction/version'].attrs['type'] = 'NX_CHAR'
root['/entry/XAS_data_reduction/version'].attrs['EX_required'] = 'true'
 
root['/entry/XAS_data_reduction/date'] = NXfield('2021-03-29T15:51:45.804350')
root['/entry/XAS_data_reduction/date'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/XAS_data_reduction/date'].attrs['EX_required'] = 'true'
 
root['/entry/XAS_data_reduction/parameters/raw_file'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/XAS_data_reduction/parameters/raw_file'].attrs['type'] = 'NX_CHAR'
root['/entry/XAS_data_reduction/parameters/raw_file'].attrs['EX_required'] = 'true'
 
root['/entry/data/energy'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/data/energy'].attrs['type'] = 'NX_CHAR'
root['/entry/data/energy'].attrs['EX_required'] = 'true'
root['/entry/data/energy'].attrs['axis'] = '1'
 
root['/entry/data/data'] = NXfield(1.0)
root['/entry/data/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/data'].attrs['EX_required'] = 'true'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/XAS_data_reduction/program'].attrs['EX_doc'] = 'Name of the program used for reconstruction '
root['/entry/XAS_data_reduction/version'].attrs['EX_doc'] = 'Version of the program used '
root['/entry/XAS_data_reduction/date'].attrs['EX_doc'] = 'Date and time of reconstruction processing. '
root['/entry/XAS_data_reduction/parameters/raw_file'].attrs['EX_doc'] = 'Original raw data file this data was derived from '
root['/entry/data/data'].attrs['EX_doc'] = 'This is corrected and calibrated I(incoming)/I(absorbed). So it is the absorption. Expect attribute ``signal=1`` '
 

# Create the ATTRIBUTES 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXxasproc.nxs', 'w')


