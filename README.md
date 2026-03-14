Automação da ativação de um sinal sonoro de uma escola com Python e ESP8266

Este projeto consiste em um aplicativo em Python com interface gráfica que permite ao usuário definir horários para acionar um sinal sonoro de uma escola (utilizado para sinalizar o fim de aulas ou intervalos).
Quando chega o horário configurado, o programa envia um comando via Wi-Fi para um ESP8266, que ativa o sinal sonoro.

O objetivo do projeto é demonstrar integração entre:

-Interface gráfica em Python
-Comunicação HTTP em rede local
-Microcontrolador ESP8266
-Armazenamento de horários em arquivo JSON

* Funcionalidades

- Adicionar horários para o alarme
- Remover horários individualmente
- Ordenação automática dos horários
- Salvamento automático dos horários
- Carregamento dos horários ao iniciar o programa
- Comunicação via Wi-Fi com o ESP8266
- Interface gráfica simples e intuitiva

* Como o sistema funciona

O sistema é dividido em duas partes:

1 - Aplicativo Python

Responsável por:

-Gerenciar os horários
-Mostrar a interface gráfica
-Verificar o horário atual
-Enviar comando HTTP para o ESP8266

Fluxo:

Usuário define horários
        ↓
Horários são salvos em arquivo JSON
        ↓
Programa verifica o horário atual
        ↓
Quando coincide com um horário salvo
        ↓
Requisição HTTP é enviada ao ESP8266

2 - ESP8266

O ESP8266 funciona como um servidor web local.

Quando recebe a requisição:

http://alarme.local/alarme

ele ativa o Sinal sonoro da escola.

*Interface do programa

A interface permite:

-Digitar horários no formato HH:MM
-Visualizar os horários cadastrados
-Remover horários individualmente
-Os horários são automaticamente ordenados.

*Armazenamento dos horários

Os horários são salvos em um arquivo:

horarios.json

Exemplo:

["08:00", "12:30", "18:45"]

Esse arquivo é carregado automaticamente quando o programa inicia.


Requisitos para o aplicativo funcionar:

O computador e o ESP8266 estão na mesma rede Wi-Fi

O mDNS esteja funcionando (Geralmente não funciona no Windows por conta do firewall, então recomenda-se utilizar um softwere externo como o Bonjour da apple)
