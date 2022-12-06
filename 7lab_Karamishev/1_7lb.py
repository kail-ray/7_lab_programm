from socket import *
def poisk(data):
    f=open('группа.txt', 'r+', encoding='utf-8')
    a=list(f)
    name=None
    if data.encode('utf-8')==b'\n':
        name='Вы не ввели фамилию\n'
    else:
        for i in range(len(a)):
            if a[i].find(data)!=-1:
                name = 'Привет, '+a[i].split()[0]+'\n'
        if name==None:
            name='Ошибка. Вас нет в журнале\n'
    return name
    f.close()
try:
    s = socket(AF_INET, SOCK_STREAM)#веб-протокол 
    s.bind(('127.0.0.1', 2001))#назначение ip адреса и порта
    #i=0
    while True:
        s.listen()#показывает количество запросов и ставит их в ожидание если их число больше чем в скобках они сбрасываются
        client_socket, adres = s.accept()#принимает запрос и разделяет его на клиента и адрес клиента
        # программа фиксируется на этом моменте и ждёт подключение клиента
        otvet='напишите свою фамилию!\n'.encode('utf-8')#дикодирование текста
        client_socket.send(otvet)# отправка ответа клиенту
        data = client_socket.recv(1024).decode('utf-8')#получение содержимого запроса и дегодировка из байтового вида
        print(data.encode('utf-8'))
        otvet=poisk(data).encode('utf-8')#дикодирование текста
        client_socket.send(otvet)# отправка ответа клиенту
        client_socket.shutdown(SHUT_WR)#закрытие соединения с данным клиентом после отправления ему ответа
except KeyboartInterrupt:  
    s.close()