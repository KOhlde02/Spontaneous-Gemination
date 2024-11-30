import pandas as pd
from pyxlsb import open_workbook

with open_workbook("BHSzip.xlsb") as wb:     # processing each sheet as a dataframe
    torah = wb.get_sheet("Torah")
    former_prophets = wb.get_sheet("FormerProphets")
    latter_prophets = wb.get_sheet("LatterProphets")
    writings = wb.get_sheet("Writings")

    torah_data = []
    for row in torah.rows():
        row_data = [cell.v for cell in row]
        torah_data.append(row_data)

    former_prophets_data = []
    for row in former_prophets.rows():
        row_data = [cell.v for cell in row]
        former_prophets_data.append(row_data)

    latter_prophets_data = []
    for row in latter_prophets.rows():
        row_data = [cell.v for cell in row]
        latter_prophets_data.append(row_data)

    writings_data = []
    for row in writings.rows():
        row_data = [cell.v for cell in row]
        writings_data.append(row_data)

torah_df = pd.DataFrame(torah_data)
former_prophets_df = pd.DataFrame(former_prophets_data)
latter_prophets_df = pd.DataFrame(latter_prophets_data)
writings_df = pd.DataFrame(writings_data)

bhs_df = pd.concat([torah_df, former_prophets_df, latter_prophets_df, writings_df], ignore_index=True)

print(bhs_df)