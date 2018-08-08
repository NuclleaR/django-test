import * as React from 'react';
import {GoogleLogin, GoogleLoginResponse} from 'react-google-login';
import './App.css';

import {config} from "./config";
import logo from './logo.svg';

class App extends React.Component {

  public gauthOnSuccess(response: GoogleLoginResponse) {
    console.log(response)
  }

  public gauthOnFailure(error: Error) {
    console.log(error);
  }

  public render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.tsx</code> and save to reload.
        </p>
        <div>
          <GoogleLogin
            onSuccess={this.gauthOnSuccess}
            onFailure={this.gauthOnFailure}
            clientId={config.googleClientId}
            buttonText={'Login with Google'}
            redirectUri={'http://localhost:3000/'}
          />
        </div>
      </div>
    );
  }
}

export default App;
