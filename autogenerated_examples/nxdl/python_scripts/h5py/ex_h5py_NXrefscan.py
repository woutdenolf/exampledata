 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXrefscan.h5', 'w')

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
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('control')
root['/entry/control'].attrs['NX_class'] = 'NXmonitor'
root['/entry/control'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-29T15:51:40.531791', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='end_time', data='2021-03-29T15:51:40.534797', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXrefscan
 
root['/entry'].create_dataset(name='definition', data='NXrefscan', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
#	 electron
 
root['/entry/instrument/source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator'].create_dataset(name='wavelength', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/wavelength'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['axis'] = '1'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/control/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
root['/entry/control/data'].attrs['units'] = 'NX_ANY'

# Create the LINKS 
root['/entry/data/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/data/data/'].attrs['target'] = '/entry/instrument/detector/data'

# Create the LINKS 
root['/entry/data/rotation_angle'] = h5py.SoftLink('/entry/sample/rotation_angle')
root['/entry/data/rotation_angle/'].attrs['target'] = '/entry/sample/rotation_angle'

# Create the LINKS 
root['/entry/data/polar_angle'] = h5py.SoftLink('/entry/instrument/detector/polar_angle')
root['/entry/data/polar_angle/'].attrs['target'] = '/entry/instrument/detector/polar_angle'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/control/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
root['/entry/control/data'].attrs['EX_doc'] = 'Monitor counts for each step '
 

# Create the ATTRIBUTES 
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXrefscan')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


