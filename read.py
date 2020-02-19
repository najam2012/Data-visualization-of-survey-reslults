def createDf(filename,csv,pd):
    size = sum(1 for line in open(filename,encoding="utf8"))-1
    with open(filename,newline='',errors='replace') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader )
        data = []
        for i in range(size):
            info = next(reader)
            data += [info]
        df = pd.DataFrame(data)
        df.columns = header
    return df
