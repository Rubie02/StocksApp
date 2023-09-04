from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import Analysis as an

group_shares = { 
                'VN30': ['BVH', 'SSI', 'ACB', 'BID', 'NVL', 'PLX', 'PDR','POW','STB','MBB','MSN','TCB','TPB', 'MWG','CTG','VIC', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG', 'KDH',], 
                'HNX': ['AAV', 'ACM', 'ADC', 'ALT', 'AMC', 'AME', 'AMV', 'API', 'APP', 'APS',],
                'HNX30': ['BVS','MBS','SHS', 'HHG', 'PVI', 'S99', 'PVS', 'LAS', 'PVC', 'PLC', 'PGS', 'VC3', 'VTV', 'CEO', 'DDG', 'DTD', 'DXP', 'HUT', 'IDC', 'IDV', 'L14', ],
                'VNCONS': ['AAM', 'ABT', 'ACL', 'AGM', 'ANV', 'BBC', 'CLC', 'CMX', 'DBC', 'DGC',],
                'VNFIN': ['ACB', 'AGR', 'APG', 'BIC', 'BID', 'BMI', 'BSI', 'BVH', 'CTG', 'CTS',],
                }

lstTempListDataRow=[]
tempData=[]

def CostFollow(company_follwed):
    dataRowFollow=[]
    for company in company_follwed:
        tempData = an.inforCost(company)
        lstTempListDataRow.append(company)
        lstTempListDataRow.append(tempData[0]/1000) #[1]Close
        lstTempListDataRow.append(tempData[1]/1000) #[2]Change
        lstTempListDataRow.append(tempData[2])      #[3]%Change
        lstTempListDataRow.append(tempData[3]/1000) #[4]Vol
        color = colorChecking(lstTempListDataRow)
        lstTempListDataRow.append(color)            #[5]color
        temprow=lstTempListDataRow.copy()
        dataRowFollow.append(temprow)
        lstTempListDataRow.clear()
        tempData.clear()

    data_tables = MDDataTable(
        size_hint=(1, 1),
        rows_num = 30,
        column_data=[
            ("[size=12]Mã CP", dp(15)),
            ("[size=12]Giá khớp", dp(15)),
            ("[size=12]+/-", dp(10)),
            ("[size=12]+/-(%)", dp(10)),
            #("[size=12]Tổng KL", dp(15)),
        ],
        row_data=[
            (
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[0]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[1]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[2]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[3]}",
                    #f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[4]}",
                    
                )
                
                #for tempDataRow in dataOfRow[:len(company)]
                for tempDataRow in dataRowFollow[:99]
        ],
        
        
    )
    return data_tables

def Check(text):
    if text in group_shares.keys():
        return True
    return False

def Cost(text):
    dataOfRow=[]
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
        rows_num = 30,
        column_data=[
            ("[size=12]Mã CP", dp(15)),
            #("[size=12]Giá khớp", dp(15)),
            ("[size=12]+/-", dp(10)),
            ("[size=12]+/-(%)", dp(10)),
            ("[size=12]Tổng KL", dp(15)),
        ],
        row_data=[
            (
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[0]}",
                    #f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[1]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[2]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[3]}",
                    f"{'[size=12][color='+ tempDataRow[5] +']'}{tempDataRow[4]}",
                )
                # for tempDataRow in dataOfRow[:len(group_shares[text])]
                for tempDataRow in dataOfRow[:99]
        ],
    )
    return data_tables

def colorChecking(lst):
    if (lst[2] > 0) :
        return "#02a002" #green
    elif(lst[2] == 0) :
        return "#ffc800" #yelllow
    else:
        return "#ff0000" #red