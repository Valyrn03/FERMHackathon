import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import fs from 'fs';

function loadFile() {
  fs.readFile('../state.txt', (error, data) => {
    if (error) {
      console.log('damn, an error');
      console.log(error);
      return;
    }

    console.log('got data');
    console.log(data);
  });
}

// write to the file and set the mutex so the back end can read it then write to this file
// namely we will want to write the current state plus the move that was made
function writeFile() {

}

function App() {
  const [count, setCount] = useState(0)
  const [playerHP, setPlayerHP] = useState(0)
  const [opponentHP, setOpponentHP] = useState(0)

  const renderPlayerArea = (playerName, hitPoints) => {
    return (
      <div class="stat-bar">
        <h2>{playerName}</h2>
        <h4>{hitPoints}</h4>
      </div>
    )
  }

  return (
    <>
      <div id="game-area">
        Insert game graphics here
      </div>
      <div id="stat-bars-area">
        {renderPlayerArea('The Player', playerHP)}
        {renderPlayerArea('The AI Opponent', opponentHP)}
      </div>
    </>
  )
}

export default App
