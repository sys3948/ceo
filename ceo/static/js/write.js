$(document).ready(function() {
    $('.summernote').summernote({
        height: 150
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