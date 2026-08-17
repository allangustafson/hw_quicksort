import csv

def getDataInput() -> list:
    '''
    Read the CSV
    All values are string format
    :return: list of lists of strings
    '''

    try:
        with open('input_hw.csv', 'r') as f:
            reader = csv.reader(f)
            #list of lists starting after headers
            data = [row for row in reader][1:]

    # general exception catch
    except Exception as err:
        print(f"General error: {format(err)}")

    return data
def outputCSV(hw_dict):
    hw_dict = dict(sorted(hw_dict.items()))
    with open('output_hw.csv', 'w') as f:
        writer = csv.writer(f)
        for key, value in hw_dict.items():
            writer.writerow([key, value])

    
def main():
    lData = getDataInput()
    
    dModels = {}

    for record in lData:
        
        sModel = str(record[0])
        
        if sModel in dModels:
            dModels[sModel] += 1
        else:
            dModels.update({sModel: 1})

    outputCSV(dModels)
if __name__ == "__main__":
    main()
