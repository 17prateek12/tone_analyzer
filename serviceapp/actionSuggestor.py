ACTIONS = {
    "ORDER_FOOD": "Order Food Online",
    "FIND_RECIPE": "Find Food Recipes",
    "ASK_HELP": "Ask for Help",
    "SHARE_NEWS": "Share News with Friends and Family"
}

def suggest_actions(tone,intent):
    suggestion = []
    intent = intent.lower() if intent else ""
    tone = tone.lower() if tone else ""
    
    if any(word in intent for word in ['food', 'order', 'order food', 'deliver', 'delivery']):
        suggestion.append({'action': 'ORDER_FOOD', 'display_text': ACTIONS['ORDER_FOOD']})
    elif any(word in intent for word in ['recipe', 'make', 'prepare', 'ingredients', 'instruction']):
        suggestion.append({'action': 'FIND_RECIPE', 'display_text': ACTIONS['FIND_RECIPE']})
    elif any(word in intent for word in ['question', 'help', '?', 'request', 'assistance', 'guidance']):
        suggestion.append({'action': 'ASK_HELP', 'display_text': ACTIONS['ASK_HELP']})
    elif tone in ['happy', 'joy']:
        suggestion.append({'action': 'SHARE_NEWS', 'display_text': ACTIONS['SHARE_NEWS']})
        
    return suggestion