import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


def plot_items(world_type, dataset):
    filtered_df = df[df['World Type:'] == world_type]
    x = filtered_df['x']
    y = filtered_df['z'] #yes this is suppose to be y as mojang use z for y and y for z
    z = filtered_df['y'] * 0.5
    
    plt.scatter(x,y,z)

    plt.xlabel('X Cords')
    plt.ylabel('Z cords')
    plt.title(world_type)
    plt.show()

if __name__=="__main__":
    # Grab edge list data hosted on Gist
    #csv_headers = ['ID', 'World Type', 'Type', 'X', 'Y', 'Z']
    df = pd.read_csv('test_data.csv', header=0)
    print('Data headers: {df_headers}'.format(df_headers=df.head(0)))
    plot_items('Overworld', df)
    plot_items('Nether', df)



