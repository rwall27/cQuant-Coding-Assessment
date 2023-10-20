import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
def Question1():
    PriceData_A =pd.read_csv("data/PriceData_A.csv")
    PriceData_B =pd.read_csv("data/PriceData_B.csv")
    return PriceData_A, PriceData_B

def Question2(DataA, DataB):
    DataA = DataA.melt(id_vars = ["Name", "Date"], value_vars= ["Run_1", "Run_2", "Run_3", "Run_4", "Run_5"], var_name= "Run", value_name = "Value")
    DataB = DataB.melt(id_vars = ["Name", "Date"], value_vars= ["Run_1", "Run_2", "Run_3", "Run_4", "Run_5"], var_name= "Run", value_name = "Value")
    return DataA, DataB

def Question3(DataA, DataB):
    CombinedData = DataA.merge(DataB, how = "outer", on = ["Name", "Date", "Run"])
    print(CombinedData.head())
    return CombinedData

def Question4(CombinedData):
    CombinedData["Difference"] = CombinedData["Value_x"] - CombinedData["Value_y"]
    CombinedData["PercentDifference"] = (CombinedData["Difference"])/(CombinedData["Value_x"]) 
    CombinedData["AbsoluteDifference"] = CombinedData["Difference"] .abs()
    CombinedData["AbsolutePercentDifference"]= CombinedData["PercentDifference"].abs()
    print(CombinedData.head())
    return CombinedData

def Question5(CombinedData):
    CombinedDataDates = CombinedData.copy()[["Date", "AbsoluteDifference"]]
    CombinedDataDates["Date"] = (pd.to_datetime(CombinedDataDates["Date"]))
    CombinedDataDates['Date'] = CombinedDataDates['Date'].dt.year
    CombinedDataByYear = CombinedDataDates.groupby("Date")["AbsoluteDifference"].agg(["min", "max", "mean"])
    CombinedDataByYear = CombinedDataByYear.rename_axis("Year")

    CombinedDataDates = CombinedData.copy()[["Date", "AbsoluteDifference"]]
    CombinedDataDates["Date"] = (pd.to_datetime(CombinedDataDates["Date"]))
    CombinedDataDates['Date'] = CombinedDataDates['Date'].dt.month
    CombinedDataByMonth = CombinedDataDates.groupby("Date")["AbsoluteDifference"].agg(["min", "max", "mean"])
    CombinedDataByMonth = CombinedDataByMonth.rename_axis("Month")


    CombinedDataDates = CombinedData.copy()[["Date", "AbsoluteDifference"]]
    CombinedDataDates["Date"] = (pd.to_datetime(CombinedDataDates["Date"]))
    CombinedDataDates['Date'] = CombinedDataDates['Date'].dt.dayofweek
    CombinedDataByDayOfWeek = CombinedDataDates.groupby("Date")["AbsoluteDifference"].agg(["min", "max", "mean"])
    CombinedDataByDayOfWeek = CombinedDataByDayOfWeek.rename_axis("DayOfWeek")


    CombinedDataDates = CombinedData.copy()[["Date", "AbsoluteDifference"]]
    CombinedDataDates["Date"] = (pd.to_datetime(CombinedDataDates["Date"]))
    CombinedDataDates['Date'] = CombinedDataDates['Date'].dt.hour
    CombinedDataByHour = CombinedDataDates.groupby("Date")["AbsoluteDifference"].agg(["min", "max", "mean"])
    CombinedDataByHour = CombinedDataByHour.rename_axis("Hour")




    return CombinedDataByYear, CombinedDataByMonth, CombinedDataByDayOfWeek, CombinedDataByHour, 

def Question6(CombinedDataByYear, CombinedDataByMonth, CombinedDataByDayOfWeek, CombinedDataByHour):
    CombinedDataByYear.to_csv("summary_tables_and_images/CombinedDataByYear.csv")
    CombinedDataByMonth.to_csv("summary_tables_and_images/CombinedDataByMonth.csv")
    CombinedDataByDayOfWeek.to_csv("summary_tables_and_images/CombinedDataByDayOfWeek.csv")
    CombinedDataByHour.to_csv("summary_tables_and_images/CombinedDataByHour.csv")

def Question7(CombinedData, CombinedDataByHour):
    CombinedDataDates = CombinedData.copy()[["Date", "AbsoluteDifference"]]
    CombinedDataDates["Date"] = (pd.to_datetime(CombinedDataDates["Date"]))
    CombinedDataDates['Date'] = CombinedDataDates['Date'].dt.month
    sns.boxplot(x = "Date", y ="AbsoluteDifference", data = CombinedDataDates, showfliers = False)
    plt.xlabel('Month')
    plt.title('Distribution of Absolute Difference in Power Prices by Month')
    plt.show()
    plt.savefig("summary_tables_and_images/Boxplot.png")
    sns.lineplot(x = "Hour", y = "mean", data = CombinedDataByHour)
    plt.xlabel('Hour')
    plt.title('Mean of Absolute Difference in Power Prices by Hour')
    plt.show()
    plt.savefig("summary_tables_and_images/Lineplot.png")

    
if __name__ == "__main__":
    PriceData_A, PriceData_B = Question1()
    PriceData_A, PriceData_B = Question2(PriceData_A, PriceData_B)
    CombinedData  = Question3(PriceData_A, PriceData_B)
    CombinedData = Question4(CombinedData)
    CombinedDataByYear, CombinedDataByMonth, CombinedDataByDayOfWeek, CombinedDataByHour = Question5(CombinedData)
    Question6(CombinedDataByYear, CombinedDataByMonth, CombinedDataByDayOfWeek, CombinedDataByHour)
    Question7(CombinedData, CombinedDataByHour)