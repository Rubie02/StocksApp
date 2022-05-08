from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import Analysis as an

group_shares = {'VNINDEX': ['AAA', 'AAM', 'ADS', 'ABR', 'ABS', 'ABT', 'ACB', 'ACC', 'ACL', 'ADG',], 
                'VN30': ['ACB', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG', 'KDH',], 
                'HNX': ['AAV', 'ACM', 'ADC', 'ALT', 'AMC', 'AME', 'AMV', 'API', 'APP', 'APS',],
                'HNX30': ['BVS', 'CEO', 'DDG', 'DTD', 'DXP', 'HUT', 'IDC', 'IDV', 'L14', 'LAS',],
                'UPCOM': ['A32', 'AAS', 'ABB', 'ABC', 'ABI', 'ACE', 'ACG', 'ACS', 'ACV', 'ADP',],
                'VN100': ['AAA', 'ACB', 'AGG', 'ANV', 'APH', 'ASM', 'BID', 'BMI', 'BMP', 'BVH',],
                'VNCOND': ['AGR', 'ADS', 'AST', 'BKG', 'CSM', 'CTF', 'DAH', 'DRC', 'DSN', 'EVE',],
                'VNCONS': ['AAM', 'ABT', 'ACL', 'AGM', 'ANV', 'BBC', 'CLC', 'CMX', 'DBC', 'DGC',],
                'VNENE': ['ASP', 'CNG', 'GSP', 'PGC', 'PJT', 'PLX', 'PSH', 'PVD', 'PVT', 'TDG',],
                'VNFIN': ['ACB', 'AGR', 'APG', 'BIC', 'BID', 'BMI', 'BSI', 'BVH', 'CTG', 'CTS',],
                'VNHEAL': ['DBD', 'DBT', 'DCL', 'DMC', 'IMP', 'OPC', 'SPM', 'TNH', 'VMD', 'VTO',],
                }

lstTempListDataRow=[]
dataOfRow=[]
tempData=[]

def CostFollow(company):
    tempData = an.inforCost(company)
    lstTempListDataRow.append(company)
    lstTempListDataRow.append(tempData[0]/1000) #[1]Close
    lstTempListDataRow.append(tempData[1]/1000) #[2]Change
    lstTempListDataRow.append(tempData[2])      #[3]%Change
    lstTempListDataRow.append(tempData[3]/1000) #[4]Vol
    color = colorChecking(lstTempListDataRow)
    lstTempListDataRow.append(color)            #[5]color
    temprow=lstTempListDataRow.copy()
    dataOfRow.append(temprow)
    lstTempListDataRow.clear()
    tempData.clear()

    data_tables = MDDataTable(
        size_hint=(1, 1),
        rows_num = 10,
        column_data=[
            ("[size=12]Mã CP", dp(15)),
            ("[size=12]Giá khớp", dp(15)),
            ("[size=12]+/-", dp(10)),
            ("[size=12]+/-(%)", dp(10)),
            ("[size=12]Tổng KL", dp(15)),
        ],
        row_data=[
            (
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[0]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[1]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[2]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[3]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[4]}",
                    
                )
                
                #for tempDataRow in dataOfRow[:len(company)]
                for tempDataRow in dataOfRow[:99]
        ],
        
        
    )
    # data_tables.bind(on_row_press=on_row_press)
    return data_tables

def Check(text):
    if text in group_shares.keys():
        return True
    return False

def Cost(text):
    for company in group_shares[text]:
        tempData = an.inforCost(company)
        lstTempListDataRow.append(company)
        lstTempListDataRow.append(tempData[0]/1000) #[1]Close
        lstTempListDataRow.append(tempData[1]/1000) #[2]Change
        lstTempListDataRow.append(tempData[2])      #[3]%Change
        lstTempListDataRow.append(tempData[3]/1000) #[4]Vol
        color = colorChecking(lstTempListDataRow)
        lstTempListDataRow.append(color)            #[5]color
        temprow=lstTempListDataRow.copy()
        dataOfRow.append(temprow)
        lstTempListDataRow.clear()
        tempData.clear()

    data_tables = MDDataTable(
        size_hint=(1, 1),
        rows_num = 10,
        column_data=[
            ("[size=12]Mã CP", dp(15)),
            ("[size=12]Giá khớp", dp(15)),
            ("[size=12]+/-", dp(10)),
            ("[size=12]+/-(%)", dp(10)),
            ("[size=12]Tổng KL", dp(15)),
        ],
        row_data=[
            (
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[0]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[1]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[2]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[3]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[4]}",
                )
                for tempDataRow in dataOfRow[:len(group_shares[text])]
        ],
    )
    # data_tables.bind(on_row_press=on_row_press)
    return data_tables

# def on_row_press(table, row):
#         start_index, end_index = row.table.recycle_data[row.index]["range"]
#         print(row.table.recycle_data[start_index]["text"][-3:])

def colorChecking(lst):
        if (lst[2] > 0) :
            return "#02a002" #luc
        if (lst[2] == 0) :
            return "#ffc800" #vang
        # if (lst[0] > 0) :
        #      return "#006eff" #lam
        # if (lst[0] > 0) :
        #     return "b400ff" #tim
        if (lst[2] < 0) :
            return "#ff0000" #do