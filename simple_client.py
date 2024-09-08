import asyncio, websockets, listener, time, sys
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
    latency1 = time.time()
    try:
        async with websockets.connect(conf.ENDPOINT, ping_timeout=300) as websocket:
            await send_audio(websocket, filename=recorder.filename)
            print("Enviado")
            text = await websocket.recv()
            #print(f"Received {text.decode(conf.CODIFICATION)}")
            latency2 = time.time()
            await websocket.close()
        print(f"Tiempo desde conexión hasta obtención de respuesta: {latency2-latency1} segundos")
        with open(f'./resultados/test{sys.argv[1]}x{sys.argv[2]}_{sys.argv[3]}.txt', 'a') as file:
            file.write(f"{latency2-latency1}\n")
    except (ConnectionRefusedError, OSError) as e:
            with open('client_error_log.txt', 'a') as file:
                file.write(f"Failed to connect to server: {e}\n")
            #print(f"Failed to connect to server: {e}")
   
        
async def client():

    if len(sys.argv) != 4:
        print("Debe introducir: numero de clientes, peticiones, n prueba")
        sys.exit(1)

    recorder = listener.Recorder()

    recorder.default_audio()

    for i in range(int(sys.argv[2])):
        # Esperamos, duracion do ficheiro de audio antes de enviar a peticion
        time.sleep(11)

        await connect_to_server(recorder)

try:
    asyncio.run(client())
except KeyboardInterrupt:
    print("Interrupción de teclado, saliendo")


