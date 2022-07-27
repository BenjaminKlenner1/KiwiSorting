import csv

def Import():
    with open('data.csv', newline='') as in_file:
        reader = csv.reader(in_file)
        dataset = list(reader)
        dataset.pop(0)

    Start(dataset)


def Start(dataset):
    n = len(dataset)
    print(n)
    while True:
        print("How should the data be sorted\n1 - Weight\n2 - Height")
        selection = input("")

        if selection == "1":
            sortby = 2
            print("Weight selected")
            break
        elif selection == "2":
            sortby = 3
            print("Height selected")
            break
        else: 
            print("Incorrect entry")
    while True:
        print("Which sorting algorithm would you like to use?\n1 - Bubble\n2 - Selection")
        selection = input("")

        if selection == "1":
            Bubble(dataset,n,sortby)
            break
        elif selection == "2":
            Selection(dataset,n,sortby)
            break
        else: 
            print("Incorrect entry")


def Bubble(a,n):
    x = 0
    while x < n - 1:
        i = 0
        while i < n - 1:
            if ([i]>a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
            i = i + 1
        x = x + 1

    exportfile(a)

def Selection(a,n):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j   
        a[i], a[min_idx] = a[min_idx], a[i]

    exportfile(a)

def exportfile(dataset):
    fields = ["Species","Gender","Weight(kg)","Height(cm)","Location"]
    rows = dataset
    with open("output_file.csv", "w", newline="") as out_file:
        write = csv.writer(out_file)
        write.writerow(fields)
        write.writerows(rows)


Import()