#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 05/14/2018                                  
# REVISED DATE: 08/03/2024                      
# PURPOSE: Functions for checking and validating the image classification code.
#          Each function is designed to test a specific part of the classification
#          process and print relevant statistics and comparisons.
##

from typing import Dict, List, Union, Optional
from argparse import Namespace

def print_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{title}")

def print_dict_preview(dictionary: dict, num_items: int = 10) -> None:
    """Print first n items of a dictionary in a formatted way."""
    items_to_show = min(num_items, len(dictionary))
    print(f"\nDictionary has {len(dictionary)} items.")
    print(f"Showing first {items_to_show} items:")
    
    for i, (key, value) in enumerate(dictionary.items(), 1):
        if i > items_to_show:
            break
        print(f"{i:2d} key: {key:>30}  label: {value[0]:>26}")

def check_command_line_arguments(in_arg: Optional[Namespace]) -> None:
    """
    Validate and print command line arguments.
    
    Args:
        in_arg: Namespace object containing command line arguments
    """
    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
        return
        
    print("Command Line Arguments:")
    print(f"     dir = {in_arg.dir}")
    print(f"    arch = {in_arg.arch}")
    print(f" dogfile = {in_arg.dogfile}")

def check_creating_pet_image_labels(results_dic: Optional[Dict[str, List[str]]]) -> None:
    """
    Validate and print pet image label dictionary.
    
    Args:
        results_dic: Dictionary with image filenames as keys and pet labels as values
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
        return
        
    print_dict_preview(results_dic)

def print_match_results(results_dic: Dict[str, List], match: bool = True) -> tuple:
    """
    Print matching or non-matching classification results.
    
    Args:
        results_dic: Results dictionary containing classification data
        match: If True, print matches; if False, print non-matches
    
    Returns:
        tuple: Count of matches/non-matches
    """
    count = 0
    header = "     MATCH:" if match else " NOT A MATCH:"
    print_header(header)
    
    match_value = 1 if match else 0
    for key, values in results_dic.items():
        if values[2] == match_value:
            count += 1
            if len(values) >= 5:  # Full results including dog classification
                print(f"\n{key:>30}: \nReal: {values[0]:>26}   Classifier: {values[1]:>30}"
                      f"\nPetLabelDog: {values[3]:1d}  ClassLabelDog: {values[4]:1d}")
            else:  # Basic results
                print(f"\n{key:>30}: \nReal: {values[0]:>26}   Classifier: {values[1]:>30}")
    
    return count

def check_classifying_images(results_dic: Optional[Dict[str, List]]) -> None:
    """
    Validate and print image classification results.
    
    Args:
        results_dic: Dictionary containing classification results
    """
    if not results_dic or len(next(iter(results_dic.values()))) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
        return
        
    n_match = print_match_results(results_dic, match=True)
    n_notmatch = print_match_results(results_dic, match=False)
    
    print(f"\n# Total Images {n_match + n_notmatch}, # Matches: {n_match}, "
          f"# NOT Matches: {n_notmatch}")

def check_classifying_labels_as_dogs(results_dic: Optional[Dict[str, List]]) -> None:
    """
    Validate and print dog classification results.
    
    Args:
        results_dic: Dictionary containing dog classification results
    """
    if not results_dic or len(next(iter(results_dic.values()))) < 4:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
        return
        
    n_match = print_match_results(results_dic, match=True)
    n_notmatch = print_match_results(results_dic, match=False)
    
    print(f"\n# Total Images {n_match + n_notmatch}, # Matches: {n_match}, "
          f"# NOT Matches: {n_notmatch}")

def calculate_statistics(results_dic: Dict[str, List]) -> dict:
    """
    Calculate classification statistics from results dictionary.
    
    Args:
        results_dic: Dictionary containing classification results
    
    Returns:
        dict: Calculated statistics
    """
    n_images = len(results_dic)
    n_pet_dog = sum(1 for v in results_dic.values() if v[3] == 1)
    n_pet_notd = n_images - n_pet_dog
    n_class_cdog = sum(1 for v in results_dic.values() if v[3] == 1 and v[4] == 1)
    n_class_cnotd = sum(1 for v in results_dic.values() if v[3] == 0 and v[4] == 0)
    n_match_breed = sum(1 for v in results_dic.values() if v[2] == 1 and v[3] == 1 and v[4] == 1)
    
    return {
        'n_images': n_images,
        'n_pet_dog': n_pet_dog,
        'n_pet_notd': n_pet_notd,
        'pct_corr_dog': (n_class_cdog / n_pet_dog * 100) if n_pet_dog else 0,
        'pct_corr_notdog': (n_class_cnotd / n_pet_notd * 100) if n_pet_notd else 0,
        'pct_corr_breed': (n_match_breed / n_pet_dog * 100) if n_pet_dog else 0
    }

def print_statistics(stats: dict, source: str) -> None:
    """
    Print formatted statistics.
    
    Args:
        stats: Dictionary containing statistics
        source: Source of the statistics (for header)
    """
    print(f"\n ** Statistics from {source}:")
    print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d}"
          "\nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              stats['n_images'], stats['n_pet_dog'], stats['n_pet_notd'],
              stats['pct_corr_dog'], stats['pct_corr_notdog'], stats['pct_corr_breed']))

def check_calculating_results(results_dic: Optional[Dict[str, List]], 
                            results_stats_dic: Optional[Dict[str, Union[int, float]]]) -> None:
    """
    Compare calculated statistics with provided statistics dictionary.
    
    Args:
        results_dic: Dictionary containing classification results
        results_stats_dic: Dictionary containing pre-calculated statistics
    """
    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
        return
    
    # Print provided statistics
    provided_stats = {
        'n_images': results_stats_dic['n_images'],
        'n_pet_dog': results_stats_dic['n_dogs_img'],
        'n_pet_notd': results_stats_dic['n_notdogs_img'],
        'pct_corr_dog': results_stats_dic['pct_correct_dogs'],
        'pct_corr_notdog': results_stats_dic['pct_correct_notdogs'],
        'pct_corr_breed': results_stats_dic['pct_correct_breed']
    }
    print_statistics(provided_stats, "calculates_results_stats() function")
    
    # Calculate and print verification statistics
    calc_stats = calculate_statistics(results_dic)
    print_statistics(calc_stats, "function check")
