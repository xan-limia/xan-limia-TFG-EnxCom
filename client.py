import asyncio, websockets, listener, time
import config as conf
import textToSpeech as tts


async def send_audio(websocket, filename = conf.DEFAULT_AUDIO_NAME):
    latency1 = time.time()

    # Lectura del fichero y envio de su contenido en bytes
    with open(filename, 'rb') as file:
        content = file.read()
        await websocket.send(content)
        print("Enviado")

    latency2 = time.time()
    print(f"tiempo de envio: {latency2-latency1}\n")

# Metodo asincrono
async def connect_to_server(recorder):
    # Tiempo inicial
    try:
        latency1 = time.time()
        # Incicio de la comunicacion al endpoint por defecto
        async with websockets.connect(conf.ENDPOINT, ping_timeout=300) as websocket:
            # Envio del fichero de audio
            await send_audio(websocket, filename=recorder.filename)

            # Espera a recibir la respuesta
            text_bytes = await websocket.recv()
            
            # Decodificacion de la respuesta recibida en bytes
            text = text_bytes.decode(conf.CODIFICATION)
            print(f"Received {text}")

            # Tiempo final
            latency2 = time.time()

            # Final de la conexion
            await websocket.close()
        print(f"Tiempo desde conexión hasta obtención de respuesta: {latency2-latency1} segundos")
        with open('test.txt', 'a') as file:
            file.write(f"{latency2-latency1}\n")
        return text

    # Captura de posibles errores de conexion
    except (ConnectionRefusedError, OSError) as e:
            with open('./log/client_error_log.txt', 'a') as file:
                file.write(f"Failed to connect to server: {e}\n")
            print(f"Failed to connect to server: {e}")
    
    
        
async def client():
    stop = True
    recorder = listener.Recorder()

    while True:
        # DESPERTADOR
        # Opcion 1 Palabras clave en LOCAL Vosk
        # output = recorder.listen_forever()

        # Opcion 2 Palabras clave en REMOTO Whisper
        # recorder.record_audio(record_max_time=5)
        # output = await connect_to_server(recorder)

        # EL cliente está inactivo
        if stop:
            # Opcion 3 Palabras clave despertar en LOCAL Vosk
            output = recorder.listen_forever()
            if "despertar" in output.lower():
                stop = False
                print("Hola, que deseas?")
                tts.text_to_speech("Hola, que deseas?")
        
        # El cliente está activo
        if stop == False:
            # Opcion 3 Palabras clave en REMOTO Whisper excepto despertar
            recorder.record_audio(record_max_time=30)
            output = await connect_to_server(recorder)

            # Otras palabras clave para acciones especificas
            if "suspender" in output.lower():
                stop = True
                print("Suspendiendo cliente...")
                tts.text_to_speech("Suspendiendo cliente...")
            elif "terminar" in output.lower():
                print("Apagando cliente...")
                tts.text_to_speech("Apagando cliente...")
                break
            elif "prueba" in output.lower():
                print("Enviando audio por defecto")
                tts.text_to_speech("Enviando audio por defecto")
                recorder.default_audio()
                await connect_to_server(recorder)
            elif "test" in output.lower():
                print("Realizando test de 10 peticiones")
                tts.text_to_speech("Realizando test de 10 peticiones")
                recorder.default_audio()
                for i in range (11):
                    await connect_to_server(recorder)
            else:
                tts.text_to_speech(output)

        # MANUAL
        # key = input("r para grabar, p para enviar audio predefinido, t para test de 10 peticiones, CTRL+C para salir\n")
        # if key == "":
        #     pass
        # elif key == 'r':
        #     recorder.record_audio()
        #     await connect_to_server(recorder)
        # elif key == 'p':
        #     recorder.default_audio()
        #     await connect_to_server(recorder)
        # elif key == 't':
        #     print("Realizando test de 10 peticiones")
        #     recorder.default_audio()
        #     for i in range (11):
        #         await connect_to_server(recorder)

try:
    asyncio.run(client())
except KeyboardInterrupt:
    print("Interrupción de teclado, saliendo")


