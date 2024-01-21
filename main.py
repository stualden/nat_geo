# main.py for National Geographic project - merge thousands of JPEGs into PDFs, one per "issue"
# (sporadic at first, eventually monthly)
# Stu Alden 
################################################

import os, sys

import img2pdf  # install with conda install img2pdf (it's on conda forge)

# Suppress the rotation error messages
sys.stderr = open(os.devnull, 'w')

# Main Program ################################################################

image_folder = 'L:/Stu/_Projects/NatGeo/images'

decade = '/200x'  # Do a decade at a time and check for accuracy

# Build a list of all folders under that decade
ng_volumes = os.listdir(image_folder + decade )

# Now handle each folder in turn
for ng_volume in ng_volumes:

    image_path = image_folder + decade + '/' + ng_volume + '/' # final / needed for clean filenames!
  
    image_list = []                                                 
    for image in os.listdir(image_path):                            # Within folder, built list of jpegs  
        image_list.append(image_path + image)                       # Need the full filespec

    pdf_name = 'L:/Stu/_Projects/NatGeo/PDFs/NGM_' + \
                ng_volume[0:4] + '-' + ng_volume[4:6] + '-' + ng_volume[6:8] + '.pdf'   # readable name

    print("Writing:", pdf_name)
    with open(pdf_name, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(image_list, 
                                       rotation=img2pdf.Rotation.ifvalid))  # blast through rotation error
