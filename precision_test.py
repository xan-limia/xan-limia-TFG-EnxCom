import asyncio, websockets, listener, precision
import config as conf

async def send_audio(websocket, filename = conf.DEFAULT_AUDIO_NAME):
    with open(filename, 'rb') as file:
        content = file.read()
        await websocket.send(content)

async def connect_to_server(recorder):
    async with websockets.connect(conf.ENDPOINT, ping_timeout=300) as websocket:
        await send_audio(websocket, filename=recorder.filename)
        text = await websocket.recv()
        await websocket.close()
    
    return text
        
async def client():

    # Textos orixinais
    texts = ["""La punta está bien y mide 12 milímetros. Medidas de los diámetros son: 3 milímetros, 5 milímetros. El vástago está roto""",
              """La segunda cara tiene 4 y la tercera 23. El vástago mide 45 milímetros. La punta y el mango salieron defectuosos""",
              """El diámetro de la primera cara es de 4 milímetros y el de la segunda de 9 milímetros, se ve todo correcto, menos el vástago que tiene varios defectos""",
              """Se han encontrado defectos en la punta y el mango""", 
              """La punta tiene algún problemilla, los diámetros de las caras son 3 milímetros, 6 milímetros y 15 milímetros, el resto todo bien""",
              """El mango está roto. La punta mide 5 milímetros, medidas de las caras: primera 5 milímetros, segunda 9 milímetros, tercera 3 milímetros. El vástago mide 34 milímetros, pero tiene varios defectos"""]
    recorder = listener.Recorder()

    ruido = ["005", "01", "025", "05", "075", "1"]


    for audio in range(1, 7):
        for i in range(0, 6):

            recorder.filename = f"./audio/control_calidad/calidad_{audio}_con_blanco_{ruido[i]}.mp3"
            text_bytes = await connect_to_server(recorder)

            text = text_bytes.decode(conf.CODIFICATION)

            text = precision.replace_word(text, "mm", " milímetros")

            _, _, precision_percentage = precision.compare_texts(texts[audio-1], text)

            with open('precision_test.txt', 'a') as file:
                text_to_write = f"filename: {recorder.filename} \n only original text: {texts[audio-1]} \n only response text: {text} \n precision: {precision_percentage} \n"
                file.write(text_to_write)
            
try:
    asyncio.run(client())
except KeyboardInterrupt:
    print("Interrupción de teclado, saliendo")


