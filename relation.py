from typing import List, Any
import json
from enum import Enum
import pandas as pd

GROUP_NAME = 'group_name'
CHECKS = 'checks'
CHECK_GROUPS = 'check_groups'


class KeyType(Enum):
    COMPANY = 'company'
    APPLICATION = 'application'

    def __str__(self):
        return self.value

class KeyId(Enum):
    ENTITY_ID = 'id'
    ENTITY_TYPE = 'type'

    def __str__(self):
        return self.value

class KeyPair(Enum):
    RESOURCE = 'resource'
    SUBJECT = 'subject'

    def __str__(self):
        return self.value

class PermissionEntity:
    def __init__(self, entity_type, entity_id):
        self.entity_type: str = entity_type
        self.entity_id: str = entity_id

class PermissionCheck:
    def __init__(self, resource, relation, subject):
        self.resource: PermissionEntity = resource
        self.relation: str = relation
        self.subject: PermissionEntity = subject


def hermes_endpoint(token):
    """
    Takes token return Something good
    """
    return False


# json.dumps(c, default=lambda o: o.__dict__)

# [
#    {"resource": {"entity_type": "company", "entity_id": "moes_tavern"}, "relation": "writer", "subject": {"entity_type": "user", "entity_id": "homer@test.com"}},
#    {}
#]


list_of_checks = {
   "check_groups":[

    {
         "group_name":"something",
         "checks":[
            {
               "resource":{
                  "type":"application",
                  "id":"console"
               },
               "relation":"writer",
               "subject":{
                  "type":"user",
                  "id":"home@test.com"
               }
            },
            {
               "resource":{
                  "type":"application",
                  "id":"Zerondha"
               },
               "relation":"writer",
               "subject":{
                  "type":"user",
                  "id":"home@test.com"
               }
            }
         ]
      },
      {
         "group_name":"something2",
         "checks":[
            {
               "resource":{
                  "type":"company",
                  "id":"apple"
               },
               "relation":"writer",
               "subject":{
                  "type":"user",
                  "id":"rs@test.com"
               }
            },
            {
               "resource":{
                  "type":"application",
                  "id":"microsoft"
               },
               "relation":"writer",
               "subject":{
                  "type":"user",
                  "id":"rs@test.com"
               }
            }
         ]
      }
      
   ]
}

empty_json = []


def get_filtered_json(json: List[Any], key_type: KeyType, key_id: KeyId, entity_type: KeyType):
    """
    Returns filtered list of json based on type, resource
    """
    return list(filter(lambda object: object[key_type][key_id] == entity_type, json))


def get_formatted_json(json: List[Any], key_type: KeyType, key_id: KeyId, entity_type: KeyType):
    """
    Return formatted JSON grouped by given filters
    """
    sub_level_json = json.get(CHECK_GROUPS)
    result_lists = []

    for json_obj in sub_level_json:
        group_name = json_obj.get(GROUP_NAME, '')
        checks_under_group = json_obj.get(CHECKS, [])

        filtered_result = get_filtered_json(checks_under_group, key_type, key_id, entity_type)
        # import pdb; pdb.set_trace()

        if filtered_result:
            return_result = {
                GROUP_NAME: group_name,
                CHECKS: filtered_result
            }
            result_lists.append(return_result)

    return result_lists


user_company_checks = get_formatted_json(list_of_checks, str(KeyPair.RESOURCE), str(KeyId.ENTITY_TYPE), str(KeyType.COMPANY))

# print(user_company_checks)

import requests

example_json = {"check_groups":[
  {
      "group_name":"something",
      "checks":[
        {
            "resource":{
              "type":"company",
              "id":"rosebud"
            },
            "relation":"writer",
            "subject":{
              "type":"person",
              "id":"orsonwells"
            }
        }
      ]
  }
]}

testing_request = {
   "url": "http://127.0.0.1:8000/permission-check",
   "headers": {"Authorization": f"Bearer xyz"},
   "json": {CHECKS: example_json }
}

res = requests.get(**testing_request)

print(res.json())

# print(get_filter_permission(list_of_checks))

# user_company_checks = get_filter_permission(list_of_checks, str(KeyPair.RESOURCE), str(KeyId.ENTITY_TYPE), str(KeyType.COMPANY))
# company_application_checks = get_filter_permission(list_of_checks, str(KeyPair.RESOURCE), str(KeyId.ENTITY_TYPE), str(KeyType.APPLICATION))


# print(user_company_checks)

# print(company_application_checks)


def check_permission(token, hermes_url, checks: List[Any]) -> bool:

    email = payload.get('email')

    cu = companyUser.object.filter(user__email = email)

    for company in company_application_checks:
        application_name = company.get('resource')['entity_id']
        
        permission['artemis_employee']['checks'][application_name] = f'{application_name}' in cu.user.beta_flags
    
    
    for user in user_company_checks:
        user_name = user.get('resource')['entity_id']
        


        
    


valid_user_email = "homer@test.com"
invalid_user_email = "herm@test.com"
non_beta_user_email = "dam@test.com"
valid_token = 'xyz123'

company_entity = PermissionEntity("company", "moes_tavern")
pharos_entity = PermissionEntity("application", "pharos")
non_pharos_entity = PermissionEntity("application", "springfield")


valid_user_entity = PermissionEntity("user", valid_user_email)
invalid_user_entity = PermissionEntity("user", invalid_user_email)
non_beta_user_entity = PermissionEntity("user", non_beta_user_email)


valid_company_check = PermissionCheck(company_entity, "writer", valid_user_entity)
invalid_company_check = PermissionCheck(company_entity, "writer", invalid_user_entity)
non_beta_company_check = PermissionCheck(company_entity, "writer", non_beta_user_entity)


# check_permission(valid_token, '', [valid_company_check, invalid_company_check])