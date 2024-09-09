import asyncio, websockets, listener, time, sys, precision
import config as conf
import textToSpeech as tts

async def send_audio(websocket, filename = conf.DEFAULT_AUDIO_NAME):
    latency1 = time.time()
    with open(filename, 'rb') as file:
        content = file.read()
        await websocket.send(content)
    latency2 = time.time()
    print(f"tiempo de envio: {latency2-latency1}\n")

async def connect_to_server(recorder): 
    try:
        latency1 = time.time()
        async with websockets.connect(conf.ENDPOINT, ping_timeout=300) as websocket:
            await send_audio(websocket, filename=recorder.filename)
            print("Enviado")
            text = await websocket.recv()
            #print(f"Received {text.decode(conf.CODIFICATION)}")
            latency2 = time.time()
            await websocket.close()
        print(f"Tiempo desde conexión hasta obtención de respuesta: {latency2-latency1} segundos")
        with open(f'./resultados/testContexto{sys.argv[1]}x{sys.argv[2]}_cliente{sys.argv[3]}.txt', 'a') as file:
            file.write(f"{latency2-latency1}\n")
        return text
    except (ConnectionRefusedError, OSError) as e:
            with open('client_error_log.txt', 'a') as file:
                file.write(f"Failed to connect to server: {e}\n")
      
async def client():

    # Textos orixinais da proba de contexto
    texts = ["""Hoy me gustaría hablar sobre la importancia de la sostenibilidad ambiental. Este es un tema crucial en nuestro tiempo, dado el impacto significativo de que las actividades humanas han tenido en el planeta.""",
              """El perro corrió por el parque, persiguiendo una pelota que lanzaba a su dueño. El aire fresco llenaba el ambiente mientras los niños jugaban en los columpios y el sol brillaba en el cielo, anunciando un día perfecto.""",
              """el tren llegó a la estación justo a tiempo. Los pasajeros se apresuraron a subir buscando sus asientos. Afuera, el pasaje comenzaba a moverse lentamente, con casas y árboles que pasaban en un abrir y cerrar de ojo.""",
              """El avión despegó suavemente, dejando atrás la ciudad. A medida que ganaba altura, las luces abajo se volvieron pequeñas estrellas. Los pasajeros se acomodaron en sus asientos, listos para disfrutar el vuelo.""", 
              """El chef preparó los ingredientes con precisión, cortó las verduras, añadió especias y dejó que el aroma de la comida llenara la cocina. En minutos el plato estaba listo, servido con una presentación impecable."""]

    if len(sys.argv) != 4:
        print("Debe introducir: numero de clientes, peticiones, cliente")
        sys.exit(1)

    recorder = listener.Recorder()
    recorder.filename = f"./audio/es_11s_{sys.argv[3]}.mp3"

    for i in range(int(sys.argv[2])):
        # Esperamos, duracion do ficheiro de audio antes de enviar a peticion
        time.sleep(12)

        text_bytes = await connect_to_server(recorder)

        text = text_bytes.decode(conf.CODIFICATION)

        _, _, precision_percentage = precision.compare_texts(texts[int(sys.argv[3])-1], text)

        # Si o texto non coincide é que recibiu o equivocado
        if precision_percentage < 100:
            with open(f'./resultados/erroresContexto{sys.argv[1]}x{sys.argv[2]}.txt', 'a') as file:
                file.write(f"cliente {sys.argv[3]} en peticion {i}\n")

try:
    asyncio.run(client())
except KeyboardInterrupt:
    print("Interrupción de teclado, saliendo")


