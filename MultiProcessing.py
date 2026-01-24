#MultiProcessing in python=It is a python module that provides a simple way to run multiple process in parallel.It allows you to take advantage of multiple processors on your system and can significantly improve the performance of your code.

import multiprocessing
import requests
def downloadFile(url,name):
    print(f"Started Downloading {name}")
    response=requests.get(url)
    open(f"data/file {name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")
if __name__ == "__main__":  # REQUIRED on Windows
    url="https://picsum.photos/200/300" #So I downloaded 5 images present from this url into my folder.
    pros=[]
    for i in range(5):
        p=multiprocessing.Process(target=downloadFile,args=[url,i]) #here we can use args as list but disciplined developers still use args as tuples.
        p.start()
        pros.append(p)