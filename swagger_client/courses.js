var userId = $.cookie("user_id"), token = $.cookie("user_id");
if (!$.cookie("user_id") || !$.cookie("token"))
    location.assign("/");

let main = document.getElementById('SelectAll');
let select = document.getElementsByClassName('select')
main.onclick = () => {
    if (main.checked === true) {
        for (let i = 0; i < select.length; i++) {
            select[i].checked = true;
            document.querySelector('button').style.display = 'block';
        }
    } else {
        for (let i = 0; i < select.length; i++) {
            select[i].checked = false;
            document.querySelector('button').style.display = 'none';
        }
    }
}
