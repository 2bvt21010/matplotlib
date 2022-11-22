import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('visitsit.csv', sep='\t').head(100)
plt.ylim([-100, 1000])
plt.yticks(list(range(-100, 1100, 100)))
#plt.xlim()
plt.boxplot(data["time_spent"])
plt.show()
