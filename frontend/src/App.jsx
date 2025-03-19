import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Auth from './pages/Auth';
import AuthGoogle from './pages/AuthGoogle';
import AuthGithub from './pages/AuthGithub';
import AuthYandex from './pages/AuthYandex';
import Home from './pages/Home';
import "./auth.css"
import "./home.css"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth />} />
        <Route path="/auth/github" element={<AuthGithub />} />
        <Route path="/auth/google" element={<AuthGoogle />} />
        <Route path="/auth/yandex" element={<AuthYandex />} />
      </Routes>
    </Router>
  );
}

export default App;