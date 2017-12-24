class GreetingMessageAnalyzer:
    def __init__(self,event):
        self._event = event

    def analyze(
        self
        ,morning=lambda text:None
        ,noon=lambda text:None
        ,evening=lambda text:None
        ,not_greeting=lambda text:None
    ):
        if not self._is_text():
            return not_greeting(None)
            
        if self._is_morning():
            return morning(self._event["message"]["text"])
        
        if self._is_noon():
            return noon(self._event["message"]["text"])
            
        if self._is_evening():
            return evening(self._event["message"]["text"])
            
        return not_greeting(self._event["message"]["text"])
    
    def _is_text(self):
        return self._event["message"]["type"] == "text"
        
    def _is_morning(self):
        return self._event["message"]["text"] == "おはよう"
        
    def _is_noon(self):
        return self._event["message"]["text"] == "こんにちは"
        
    def _is_evening(self):
        return self._event["message"]["text"] == "こんばんは"