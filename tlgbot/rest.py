import requests
import time

class RestAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_get_request(self, url, params):
        response = None
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud GET: {e}')
            return None

    def make_post_request(self, url, data, files=None):
        response = None
        try:
            response = requests.post(url, data=data, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud POST: {e}')
            return None

    def get_last_msg(self, chat_id):
        url = f'{self.base_url}/getUpdates'
        params = {
            'chat_id': chat_id,
            'limit': 1,
        }
        response = self.make_get_request(url, params)
        
        if response and 'result' in response:
            updates = response['result']
            if updates:
                last_update = updates[0]
                if 'message' in last_update:
                    message = last_update['message']
                    message_id = message.get('message_id')
                    message_text = message.get('text')
                    return {'message_id': message_id, 'text': message_text}

        return None


    def get_messages_with_keywords(self, chat_id, keywords=None):
        messages_with_keywords = []

        for _ in range(4):
            updates = self.get_updates_with_offset(chat_id)
            
            for update in updates:
                if 'message' in update and 'text' in update['message']:
                    message_id = update['message']['message_id']
                    message_text = update['message']['text']
                    message_chat_id = update['message']['chat']['id']  # Agregar chat_id
                    
                    if keywords and all(keyword in message_text for keyword in keywords):
                        messages_with_keywords.append({
                            'message_id': message_id,
                            'text': message_text,
                            'chat_id': message_chat_id,  # Incluir chat_id en el diccionario
                        })

            if messages_with_keywords:
                break
            else:
                time.sleep(5)

        return messages_with_keywords


    # Resto de las funciones de obtención de mensajes aquí...

    def get_updates_with_offset(self, chat_id):
        url = f'{self.base_url}/getUpdates'
        params = {
            'chat_id': chat_id,
        }

        updates = self.make_get_request(url, params)

        if updates and 'result' in updates:
            return updates['result']
        else:
            return []

    # Otras funciones de obtención de mensajes aquí...
    def get_chat_description(self, chat_id):
        url = f'{self.base_url}/getChat'
        params = {
            'chat_id': chat_id,
        }
        response = self.make_get_request(url, params)
        
        if response and 'ok' in response:
            chat_info = response['result']
            if 'description' in chat_info:
                return chat_info['description']
        
        return None
