import React from "react";
import Header from "./components/Header";
import SearchBar from "./components/SearchBar";
import BookData from "./Data.json"
import "./App.css"

const App = () => {
  return (
    <div className="App">
      <Header/>
      <SearchBar placeholder="Enter your origin..." data={BookData} />
      <SearchBar placeholder="Enter your destination..." data={BookData} />
    </div>
  );
}

export default App;