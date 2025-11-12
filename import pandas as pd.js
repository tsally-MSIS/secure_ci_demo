import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

plt.plot(data['x'], data['y'])
plt.show()