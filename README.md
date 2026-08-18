## Clone this repo

From the command line navigate to where you would like this project to be and run this command:

`git clone git@github.com:allangustafson/hw_quicksort.git`

## Get data from ServiceNow HAM

1. Hardware Assets > Asset Estate > (gear icon in top right) > edit columns
   
     Add the following columns in this order
      
      - Model
      - Department
      - State
   
     Click OK to save

2. Click the 3 dots next to Department column. Select "contains" and type your department.
   
   Click the 3 dots next to State column. Uncheck "retired" and "missing"

3. In top right, export and select CSV.

4. Rename the CSV to `input_hw.csv` and place it in the directory you cloned from here alongside the python script.

## Run the script

From the command line navigate to the location of the script and run this command:

`python3 hw_quicksort.py`

The script will output a csv named `output_hw.csv` with the following columns:

category | model | quantity 

You can copy these columns into your spreadsheet. You may have to play with formatting to get it to look nice. Adding all borders and setting row height to 33.75 worked for us.
