import React from 'react'; 
import "./App.css"

class App extends React.Component {
  jobPostForm() {
    alert("To be implemented");
  }

  lookAtJobs(){
    alert("To be implemented");
  }
  
  render() {
    return (
      <React.Fragment>
        <div class="App-header">
        <a href="#" class="logo">JobPortal</a>
          <div class="App-header-right">
            <a class="active" href="#home">Home</a>
            <a href="#contact">Contact</a>
            <a href="#about">About</a>
          </div>
        </div>
        <div class="centered"><button class="centerbuttons" onClick={this.jobPostForm}>Post a job</button>
        <br/>
        <br/>
        <button class="centerbuttons" onClick={this.lookAtJobs}>Look at jobs</button>
        </div>
      </React.Fragment>
    );
  }
}

export default App;
