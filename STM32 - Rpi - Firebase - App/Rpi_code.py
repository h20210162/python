import serial
import pyrebase 
import time

from time import sleep


config = {     
  "apiKey": "AIzaSyAo9cEmTy2pOEygEEIXdCUHc7uOlSFdcW4",
  "authDomain": "garageapp-94e6a",
  "databaseURL": "https://garageapp-94e6a-default-rtdb.firebaseio.com/",
  "storageBucket": "project-221974637415"
}

ser = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=1)
firebase = pyrebase.initialize_app(config)


try:
    while True:
        database = firebase.database()
        ProjectBucket = database.child("garage_info")
        received_data = ser.read(3)
        dcd = received_data.decode()
        #print(dcd)
        print(len(dcd))

        if(len(dcd)!=0):

            if(dcd[2]=="0"):

                print("dcd[2]",dcd[2])
                ProjectBucket.child("State").set("IDLE")

            elif(dcd[2]=="1"):

                if(dcd[1]=="0"):

                    ProjectBucket.child("trig").set(1)
                    ProjectBucket.child("garage_info").child("State").set("ENTRY of a person")
                    time.sleep(4)
                    door = ProjectBucket.child("garage_info").child("Door").get().val()
                    #time.sleep(1)
                    #print("door",door)

                    if(door==0):
                        data3=ser.write(b'e\n')
                        print("data3",data3)
                        #time.sleep(2)
                    else:
                        data4=ser.write(b'l\n')
                        print("dta4",data4)
                        #time.sleep(2)

                elif(dcd[1]=="1"):

                    ProjectBucket.child("garage_info").child("trig").set(1)
                    ProjectBucket.child("garage_info").child("State").set("ENTRY of a Car")
                    time.sleep(4)
                    door = ProjectBucket.child("Door").get().val()
                    #time.sleep(1)
                    print("door",door)

                    if(door==0):
                        data=ser.write(b'e\n')
                        print("data",data)
                    else:
                        data2=ser.write(b'l\n')
                        print("data2",data2)

            elif(dcd[2]=="2"):

                if(dcd[1]=="0"):

                    ProjectBucket.child("State").set("EXIT of a person")
                    ProjectBucket.child("garage_info").child("trig").set(1)
                    time.sleep(4)
                    door = ProjectBucket.child("garage_info").child("Door").get().val()
                    #time.sleep(1)
                    #print("door",door)

                    if(door==0):
                        ser.write(b'e\n')
                        #time.sleep(2)
                    else:
                        ser.write(b'l\n')
                        #time.sleep(2)

                elif(dcd[1]=="1"):

                    ProjectBucket.child("State").set("EXIT of a Car")
                    count = ProjectBucket.child("garage_info").child("garage_capacity").get().val()
                    print(type(count))
                    count = count + 1
                    print(count)
                    time.sleep(4)
                    door = ProjectBucket.child("garage_info").child("Door").get().val()
                    #time.sleep(1)
                    #print("door",door)

                    if(door==0):
                        ser.write(b'e\n')
                        #time.sleep(2)
                    else:
                        ser.write(b'l\n')       

                    ProjectBucket.child("garage_info").child("garage_capacity").set(count)

        else:

            ProjectBucket.child("State").set("IDLE")
            time.sleep(2)
            ProjectBucket.child("garage_info").child("trig").set(0)
            

except KeyboardInterrupt:  
    print("successfull")
    
