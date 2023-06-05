# SocketPython

Neste projeto, você desenvolverá uma aplicação em Python para simular uma comunicação
publisher/subscriber em uma rede de computadores, utilizando a biblioteca socket para
estabelecer a conexão entre diversos clientes e um servidor central.
Introdução ao modelo Publisher/Subscriber:
O modelo publisher/subscriber (publicador/assinante) é um padrão de comunicação
amplamente utilizado em sistemas distribuídos. Nesse modelo, os publicadores (publishers)
produzem e enviam mensagens a um intermediário (geralmente, um servidor), enquanto os
assinantes (subscribers) se registram no servidor para receber mensagens de interesse. Os
assinantes não precisam ter conhecimento direto dos publicadores, e vice-versa. Esse
padrão de comunicação permite o desacoplamento entre os produtores e consumidores de
mensagens, facilitando a escalabilidade, a manutenção e a evolução dos sistemas.

Objetivos do projeto:
1. Familiarizar-se com o modelo publisher/subscriber e a biblioteca socket em Python;
2. Implementar um servidor central que gerencia as mensagens dos publicadores e
distribui para os assinantes;
3. Criar clientes que atuam como publicadores e assinantes, interagindo com o servidor
através de conexões de rede;
4. Testar a comunicação entre os clientes e o servidor, garantindo o correto
funcionamento do sistema.


Especificações chave:
1. Ao conectar ao servidor, os clientes devem indicar qual tópico deve ser utilizado para
receber/enviar mensagens;
2. Um cliente pode ser publisher ou subscriber, exclusivamente. Nunca os dois;
3. O servidor deve armazenar o nome dos tópicos mesmo que todos os clientes que
utilizam o tópicos tenham se desconectado;

4. O servidor deve enviar a última mensagem armazenad em um tópico, se a mesma
existir, para todo novo subscriber que se inscrever no dito tópico.
Ao concluir este projeto, você terá adquirido habilidades práticas na criação de aplicações
de rede em Python, utilizando a biblioteca socket e o modelo de comunicação
publisher/subscriber. Além disso, você estará apto a aplicar esse conhecimento no
desenvolvimento de sistemas distribuídos mais complexos, como sistemas de mensagens
em tempo real, sistemas de notificação e aplicações IoT (Internet das Coisas).
