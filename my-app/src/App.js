import React from 'react'; 
import "./App.css";
import ReactDom from 'react-dom';

class App extends React.Component {
  
  candidate_login(){

  }

  hr_login(){

  }

  signUp(){

  }

  browseJobs(){

  }

  render() {
    return (
      <React.Fragment>
        <body class="App">
          <div class="App-header">
          <a href="#" class="logo">JobPortal</a>
            <div class="App-header-right">
              <a class="active" href="#home">Home</a>
              <a href="#contact">Contact</a>
              <a href="#about">About</a>
              <a href="#browse">Browse jobs</a>
              <a href="#HR">HR Log in</a>
            </div>
          </div>
          <table class="centered">
            <h1 class="innerHeader">Welcome!</h1>
            <button class="centerbuttons" onClick={this.candidate_login}>Candidate log in</button>
            <br/>
            <button class="centerbuttons" onClick={this.signUp}>Candidate sign up</button>
          </table>
        </body>
      </React.Fragment>
    );
  }
}

export default App;
