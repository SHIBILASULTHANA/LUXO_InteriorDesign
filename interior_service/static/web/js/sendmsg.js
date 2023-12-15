function sendwhatsapp() {
    var phonenumber = "7356398718";

    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    var url = "https://wa.me/" + phonenumber + "?text=" +
        "name: " + name + "%0a" +
        "email: " + email + "%0a" +
        "subject: " + subject + "%0a" +
        "message: " + message + "%0a%0a" +
        "LUXO Interior Design";

    window.open(url, '_blank').focus();
}