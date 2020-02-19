class histogram:
    
    def __init__(self, name,bins,positions,labels,rwidth):
        self.name=name
        self.bins=bins
        self.positions=positions
        self.labels=labels   
        self.rwidth=rwidth

    def plotHist(self,plt,result):
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = 22
        fig_size[1] = 9
        plt.rcParams["figure.figsize"] = fig_size
        result[[self.name]].plot(kind='hist',bins=self.bins,rwidth=self.rwidth)
        #changing the axis labels

        plt.xticks(self.positions, self.labels)
        plt.show()