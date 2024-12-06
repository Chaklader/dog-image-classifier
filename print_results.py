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
##

def print_percentage_stats(results_stats_dic):
    """Print percentage statistics from results."""
    print("\nModel Statistics:")
    for key, value in results_stats_dic.items():
        if key.startswith('p'):
            print("{:20}: {:.1f}%".format(key, value))

def check_incorrect_dogs(results_stats_dic):
    """Check if there are any incorrect dog/not-dog classifications."""
    total_correct = (results_stats_dic['n_correct_dogs'] + 
                    results_stats_dic['n_correct_notdogs'])
    return total_correct != results_stats_dic['n_images']

def check_incorrect_breeds(results_stats_dic):
    """Check if there are any incorrect breed classifications."""
    return results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']

def display_incorrect_dogs(results_dic):
    """Print cases where dogs/not-dogs were incorrectly classified."""
    print("\nINCORRECT Dog/NOT Dog Assignments:")
    for key, values in results_dic.items():
        # Check if exactly one of is_dog or classified_as_dog is True
        if sum(values[3:]) == 1:
            print("Real: {:>26}   Classifier: {:>30}".format(values[0], values[1]))

def display_incorrect_breeds(results_dic):
    """Print cases where dog breeds were incorrectly classified."""
    print("\nINCORRECT Dog Breed Assignment:")
    for key, values in results_dic.items():
        # Both are dogs (sum == 2) but breeds don't match (idx 2 == 0)
        if sum(values[3:]) == 2 and values[2] == 0:
            print("Real: {:>26}   Classifier: {:>30}".format(values[0], values[1]))

def print_results(results_dic, results_stats_dic, model, 
                 should_print_incorrect_dogs=False, 
                 should_print_incorrect_breed=False):
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
      should_print_incorrect_dogs - True prints incorrectly classified dog images
                           False doesn't print anything(default) (bool)  
      should_print_incorrect_breed - True prints incorrectly classified dog breeds
                            False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    print("\n\n*** Results Summary for CNN Model Architecture {} ***".format(model.upper()))
    
    # Print basic statistics
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    
    # Print percentage statistics
    print_percentage_stats(results_stats_dic)
    
    # Print incorrect dogs if requested and if there are any
    if should_print_incorrect_dogs and check_incorrect_dogs(results_stats_dic):
        display_incorrect_dogs(results_dic)
        
    # Print incorrect breeds if requested and if there are any
    if should_print_incorrect_breed and check_incorrect_breeds(results_stats_dic):
        display_incorrect_breeds(results_dic)