import numpy as np

def var(list):
    return np.var(list)



y=list(map(float, input("Enter the target values: ").split()))
print("Varience of the target values is: ",var(y))

a=input("Enter the number of features:")

variance_reductions = []

for i in range(int(a)):
    print("Feature",i+1)
    x=list(map(float, input("Enter the true values: ").split()))
    print("Varience of the feature values is: ",var(x))
    z=list(map(float,input("Enter the flase values: ").split()))
    print("Varience of the feature values is: ",var(z))
    t =float(input("Enter the true probability: "))
    var_reduction=t*(var(y)-var(x))+(1-t)*(var(y)-var(z))
    variance_reductions.append(var_reduction)
    print("varience reduction of feature",i+1 ,"is:",t*(var(y)-var(x))+(1-t)*(var(y)-var(z)))
    print(" ")


max_var_reduction = max(variance_reductions)
max_feature_index = variance_reductions.index(max_var_reduction) + 1 
print("The feature with the maximum variance reduction is feature", max_feature_index, "with variance reduction", max_var_reduction)