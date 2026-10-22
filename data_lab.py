import pandas as pd
data = {
    "Agent":["cipher","ghost","viper","echo","titan"],
    "role":["infiltrator","exploit dev","infiltrator","cryptanalyst","exploit dev"],
    "bounty_k":[120,85,210,95,300],
    "clearence_level":[4,5,3,5,4]
}
df=pd.DataFrame(data)
exploit_devs=df[(df["role"]== "exploit dev")&(df["bounty_k"]>100)]
print("==MASTER EXPLOIT DEVS==")
print(exploit_devs)
operatives=df[(df["clearence_level"]==5)|(df["bounty_k"]>=200)]
print("==THE MAIN OPERATIVES==")
print(operatives)
average_salary=df[df["clearence_level"]==5]["bounty_k"].mean()
print("THE AVERAGE SALARY OF THE EMPLOYES IS:",average_salary)