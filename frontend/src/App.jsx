import React from 'react';
import EmailList from './components/EmailList';
import './App.css'; 

function App() {
  return (
    <div className="container-wrapper">
      <div className="app-box">
        <nav className="navbar">
          <h2>AI Gmail Manager</h2>
          <a href="http://localhost:8000/google/login/" className="login-btn"> 
            Login with Google
          </a>
        </nav>

        <main className="content">
          <EmailList />
        </main>
      </div>
    </div>
  );
}

export default App;