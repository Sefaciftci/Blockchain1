from ast import Str
from hashlib import sha256
from re import S
import time 

class block:
    def __init__(self,timeStamp,data,previousHash=''):
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.kuvvet = 0
        self.hash = self.hesapla()

    def hesapla(self):
        while True:
            self.kuvvet = self.kuvvet+1

            ozet =sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:2] =="00":
                break
            return ozet

class blokChain:
    def __init__(self):
        self.chain =[self.genesisOlustur()]

    def genesisOlustur(self):
        return block(time.ctime(),"-","")

    def blockEkle(self,data):
        node = block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk = self.chain[i-1].hash
                suan = self.chain[i].previousHash
                if ilk!=suan:
                    return "Zincir Kopmus"
                if sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest() != self.chain[i].hash:
                    return "Zincir Kopmus"
        return "Saglam"

    def listeleme(self):
        print("Blokchain =\n")
        for i in range(len(self.chain)):
            print("Block => ",i,"\nHash =  ",str(self.chain[i].hash),"\nTimeStamp = ",str(self.chain[i].timeStamp),"\nData = ",str(self.chain[i].data),"\nKuvvet = ",str(self.chain[i].kuvvet),"\nPreviousHash = ",str(self.chain[i].previousHash))
            print("---------------------------")


AsilChain = blokChain()
while True:
    print("Lütfen seciminizi yapın \nBlock eklemek için 1 \nBlokchain'i Görmek için 2 \nZinciri Kontrol etmek için 3\nÇımak İçin 4'ü Seçin")
    data = input()
    if data == "1":
        print("Gonderilen Miktarı giriniz.")
        miktar = input()
        AsilChain.blockEkle(miktar)
    elif data == "2":
        AsilChain.listeleme()
    elif data == "3":
        print(str(AsilChain.kontrol()))
    elif data == "4":
        break
