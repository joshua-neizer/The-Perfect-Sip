function deleted(userId){
    //send a request to backend to delete note
    fetch("/delete-user", {
        method : "POST",
        body : JSON.stringify({ userId: userId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}