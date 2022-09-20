import numpy as np
import matplotlib.pyplot as plt

total_rank = []
year_of_birth = []
total_time = []
swimming_time = []
swimming_rank = []
cycling_time = []
cycling_rank = []
runnning_time = []
running_rank = []

f = np.loadtxt('ironman.txt')

for row in f:
    total_rank.append(float(row[0]))
    year_of_birth.append(2010-float(row[1]))
    total_time.append(float(row[2]))
    swimming_time.append(float(row[3]))
    swimming_rank.append(float(row[4]))
    cycling_time.append(float(row[5]))
    cycling_rank.append(float(row[6]))
    runnning_time.append(float(row[7]))
    running_rank.append(float(row[8]))

fig = plt.figure()
plt.plot(total_rank, total_time, '.')
plt.xlabel('total rank')
plt.ylabel('total time in minutes')
plt.savefig('total_rank_vs_total_time.pdf')
plt.show()
plt.plot(year_of_birth, total_time, '.')
plt.xlabel('age')
plt.ylabel('total time in minutes')
plt.savefig('age_vs_total_time.pdf')
plt.show()
plt.plot(runnning_time, swimming_time, '.')
plt.xlabel('running time in minutes')
plt.ylabel('swimming time in minutes')
plt.savefig('running_vs_swimming.pdf')
plt.show()
plt.plot(swimming_time, total_time, '.')
plt.xlabel('swimming time in minutes')
plt.ylabel('total time in minutes')
plt.savefig('swimming_vs_total.pdf')
plt.show()
plt.plot(cycling_time, total_time, '.')
plt.xlabel('cycling time in minutes')
plt.ylabel('total time in minutes')
plt.savefig('cycling_vs_total.pdf')
plt.show()
plt.plot(runnning_time, total_time, '.')
plt.xlabel('running time in minutes')
plt.ylabel('total time in minutes')
plt.plot('running_vs_total.pdf')
plt.show()

plt.hist(total_time)
plt.savefig('total_time_hist.pdf')
plt.show()
plt.hist(year_of_birth)
plt.savefig('age_hist.pdf')
plt.show()
