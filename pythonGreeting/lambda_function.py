from pythonGreeting import analyzer
        

def lambda_handler(event, context):
    greetingMessageAnalyzer = analyzer.GreetingMessageAnalyzer(event)
    return greetingMessageAnalyzer.analyze(
        morning=on_morning,
        noon=on_noon,
        evening=on_evening,
        not_greeting=on_not_greeting
    )
    
def on_morning(text):
    return "おはよう！"
    
def on_noon(text):
    return "こんにちは！"
    
def on_evening(text):
    return "こんばんは！"
    
def on_not_greeting(text):
    return None