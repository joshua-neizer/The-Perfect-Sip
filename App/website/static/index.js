function deleteNote(noteId){
    //send a request to backend to delete note
    fetch("/delete-note", {
        method : "POST",
        body : JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}