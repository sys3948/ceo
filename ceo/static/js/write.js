$(document).ready(function() {
    $('.summernote').summernote({
        height: 150
    });

    $('.recipe_form').submit((e) =>{
        e.preventDefault();
        var recipeName = document.querySelector('#recipe_name').value;
        console.log(recipeName);
        var nutrition = document.querySelectorAll('.note-editable')[0].innerHTML;
        console.log(nutrition);
        var recipeDoc = document.querySelectorAll('.note-editable')[1].innerHTML;
        console.log(recipeDoc);
        var foodStuff = document.getElementById('foodStuff').value;
        console.log(foodStuff);
    });

    $('.storage_form').submit((e) => {
        e.preventDefault();
    });
});