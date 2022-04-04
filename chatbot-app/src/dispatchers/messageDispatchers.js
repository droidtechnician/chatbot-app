import { addNewMessage, sendingMessage, sendingMessageFailure, messageSentSuccessfully } from '../reducers/messageReducers';
import axios from 'axios';

export async function sendMessage(dispatch, message) {
    dispatch(sendingMessage({
        from: 'User',
        message
    }))
    dispatch(sendingMessage({
        from: 'Chatbot',
        message: 'Please wait while we check this out for you.'
    }))
    try {
        const response = await axios.post('http://192.168.2.14:105/predict', { sentence: message })
        dispatch(messageSentSuccessfully({
            from: 'Chatbot',
            message: 'Response',
            status: response.data
        }))
    } catch(e) {
        console.log(e)
    }
}