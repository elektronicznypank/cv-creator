import json
from time import asctime

with open('data.json', encoding='utf-8') as json_file:
    data_from_json: dict = json.load(json_file)

print(data_from_json)

input_data = f'''

# **CURRICULUM VITAE**  



## Personal data  



name: {data_from_json['firstName']} {data_from_json['lastName']}
<img align='right' src='picture.png', width='100' height='100'>


date of birth: {data_from_json['dateOfBirth']} r.


mail: {data_from_json['mail']}


phone number: {data_from_json['phoneNumber']}


## Education


secondary school: {data_from_json['education']['secondarySchool']}  


## Job experience  


# {data_from_json['jobHistory']['place1']['name']}  



# {data_from_json['jobHistory']['place1']['name']}  

*Wyrażam zgodę na przetwarzanie moich danych osobowych dla potrzeb niezbędnych do realizacji procesu rekrutacji
(zgodnie z ustawą z dnia 10 maja 2018 roku o ochronie danych osobowych (Dz. Ustaw z 2018, poz. 1000) 
oraz zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r.
w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu
takich danych oraz uchylenia dyrektywy 95/46/WE (RODO).*'''

with open(f'CV {asctime()}.md', 'w') as CV:
    CV.write(input_data)

print('Your simple CV has been created.')