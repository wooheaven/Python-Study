from __future__ import print_function
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(
                 description="Enter any numbers to sum")
    parser.add_argument('X', type=float, nargs='+')
    args = parser.parse_args()
    X_list = args.X

    sum = 0.0
    for x in X_list:
        sum += x
    print("Total = %g" % sum)

