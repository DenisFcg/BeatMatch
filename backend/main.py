import os, base64, json, re, pygame
from difflib import get_close_matches
from dotenv import load_dotenv
from requests import post, get, put
from gtts import gTTS

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    
    if result.status_code != 200:
        print("Erro ao obter token:", result.status_code)
        print("Resposta:", result.content)
        return None

    json_result = json.loads(result.content)
    token = json_result.get("access_token")
    if not token:
        print("access_token não encontrado na resposta")
        return None
    
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    
    headers = get_auth_header(token)
    
    response = get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        search_results = response.json()
        if search_results['artists']['items']:
            artist_info = search_results['artists']['items'][0]
            return artist_info
        else:
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def search_for_track(token, track_name):
    url = "https://api.spotify.com/v1/search"
    
    params = {
        "q": track_name,  
        "type": "track",
        "limit": 1
    }
    
    headers = get_auth_header(token)
    
    response = get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        search_results = response.json()
        if search_results['tracks']['items']:
            track_info = search_results['tracks']['items'][0]
            return track_info  # Retorna todas as informações da música
        else:
            print("Música não encontrada.")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def play_track(token, track_uri):
    url = "https://api.spotify.com/v1/me/player/play"
    
    headers = get_auth_header(token)
    
    data = {
        "uris": [track_uri]  # Adiciona a URI da música
    }
    
    response = put(url, headers=headers, json=data)
    
    if response.status_code == 204:
        print("Música tocando com sucesso!")
    else:
        print(f"Erro ao tocar a música: {response.status_code} - {response.text}")

def search_music_by_mood(token, mood):
    mood_to_genre = {
        "feliz": "pop",
        "triste": "acoustic",
        "animado": "dance",
        "calmo": "chill",
        "raiva": "metal",
        "romântico": "romance"
    }
    
    genre = mood_to_genre.get(mood.lower(), "pop") 
    url = f"https://api.spotify.com/v1/recommendations?seed_genres={genre}&limit=1"
    
    headers = get_auth_header(token)
    response = get(url, headers=headers)
    
    if response.status_code == 200:
        recommendations = response.json()
        if recommendations['tracks']:
            track_info = recommendations['tracks'][0]
            track_uri = track_info['uri']
            track_url = track_info['external_urls']['spotify']
            print(f"Música recomendada para você: {track_url}")
            play_music = input('Deseja tocar esta música? (s/n): ')
            if play_music.lower() == 's':
                play_track(token, track_uri)
        else:
            print("Nenhuma música recomendada encontrada.")
    else:
        print(f"Erro ao buscar recomendações: {response.status_code} - {response.text}")

def load_knowledge_base(file_path: str) -> dict:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({"questions": []}, file, indent=2)
        print(f"O arquivo '{file_path}' foi criado.")

    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, question: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

# Função para remover URLs de um texto
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')  # Padrão para URLs
    return url_pattern.sub(r'', text)  # Substitui as URLs por uma string vazia

# Função para converter texto em fala e reproduzir o áudio
def text_to_speech(text):
    # Remover URLs antes de converter o texto em fala
    clean_text = remove_urls(text)
    
    tts = gTTS(text=clean_text, lang='pt')
    audio_file = "response.mp3"
    tts.save(audio_file)
    
    # Inicializando o mixer do pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    
    # Espera até a música terminar antes de continuar
    while pygame.mixer.music.get_busy():
        continue
    
    pygame.mixer.quit()
    os.remove(audio_file)

def chat_bot(token):
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
            text_to_speech(answer)  # Responder com voz
        else:
            print('Bot: Eu não sei sobre esta pergunta. Pode me ensinar?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base['questions'].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Obrigado, eu aprendi o que você respondeu.')
                text_to_speech("Obrigado, eu aprendi o que você respondeu.")  # Responder com voz

        if "buscar artista" in user_input.lower():
            artist_name = input('Qual artista você gostaria de buscar? ')
            artist_info = search_for_artist(token, artist_name)
            if artist_info:
                response_text = f"Artista encontrado: {artist_info['name']} - {artist_info['external_urls']['spotify']}"
                print(response_text)
                text_to_speech(response_text)  # Responder com voz
            else:
                response_text = "Artista não encontrado."
                print(response_text)
                text_to_speech(response_text)  # Responder com voz

        elif "buscar musica" in user_input.lower():
            track_name = input('Qual música você gostaria de buscar? ')
            track_info = search_for_track(token, track_name)
            if track_info:
                track_uri = track_info['uri']  # Obtendo a URI da música
                track_url = track_info['external_urls']['spotify']
                response_text = f"Música encontrada: {track_url}"
                print(response_text)
                text_to_speech(response_text)  # Responder com voz
                
        elif "buscar musica por humor" in user_input.lower():
            mood = input("Como você está se sentindo? (ex: feliz, triste, calmo, animado): ")
            search_music_by_mood(token, mood)

if __name__ == '__main__':
    token = get_token()
    if token:
        chat_bot(token)
