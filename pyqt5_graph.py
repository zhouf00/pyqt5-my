import pyqtgraph as pg
from TmpData import _read_data, wind_mach_chooice

colour = ["r", "g", "b"]
yp_list = ["叶片1", "叶片2", "叶片3"]

def _data_to_dict():
    mydict = {}
    for my_vars, i in zip(_read_data(), range(len(_read_data()))):
        tmp_dict = {}
        for var, j in zip(my_vars, range(len(my_vars))):
            tmp_dict[var[0]] =var[1]
        mydict[i] = tmp_dict
    return mydict

def plt_init():
    pg.setConfigOption("background", "w")
    plt = pg.PlotWidget()
    plt.addLegend(size=(150, 80))
    plt.showGrid(x=True, y=True, alpha=0.5)
    return plt

def plt_show(num):
    mydict = _data_to_dict()
    pg.setConfigOption("background", "w")
    plt = pg.PlotWidget()
    plt.addLegend(size=(150, 80))
    plt.showGrid(x=True, y=True, alpha=0.5)
    for i in num.split(","):
        i = int(i)-1
        print("类型%s，值%d"%(type(i), i))
        plt.plot(x=list(mydict[i].keys()), y=list(mydict[i].values()), pen=colour[i],
                 name=yp_list[i])
        print(i)
    return plt

def testplot():
    mydict = _data_to_dict()
    pg.setConfigOption("background", "w")
    plt = pg.PlotWidget()
    plt.addLegend(size=(150, 80))
    plt.showGrid(x=True, y=True, alpha=0.5)
    # 决定显示哪条线

    #for i in num:
    #    plt.plot(x=list(mydict[i].keys()), y=list(mydict[i].values()), pen=colour[i],
      #           name=yp_list[i])
    """
    plt.plot(x=list(mydict[0].keys()), y=list(mydict[0].values()), pen="r",
             name="叶片1")
    plt.plot(x=list(mydict[1].keys()), y=list(mydict[1].values()), pen="g",
             name="叶片2")
    plt.plot(x=list(mydict[2]), y=list(mydict[2].values()), pen="b",
             name="叶片3")
    #plt.setLabel(axis="left", text="test")
    """
    return plt

if __name__ == '__main__':
    _data_to_dict()
    pass