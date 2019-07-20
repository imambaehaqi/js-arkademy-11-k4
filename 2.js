is_username_valid("Xrutaf888"); // true
is_username_valid("1Diana"); // false
is_password_valid("passW0rd="); // true 
is_password_valid("C0d3YourFuture!#"); // false

function is_username_valid(username){
    let usn = /^[^0-9$&\+,:;\=\?@#|'<>\.\-_^\*()%!][$&\+,:;\=\?@#|'<>\.\-_^\*()%!0-9a-zA-z]{5,9}$/;
    if(username.match(usn)){
        // return true;
        console.log(true);
    }else{
        // return false;
        console.log(false);
    }
}

function is_password_valid(password){
    let pwd = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*=)(?=.*[\=\+\-\_\@\#\$\%\&]).{8,}$/;
    if(password.match(pwd)){
        // return true;
        console.log(true);
    }else{
        // return false;
        console.log(false);
    }
}