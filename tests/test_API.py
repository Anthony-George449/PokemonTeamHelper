import base64
import requests
import json
import unittest
import tkinter as tk

class ApiTestMethods(unittest.TestCase):
    def testAPIs(self):
        index = 0
        responses = []
        for url in [
            "https://championsbattledata.com/api",
            "https://championsbattledata.com/api/index",
            "https://championsbattledata.com/data/pokemon-index.json",
        ]:
            PrintResponse(url, responses)
            index += 1
        for response in responses:
            self.assertEqual(response.status_code, 200)

    def testRetreivingSprites(self):
        api_url = "https://championsbattledata.com/api"
        responses = ParseSpriteAndName(api_url)
        for response in responses:
            self.assertEqual(response.status_code, 200)

    def testRetreivingSprites_Hardcoded(self):
        responses = []
        for url in [
            {"name": "Eelektross", "url": "https://championsbattledata.com/pokemon_champions_assets/pokemon/Eelektross.png"},
            {"name": "Mega Eelektross", "url": "https://championsbattledata.com/pokemon_champions_assets/pokemon/Mega Eelektross.png"}
        ]:
            responses.append(DisplaySprite(url["name"], url["url"]))
        for response in responses:
            self.assertEqual(response.status_code, 200)

def ParseSpriteAndName(api_url):
     responses = []
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
                 responses.append(DisplaySprite(form['form_name'], sprite_url))
     return responses

def DisplaySprite(name, sprite_url):
    sprite_response = requests.get(sprite_url)
    sprite_response.raise_for_status()
    image_data = base64.b64encode(sprite_response.content).decode("ascii")

    window = tk.Tk()
    window.title(name)
    sprite_image = tk.PhotoImage(data=image_data)
    tk.Label(window, image=sprite_image).pack()
    window.mainloop()
    return sprite_response
                             
def CreateResponseFile(api_url, output_file):
    response = requests.get(api_url)
    json_response = json.dumps(response.json(), indent=4, sort_keys=True)
    with open(output_file, "w") as f:
        f.write(json_response)

def PrintResponse(api_url, responses):
    response = requests.get(api_url)
    responses.append(response)
    json_response = json.dumps(response.json(), indent=4, sort_keys=True)
    print(json_response)

if __name__ == "__main__":
    unittest.main()
