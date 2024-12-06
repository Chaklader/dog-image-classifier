#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                          
# PROGRAMMER: Chaklader A. Arefe
# DATE CREATED: 08/03/2024
# REVISED DATE: 08/03/2024
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
##

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.
    """
    stats = {
        'n_dogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0,
        'n_images': len(results_dic)
    }
    
    for _, result in results_dic.items():
        # Unpack values for better readability
        _, _, label_match, is_dog, classified_as_dog = result
        
        # Update match count
        stats['n_match'] += label_match
        
        if is_dog:
            stats['n_dogs_img'] += 1
            stats['n_correct_dogs'] += classified_as_dog
            stats['n_correct_breed'] += (label_match and is_dog)
        else:
            stats['n_correct_notdogs'] += (not classified_as_dog)
    
    # Calculate derived statistics
    stats['n_notdogs_img'] = stats['n_images'] - stats['n_dogs_img']
    
    # Calculate percentages
    def calculate_percentage(numerator, denominator):
        return (numerator / denominator * 100.0) if denominator > 0 else 0.0
    
    stats['pct_match'] = calculate_percentage(stats['n_match'], stats['n_images'])
    stats['pct_correct_dogs'] = calculate_percentage(stats['n_correct_dogs'], stats['n_dogs_img'])
    stats['pct_correct_breed'] = calculate_percentage(stats['n_correct_breed'], stats['n_dogs_img'])
    stats['pct_correct_notdogs'] = calculate_percentage(stats['n_correct_notdogs'], stats['n_notdogs_img'])
    
    return stats