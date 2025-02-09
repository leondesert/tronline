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


// Активируем меню
document.addEventListener("DOMContentLoaded", () => {
  const currentUrl = window.location.pathname.split('/')[1]; // Получаем первый сегмент пути

//  console.log(currentUrl);

  const menuItems = document.querySelectorAll('.sidebar-link'); // Выбираем все ссылки меню

  menuItems.forEach((item) => {
    const itemUrl = item.getAttribute('href').split('/')[1]; // Получаем первый сегмент из href
    if (itemUrl === currentUrl) {
      item.classList.add('active'); // Добавляем класс 'active'
    }
  });
});
