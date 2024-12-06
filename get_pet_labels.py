#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                          
# PROGRAMMER: Chaklader A. Arefe
# DATE CREATED: 08/03/2024
# REVISED DATE: 08/03/2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
##

from os import listdir

def create_pet_label(filename):
    """
    Creates a standardized pet label from a filename.
    Args:
        filename: The name of the pet image file
    Returns:
        A string containing the pet label
    """
    words = filename.lower().split('_')
    return ' '.join(word for word in words if word.isalpha()).strip()

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Get list of files, excluding hidden files
    image_files = [f for f in listdir(image_dir) if not f.startswith('.')]
    
    # Create dictionary with filename keys and pet name values
    results_dic = {}
    
    for filename in image_files:
        if filename not in results_dic:
            results_dic[filename] = [create_pet_label(filename)]
        else:
            print(f"** Warning: Duplicate files exist in directory: {filename}")
    
    return results_dic