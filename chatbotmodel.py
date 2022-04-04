from categoricalclassification import CategoricalClassificationModel
from contextclassification import ContextClassificationModel

class ChatModel:

    categorical_model = None
    context_model = None

    def __init__(self):
        self.categorical_model = CategoricalClassificationModel()
        self.ner_model = ContextClassificationModel() 


    def evaluate(self, text):
        evaluate_text = {}
        evaluate_text['categories'] = self.categorical_model.evaluate(text)
        evaluate_text['tokens'] = self.ner_model.evaluate(text)

        return evaluate_text