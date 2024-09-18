import logging
import os 
import sys
from data_transformation import DataTransformation
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from model_trainer import ModelTrainer
 
from dataclasses import dataclass


@dataclass
class DataIngestionConfig: 
    train_data_path: str =  os.path.join('artifact',"train.csv")
    test_data_path: str =  os.path.join('artifact',"test.csv")
    raw_data_path: str =  os.path.join('artifact',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df= pd.read_csv('data.csv')
            logging.info('read the dataset')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)
            df.to_csv(self.ingestion_config.raw_data_path,index= False, header=True)

            logging.info('Train test split initiated')
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index= False, header=True)


            test_set.to_csv(self.ingestion_config.test_data_path,index= False, header=True)

            logging.info("Ingestion of data is completed")
        
        except Exception as e:
            raise CustomException(e, sys) 
            
        

        return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path



if __name__ =="__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr ,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_array = train_arr,test_array = test_arr))

