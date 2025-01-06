// Выбрать все записи
document.getElementById('selectAll').addEventListener('change', function() {
    const isChecked = this.checked;
    document.querySelectorAll('.select-client').forEach(cb => cb.checked = isChecked);
});


function showAlert(type, message) {
    const alertContainer = document.getElementById('alert-container');
    const successAlert = document.getElementById('success-alert');
    const errorAlert = document.getElementById('error-alert');

    // Скрыть все уведомления перед показом нового
    successAlert.style.display = 'none';
    errorAlert.style.display = 'none';

    if (type === 'success') {
      document.getElementById('success-message').textContent = message;
      successAlert.style.display = 'block';
    } else if (type === 'error') {
      document.getElementById('error-message').textContent = message;
      errorAlert.style.display = 'block';
    }

    // Показать контейнер
    alertContainer.style.display = 'block';

    // Автоматически скрыть уведомление через 5 секунд
    setTimeout(() => {
      alertContainer.style.display = 'none';
    }, 5000);
  }


// Функция для Toast
function showToast(type, title, message) {
    const toast = document.getElementById('myToast');
    const toastTitle = document.getElementById('toastTitle');
    const toastMessage = document.getElementById('toastMessage');
    let myAlert = document.querySelectorAll('.toast')[0];


    // Обновляем заголовок и сообщение
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Меняем стиль в зависимости от типа
    myAlert.classList.remove('text-bg-primary', 'text-bg-success', 'text-bg-danger', 'text-bg-info');
    if (type === 'success') {
        myAlert.classList.add('text-bg-success');
    } else if (type === 'error') {
        myAlert.classList.add('text-bg-danger');
    } else if (type === 'info') {
        myAlert.classList.add('text-bg-info');
    }

    // Показываем toast
    if (myAlert) {
      let bsAlert = new bootstrap.Toast(myAlert);
      bsAlert.show();
    }
}


// Удалить выбранные записи
document.getElementById('deleteSelected').addEventListener('click', async function() {
    const selectedIds = Array.from(document.querySelectorAll('.select-client:checked')).map(cb => cb.value);
    if (selectedIds.length === 0) {
      showToast('error', 'Ошибка', 'Выберите хотя бы одну запись для удаления.');
      return;
    }

    const confirmed = confirm('Вы действительно хотите удалить выбранные записи?');
    if (!confirmed) return;

    const response = await fetch('/clients/delete_bulk', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ids: selectedIds }),
    });

    if (response.ok) {
      const responseData = await response.json();

      // Если удаление успешно
      if (responseData.status === 'success') {

        console.log('success', selectedIds);
        // Удаляем строки из таблицы для выбранных ID
        selectedIds.forEach(id => {
          const row = document.querySelector(`tr:has(.select-client[value="${id}"])`);

          console.log('row', row);

          if (row) {
            row.remove();
          }
        });

        showToast('success', 'Успешно', 'Записи успешно удалены.');
      } else {
        showToast('error', 'Ошибка', responseData.message || 'Ошибка при удалении записей.');
      }
    } else {
      showToast('error', 'Ошибка', 'Ошибка при удалении записей.');
    }
});







// Удалить запись
document.querySelectorAll('.btn-delete-client').forEach(button => {
    button.addEventListener('click', async function() {
        const clientId = this.dataset.clientId; // Получаем ID клиента
        const confirmed = confirm('Вы действительно хотите удалить эту запись?');
        if (!confirmed) return;

        // Отправляем запрос на сервер для удаления
        const response = await fetch(`/clients/delete/${clientId}`, { method: 'DELETE' });

        if (response.ok) {
            const responseData = await response.json();

            // Проверяем статус ответа и показываем соответствующее уведомление
            if (responseData.status === 'success') {
                // Если удаление успешно, находим строку в таблице и удаляем её
                const row = this.closest('tr');
                row.remove();

                // Показываем уведомление об успехе
                showToast('success', 'Успешно', responseData.message);
            } else {
                // Если возникла ошибка, показываем уведомление об ошибке
                showToast('error', 'Ошибка', responseData.message);
            }
        } else {
            // Если запрос не прошел успешно, показываем стандартную ошибку
            showToast('error', 'Ошибка', 'Ошибка при удалении записи.');
        }

    });
});
