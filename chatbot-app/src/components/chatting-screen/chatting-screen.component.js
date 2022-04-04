import './chatting-screen.component.css';

import ChatBotImg from '../../assets/chatbot.jpg';
import UserImg from '../../assets/user.png'

import { BiSend } from "react-icons/bi";
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { sendMessage } from '../../dispatchers/messageDispatchers';
import { debounceTime, Subject } from 'rxjs';

import { ChatBotResponse } from './chatbot-response';

export function ChattingScreen() {
    const [query, setQuery] = useState('');
    const dispatch = useDispatch();
    const getMessages = useSelector(state => state.message.messages);
    const waiting = useSelector(state => state.message.sendingMessage);
    const [queryListener$] = useState(new Subject());;

    useEffect(() => {
        queryListener$
            .pipe(
                debounceTime(500)
            )
            .subscribe(message => {
                sendMessage(dispatch, message)
            })
    }, [])

    useEffect(() => {
        console.log(getMessages)
    }, [getMessages])

    const userMessageInputChange = event => {
        setQuery(event.target.value)
    }

    const sendMessageEvent = _ => {
        if (!waiting) {
            queryListener$
                .next(query);
            setQuery('')
        }
    }

    return (
        <div className='chat-screen'>
            <div className="chatbot-img-container">
                <img src={ChatBotImg} className="chatbot-img" />
                <span className='chatbot-name'>Banking BOT</span>
            </div>
            <div className='message-container'>
                {
                    getMessages.map(({ from = '', message = '', status }) => (
                        from === 'Chatbot' ? <ChatBotResponse message={message} status={status} /> : <UserResponse message={message} />
                    ))
                }
            </div>
            <div className='input-query'>
                <input type="text" className='message-input' placeholder='Message' onChange={(e) => userMessageInputChange(e)} value={query} />
                <BiSend color='#26a5d0' opacity={(query && 1) || 0.5} onClick={sendMessageEvent} />
            </div>
        </div>
    )
}

export function UserResponse({ message = '' }) {
    return (
        <div className="user-query">
            <img src={UserImg} />
            <div className='user-query-msg'><span>{message}</span></div>
        </div>
    )
}