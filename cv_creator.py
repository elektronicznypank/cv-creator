import json
from time import asctime

with open('data.json', encoding='utf-8') as json_file:
    data_from_json: dict = json.load(json_file)

print(data_from_json)

input_data = f'''# **CURRICULUM VITAE**

## PERSONAL DATA 
<div align='left'><img src='{data_from_json['pictureFileName']}', width='100' height='100'></div>
`name:` {data_from_json['firstName']} {data_from_json['lastName']}  
date of birth: {data_from_json['dateOfBirth']} r.  
mail: {data_from_json['mail']}  
phone number: {data_from_json['phoneNumber']}  
www: {data_from_json['www']}

## EDUCATION
secondary school: {data_from_json['education']['secondarySchool']}

## WORK EXPERIENCE
{data_from_json['jobHistory']['place1']['name']}  
* from: {data_from_json['jobHistory']['place1']['beginDate']}
to: {data_from_json['jobHistory']['place1']['endDate']}  
{data_from_json['jobHistory']['place2']['name']}  
* from: {data_from_json['jobHistory']['place2']['beginDate']}
to: {data_from_json['jobHistory']['place2']['endDate']}

## LANGUAGES
* {data_from_json['languages'][0]}
* {data_from_json['languages'][1]}

## HOBBIES
* {data_from_json['hobbies'][0]}  
* {data_from_json['hobbies'][1]}  
* {data_from_json['hobbies'][2]}  
<div align="justify">
I agree to the processing of personal data provided in this document for realising the recruitment process 
pursuant to the Personal Data Protection Act of 10 May 2018 (Journal of Laws 2018, item 1000) and in agreement 
with Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection 
of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing 
Directive 95/46/EC (General Data Protection Regulation).
</div>
'''


def create_cv(data_matrix):
    with open(f'CV {asctime()}.md', 'w') as CV:
        CV.write(data_matrix)
    print('Your simple CV has been created.')

if __name__ == '__main__':
    create_cv(input_data)