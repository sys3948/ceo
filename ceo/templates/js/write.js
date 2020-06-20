$(document).ready(function() {
    $('.summernote').summernote({
        height: 150
    });

    $('.recipe_form').submit((e) =>{
        e.preventdefault();
        console.log('Submit!!!!');
    });
});