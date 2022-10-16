import React, { useState } from 'react'
import Header from "./components/Header"
import SearchBar from "./components/SearchBar"
import PlaceData from "./Data.json"
import DatePicker from "react-datepicker"
import 'react-datepicker/dist/react-datepicker.css'
import './App.css'


function App() {
  const[selectedDate, setSelectedDate] = useState(null)
  return (
    <div className="App">
      <Header />
      <SearchBar placeholder="Enter your origin..." data={PlaceData}/>
      <SearchBar placeholder="Enter your destination..." data={PlaceData}/>
      <DatePicker 
      selected={selectedDate} 
      onchange={date =>setSelectedDate(date)} 
      dateFormat = 'yyyy/MM/dd'
      minDate = {new Date()}
      isClearable
      showYearDropdown
      scrollableYearDropdown
      scrollableMonthYearDropdown
      />


    </div>
  );
}

export default App;
