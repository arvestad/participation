import matplotlib.pyplot as plt
import sys

the_sum = 0
vals = list()
with open(sys.argv[1]) as h:
    for line in h:
        idx, val_s = line.split(',')
        try:
            val = int(val_s)
            vals.append(val)
            the_sum += val
        except ValueError:
            print('Found first line')

count = len(vals)
print('Average reply:', the_sum / (100 * count))
print('Replies:', count)
print('Expected participants:', the_sum / 100)

plt.hist(vals, bins=[0,10,20,30,40,50,60,70,80,90,100])
plt.show()
