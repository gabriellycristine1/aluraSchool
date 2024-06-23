import json
import csv

class Data:
    """
    class responsible for extracting, transforming, and load the data.
    """
    def __init__(self, data):
          self.data = data
          self.name_columns = self.__get_columns()
          self.qtd_lines = self.__size_data()
    

    def __read_json(path):
        """
        JSON format file reader
        params:
        path: path where the file is stored
        """
        dados_json = []
        with open(path, 'r') as file_json:
            dados_json = json.load(file_json)

        return dados_json


    def __read_csv(path):
        """
        CSV format file reader
        params:
        path: path where the file is stored
        """
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    @classmethod
    def read_data(cls, path, type_data):
        """
        Method that allows reading two files with different extensions
        params:
        path: path where the file is stored
        type_data: type of date that is going to be worked on
        """
        data = []
        if type_data == 'csv':
            data =  cls.__read_csv(path)
        elif type_data == 'json':
            data = cls.__read_json(path)
        
        return cls(data)
    

    def __get_columns(self):
        """
        Return to Data Column
        """
        return list(self.data[-1].keys())
    
    
    def rename_columns(self, key_mapping):
        """
        Renames data columns to standardize
        params:
        key_mapping: Align with the team to decide the column names and create a dictionary, where the key is the current name and the value is the name that will be changed
        """
        new_data = []

        for old_dict in self.data:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)

        self.data = new_data
        self.name_columns = self.__get_columns()

    
    def __size_data(self):
        """
        Returns the number of rows in the data
        """
        return len(self.data)
    

    def join_datas(dataA, dataB):
        """
        After processing the data, returns a list of the data from both files combined.
        paramns:
        dataA: file that is going to be combined
        dataB: file that is going to be combined
        """
        combined_list = []

        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)



        return Data(combined_list)
    

    def __transform_data_tabel(self):
        """
        Transforms data into table format and replaces null data with 'Indisponivel'
        """
        data_combined_tabel = [self.name_columns]

        for row in self.data:
            line = []
            for columns in self.name_columns:
                line.append(row.get(columns, 'Indisponivel'))
            data_combined_tabel.append(line)

        return data_combined_tabel
    
        
    def saving_datas(self, path):
        """
        Saves the extracted and already processed data
        paramns:
        path: path where the data will be saved
        """

        data_combined_tabel = self.__transform_data_tabel()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data_combined_tabel)







