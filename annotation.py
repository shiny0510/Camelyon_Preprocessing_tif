#%%
import sys
sys.path.append({'/opt/ASAP/bin'})

import multiresolutionimageinterface as mir
reader = mir.MultiResolutionImageReader()

mr_image = reader.open('camelyon17/centre_0/patient_010_node_4.tif')
annotation_list = mir.AnnotationList()
xml_repository = mir.XmlRepository(annotation_list)

xml_repository.setSource('camelyon17/centre_0/patient_010_node_4.xml')
xml_repository.load()
annotation_mask = mir.AnnotationToMask()
camelyon17_type_mask = True
label_map = {'metastases': 1, 'normal': 2} if camelyon17_type_mask else {'_0': 1, '_1': 1, '_2': 0}
conversion_order = ['metastases', 'normal'] if camelyon17_type_mask else  ['_0', '_1', '_2']
annotation_mask.convert(annotation_list, output_path, mr_image.getDimensions(), mr_image.getSpacing(), label_map, conversion_order)
# %%
