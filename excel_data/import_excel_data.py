import wx
import xlrd
import os.path

data_1 = {}
data_2 = {}


def extract_data(sh, data, output_file):
    i = 0
    tmp_acc_no, tmp_name, tmp_total = "", "", 0
    try:
        while str(sh.cell(i, 1)).replace("text:u", "").replace("'", "").replace(" ", "") != "":
            if str(sh.cell(i, 1)).replace("text:u", "").replace("'", "").replace(" ", "") == "CustomerName":
                name_col = str(sh.cell(i, 4)).replace("empty:", "").replace("'", "").replace("text:u", "").replace(",", "")
                if name_col.strip():
                    tmp_acc_no, tmp_name = name_col.split(":")
            if str(sh.cell(i, 1)).replace("text:u", "").replace("'", "").replace(" ", "") == "CustomerTotal":
                total_col = str(sh.cell(i, 8)).replace("empty:", "").replace("'", "").replace("text:u", "").replace(",", "")
                if total_col.strip():
                    tmp_total = total_col
                    data[tmp_acc_no.strip()] = [tmp_name.strip(), tmp_total.strip()]
                    output_file.write(tmp_acc_no.strip() + "," + tmp_name.strip() + "," + total_col + "\n")
            i = i + 1
    except:
        pass


def merge_data(data1, data2, combined_file):
    combined_data = {}
    for x in data1:
        if x in data2:
            combined_data[x] = [data1[x][0], data1[x][1], data2[x][0], data2[x][1]]
        elif x not in data2:
            #pass
            combined_data[x] = [data1[x][0], data1[x][1], '0', '0']

    for x in data2:
        if x not in data1:
            combined_data[x] = ['0', '0', data2[x][0], data2[x][1]]

    for i in combined_data:
        combined_file.write(i + "," + combined_data[i][0] + "," + combined_data[i][1] + "," + combined_data[i][2] + "," + combined_data[i][3] + "\n")
        pass


def print_name(event):
    input_file1 = filePickerCtrl_1.GetPath()
    if not input_file1:
        exit()

    #input_file1 = input_file1 + ".xls"
    wb = xlrd.open_workbook(os.path.join(input_file1))
    wb.sheet_names()
    sh = wb.sheet_by_index(0)
    output_file1 = open(input_file1[input_file1.rfind("/") + 1:-4] + ".txt", "w")
    extract_data(sh, data_1, output_file1)

    #input_file2 = raw_input("Enter Current Excel File Name: ")
    input_file2 = filePickerCtrl_2.GetPath()

    if not input_file2:
        exit()

    #input_file2 = input_file2 + ".xls"
    wb = xlrd.open_workbook(os.path.join(input_file2))
    wb.sheet_names()
    sh = wb.sheet_by_index(0)
    #output_file2 = open(input_file2[:-4] + ".txt", "w")
    output_file2 = open(input_file2[input_file2.rfind("/") + 1:-4] + ".txt", "w")
    extract_data(sh, data_2, output_file2)

    output_file3 = open("combined_data.txt", "w")
    merge_data(data_1, data_2, output_file3)

    wx.MessageBox('Import Completed', 'Info', wx.OK | wx.ICON_INFORMATION)

    #print(filePickerCtrl_1.GetPath())
    #print(filePickerCtrl_2.GetPath())

app = wx.App()

win = wx.Frame(None, title="Excel File Converter", size=(410, 335))
bkg = wx.Panel(win)

importButton = wx.Button(bkg, label="Import")
importButton.Bind(wx.EVT_BUTTON, print_name)
filePickerCtrl_1 = wx.FilePickerCtrl(bkg, message="select", wildcard="*.xls")
filePickerCtrl_2 = wx.FilePickerCtrl(bkg, message="Please select xl file", wildcard="*.xls")

hbox = wx.BoxSizer()
hbox.Add(filePickerCtrl_1, proportion=1, flag=wx.EXPAND, border=5)

hbox1 = wx.BoxSizer()
hbox1.Add(filePickerCtrl_2, proportion=1, flag=wx.EXPAND, border=5)

hbox2 = wx.BoxSizer()
hbox2.Add(importButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox1, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox2, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
