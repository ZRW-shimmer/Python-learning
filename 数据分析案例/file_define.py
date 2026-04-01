"""
读取文件
"""
from data_define import Record
import json

class FileReader:

    def read_data(self) -> list[Record]:
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path=path



    def read_data(self) -> list[Record]:
        f=open(self.path,"r",encoding="utf-8")
        record_list=[]
        for line in f.readlines():
            line=line.strip()
            line_list=line.split(",")
            record=Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
            record_list.append(record)
        f.close()
        return record_list
class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path=path

    def read_data(self) -> list[Record]:
        f=open(self.path,"r",encoding="utf-8")
        record_list=[]
        for line in f.readlines():
            json_dict=json.loads(line)
            record=Record(json_dict["date"],
                          json_dict["order_id"],
                          int(json_dict["money"]),
                          json_dict["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == "__main__":
    textfileread=TextFileReader("D:/BaiduNetdiskDownload/2011年1月销售数据.txt")
    jsonfileread=JsonFileReader("D:/BaiduNetdiskDownload/2011年2月销售数据JSON.txt")
    for line in jsonfileread.read_data():
        print(line)