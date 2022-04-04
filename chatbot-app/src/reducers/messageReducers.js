import { createSlice } from '@reduxjs/toolkit';

const messageReducer = createSlice({
    name: 'messages',
    initialState: {
        sendingMessage: false,
        sendingMessageError: false,
        messageSentSuccessfully: false,
        messages: [
            {
                from: 'Chatbot',
                message: 'Hello user !!'
            }
        ],
    },
    reducers: {
        addNewMessage: (state, action) => {
            state.messages.push(action?.payload)
        },
        sendingMessage: (state, action) => {
            state.sendingMessage = true;
            state.messages.push(action?.payload)
        },
        sendingMessageFailure: (state, action) => {
            state.messages.push(action.payload)
            state.sendingMessageError = true;
        },
        messageSentSuccessfully: (state, action) => {
            state.messages.push(action?.payload);
            state.sendingMessage = false;
            state.messageSentSuccessfully = true;
            state.sendingMessageError = false
        }
    }
})

export const { addNewMessage, sendingMessage, sendingMessageFailure, messageSentSuccessfully } = messageReducer.actions;

export default messageReducer.reducer;
