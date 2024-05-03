var myButton = document.getElementById('myButton');

// Функция для смены класса
function changeClass() {
    if (myButton.classList.contains('button')) {
        myButton.classList.remove('button');
        myButton.classList.add('new-button-class');
    } else {
        myButton.classList.add('button');
        myButton.classList.remove('new-button-class');
    }
}

// Вызов функции при клике на кнопку
myButton.addEventListener('click', function() {
    changeClass();
});