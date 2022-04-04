import * as moment from 'moment';

const responseHandler = new Map();

responseHandler.set('card_delivery_estimate', () => (`Your card will be delivered on ${moment().add(2).format('MM-DD-YYYY')}`));
responseHandler.set('transfer_into_account', ({ categories, tokens: { tags }}) => {
    console.log(tags);
    const person = tags.find(item => item[1] === 'PERSON');

    if(person) return `Sure!! will transfer money to ${person[0]}`;

    return categories;
})
responseHandler.set('apple_pay_or_google_pay', () => (`Sure Anmol Let me send money through Apple or Google Pay`))

export function ChatBotResponse({ message = '', status }) {
    if (status) {
        return (
            <div className="chatbot-response">
                <div className="chatbot-response-msg"><span>{responseHandler.has(status.categories) ? responseHandler.get(status.categories)(status) : `${message} ${status.categories}`}</span></div>
            </div>
        )
    }
    return (
        <div className="chatbot-response">
            <div className="chatbot-response-msg"><span>{message}</span></div>
        </div>
    )
}
