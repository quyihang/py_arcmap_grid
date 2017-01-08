import csv


def grid_csv(xl,xr,dx,yb,yt,dy):
    with open('grid.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        k = 0
        for i in range(int(xl*1000), int(xr*1000), int(dx*1000)):
            for j in range(int(yb*1000), int(yt*1000), int(dy*1000)):
                k += 1
                x = float(i) / 1000
                y = float(j) / 1000
                spamwriter.writerow([k,x,y])


def main():
    grid_csv(120.850,122.000,0.002,30.680,31.870,0.002)


if __name__ == '__main__':
    main()