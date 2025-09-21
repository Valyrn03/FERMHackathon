import { useState } from 'react'
import player1 from './assets/Player-1.png'
import theAI from './assets/The AI-1.png'
import positiveAttack from './assets/+ATK-1.png.png'
import positiveDefense from './assets/+DEF-1.png.png'
import './App.css'


function App() {
  const [playerHP, setPlayerHP] = useState(100)
  const [opponentHP, setOpponentHP] = useState(100)
  const [abilities, setAbilities] = useState(['Punch', 'Kick', 'Run'])
  const [playerAttackBuff, setPlayerAttackBuff] = useState(1)
  const [playerDefenseBuf, setPlayerDefenseBuff] = useState(2)
  const [aiAttackBuff, setAIAttackBuff] = useState(3)
  const [aiDefenseBuff, setAIDefenseBuff] = useState(1)

const useAbilityAndSendToServer = (ability) => {
  console.log(`used ${ability}`)
  fetch('http://localhost:8000', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name: 'John', age: 30 }),
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
}

  const renderAbility = (ability) => {
    return (
      <input key={ability} type='button' className='ability' onClick={() => useAbilityAndSendToServer(ability)} value={ability}/>
    )
  }

  const renderBuffs = (numberOfBuffs, imgSrc) => {
    const rows = [];

    for (let idx = 0; idx < numberOfBuffs; idx += 1) {
      rows.push(<img key={idx} height={50} width={50} src={imgSrc}/>)
    }

    return rows;
  }

  const renderPlayerArea = (playerName, hitPoints, imageSrc, attackBuff, defenseBuff) => {
    return (
      <div className="player-area">
        <h2>{playerName}</h2>
        <h2>{hitPoints}</h2>
        <img src={imageSrc} width={100} height={100} />
        <div className='buff-wrapper'>{renderBuffs(attackBuff, positiveAttack)}</div>
        <div className='buff-wrapper'>{renderBuffs(defenseBuff, positiveDefense)}</div>
      </div>
    )
  }

  return (
    <>
      <div id="player-area-wrapper">
        {renderPlayerArea('The Player', playerHP, player1, playerAttackBuff, playerDefenseBuf)}
        {renderPlayerArea('The AI Opponent', opponentHP, theAI, aiAttackBuff, aiDefenseBuff)}
      </div>
      <div id="abilities-wrapper">
        {abilities.map(ability => renderAbility(ability))}
      </div>
    </>
  )
}

export default App
