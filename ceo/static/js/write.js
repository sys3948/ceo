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

    $('#imgFile').change((e) => {
        if(e.target.files && e.target.files[0]){
            var reader = new FileReader();

            reader.onload = (e) => {
                $('#previewImg').attr('src', e.target.result);
            }

            reader.readAsDataURL(e.target.files[0]);
        }
        
        
    });
});