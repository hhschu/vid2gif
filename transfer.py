import Algorithmia
import time
import threading

CLIENT = Algorithmia.client(API_KEY)


def putFile(img):
    print('put ' + img)
    CLIENT.file("data://chuan/hackathon/" + img).putFile("/Users/c-huan/Desktop/Dcard/hackathon/content/" + img)
    print('finish' + img)

def transfer(imglist, filterlist):
    input = {
        "images": ["data://chuan/hackathon/" + img for img in imglist],
        "savePaths": ["data://chuan/transfered/" + img for img in imglist],
        "filterName": 'blue_brush' 
    }
    algo = CLIENT.algo('deeplearning/DeepFilter/0.6.0')
    print(algo.pipe(input).result)

def main():
    imglist = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.png']
    filterlist = ['alien_goggles', 'smooth_ride', 'blue_granite']
    start_time = time.time()
    
    threads = []
    for idx, img in enumerate(imglist):
        threads.append(threading.Thread(target = putFile, args = (img,)))
        threads[idx].start()

    for t in threads:
        t.join()
    
    print(time.time() - start_time)          
    start_time = time.time()
    transfer(imglist, filterlist)
    print(time.time() - start_time)          

# jpg = CLIENT.file("data://chuan/transfered/3.jpg").getBytes()
# print(type(jpg))

if __name__ == '__main__':
    main()
