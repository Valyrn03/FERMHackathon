import { useState } from 'react'
import player1 from './assets/Player-1.png'
import theAI from './assets/The AI-1.png'
import './App.css'


function App() {
  const [playerHP, setPlayerHP] = useState(100)
  const [opponentHP, setOpponentHP] = useState(100)
  const [abilities, setAbilities] = useState(['Punch', 'Kick', 'Run'])

  // write to the file and set the mutex so the back end can read it then write to this file
// namely we will want to write the current state plus the move that was made
const writeFile = (ability) => {
  //const data = new Uint8Array(Buffer.from('Hello Node.js'));
  //fs.writeFile('../state.txt',)
  console.log(`used ${ability}`)
}

  const renderAbility = (ability) => {
    return (
      <input key={ability} type='button' className='ability' onClick={() => writeFile(ability)} value={ability}/>
    )
  }

  const renderPlayerArea = (playerName, hitPoints, imageSrc) => {
    return (
      <div className="player-area">
        <h2>{playerName}</h2>
        <h2>{hitPoints}</h2>
        <img src={imageSrc} width={100} height={100} />
      </div>
    )
  }

  return (
    <>
      <div id="player-area-wrapper">
        {renderPlayerArea('The Player', playerHP, player1)}
        {renderPlayerArea('The AI Opponent', opponentHP, theAI)}
      </div>
      <div id="abilities-wrapper">
        {abilities.map(ability => renderAbility(ability))}
      </div>
    </>
  )
}

export default App
