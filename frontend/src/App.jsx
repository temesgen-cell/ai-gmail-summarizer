// frontend/src/App.js
import React from 'react';
import EmailList from './components/EmailList';

function App() {
  return (
    <div className="App">
      <nav style={{ padding: '20px', background: '#f4f4f4' }}>
        <h2>AI Gmail Manager</h2>
        {/* This link points directly to your Django backend login route */}
        <a href="http://localhost:8000/google/login/" className="login-btn">
          Login with Google
        </a>
      </nav>

      <main>
        <EmailList />
      </main>
    </div>
  );
}

export default App;