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
            if ("imac" in key.lower()):
                category = "AIO"
            elif ("latitude" in key.lower() or "thinkbook" in key.lower() or 
                  "thinkpad" in key.lower() or "macbook" in key.lower() or
                  "laptop" in key.lower() or "notebook" in key.lower()):
                category = "Laptop"
            elif ("optiplex" in key.lower() or "precision" in key.lower() or 
                  "thinkcentre" in key.lower() or "thinkstation" in key.lower() or
                  "tower" in key.lower() or "workstation" in key.lower()):
                category = "Desktop"
            elif ("ipad" in key.lower() or "surface" in key.lower() or 
                  "galaxy" in key.lower()):
                category = "Tablet"
            else:
                category = "Other"
            writer.writerow([category, key, value])

    
def main():
    lData = getDataInput()
    
    dModels = {}

    for record in lData:
        
        sModel = str(record[0])
        
        if sModel in dModels:
            dModels[sModel] += 1
        else:
            category = "single"
            dModels.update({sModel: 1})

    outputCSV(dModels)
if __name__ == "__main__":
    main()
