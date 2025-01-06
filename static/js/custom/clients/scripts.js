console.log("qqqqqqqqqqqqq");


document.getElementById('buttonSave').addEventListener('click', async function () {
    const form = document.querySelector('form'); // Находим форму
    const formData = new FormData(form); // Собираем данные из формы


    try {
        const response = await fetch('/clients/add', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            console.log(result);

        } else {
            const result = await response.json();
            console.log(result);
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка: ' + error.message); // Уведомление об ошибке
    }
});




