import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class Dataingestionconfig():
    train_data_path=os.path.join("artifacts",'train.csv')
    test_data_path=os.path.join("artifacts",'test.csv')
    raw_data_path=os.path.join("artifacts",'data.csv')
 
class Dataingestion():
    def __init__(self):
        self.data_ingestion=Dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or Components")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as DataFrame")

            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion.raw_data_path,index=False,header=True)

            logging.info("Train Test Split Initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.data_ingestion.train_data_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=Dataingestion()
    obj.initiate_data_ingestion()