import base64
import requests
import json
import tkinter as tk

def CreateResponseFile(api_url, output_file):
    response = requests.get(api_url)
    json_response = json.dumps(response.json(), indent=4, sort_keys=True)
    with open(output_file, "w") as f:
        f.write(json_response)

def ParsePokemonData(api_url):
     pokemon_dict = {}
     response = requests.get(api_url)
     response.raise_for_status()
     response_processing = response.json()
     pokemon_list = response_processing['pokemon']
     for pokemon in pokemon_list:
         if pokemon['name'] == "Eelektross":
             pokemon = pokemon['summary']['forms']
             for form in pokemon:
                 print("Name: ", form['form_name'])
                 sprite = form['image_path']
                 sprite_url = "https://championsbattledata.com/" + sprite
                 sprite_response = requests.get(sprite_url)
                 sprite_response.raise_for_status()
                 image_data = base64.b64encode(sprite_response.content).decode("ascii")

                 window = tk.Tk()
                 window.title(form['form_name'])
                 sprite_image = tk.PhotoImage(data=image_data)
                 tk.Label(window, image=sprite_image).pack()
                 window.mainloop()


if __name__ == "__main__":
        api_url = "https://championsbattledata.com/api"
        # output_file = "JsonOutput/api_response.json"
        # CreateResponseFile(api_url, output_file)
        ParsePokemonData(api_url)
