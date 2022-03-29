# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei und konvertieren zu numpy-Array
file_name =  'input_data/power_data_1.txt'
power_data_watts = open(file_name).read().split("\n")
x = np.array(power_data_watts)

# %% Erstellen des Plots
plt.title("Line graph")
plt.plot(x, color="red")

plt.show()


# %%

# %%

##Mein Code

# Import Module
import os
from posixpath import split
  
# Folder Path
path = r"C:\Users\marku\OneDrive - mci4me.at\Dokumente\Bachelor of Science in Engineering\SS2022\Programmierübungen\MCI-MSE_Aufgaben\PÜ2\input_data"
  
# Change the directory
os.chdir(path)
  
# Read text File    
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        
        print(f.read(),"\n")
  
  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        print(file, ":")
  
        # call read text file function
        read_text_file(file_path) 


