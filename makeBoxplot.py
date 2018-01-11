import matplotlib.pyplot as plt
import numpy as np


for j in range(1,11):
    data = []
    for i in range(0,5):
        f = open(str(j) + '/' + str(i) + '/result.txt', 'r')
        nums = []
        for line in f:
            nums.append(int(line.rstrip()))
        data.append(nums)
    plt.figure()
    fig = plt.figure()
    fig.suptitle('Levinshtein Distance vs Interpolacion de ingles', fontsize=14)
    ax = fig.add_subplot(111)
    ax.set_title("utternace: " + str(j))
    ax.boxplot(data,labels=["30%","40%","50%","60%","70%"])
    ax.set_xlabel('Interpolacion de ingles')
    ax.set_ylabel('Levinshtein Distance')
    ax.set_ylim([0,50])
    plt.savefig(str(j) + '.png')
