import requests
import time
from rest import RestAPI  # Importa las funciones de obtención de mensajes desde rest.py

class TLGBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{self.token}'
        self.rest_api = RestAPI(self.base_url)
        self.keyword_message_ids = {}  

    def send_message(self, chat_id, text):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text,
        }
        self.rest_api.make_post_request(url, data)

    def send_photo(self, chat_id, photo_path, caption=None):
        url = f'{self.base_url}/sendPhoto'
        data = {
            'chat_id': chat_id,
            'caption': caption,
        }
        files = {'photo': open(photo_path, 'rb')}
        self.rest_api.make_post_request(url, data, files=files)

    def send_video(self, chat_id, video_path, caption=None):
        url = f'{self.base_url}/sendVideo'
        data = {
            'chat_id': chat_id,
            'caption': caption,
        }
        files = {'video': open(video_path, 'rb')}
        self.rest_api.make_post_request(url, data, files=files)

    def reply_last_msg(self, chat_id, text):
        for _ in range(4):
            last_message = self.rest_api.get_last_msg(chat_id)
            if last_message is not None:
                message_id = last_message.get('message_id')
                message_text = last_message.get('text')

                if message_id and message_text:
                    reply_text = f'{text}'
                    self.send_message_with_reply(chat_id, reply_text, message_id)
                    break
            else:
                time.sleep(5)


    def pin_last_msg(self, chat_id):
        message_to_pin = None

        for _ in range(4):
            last_message = self.rest_api.get_last_msg(chat_id)
            if last_message is not None:
                message_to_pin = last_message
                break
            else:
                time.sleep(5)

        if message_to_pin:
            url = f'{self.base_url}/pinChatMessage'
            data = {
                'chat_id': chat_id,
                'message_id': message_to_pin['message_id'],
            }
            response = self.rest_api.make_post_request(url, data)
            if response and response.get('ok'):
                return True
            else:
                return False
        else:
            return False


    def reply_keyword_msg(self, chat_id, keyword, text):
            for _ in range(4):
                last_messages = self.rest_api.get_messages_with_keywords(chat_id, [keyword])
                if last_messages:
                    for message in last_messages:
                        message_id = message.get('message_id')  # Obtener el ID del mensaje si existe

                        # Verifica si ya hemos respondido a este mensaje y evita enviar múltiples respuestas
                        if message_id is not None:
                            response_text = f'Respuesta: {text}'
                            self.send_message_with_reply(chat_id, response_text, message_id)
                    break
                else:
                    time.sleep(5)

    def send_message_with_reply(self, chat_id, text, reply_to_message_id):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text,
            'reply_to_message_id': reply_to_message_id,
        }
        self.rest_api.make_post_request(url, data)



    def send_document(self, chat_id, document_path, caption=None):
        url = f'{self.base_url}/sendDocument'
        data = {
            'chat_id': chat_id,
            'caption': caption,
        }
        files = {'document': open(document_path, 'rb')}
        self.rest_api.make_post_request(url, data, files=files)


    def descargar_archivo(self, file_id, nombre_archivo):
            # Construye la URL para obtener la información del archivo
            url_info = f'{self.base_url}/getFile?file_id={file_id}'

            # Realiza una solicitud GET para obtener la información del archivo
            response = self.rest_api.make_get_request(url_info, params={})

            if response and 'ok' in response:
                file_path = response['result']['file_path']

                # Construye la URL de descarga del archivo
                url_descarga = f'https://api.telegram.org/file/bot{self.token}/{file_path}'

                # Realiza una solicitud GET para descargar el archivo
                response = requests.get(url_descarga)

                # Guarda el archivo descargado con el nombre especificado
                with open(nombre_archivo, 'wb') as archivo:
                    archivo.write(response.content)

                return f'Archivo descargado como {nombre_archivo}'
            else:
                return 'Error al obtener la información del archivo'
            
            
    def edit_about(self, chat_id, new_description):
            url = f'{self.base_url}/setChatDescription'
            data = {
                'chat_id': chat_id,
                'description': new_description,
            }
            response = self.rest_api.make_post_request(url, data)
            print(response)
            if response and response.get('ok'):
                return True
            else:
                return False
               
               

    def get_chat_members_count(self, chat_id):
            url = f'{self.base_url}/getChatMembersCount'
            data = {
                'chat_id': chat_id,
            }
            response = self.rest_api.make_post_request(url, data)

            if response and 'ok' in response:
                members_count = response['result']
                return members_count
            else:
                return None
                
                
                
    def get_chat_description(self, chat_id):
        return self.rest_api.get_chat_description(chat_id)



    @staticmethod
    def last_id(token):
        url = f'https://api.telegram.org/bot{token}/getUpdates'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and data['result']:
                chat_id = data['result'][-1]['message']['chat']['id']
                return chat_id
        return None