from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import Analysis as an

group_shares = { 
                'VN30': ['BVH', 'SSI', 'ACB', 'BID', 'NVL', 'PLX', 'PDR','POW','STB','MBB','MSN','TCB','TPB', 'MWG','CTG','VIC', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG', 'KDH',], 
                'HNX': ['AAV', 'ACM', 'ADC', 'ALT', 'AMC', 'AME', 'AMV', 'API', 'APP', 'APS',],
                'HNX30': ['BVS','MBS','SHS', 'HHG', 'PVI', 'S99', 'PVS', 'LAS', 'PVC', 'PLC', 'PGS', 'VC3', 'VTV', 'CEO', 'DDG', 'DTD', 'DXP', 'HUT', 'IDC', 'IDV', 'L14', ],
                'VNCONS': ['AAM', 'ABT', 'ACL', 'AGM', 'ANV', 'BBC', 'CLC', 'CMX', 'DBC', 'DGC',],
                'VNFIN': ['ACB', 'AGR', 'APG', 'BIC', 'BID', 'BMI', 'BSI', 'BVH', 'CTG', 'CTS',],
                'Vn30': ['BVH', 'SSI', 'ACB', 'BID', 'NVL', 'PLX', 'PDR','POW','STB','MBB','MSN','TCB','TPB', 'MWG','CTG','VIC', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG', 'KDH',], 
                'Hnx': ['AAV', 'ACM', 'ADC', 'ALT', 'AMC', 'AME', 'AMV', 'API', 'APP', 'APS',],
                'Hnx30': ['BVS','MBS','SHS', 'HHG', 'PVI', 'S99', 'PVS', 'LAS', 'PVC', 'PLC', 'PGS', 'VC3', 'VTV', 'CEO', 'DDG', 'DTD', 'DXP', 'HUT', 'IDC', 'IDV', 'L14', ],
                'Vncons': ['AAM', 'ABT', 'ACL', 'AGM', 'ANV', 'BBC', 'CLC', 'CMX', 'DBC', 'DGC',],
                'Vnfin': ['ACB', 'AGR', 'APG', 'BIC', 'BID', 'BMI', 'BSI', 'BVH', 'CTG', 'CTS',],
                'Dầu khí': ['BSR', 'OIL', 'PEQ', 'PLX', 'POS', 'PVB', 'PVC', 'PVD', 'PVE',],
                'Hóa chất': ['AAA', 'APP', 'BFC', 'BRC', 'BRR', 'BT1', 'CPC', 'CSV', 'DAG', 'DCM',],
                'Tài nguyên cơ bản': ['ACM', 'AMC', 'BKC', 'BMC', 'C32', 'DHA', 'DHM', 'HGM', 'HLC',],
                'Xây dựng và vật liệu': ['ACC', 'BCC', 'BTS', 'CLH', 'CRC', 'CVT', 'DTL',],
                'Hàng và dịch vụ công nghiệp': ['VTC', 'VIE', 'TPH', 'STC', 'SMN', 'SGD', 'SED', 'PIA', 'ONE',],
                'Ô tô và phụ tùng': ['CAG', 'CDN', 'CLL', 'DL1', 'DS3', 'DVP',],
                'Thực phẩm và đồ uống': ['AGM', 'BBC', 'BHN','CAN', 'DAT', 'DBC', 'HAD', 'HHC',],
                'Hàng cá nhân và gia dụng': ['ADS', 'EVE', 'GDT', 'GIL', 'GMC', 'KMR', 'MHL', 'MSH', 'SAV', 'SHA',],
                'Y tế': ['DCL', 'DHG', 'DHT', 'DMC', 'DP3', 'FIT', 'IMP', 'LDP','DBD',],
                'Bán lẻ': ['AMD', 'AST', 'CCI', 'CIA', 'CTC', 'CTF', 'FRT', 'HAX', 'CMV', 'COM',],
                'Du lịch và giải trí': ['ATS', 'DAH', 'DSN', 'HOT', 'NVT', 'OCH', 'PDC', 'SDA', 'SGH',],
                'Viễn thông': ['IBC', 'INC', 'KPF', 'PPE', 'SDA', 'SDC', 'TV2', 'TV3',],
                'Điện, nước và xăng dầu khí đốt': ['CAV', 'DHP', 'DQC', 'EMC', 'GEX', 'KSD', 'MBG', 'PAC', 'PHN',],
                'Ngân hàng': ['NVB', 'ACB', 'BAB', 'BID', 'CTG', 'EIB', 'HDB','VIB', 'SHB',],
                'Bảo hiểm': ['BIC', 'BVH', 'BMI', 'BVH', 'MIG', 'PGI', 'PTI',],
                'Bất động sản': ['ANV','API','BAX','BCE','BCM','CCL','CDC','CEO','CIG',],
                'Dịch vụ tài chính': ['TCH' , 'AGR', 'APG', 'ART', 'BCG', 'ACB', 'FTS', 'CTS', 'BVH',],
                'Công nghệ thông tin': ['ADC', 'BDB', 'BST', 'FPT', 'DST', 'GLT', 'HEV', 'KST',],
                'dầu khí': ['BSR', 'OIL', 'PEQ', 'PLX', 'POS', 'PVB', 'PVC', 'PVD', 'PVE',],
                'hóa chất': ['AAA', 'APP', 'BFC', 'BRC', 'BRR', 'BT1', 'CPC', 'CSV', 'DAG', 'DCM',],
                'tài nguyên cơ bản': ['ACM', 'AMC', 'BKC', 'BMC', 'C32', 'DHA', 'DHM', 'HGM', 'HLC',],
                'xây dựng và vật liệu': ['ACC', 'BCC', 'BTS', 'CLH', 'CRC', 'CVT', 'DTL',],
                'hàng và dịch vụ công nghiệp': ['VTC', 'VIE', 'TPH', 'STC', 'SMN', 'SGD', 'SED', 'PIA', 'ONE',],
                'ô tô và phụ tùng': ['CAG', 'CDN', 'CLL', 'DL1', 'DS3', 'DVP',],
                'thực phẩm và đồ uống': ['AGM', 'BBC', 'BHN','CAN', 'DAT', 'DBC', 'HAD', 'HHC',],
                'hàng cá nhân và gia dụng': ['ADS', 'EVE', 'GDT', 'GIL', 'GMC', 'KMR', 'MHL', 'MSH', 'SAV', 'SHA',],
                'y tế': ['DCL', 'DHG', 'DHT', 'DMC', 'DP3', 'FIT', 'IMP', 'LDP','DBD',],
                'bán lẻ': ['AMD', 'AST', 'CCI', 'CIA', 'CTC', 'CTF', 'FRT', 'HAX', 'CMV', 'COM',],
                'du lịch và giải trí': ['ATS', 'DAH', 'DSN', 'HOT', 'NVT', 'OCH', 'PDC', 'SDA', 'SGH',],
                'viễn thông': ['IBC', 'INC', 'KPF', 'PPE', 'SDA', 'SDC', 'TV2', 'TV3',],
                'điện, nước và xăng dầu khí đốt': ['CAV', 'DHP', 'DQC', 'EMC', 'GEX', 'KSD', 'MBG', 'PAC', 'PHN',],
                'ngân hàng': ['NVB', 'ACB', 'BAB', 'BID', 'CTG', 'EIB', 'HDB','VIB', 'SHB',],
                'bảo hiểm': ['BIC', 'BVH', 'BMI', 'BVH', 'MIG', 'PGI', 'PTI',],
                'bất động sản': ['ANV','API','BAX','BCE','BCM','CCL','CDC','CEO','CIG',],
                'dịch vụ tài chính': ['TCH' , 'AGR', 'APG', 'ART', 'BCG', 'ACB', 'FTS', 'CTS', 'BVH',],
                'công nghệ thông tin': ['ADC', 'BDB', 'BST', 'FPT', 'DST', 'GLT', 'HEV', 'KST',],
                }

lstTempListDataRow=[]
tempData=[]
def check_group_stock(text):
    for k in group_shares.keys():
        if k == text:
            return True
    return False

def list_top_stocks(text):
    dataOfRow=[]
    count = 0
    for company in group_shares[text]:
        tempData = an.inforCost(company)
        lstTempListDataRow.append(company)
        lstTempListDataRow.append(tempData[0]/1000) #[1]Close
        lstTempListDataRow.append(tempData[1]/1000) #[2]Change
        lstTempListDataRow.append(tempData[2])      #[3]%Change
        lstTempListDataRow.append(tempData[3]/1000) #[4]Vol
        # lấy cổ phiếu xanh(tăng trưởng)
        if colorChecking(lstTempListDataRow) == "#02a002":
            color = colorChecking(lstTempListDataRow)
            lstTempListDataRow.append(color)            #[5]color
            temprow=lstTempListDataRow.copy()
            dataOfRow.append(temprow)
            count += 1
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
                #for tempDataRow in dataOfRow[:len(group_shares[text])]
                for tempDataRow in dataOfRow[:99]
        ],
    )
    return data_tables, count

def colorChecking(lst):
    if (lst[2] > 0) :
        return "#02a002" #green
    elif(lst[2] == 0) :
        return "#ffc800" #yelllow
    else:
        return "#ff0000" #red
