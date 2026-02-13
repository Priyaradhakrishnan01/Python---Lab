import pandas as pd
from functools import reduce
data={
    "Name":["Ravi","Anu","Meena","Kiran"],
    "Age":[30,22,45,19],
    "Income":[40000,28000,50000,30000],
    "CreditScore":[720,680,750,600],
    "LoanAmount":[300000,200000,400000,150000]
    }
df=pd.DataFrame(data)
eligible=df[
    (df["Age"]>=21)&
    (df["Name"]>=25000)&
    (df["CreditScore"]>=650)&
    (df["LoanAmount"]<=df["Income"]*10)
    ]
eligible["ProcessingFee"]=list(
    map(lambda x:x*0.02,eligible["LoanAmount"])
    )
eligible["LoanStatus"]=eligible.apply(
    lambda row:"Approved",axis=1
    )
total_loan=reduce(
    lambda x,y:x+y,eligible["LoanAmount"]
    )
print("Eligible Customers:\n")
print(eligible)
print("\n Total Approved Loan Amount:",total_loan)
