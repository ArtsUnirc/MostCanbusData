# CNMS-SPOKE6-WP1
This repository has been created to share and make usable the UniRC datasets created during the <em>Piano Nazionale di Ripresa e Resilienza</em> (PNRR) project activities. See flow_chart.pdf for major details.

## Prerequisities:
* Ubuntu OS (tested on v. 20.04 LTS and v. 22.04 LTS)
* python v. 3.8.10
* pyfiglet v. 0.8.post1
* inquirer v. 3.1.3

You can install <em>pyfiglet</em> using the following command:
```sh
pip install pyfiglet
```
You can install <em>inquirer</em> using the following command:
```sh
pip install inquirer
```

## Dataset description
The source datasets include ECU retrieved features, such as:
* Engine speed (OBD-II PID 0x0C).
* Current fuel level (OBD-II PID 0x2F).
* Speed (OBD-II PID 0x0D).
* Engine coolant temperature (OBD-II PID 0x05).
* Acceleration (OBD-II PID 0x5A).
* Ambiental temperature (OBD-II PID 0x46).
* Fuel rate (OBD-II PID 0x5E).

These features are in decimal or hexadecimal format.
Also, every data is merged with information about vehicle position retrieved simultaneously with ECU data. Specifically, position data includes latitude, longitude, and altitude.
Furthermore, acquired data refers to different mobility scenarios, such as rural, suburban, and urban. Every data has been collected along the streets of Reggio Calabria.


## Usage
Download this repository and from inside the <em>CNMS-SPOKE6-WP1</em> folder open a terminal to execute the following command:
```sh
python3 dataset_reader.py
```
The interactive command line user interface asks you to choose a data format, a mobility scenario, and the features to consider.
According to user choices, a dataset is generated and stored in .csv format in the <em>custom_datasets</em> folder.


## Note
This is a preliminary version of the application, so some of the included datasets in the homonym folder have been retained only for testing purposes. To see two examples of real datasets, select the following options from the command line:
* decimal format
* urban/suburban scenario
