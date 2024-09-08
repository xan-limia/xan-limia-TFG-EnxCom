IS_CLOUD = False
IS_FASTER = True

if IS_FASTER or IS_CLOUD:
    MODEL = 'medium'
    #MODEL = 'large-v3'
    #MODEL = 'distil-large-v3'
else:
    MODEL = 'medium'
    #MODEL = 'large'

DEVICE = 'cuda'
#DEVICE = 'cpu' 

if DEVICE == 'cuda':
    COMPUTE_TYPE = 'float16' 
else:
    COMPUTE_TYPE = 'float32'

LANGUAGE = 'es'
VERBOSE_TRASCRIPTION = False

PORT = 65431
LOCAL_IP = '192.168.1.100'
HOST = LOCAL_IP
ENDPOINT = f'ws://{LOCAL_IP}:{PORT}'


CODIFICATION = 'utf-8'
# en segundos
RECORD_MAX_TIME = 5 
DEFAULT_AUDIO_NAME = "./audio/es_11s_2.mp3"

#DEFAULT_AUDIO_NAME = "./audio/control_calidad/calidad_1_con_blanco_075.mp3"
