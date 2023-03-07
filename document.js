const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'greenyellow';
myDiv.style.textAlign = 'center';

['Додати в друзі', 'Написати повідомлення', 'Запропонувати роботу'].map((buttonName) => {
  let button = document.createElement('button');
  button.className = 'btns';
  button.innerText = buttonName;
  button.style.margin = '5px';
  myDiv.appendChild(button);
});

document.getElementsByTagName('header')[0].appendChild(myDiv);

const friendCount = document.createElement('div');
let count = Math.floor(Math.random() * 100);
friendCount.innerText = `Кількість друзів: ${count}`;

const btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click', (myButtonEvent) =>{
  myButtonEvent.target.disabled = true;
  myButtonEvent.target.innerText = 'Очікується підтвердження'
  count++;
  friendCount.innerText = `Кількість друзів: ${count}`;
});


document.getElementsByTagName('header')[0].appendChild(friendCount)


