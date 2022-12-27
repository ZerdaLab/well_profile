import pandas as pd
import numpy as np
import well_profile as wp
well = wp.load('trajectory.xlsx',set_info={'dlsResolution': 30, 'wellType': 'offshore', 'units': 'metric'},
              set_start={'north': 0, 'east': 0, 'depth': 0})  # (optional) set the location of initial point

# well.plot(names=['well Zerdalab']).show()

nums = np.linspace(1000, 1100, num=100).round(decimals=0)



well = wp.load('trajectory.xlsx', inner_points=1)   # loading file with only original survey points
well.plot(style={'darkMode': True,'color': 'dls'}).show()


def func(list_):
    ls = []
    for i in (list_):
        dict = well.get_point(i)
        ls.append(dict)
    # print(ls)


    df = pd.DataFrame(ls)
    print(df)

# func(nums)