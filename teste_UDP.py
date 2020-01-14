# import time # não usado - delay, pegar tempo real
import socket   # soquete
import mysql.connector  #conexão banco de dados

UDP_IP = "192.168.43.109"   # IP do máquina servidor
UDP_PORT = 1234 # UDP_PORT conexão

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# dados da conexão com o servidor
mydb = mysql.connector.connect(host="localhost",user="root",password="password",auth_plugin='mysql_native_password',database="Giraffe")
mycursor = mydb.cursor()

cont = True
sqlform = "INSERT INTO teste_3 (latitude, longitude) VALUES (%s, %s)"

while cont:
    data1, addr1 = sock.recvfrom(1024) # buffer size de 1024 bytes
    print ("received message:", data1)
    if(data1 == b'apagar'):  #apaga a tabela e cria uma outra
        mycursor.execute("DROP TABLE teste_3; ")
        mycursor.execute("CREATE TABLE teste_3 (id INT PRIMARY KEY AUTO_INCREMENT, criado_em TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP(3), latitude VARCHAR(100), longitude(100));")
    elif(data1 == b'parar'): #para o programa
        cont = False
        # break - pode ser usado em vez de cont
    else:   #coloca na tabela a data recebida
        data2, addr2 = sock.recvfrom(1024) # buffer size de 1024 bytes
        entrada = [(data1), (data2)]
        mycursor.execute(sqlform, entrada)
        mydb.commit()
        mycursor.execute("SELECT * FROM teste_3") #printa tabela
        # mycursor.executemany("SELECT * FROM teste_3")
        for tb in mycursor:
            print(tb)
sock.close()