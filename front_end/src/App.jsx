import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import fs from 'fs';


function App() {
  const [playerHP, setPlayerHP] = useState(0)
  const [opponentHP, setOpponentHP] = useState(0)
  const [abilities, setAbilities] = useState(['Punch', 'Kick', 'Run'])

const readFile = () => {
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
const writeFile = (ability) => {
  //const data = new Uint8Array(Buffer.from('Hello Node.js'));
  //fs.writeFile('../state.txt',)
  console.log(`used ${ability}`)
}

  const renderAbility = (ability) => {
    return (
      <div className='ability' onClick={() => writeFile(ability)}>{ability}</div>
    )
  }

  const renderPlayerArea = (playerName, hitPoints, isHuman) => {
    return (
      <div className="stat-bar">
        <h2>{playerName}</h2>
        <h4>{hitPoints}</h4>
        {isHuman && (
          <div id="abilities-wrapper">
            {abilities.map(ability => renderAbility(ability))}
          </div>
        )}
      </div>
    )
  }

  return (
    <>
      <div id="game-area" onClick={() => readFile()}>
        Insert game graphics here
      </div>
      <div id="stat-bars-area">
        {renderPlayerArea('The Player', playerHP, true)}
        {renderPlayerArea('The AI Opponent', opponentHP)}
      </div>
    </>
  )
}

export default App
