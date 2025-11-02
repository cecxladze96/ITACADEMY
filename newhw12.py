import os, sys, json

def create_json_file(path, file):
    file_path = None

    if len(path.split('/')) == 2:
     file_path=f"{path}/{file}.json"
     os.makedirs(path, exist_ok=True)

    try:
      with open(file_path, mode='x', encoding='utf-8'):
       ...
    except  FileExistsError:
      print(f"file '{file_path}' უკვე არსებობს")
      print("მუშაობის გაგრძელება")    
    except TypeError:
     print("უნდა იყოს ორ-საფეხურიანი, მაგალითად: 'files/jspms'")
     sys.exit()

    return file_path



def write_json_file(path, json_data:list):
  with open(path, 'w', encoding='utf_8') as f:
    f.write(json.dumps(json_data, indent=2))
  

def read_json_file(path):
   with open (path, 'r' , encoding='utf-8') as f:
     return json.loads(f.read())



def add_player_json_file(path, data: dict):
  players=read_json_file(path)
  if type(data["id"]) != int:
    print("მოთამაშის  ID უნდა იყოს ციფრი")
    return
  for player in players:
    if player["id"]==data["id"]:
      print(f"მოთამაშე ID-ით '{data["id"]}' უკვე არსებობს")
      return
  else:
      players.append(data)
      players.sort(key=lambda x: x["id"])

  write_json_file(path, players)  




def update_json_file(path):
   Players=read_json_file(path)
   data={}
    
   data['id']=input("\nID [დააჭირეთ 'ENTER' დასრულებისთვის]:") or None

   if data['id'] is None or not data['id'].isdigit():
     print("ID აუცილებლა უნდა იყოს რიცხვი, კიდევ ცადეთ...")
     return
   for i in range(len(Players)):
     data['id']=int(data['id'])

     if data['id'] == Players[i]['id']:
        print(Players[i], "\n")

        data['name']=input("სახელი [დააჭირეთ 'ENTER' გაგრძელებისთვის]:") or Players[i]['name']
        data['country']=input("ქვეყანა [დააჭირეთ 'ENTER' გაგრძელებისთვის]:") or Players[i]['country']
        data['rating']=input("შეფასება [დააჭირეთ 'ENTER' გაგრძელებისთვის]:") or Players[i]['rating']
        data['rating']=int(data['rating']) if data['rating'].isdigit() else Players[i]['rating']
        data['age']=input("ასაკი[დააჭირეთ 'ENTER' გაგრძელებისთვის]:") or Players[i]['age']
        data['age']=int(data['age']) if data['age'].isdigit() else Players[i]['age']

        print(f"\n{data}")
        Players[i] = data
        break
   else:
      print(f"\n მოთამაშე ID-ით '{data['id']}' არ მოიძებნა")
      print("გამოსვლა")
      return

   question=input(" განვაახლოთ ინფორმაცია ფაილში(y.n)?")

   if question.lower() =="y":
      write_json_file(path, Players)
      print("მონაცემები განახლდა წარმატებით")
   else:
      print("მონაცემების შენახვა არ მოხდა")
       




