import os
import urllib.request

data_dir = r'C:\Users\przemoai\Desktop\PythonKurs\S001\webpages'
pages = [
    { 'name': 'mobilo','url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent','url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy','url': 'http://www.kursyonline24.eu/'}
]

for page in pages:
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
        print("processing {} => {}...".format(page["url"],file_name))
        urllib.request.urlretrieve (page["url"], path)
    except:
        print("Failure during downloading data from {}.".format(page["url"]))

else:
    print("My job here is done!")