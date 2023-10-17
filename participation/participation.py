import matplotlib.pyplot as plt
import math
import sys

def main():
    the_sum = 0
    the_var_sum = 0
    vals = list()
    with open(sys.argv[1]) as h:
        for line in h:
            idx, val_s = line.split(',')
            try:
                val = int(val_s) / 100
                vals.append(100 *val)
                the_sum += val
                the_var_sum += val * (1 - val)
            except ValueError:
                print('Found first line')
                
    count = len(vals)
    print('Average reply:', the_sum / count)
    print('Replies:', count)
    print('Expected participants:', the_sum)
    print('Standard deviation:   ', math.sqrt(the_var_sum))

    plt.hist(vals, bins=[0,10,20,30,40,50,60,70,80,90,100])
    plt.xlabel('%')
    plt.title('Histogram')
    plt.savefig('participation.pdf')


if __name__ == '__main__':
    main()
    
