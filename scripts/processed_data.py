import json
import csv

class Data:
     
    def __init__(self, data):
          self.data = data
          self.name_columns = self.__get_columns()
          self.qtd_lines = self.__size_data()
    

    def __read_json(path):
        dados_json = []
        with open(path, 'r') as file_json:
            dados_json = json.load(file_json)

        return dados_json


    def __read_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    @classmethod
    def read_data(cls, path, type_data):
        data = []
        if type_data == 'csv':
            data =  cls.__read_csv(path)
        elif type_data == 'json':
            data = cls.__read_json(path)
        
        return cls(data)
    

    def __get_columns(self):
        return list(self.data[-1].keys())
    
    
    def rename_columns(self, key_mapping):
        new_data = []

        for old_dict in self.data:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)

        self.data = new_data
        self.name_columns = self.__get_columns()

    
    def __size_data(self):
        return len(self.data)
    

    def join_datas(dataA, dataB):
        combined_list = []

        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)



        return Data(combined_list)
    

    def __transform_data_tabel(self):
        data_combined_tabel = [self.name_columns]

        for row in self.data:
            line = []
            for columns in self.name_columns:
                line.append(row.get(columns, 'Indisponivel'))
            data_combined_tabel.append(line)

        return data_combined_tabel
    
        
    def saving_datas(self, path):

        data_combined_tabel = self.__transform_data_tabel()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data_combined_tabel)







