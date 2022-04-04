import { useSelector } from "react-redux";

export const getMessages = useSelector(state => state.message.messages)
export const isWaitingResponse = useSelector(state => state.message.sendingMessage)