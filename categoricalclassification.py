from matplotlib.pyplot import axes
from transformers import DistilBertTokenizer
import tensorflow as tf
from transformers import TFDistilBertModel
import string
from nltk.corpus import stopwords

class CategoricalClassificationModel:
    english_stop_words = stopwords.words('english')
    model = None

    def load_model(self):

        dbert_model = TFDistilBertModel.from_pretrained('distilbert-base-uncased')

        new_input_ids = tf.keras.Input(shape=(98,), name='input_token', dtype='int32')
        new_input_masks = tf.keras.Input(shape=(98,), name='masked_token', dtype='int32')

        new_dbert_layer = dbert_model(new_input_ids, attention_mask=new_input_masks)[0][:,0,:]

        new_dropout = tf.keras.layers.Dropout(0.1)(new_dbert_layer)

        new_output_layer = tf.keras.layers.Dense(
            77, 
            activation='softmax', 
            kernel_regularizer='l2'
            )(new_dropout)

        self.model = tf.keras.Model(inputs=[new_input_ids, new_input_masks], outputs=new_output_layer)

        for layer in self.model.layers[:2]:
            layer.trainable = False

        sched_lr = tf.keras.optimizers.schedules.CosineDecay(
            initial_learning_rate=0.0001,
            decay_steps=314*10,  
            alpha=0.01
        )

        sched_opt = tf.keras.optimizers.Adam(learning_rate=sched_lr)    # 0.0001

        self.model.compile(
            optimizer=sched_opt, 
            loss='categorical_crossentropy', # categorical crossentropy is to be minimised since we have 77 categories to classify into
            metrics=['categorical_accuracy']  
            )

        self.model.load_weights("categorical_pred_weights")

    def get_model(self):
        if self.model == None:
            self.load_model()

        return self.model

    def evaluate(self, text):
        model = self.get_model()
        format_str = self.format_sentence(text)
        tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

        transformed_input = tokenizer(
            format_str, 
            add_special_tokens=True, 
            max_length=98, 
            padding='max_length', 
            truncation=True, 
            return_tensors='tf'
        )
        pred = model.predict([[transformed_input['input_ids']], [transformed_input['attention_mask']]])

        return self.convert_pred_to_label(pred)

    def convert_pred_to_label(self, preds):
        return classes[preds.argmax(axis = 1)[0]]


    def format_sentence(self, textStr):
        textStrList = textStr.split()
        finalStr = ' '
        for word in textStrList:
            if word not in (self.english_stop_words):
                finalStr += ' ' + word

        return finalStr.translate(str.maketrans('', '', string.punctuation))

classes = [
    "activate_my_card",
    "age_limit",
    "apple_pay_or_google_pay",
    "atm_support",
    "automatic_top_up",
    "balance_not_updated_after_bank_transfer",
    "balance_not_updated_after_cheque_or_cash_deposit",
    "beneficiary_not_allowed",
    "cancel_transfer",
    "card_about_to_expire",
    "card_acceptance",
    "card_arrival",
    "card_delivery_estimate",
    "card_linking",
    "card_not_working",
    "card_payment_fee_charged",
    "card_payment_not_recognised",
    "card_payment_wrong_exchange_rate",
    "card_swallowed",
    "cash_withdrawal_charge",
    "cash_withdrawal_not_recognised",
    "change_pin",
    "compromised_card",
    "contactless_not_working",
    "country_support",
    "declined_card_payment",
    "declined_cash_withdrawal",
    "declined_transfer",
    "direct_debit_payment_not_recognised",
    "disposable_card_limits",
    "edit_personal_details",
    "exchange_charge",
    "exchange_rate",
    "exchange_via_app",
    "extra_charge_on_statement",
    "failed_transfer",
    "fiat_currency_support",
    "get_disposable_virtual_card",
    "get_physical_card",
    "getting_spare_card",
    "getting_virtual_card",
    "lost_or_stolen_card",
    "lost_or_stolen_phone",
    "order_physical_card",
    "passcode_forgotten",
    "pending_card_payment",
    "pending_cash_withdrawal",
    "pending_top_up",
    "pending_transfer",
    "pin_blocked",
    "receiving_money",
    "Refund_not_showing_up",
    "request_refund",
    "reverted_card_payment?",
    "supported_cards_and_currencies",
    "terminate_account",
    "top_up_by_bank_transfer_charge",
    "top_up_by_card_charge",
    "top_up_by_cash_or_cheque",
    "top_up_failed",
    "top_up_limits",
    "top_up_reverted",
    "topping_up_by_card",
    "transaction_charged_twice",
    "transfer_fee_charged",
    "transfer_into_account",
    "transfer_not_received_by_recipient",
    "transfer_timing",
    "unable_to_verify_identity",
    "verify_my_identity",
    "verify_source_of_funds",
    "verify_top_up",
    "virtual_card_not_working",
    "visa_or_mastercard",
    "why_verify_identity",
    "wrong_amount_of_cash_received",
    "wrong_exchange_rate_for_cash_withdrawal"
]