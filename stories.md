## story 01
* greet
  - utter_greet

## story 02
* greet
  - utter_greet
* goodbye
  - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* perform{"operation": "add"}
    - slot{"operation": "add"}
    - utter_ask_username
* perform{"username": "abc"}
    - slot{"username": "abc"}
    - action_perform
* goodbye

## interactive_story_2
* greet
    - utter_greet
* perform{"operation": "update"}
    - slot{"operation": "update"}
    - utter_ask_username
* perform{"username": "kumar"}
    - slot{"username": "kumar"}
    - action_perform
* goodbye

## interactive_story_3
* greet
    - utter_greet
* perform{"operation": "delete"}
    - slot{"operation": "delete"}
    - utter_ask_username
* perform{"username": "abc"}
    - slot{"username": "abc"}
    - action_perform
* goodbye

## interactive_story_4
* greet
    - utter_greet
* perform{"operation": "get"}
    - slot{"operation": "get"}
    - utter_ask_username
* perform
    - action_perform
* goodbye
## interactive_story_1
* greet
    - utter_greet
* get

## interactive_story_1
* greet
    - utter_greet
* get

## interactive_story_1
* greet
    - utter_greet
* add
