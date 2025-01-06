document.getElementById('selectAll').addEventListener('change', function() {
    const isChecked = this.checked;
    document.querySelectorAll('.select-client').forEach(cb => cb.checked = isChecked);
});

document.getElementById('deleteSelected').addEventListener('click', async function() {
    const selectedIds = Array.from(document.querySelectorAll('.select-client:checked'))
                              .map(cb => cb.value);
    if (selectedIds.length === 0) {
      alert('Выберите хотя бы одну запись для удаления.');
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
      alert('Записи успешно удалены.');
      location.reload();
    } else {
      alert('Ошибка при удалении записей.');
    }
    });

document.querySelectorAll('.btn-delete-client').forEach(button => {
    button.addEventListener('click', async function() {
      const clientId = this.dataset.clientId;
      const confirmed = confirm('Вы действительно хотите удалить эту запись?');
      if (!confirmed) return;

      const response = await fetch(`/clients/delete/${clientId}`, { method: 'DELETE' });
      if (response.ok) {
        alert('Запись успешно удалена.');
        location.reload();
      } else {
        alert('Ошибка при удалении записи.');
      }
    });
});