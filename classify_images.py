#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Chaklader Asfak Arefe
# DATE CREATED: August 3, 2024
# REVISED DATE: August 3, 2024
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function
#             and as in_arg.dir for function call within main.
#            -The results dictionary as results_dic within classify_images
#             function and results for the function call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main.

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function.
    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
        # Runs classifier function to classify the images classifier function 
        # inputs: path + filename  and  model, returns model_label 
        # as classifier label
        model_label = classifier(images_dir + key, model)

        # Processes the results so they can be compared with pet image labels
        # set labels to lowercase (lower) and stripping off whitespace(strip)
        model_label = model_label.lower().strip()
              
        # defines truth as pet image label 
        truth = results_dic[key][0]

        # If the pet image label is found within the classifier label list of terms 
        # as an exact match to on of the terms in the list - then they are added to 
        # results_dic as an exact match(1) using extend list function
        if truth in model_label:
            results_dic[key].extend([model_label, 1])

        # if not found then added to results dictionary as NOT a match(0) using
        # the extend function 
        else:
            results_dic[key].extend([model_label, 0])