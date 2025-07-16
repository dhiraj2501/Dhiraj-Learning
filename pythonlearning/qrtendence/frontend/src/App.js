import React, { useState } from 'react';
import './App.css';

function App() {
  const [name, setName] = useState('');
  const [studentId, setStudentId] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(''); // Clear previous messages

    try {
      const response = await fetch('http://127.0.0.1:8000/register_student', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, student_id: studentId, email }),
      });

      const data = await response.json();
      setMessage(data.message);
      if (response.ok) {
        // Clear form on successful registration
        setName('');
        setStudentId('');
        setEmail('');
      }
    } catch (error) {
      console.error('Error registering student:', error);
      setMessage('Error registering student. Please try again.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Student Registration</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label>
              Name:
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Student ID:
              <input
                type="text"
                value={studentId}
                onChange={(e) => setStudentId(e.target.value)}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Email:
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </label>
          </div>
          <button type="submit">Register</button>
        </form>
        {message && <p>{message}</p>}
      </header>
    </div>
  );
}

export default App;
