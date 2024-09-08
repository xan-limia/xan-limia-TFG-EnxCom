import asyncio, time, websockets, tempfile, datetime, json
import speechToText as stt
import config as conf

async def transcription(data_received):
    # Creacion del achivo temporal con los datos recibidos
    with tempfile.NamedTemporaryFile(delete=True, suffix='.wav') as temp_file:
            temp_file.write(data_received)

            temp_file_name = temp_file.name
            
            file = open(temp_file_name, "rb")
            data = file.read()
            file.close()

            # Transcricion
            transcription_time1 = time.time()
            if conf.IS_CLOUD:
                output = stt.transcribe(data)
            elif conf.IS_FASTER:
                output, info = stt.transcribe(temp_file_name)
            else:
                output = stt.transcribe(temp_file_name)
            transcription_time2 = time.time()

            temp_file.close()
    
    print(f"trasncripción completada, {transcription_time2-transcription_time1} segundos")
    with open('transcription.txt', 'a') as file:
        file.write(f"{transcription_time2-transcription_time1}\n")

    return output

# Recuperacion del texto
async def get_text(input):
    print("Obteniendo texto")
    if conf.IS_CLOUD:
        text = input.get('transcription', '')
    elif conf.IS_FASTER:
        text = "".join([segment.text for segment in input])
    else:
        text = input.get('text', '')
    print(text)
    return text


async def receive_audio(websocket):
    # Registrar datos de las peticiones al servidor
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    petition_data = {
        "IP": f"{websocket.remote_address[0]}",
        "PORT": f"{websocket.remote_address[1]}",
        "Time": f"{date}"
    }
    try:
        with open('./log/petitions_logs.json', 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        json_data = {"petitions": []}

    json_data["petitions"].append(petition_data)
    with open('./log/petitions_logs.json', 'w') as file:
        json.dump(json_data, file, indent=4)

    # Recibir el mensaje de la peticion
    async for data_received in websocket:
        print(f"Receive message")
        
        # Creacion de la tarea asincrona de transcricion
        transcription_task = asyncio.create_task(transcription(data_received=data_received))
        output = await transcription_task
        
        # Recuperacion del texto
        text = await get_text(output)
        text_to_bytes = (bytes(text, conf.CODIFICATION))

        # Envio de la respuesta
        await websocket.send(text_to_bytes)    

async def server():
    # Inicializacion del servidor
    async with websockets.serve(receive_audio, conf.HOST, conf.PORT, max_size = None):
        print(f"WebSocket server is running on ws://{conf.HOST}:{conf.PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        # Ejecucion constante hasta interrupcion de teclado
        asyncio.run(server())
    except KeyboardInterrupt:
        print("Saliendo...")
