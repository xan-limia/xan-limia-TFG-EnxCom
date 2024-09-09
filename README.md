# xan-limia-TFG-EnxCom

Traballo Fin de Grao 2024 

Arquitectura con captura de datos distribuída e computación centralizada aplicada á tradución e xestión de voz a texto

Xan Limia García

Traballo Fin de Grao 2023 

Uso de coñecemento externo na aprendizaxe por reforzo dun comportamento visual en robótica móvil 
Arquitectura con captura de datos distribuída e computación centralizada aplicada á tradución e xestión de voz a texto

Xan Limia García


**Guia de usuario**

    A continuación detállase como poñer en funcionamento o noso sistema.

    git clone https://github.com/xan-limia/xan-limia-TFG-EnxCom

    
Execución do contorno servidor e cliente:

    COnfigurar en config.py a IP correspondente e demais parámetros que se consideren necesarios

    Para executar o servidor executamos:
    python3 server.py
    Para executar o cliente executamos: 
    python3 client.py



Para realizar as probas:

    Concorrencia:
    ./concurrency_test.sh

    Contexto:
    ./context_test.sh

    Precisión
    python3 precision_test.py

Definicion dos arquivos do repositorio:

    server.py -> servidor
    client.py -> cliente con módulo despertador
    config -> configuración de parámetros do cliente e servidor

    listener.py -> módulo que graba a voz, e utiliza Vosk para o módulo despertador
    speechToText.py -> módulo de transcrición de voz a texto
    textToSpeech.py -> módulo que se encarga de reproducir polo altavoz do cliente o texto recibido

    simple_client.py -> cliente sen módulo despertador que realiza un numero determinado de probas
    context_test.py -> cliente que executa un arquivo de audio diferente, pensado para as probas de contexto

    estadísticas_concurrencia.py -> ficheiro para analizar datos
    graficas.py -> ficheiro para analizar datos

    precision_test.py -> ficheiro que realiza varias peticions e comproba a precisión dos textos
    precision.py -> ficheiro cas funcions necesarias para comparar dous textos

    
    

    

