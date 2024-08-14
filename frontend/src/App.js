import React from 'react';
import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Bookings from './components/Bookings';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element = {<Bookings/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
