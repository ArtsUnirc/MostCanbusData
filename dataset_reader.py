import pyfiglet
import pandas as pd
import os
from pprint import pprint
import inquirer


#Variables definition:
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']
formats = ['decimal', 'hexadecimal']
scenarios = ['rural', 'suburban', 'urban']
gnss_data = ['timestamp','latitude', 'longitude', 'altitude'] #actually stored in the dataset
ecu_data = ['engine_speed', 'current_fuel_level', 'speed', 'eng_coolant_temp', 'acceleration', 'ambiental_temperature', 'fuel_rate'] #actually stored in the dataset
ny_choiches = ['no', 'yes']

#Messages to user:
format_query = 'Choose ECU data format'
scenario_query = 'Choose the desidered scenario'
source_query = 'Select the data source'
features_query = 'Select ECU data you want to use using right key or deselect using left key'
ny_query = 'Revert your previous choice?'

#Folders definition:
dataset_folder = os.path.dirname(os.path.abspath(__file__))+'/datasets/'
custom_folder = os.path.dirname(os.path.abspath(__file__))+'/custom_datasets/'


def testing_yn(x): #TESTED
    '''This function checks the user decision input. 
    Input are a string describing the required input and a parameter to customize this string, output is the user decision.'''
    while True:
        user_input = input('- '+x+' [y/n] ')
        if user_input.lower() not in yes_choices+no_choices:
                print('Invalid option! Type only y, yes, n or no.')
        else:
            return user_input
            break


def user_choiches(alternatives, message): #TESTED
    '''This function enables an interactive CLI to allow user to make choices. 
    Input are alternatives and instruction, output is a string.'''
    questions = [
            inquirer.List(
                "selection",
                message = message,
                choices = alternatives,
                        ),
                ]
    answers = inquirer.prompt(questions)
    return answers['selection']


def source_path(choosen_format, choosen_scenario): #TESTED
    '''This function defines the path to the selected data source, based on user choices. 
    Input are the choosen format and scenario, the output is a string to the selected source.'''
    selected_path = dataset_folder+choosen_format+'/'+choosen_scenario+'/'
    sources = os.listdir(selected_path)
    if len(sources) == 1:
         selected_source = selected_path+sources[0]
    elif len(sources) > 1:
        source = revert(user_choiches, sources, source_query)
        selected_source = selected_path+source
    return selected_source


def choosing_data(alternatives, message): #TESTED
    '''This function selects desidered dataset columns. 
    Output is a list of strings (i.e., dataset features).'''
    selected_features = []
    while bool(selected_features) is False:
        questions = [
            inquirer.Checkbox(
                "features",
                message = message,
                choices = alternatives,

            ),
        ]
        answers = inquirer.prompt(questions)
        selected_features = answers['features']
    return selected_features


def custom_dataset(selected_source, selected_data): #TESTED
    '''This function returns the dataset built by users. 
    Input is the list of selected fields, output is saved on a .csv file in custom_datasets directory.'''
    dataset = pd.read_csv(selected_source)
    dataset_name = input('Your dataset will be saved in the custom_datasets directory in .csv format. Please, enter a name: ')
    if len(selected_data) != len(ecu_data):
        selected_data = gnss_data + selected_data
        custom_dataset = dataset[selected_data]
        custom_dataset.to_csv(custom_folder+dataset_name+'.csv', index=False)
        print('Custom dataset generation done. Saving path: '+custom_folder)
    else:
        dataset.to_csv(custom_folder+dataset_name+'.csv', index=False)
        print('Dataset generation done. Saving path: '+custom_folder)


def revert(func, argument1, argument2): #TESTED
    '''This function confirms or reverts the single choice. 
    Inputs are the desidered function and its arguments, output is the desidered function output.'''
    output = func(argument1, argument2)
    while True:
        ans = user_choiches(ny_choiches, ny_query)
        if ans == 'yes':
           output = func(argument1, argument2)
        else:
            break
    return output


def saving_folder_creation(): #TESTED
    '''This function creates (if not exists) the folder to store created datasets.'''
    if not os.path.exists(custom_folder):
        os.makedirs(custom_folder)


def main():
    result = pyfiglet.figlet_format("CNMS Spoke 6 WP 1")
    print(result)
    print('This script has been deployed to use UniRC datasets created in the Spoke6 WP1 activities.')
    saving_folder_creation()
    data_format = revert(user_choiches, formats, format_query)
    scenario = revert(user_choiches, scenarios, scenario_query)
    path_to_source = source_path(data_format, scenario)
    data = revert(choosing_data, ecu_data, features_query)
    custom_dataset(path_to_source, data)

main()