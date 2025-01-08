// Уведомления
document.addEventListener('DOMContentLoaded', function () {
    // Получаем данные из sessionStorage
    const toastStatus = sessionStorage.getItem('toastStatus');
    const toastTitle = sessionStorage.getItem('toastTitle');
    const toastMessage = sessionStorage.getItem('toastMessage');

//    console.log(toastStatus)
//    console.log(toastMessage)

    if (toastStatus && toastMessage) {
        // Показываем toast
        showToast(toastStatus, toastTitle, toastMessage);

        // Очищаем данные из sessionStorage
        sessionStorage.removeItem('toastStatus');
        sessionStorage.removeItem('toastTitle');
        sessionStorage.removeItem('toastMessage');
    }
});



// Выбрать все записи
document.getElementById('selectAll').addEventListener('change', function() {
    const isChecked = this.checked;
    document.querySelectorAll('.select-client').forEach(cb => cb.checked = isChecked);
});




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
