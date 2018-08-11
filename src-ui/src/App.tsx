import * as React from 'react';
import {GoogleLogin, GoogleLoginResponse} from 'react-google-login';
import './App.css';

import {config} from './config';
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
            buttonText="Login with Google"
            redirectUri="http://localhost:8080/auth/"
            uxMode="popup"
          />
        </div>
      </div>
    );
  }
}

export default App;

/*
* http://localhost:3000/auth/#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjlhMzNiNWVkYjQ5ZDA4NjdhODY3MmQ5NTczYjFlMGQyMzc1ODg2ZTEifQ.eyJhenAiOiI1Mjc2NzIxMjI4MzYtaWZiMDhmaGk4MzRtdWJsdWU2ZzVtOWNtYjk3amh2OWcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI1Mjc2NzIxMjI4MzYtaWZiMDhmaGk4MzRtdWJsdWU2ZzVtOWNtYjk3amh2OWcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDM5ODY3Mjg2NzU5NjI0NTIwNDIiLCJlbWFpbCI6Im1vZGVsbi5jb25maWdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV4cCI6MTUzMzc2NzM2MywiaXNzIjoiYWNjb3VudHMuZ29vZ2xlLmNvbSIsImp0aSI6IjNjMGQwOTk3NzdhYWQ3N2YzNGE0YTU1MTQ1NGVmZWFjNTIwYmQ0ZjMiLCJpYXQiOjE1MzM3NjM3NjN9.ZT32zJhJej_Pfd3JhqbfDYDV6JQXL33GOuU7-X2vibqXuk6ZV8ZgwNgCRsvXqLRyLyu8a-OC2xng0mkZ59mNuZEWplQxKWDNGCwP3HVhdVeePOhpF748MmVbElxMmN13EX0gvXdNyhM-lgSvXqlz2o5oumldaK6zxjT1jnEcsACDaCQ1UeV56VDAhDg474MvLievGFia7rXiQfCD3RQdFIzghjp5dy-I7nsWP0Pftfej0X2353zglenZvgEht2pvsAun-9JYKQUYUwiEX8VPXXTyO7h42rsLs2HRJyaDZo4SLM-3EQnL_29PuJs1MUBKtFK6uMR5QOlvw6Y-Z6HnHw&login_hint=AJDLj6JUa8yxXrhHdWRHIV0S13cAEU-3QS7I6yPa_u1JyELq6BqFxvAMbwiU7dxUIT2DTqT9h_YdMi9aw4quZhYHDlhV3IhPuQ&client_id=527672122836-ifb08fhi834mublue6g5m9cmb97jhv9g.apps.googleusercontent.com&prompt=consent
* */