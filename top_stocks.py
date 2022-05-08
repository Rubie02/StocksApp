from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import Analysis as an

# group_shares_branch = {'Dầu khí': ['BSR', 'OIL', 'PEQ', 'PLX', 'POS', 'PVB', 'PVC', 'PVD', 'PVE',],
#                 'Hóa chất': ['AAA', 'APP', 'BFC', 'BRC', 'BRR', 'BT1', 'CPC', 'CSV', 'DAG', 'DCM',],
#                 'Tài nguyên cơ bản': ['ACG', 'ACM', 'ALV', 'AMC', 'ATG', 'BCA', 'BCB', 'BKC', 'BMC', 'BMJ',],
#                 'Xây dựng và vật liệu': ['ACC', 'ACE', 'ACS', 'ADP', 'AMS', 'ATB', 'B82', 'BAX', 'BCC', 'BCE',],
#                 'Hàng và dịch vụ công nghiệp': ['ABR', 'ACV', 'AME', 'APH', 'APL', 'ARM', 'ASG', 'BAL', 'BBH', 'BBS',],
#                 'Ô tô và phụ tùng': ['CMC', 'CSM', 'CTF', 'DRC', 'GGG', 'HAX', 'HHS', 'HTL', 'SRC',],
#                 'Thực phẩm và đồ uống': ['AAM', 'ABT', 'ACL', 'AGF', 'AGM', 'ANT', 'ANV', 'APF', 'APT', 'ASM',],
#                 'Hàng cá nhân và gia dụng': ['A32', 'AAT', 'ADS', 'AG1', 'ASA', 'BBT', 'BDG', 'BEL', 'BKG', 'BMG',],
#                 'Y tế': ['AGB', 'AMP', 'AMV', 'APC', 'BCP', 'BIO', 'CDP', 'CNC', 'DAN', 'DBD',],
#                 'Bán lẻ': ['ABS', 'AFX', 'AGX', 'AST', 'BSC', 'BTT', 'CEN', 'CGL', 'CMV', 'COM',],
#                 'Truyền thông': ['ADC', 'ADG', 'ALT', 'BDB', 'BED', 'BST', 'CAB', 'DAD', 'DAE', 'DST',],
#                 'Du lịch và giải trí': ['ATS', 'BCV', 'BLN', 'BSG', 'BTV', 'CTC', 'DAH', 'DAR', 'DBH', 'DLD',],
#                 'Viễn thông': ['ABC', 'FOX', 'MFS', 'PAI', 'PIA', 'PTP', 'TTN', 'VGI',],
#                 'Điện, nước và xăng dầu khí đốt': ['ASP', 'AVC', 'BDW', 'BGW', 'BHA', 'BLW', 'BMF', 'BNW', 'BSA', 'BTP',],
#                 'Ngân hàng': ['ABB', 'ACB', 'BAB', 'BID', 'BVB', 'CTG', 'EIB', 'HDB','KLB', 'LPB',],
#                 'Bảo hiểm': ['ABI', 'AIC', 'BIC', 'BLI', 'BMI', 'BVH', 'MIG', 'PGI', 'PRE', 'PTI',],
#                 'Bất động sản': ['AAV', 'AGG', 'AMD', 'API', 'BCM', 'BIG', 'BII', 'BVL', 'C21', 'CCI',],
#                 'Dịch vụ tài chính': ['AAS', 'AGR', 'APG', 'APS', 'ART', 'BCG', 'BMS', 'BSI', 'BVS', 'CSI',],
#                 'Công nghệ thông tin': ['CKV', 'CMG', 'CMT', 'ELC', 'FPT', 'HIG', 'HPT', 'ICT', 'ITD', 'KST',],
#                 }

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
                'Dầu khí': ['BSR', 'OIL', 'PEQ', 'PLX', 'POS', 'PVB', 'PVC', 'PVD', 'PVE',],
                'Hóa chất': ['AAA', 'APP', 'BFC', 'BRC', 'BRR', 'BT1', 'CPC', 'CSV', 'DAG', 'DCM',],
                'Tài nguyên cơ bản': ['ACG', 'ACM', 'ALV', 'AMC', 'ATG', 'BCA', 'BCB', 'BKC', 'BMC', 'BMJ',],
                'Xây dựng và vật liệu': ['ACC', 'ACE', 'ACS', 'ADP', 'AMS', 'ATB', 'B82', 'BAX', 'BCC', 'BCE',],
                'Hàng và dịch vụ công nghiệp': ['ABR', 'ACV', 'AME', 'APH', 'APL', 'ARM', 'ASG', 'BAL', 'BBH', 'BBS',],
                'Ô tô và phụ tùng': ['CMC', 'CSM', 'CTF', 'DRC', 'GGG', 'HAX', 'HHS', 'HTL', 'SRC',],
                'Thực phẩm và đồ uống': ['AAM', 'ABT', 'ACL', 'AGF', 'AGM', 'ANT', 'ANV', 'APF', 'APT', 'ASM',],
                'Hàng cá nhân và gia dụng': ['A32', 'AAT', 'ADS', 'AG1', 'ASA', 'BBT', 'BDG', 'BEL', 'BKG', 'BMG',],
                'Y tế': ['AGB', 'AMP', 'AMV', 'APC', 'BCP', 'BIO', 'CDP', 'CNC', 'DAN', 'DBD',],
                'Bán lẻ': ['ABS', 'AFX', 'AGX', 'AST', 'BSC', 'BTT', 'CEN', 'CGL', 'CMV', 'COM',],
                'Truyền thông': ['ADC', 'ADG', 'ALT', 'BDB', 'BED', 'BST', 'CAB', 'DAD', 'DAE', 'DST',],
                'Du lịch và giải trí': ['ATS', 'BCV', 'BLN', 'BSG', 'BTV', 'CTC', 'DAH', 'DAR', 'DBH', 'DLD',],
                'Viễn thông': ['ABC', 'FOX', 'MFS', 'PAI', 'PIA', 'PTP', 'TTN', 'VGI',],
                'Điện, nước và xăng dầu khí đốt': ['ASP', 'AVC', 'BDW', 'BGW', 'BHA', 'BLW', 'BMF', 'BNW', 'BSA', 'BTP',],
                'Ngân hàng': ['ABB', 'ACB', 'BAB', 'BID', 'BVB', 'CTG', 'EIB', 'HDB','KLB', 'LPB',],
                'Bảo hiểm': ['ABI', 'AIC', 'BIC', 'BLI', 'BMI', 'BVH', 'MIG', 'PGI', 'PRE', 'PTI',],
                'Bất động sản': ['AAV', 'AGG', 'AMD', 'API', 'BCM', 'BIG', 'BII', 'BVL', 'C21', 'CCI',],
                'Dịch vụ tài chính': ['AAS', 'AGR', 'APG', 'APS', 'ART', 'BCG', 'BMS', 'BSI', 'BVS', 'CSI',],
                'Công nghệ thông tin': ['CKV', 'CMG', 'CMT', 'ELC', 'FPT', 'HIG', 'HPT', 'ICT', 'ITD', 'KST',],
                }

lstTempListDataRow=[]
dataOfRow=[]
tempData=[]
def check_group_stock(text):
    for k in group_shares.keys():
        if k == text:
            return True
    return False

def list_top_stocks(text):
    for company in group_shares[text]:
        tempData = an.inforCost(company)
        lstTempListDataRow.append(company)
        lstTempListDataRow.append(tempData[0]/1000) #[1]Close
        lstTempListDataRow.append(tempData[1]/1000) #[2]Change
        lstTempListDataRow.append(tempData[2])      #[3]%Change
        lstTempListDataRow.append(tempData[3]/1000) #[4]Vol
        if top_checking(lstTempListDataRow):
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

def top_checking(lst):
        if (lst[2] > 0) :
            return True
        else:
            return False

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