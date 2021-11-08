## Sobre o APP

O aplicativo web lê um formulário contendo medidas dos usuários usando HTML e Flask + WTForms, envia o formulário como um arquivo JSON através do código (Python + Flask) para um modelo de predição de Machine Learning usando os serviços da IBM: Watson Studio e AutoAI, e a capacidade de processamento do Watson Machine Learning. 
E retona na tela qual tamanho o usuário deve usar de acordo com cada loja especifica. 

## Material e Serviços

Para usar o aplicativo você vai precisar de um DataSet contendo as medidas de cada loja com a qual quer trabalhar os dados.
Também uma conta na IBMCloud com uma instância do serviço Watson Machine Learning, com o serviço Watson Studio (integrado com o AutoAI e IBM Cloud Pak For Data) e uma instância do Cloud Object Storage.

## Créditos

Esse aplicativo foi construído com ajuda do repositório: https://github.com/IBM/predict-insurance-charges-with-autoai 