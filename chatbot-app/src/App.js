import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import LoginPage from './components/login-page/login-page.component';
import { ChattingScreen } from './components/chatting-screen/chatting-screen.component';
import { Provider } from 'react-redux';
import messageStore from './store/messageStore';

function App() {
  return (
    <Provider store={messageStore}>
      <ChattingScreen />
    </Provider>
  );
}

export default App;
