#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Chaklader A. Arefe
# DATE CREATED: 08/03/2024
# REVISED DATE: 08/03/2024
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

def print_statistics(results_stats_dic):
    """Print percentage statistics from results."""
    print("\nModel Statistics:")
    for key, value in results_stats_dic.items():
        if key.startswith('p'):
            print(f"{key:20}: {value:5.1f}%")

def has_incorrect_dog_classifications(results_stats_dic):
    """Check if there are any incorrect dog/not-dog classifications."""
    total_correct = (results_stats_dic['n_correct_dogs'] + 
                    results_stats_dic['n_correct_notdogs'])
    return total_correct != results_stats_dic['n_images']

def has_incorrect_breed_classifications(results_stats_dic):
    """Check if there are any incorrect breed classifications."""
    return results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']

def print_incorrect_dogs(results_dic):
    """Print cases where dogs/not-dogs were incorrectly classified."""
    print("\nINCORRECT Dog/NOT Dog Assignments:")
    for key, values in results_dic.items():
        # Check if exactly one of is_dog or classified_as_dog is True
        if sum(values[3:]) == 1:
            print(f"Real: {values[0]:>26}   Classifier: {values[1]:>30}")

def print_incorrect_breeds(results_dic):
    """Print cases where dog breeds were incorrectly classified."""
    print("\nINCORRECT Dog Breed Assignment:")
    for key, values in results_dic.items():
        # Both are dogs (sum == 2) but breeds don't match (idx 2 == 0)
        if sum(values[3:]) == 2 and values[2] == 0:
            print(f"Real: {values[0]:>26}   Classifier: {values[1]:>30}")

def print_results(results_dic, results_stats_dic, model, 
                 print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                     a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                           False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                            False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    
    # Print statistics
    print(f"{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print(f"{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print(f"{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    print_statistics(results_stats_dic)
    
    # Print incorrect dogs if requested and if there are any
    if print_incorrect_dogs and has_incorrect_dog_classifications(results_stats_dic):
        print_incorrect_dogs(results_dic)
        
    # Print incorrect breeds if requested and if there are any
    if print_incorrect_breed and has_incorrect_breed_classifications(results_stats_dic):
        print_incorrect_breeds(results_dic)