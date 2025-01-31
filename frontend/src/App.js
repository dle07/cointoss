import './App.css';
import React from 'react'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import About from './pages/about_us'
import Landing from './pages'
import Portfolio from './pages/portfolio'
import Login from './pages/Login'
import SignUp from './pages/SignUp';
import StockPrice from './pages/StockPrice';
import HistoricalData from './pages/HistoricalData';
import AccessRoutes from './AccessRoutes';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path='/' element={<Landing />} />
        <Route path='/about_us' element={<About/>} />
        <Route element={<AccessRoutes />} >
          <Route path='/portfolio' element={<Portfolio/>} />
        </Route>
        <Route path='/Login' element={<Login/>} />
        <Route path='/SignUp' element={<SignUp/>} />
        <Route path='/StockPrice/:ticker' exact element={<StockPrice />} />
        <Route path='/HistoricalData/:ticker' element={<HistoricalData />} />
      </Routes>
    </Router>
  );
}

export default App;
