import { configureStore } from '@reduxjs/toolkit'
import messageReducers from '../reducers/messageReducers';

export default configureStore({
  reducer: {
    message: messageReducers,
  },
  middleware: getDefaultMiddleware => getDefaultMiddleware()
})