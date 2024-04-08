const check_button = document.getElementById('check_answer_button');


check_button.addEventListener('click', () => {
    const correct_answer = document.getElementById('answer').value;
    const gotten_answer = document.getElementById('answer_field').value;
    if (correct_answer === gotten_answer) {
        alert('Ответ верный');
    } else {
        alert('Ответ неверный, перечитайте теорию еще раз');
    }
})