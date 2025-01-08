document.getElementById('buttonSave').addEventListener('click', async function () {
    const form = document.querySelector('form'); // Находим форму
    const formData = new FormData(form); // Собираем данные из формы

    // Вывод всех значений формы
//    for (const [key, value] of formData.entries()) {
//        console.log(`${key}: ${value}`);
//    }

    try {
        const response = await fetch(params['action'], {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const responseData = await response.json();

            console.log(responseData);

            // Проверяем статус ответа и показываем соответствующее уведомление
            if (responseData.status === 'success') {
                // Сохраняем сообщение в sessionStorage
                sessionStorage.setItem('toastStatus', 'success');
                sessionStorage.setItem('toastTitle', 'Успешно');
                sessionStorage.setItem('toastMessage', responseData.message);

                // Перенаправляем на страницу клиентов
                // window.location.href = '/clients';
            } else {
                // Если возникла ошибка, показываем уведомление об ошибке
                showToast('error', 'Ошибка', responseData.message);
            }
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка: ' + error.message); // Уведомление об ошибке
    }
});




