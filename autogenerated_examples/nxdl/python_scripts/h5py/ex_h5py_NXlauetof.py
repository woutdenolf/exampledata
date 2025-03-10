 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXlauetof.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('control')
root['/entry/control'].attrs['NX_class'] = 'NXmonitor'
root['/entry/control'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('name')
root['/entry/name'].attrs['NX_class'] = 'NXdata'
root['/entry/name'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXlauetof
 
root['/entry'].create_dataset(name='definition', data='NXlauetof', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='azimuthal_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/azimuthal_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/azimuthal_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='time_of_flight', data=1.0, maxshape=None)
root['/entry/instrument/detector/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='orientation_matrix', data=1.0, maxshape=None)
root['/entry/sample/orientation_matrix'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/orientation_matrix'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='unit_cell', data=1.0, maxshape=None)
root['/entry/sample/unit_cell'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/unit_cell'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/control/data'].attrs['type'] = 'NX_INT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='time_of_flight', data=1.0, maxshape=None)
root['/entry/control/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/control/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'

# Create the LINKS 
root['/entry/name/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/name/data/'].attrs['target'] = '/entry/instrument/detector/data'

# Create the LINKS 
root['/entry/name/time_of_flight'] = h5py.SoftLink('/entry/instrument/detector/time_of_flight')
root['/entry/name/time_of_flight/'].attrs['target'] = '/entry/instrument/detector/time_of_flight'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/detector'].attrs['EX_doc'] = 'This assumes a planar 2D detector. All angles and distances refer to the center of the detector. '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = 'The polar_angle (two theta) where the detector is placed. '
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_doc'] = 'The azimuthal angle where the detector is placed. '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/sample/orientation_matrix'].attrs['EX_doc'] = 'The orientation matrix according to Busing and Levy conventions. This is not strictly necessary as the UB can always be derived from the data. But let us bow to common usage which includes thie UB nearly always. '
root['/entry/sample/unit_cell'].attrs['EX_doc'] = 'The unit cell, a, b, c, alpha, beta, gamma. Again, not strictly necessary, but normally written. '
root['/entry/control/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
root['/entry/control/data'].attrs['EX_doc'] = 'use these attributes ``primary=1 signal=1`` '
 

# Create the ATTRIBUTES 
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'name'
root['/entry/name'].attrs['signal'] = 'data'
root['/entry/name/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXlauetof')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


