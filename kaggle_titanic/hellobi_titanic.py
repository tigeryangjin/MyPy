# import matplotlib.pyplot as plt
# %matplotlib qt
# import numpy as np
import pandas


def load_data():
    titanic = pandas.read_csv("../data/train.csv")
    return titanic
