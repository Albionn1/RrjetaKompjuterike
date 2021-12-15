from typing_extensions import Self
from pandas.core.frame import DataFrame
import speedtest as st
import pandas as pd
from datetime import datetime
import readchar

def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()
    print("Measuring speed...(approx. 25sec)")
    ping = speed_test.results.ping

    download = speed_test.download()
    upload = speed_test.upload()

    download_mbs = round(download / (10**6), 2)
    upload_mbs = round(upload / (10**6), 2)

    print("Ping: {}\nDownload: {}\nUpload: {}".format(ping, download_mbs, upload_mbs))
    return(ping, download_mbs, upload_mbs)

def update_csv(internet_speeds):
    date_today = datetime.today().strftime("%m/%d/%y")
    csv_file_name = "internet_speeds_dataset.csv"

    try:
        csv_dataset = pd.read_csv(csv_file_name, index_col="Date")
    except:
        csv_dataset = pd.DataFrame(
            list(),
            columns=["Ping (ms)", "Download (Mb/s)", "Upload (Mb/s)"]
        )
    
    results_df = pd.DataFrame(
        [[internet_speeds[0], internet_speeds[1], internet_speeds[2] ]],
        columns=["Ping (ms)", "Download (Mb/s)", "Upload (Mb/s)"],
        index=[date_today]
    )

    updated_df = csv_dataset.append(results_df, sort=False)
    updated_df\
        .loc[~updated_df.index.duplicated(keep="last")]\
            .to_csv(csv_file_name, index_label="Date")
    """ set_column_width() """

""" def set_column_width(self):
    workbook = self.Workbook(self.dataDir +'Book1.csv')

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

# Setting the width of the second column to 17.5

    cells.setColumnWidth(0, 17.5)

# Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(self.dataDir + "Set Column Width.xls")

    print("Set Column Width Successfully.") """

new_speeds = get_new_speeds()
update_csv(new_speeds)
print("Press any key to Exit")
k = readchar.readchar()