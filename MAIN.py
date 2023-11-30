import os
from funcs import *

#user input ======================================================================================================
#CHANGE img_dir1 to be your path
#CHANGE img_dir2 to be your path with a forward slash before spaces 

img_dir1  = #"/Users/user/Desktop/Motorbike_Files/Triumph_Tiger_Cub/Documenting Restoration/Images/time_ordered/"
img_dir2  = #"/Users/user/Desktop/Motorbike_Files/Triumph_Tiger_Cub/Documenting\ Restoration/Images/time_ordered/"
#=================================================================================================================


#set directory 
os.chdir(img_dir1)
onlyfiles, onlyfilesnospace = onboard_filenames(img_dir1)

#create dictionary to associate filename and date 
dates_dict  = sort_namedate(onlyfiles, onlyfilesnospace, img_dir2)

#sort by date in a list 
sorted_list = list(sorted(dates_dict.items(), key=lambda item: item[1]))

#rename the files
rename_files(sorted_list)
