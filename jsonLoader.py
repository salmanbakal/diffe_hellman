import json

def json_loader():

  with open('jsonData.json', 'r') as data:
    access_data = json.load(data)
    # print(access_data)
    res = access_data['results']
    # print(res[1])
    for access_class in res:
      reply_data=access_class['replies']
      for names in reply_data:
        user_names=names['user']['display_name']
        save_data=[]
        save_data.append(user_names)
        print(save_data)

        with open('user_names.json','w') as new_data:
          json.dump(save_data,new_data)


json_loader()