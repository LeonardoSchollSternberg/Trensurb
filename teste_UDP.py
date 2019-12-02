import time # não usado - delay, pegar tempo real
import socket   # soquete
import mysql.connector  #conexão banco de dados

UDP_IP = "192.168.43.109"   # IP do máquina servidor
UDP_PORT = 1234 # UDP_PORT conexão

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# dados da conexão com o servidor
mydb = mysql.connector.connect(host="localhost",user="root",password="password",auth_plugin='mysql_native_password',database="dadosS200")
mycursor = mydb.cursor()

cont = True
# id_r=0  # ID PRIMARY KEY de cada data (para testes) - implementação antiga
sqlform = "INSERT INTO teste (message) VALUES (%s)"

while cont:
    data, addr = sock.recvfrom(1024) # buffer size de 1024 bytes
    print ("received message:", data)
    if(data == b'apagar'):  #apaga a tabela e cria uma outra
        mycursor.execute("DROP TABLE teste")
        mycursor.execute("CREATE TABLE teste (id INT PRIMARY KEY, criado_em TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP(3), message VARCHAR(100))")
        #id_r=0 - implementação antiga
    elif(data == b'parar'): #para o programa
        cont = False
        # break - pode ser usado em vez de cont
    else:   #coloca na tabela a data recebida
        entrada = [(data), ]
        mycursor.execute(sqlform, entrada)
        mydb.commit()
        #id_r=id_r+1 - implementação antiga
        mycursor.execute("SELECT * FROM teste") #printa tabela
        for tb in mycursor:
            print(tb)
sock.close()