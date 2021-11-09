import os 
tree = []
intro = 'How it works: Copy and Paste this program into the directory you want to search recursively, and enter search and replace texts\n'
thisdir = os.getcwd()
if thisdir.find('/') > -1:
    thisdir = thisdir + '/'
elif thisdir.find('\\') > -1:
    thisdir = thisdir + '\\'

def main():
    global thisdir 
    a = input('find\n').rstrip()
    b = input('replace\n').rstrip()

    yetToCrawl = []
    listfound = []
    lisy = os.listdir(thisdir)
    for x in lisy:
        if os.path.isdir(thisdir + x):
            if thisdir + x not in listfound and thisdir + x not in yetToCrawl:
                listfound.append(thisdir + x)
                yetToCrawl.append(thisdir + x)
        if os.path.isfile(thisdir + x):
            listfound.append(thisdir + x)
    
    while len(yetToCrawl) > 0:
        lastdir = yetToCrawl.pop(0)
        lisy = os.listdir(lastdir)
        for x in lisy:
            if os.path.isdir(lastdir + '\\' + x):
                if lastdir + '\\' + x not in listfound and lastdir + '\\' + x not in yetToCrawl:
                    listfound.append(lastdir + '\\' + x)
                    yetToCrawl.append(lastdir + '\\' + x)
            if os.path.isfile(lastdir + '\\' + x):
                listfound.append(lastdir + '\\' + x)
    print('List found:')
    print(listfound)

    print('replacing string: ' + a + '\n with string: ' + b + '\n')
    
    for x in listfound:
        if os.path.isfile(x):
            print('Editing file: ' + x)
            fileio = open(x)
            filedat = fileio.read()
            fileio.close()
            filedat = filedat.replace(a, b)
            fileio = open(x, 'w')
            fileio.write(filedat)
            fileio.close()

if __name__ == "__main__":
    print(intro)
    main()