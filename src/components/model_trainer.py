import os
import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import save_object
from src.utils import evaluate_models

from src.exception import CustomException
from src.logger import logging

@dataclass
class Modeltrainerconfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class Modeltrainer:

    def __init__(self):
        self.model_trainer_config=Modeltrainerconfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Spliting trainig and test input data')
            xtrain,ytrain,xtest,ytest=(train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                'Random Forest': RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'K-Neighbour Classifier': KNeighborsRegressor(),
                'XGB Classifier': XGBRegressor(),
                'CatBossting Classifier': CatBoostRegressor(),
                'AdaBoost Classifier': AdaBoostRegressor()
            }

            model_report:dict=evaluate_models(xtrain=xtrain,
                    ytrain=ytrain,
                    xtest=xtest,
                    ytest=ytest,
                    models=models)

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException('No bset model found')
            
            logging.info('Best model found on both trainig and test dataset')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(xtest)

            r2_square=r2_score(ytest,predicted)
            return r2_square



        except Exception as e:
            raise CustomException(e,sys)