from json_checker import Checker


expected  = {
    "resource": {
        "entity_type": str,
        "entity_id": str
    },
    "relation": str,
    "subject": {
        "entity_type": str,
        "entity_id": str
    }
}



current_data = [{"resource": {"entity_type": "company", "entity_id": "moes_tavern"}, "relation": "writer", "subject": 
                {"entity_type": "user", "entity_id": "homer@test.com"}}, 

                {"resource": {"entity_type": "company", "entity_id": "raj_travel"}, "relation": "writer", "subject": 
                {"entity_type": "user", "entity_id": "homer@test.com"}}, 

                {"resource": {"entity_type": "application", "entity_id": "pharos"}, "relation": "writer", "subject": 
                {"entity_type": "window", "entity_id": "herm@test.com"}}]

try:
    checker = Checker(expected, soft=True)
    
    for data in current_data:
        checker.validate(data)

except Exception as e:
    print(str(e))