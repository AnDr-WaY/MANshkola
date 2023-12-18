// Функція таймеру
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Поділитися через вайбер
document.getElementById('share_viber').setAttribute('href',"viber://forward?text=" + encodeURIComponent(window.location.href));
// Поділитися через фейсбук
document.getElementById('share_facebook').setAttribute('href',"https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(window.location.href));
// Поділитися через телеграм
document.getElementById('share_telegram').setAttribute('href',"https://t.me/share/url?url=" + encodeURIComponent(window.location.href));

// Скопіювати посилання
var isOpened = false
const copiedAllert = document.getElementById('link_copied_alert')
document.getElementById('copy_link').addEventListener('click', async (e)=>{
    if (isOpened === false){
        isOpened = true;
        navigator.clipboard.writeText(window.location.href);
        copiedAllert.classList.add('active');
        await sleep(2000);
        copiedAllert.classList.remove('active');
        isOpened = false;
    };
})

