 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXxas.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('source')
root['/entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('monochromator')
root['/entry/instrument/monochromator'].attrs['NX_class'] = 'NXmonochromator'
root['/entry/instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('incoming_beam')
root['/entry/instrument/incoming_beam'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/incoming_beam'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('absorbed_beam')
root['/entry/instrument/absorbed_beam'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/absorbed_beam'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('monitor')
root['/entry/monitor'].attrs['NX_class'] = 'NXmonitor'
root['/entry/monitor'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-29T15:51:45.626352', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxas
 
root['/entry'].create_dataset(name='definition', data='NXxas', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 x-ray
 
root['/entry/instrument/source'].create_dataset(name='probe', data='x-ray', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator'].create_dataset(name='energy', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/energy'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/energy'].attrs['axis'] = '1'
 
root['/entry/instrument/incoming_beam'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/incoming_beam/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/incoming_beam/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/absorbed_beam'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/absorbed_beam/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/absorbed_beam/data'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/monitor'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/monitor'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/monitor/data'].attrs['type'] = 'NX_INT'
root['/entry/monitor/data'].attrs['EX_required'] = 'true'

# Create the LINKS 
root['/entry/data/energy'] = h5py.SoftLink('/entry/instrument/monochromator/energy')
root['/entry/data/energy/'].attrs['target'] = '/entry/instrument/monochromator/energy'

# Create the LINKS 
root['/entry/data/absorbed_beam'] = h5py.SoftLink('/entry/instrument/absorbed_beam/data')
root['/entry/data/absorbed_beam/'].attrs['target'] = '/entry/instrument/absorbed_beam/data'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/absorbed_beam/data'].attrs['EX_doc'] = 'mark this field with attribute ``signal=1`` '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/monitor/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/monitor/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
 

# Create the ATTRIBUTES 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'absorbed_beam'
root['/entry/data/absorbed_beam'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXxas')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


